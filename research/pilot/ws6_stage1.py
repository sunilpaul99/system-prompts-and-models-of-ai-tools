#!/usr/bin/env python3
"""WS6 Stage 1: screen host turns for candidate disagreement moves (H1-R).

PINNED CONFIG (PROTOCOL §6 / staged amendment B1 — the V2 lesson was that a
model name alone does not reproduce a corpus):

    anthropic-<sdkver>/claude-haiku-4-5/temp0/maxtok<N>/stage1-v1

Why Haiku 4.5 rather than a Sonnet/Opus-class model:
  - It is the model the FULL study would run on anyway (~$93 vs ~$280 at
    1,800 episodes), so validating on it tests the thing we would ship.
  - It still accepts `temperature`. Sonnet 5 / Opus 5 REJECT sampling
    parameters with a 400, so temperature=0 is not expressible there. For a
    study whose credibility rests on reproducibility, being able to pin
    sampling is worth more than a marginally stronger annotator.
  - Escalation rule: if Haiku fails the kappa>=0.70 gate against the PI's
    gold labels, re-validate a Sonnet-class model on the SAME gold sample
    before committing. That decision is the PI's (§10).

temperature=0 is NOT a determinism guarantee — API inference can still vary.
It removes deliberate sampling variance, which is the part we control. V2's
reproducibility probe applies to transcription, not to this stage; the
analogous check here is the kappa gate plus a re-run probe on a subset.

Blinding (§2): this stage emits per-turn labels only. It never sees exposure
labels and never crosses them with features. Same posture as WS5.

Usage:
  ws6_stage1.py <turns_dir> <out_dir> [--limit N] [--dry-run]

--dry-run costs nothing: it counts tokens with the count_tokens endpoint and
reports projected spend without generating. Run it first.
"""
import glob, json, os, sys

MODEL = "claude-haiku-4-5"
TEMPERATURE = 0.0
MAX_TOKENS = 4096
STAGE = "stage1-v1"

# Published rates for claude-haiku-4-5, $/1M tokens (skill cache 2026-06-24).
RATE_IN, RATE_OUT = 1.00, 5.00

SYSTEM = """You are screening transcript turns from a podcast interview.

For each numbered turn by the HOST, decide whether the host is expressing
DISAGREEMENT, PUSHBACK, CORRECTION, or CHALLENGE toward what the guest said.

Include: direct contradiction, raising a counterexample, questioning a
premise, expressing doubt, hedged disagreement ("I'm not sure that follows"),
and reframing that implies the guest is wrong.

Exclude: neutral follow-up questions, requests for clarification,
backchannels ("right", "mhm"), agreement, and topic changes.

Judge only what is in the turn. Do not infer from your knowledge of the
speakers or the subject matter. If a turn is ambiguous, mark it as a
candidate — Stage 2 resolves borderline cases, and a missed turn cannot be
recovered downstream.

Return one entry per turn you were given, in the same order."""

SCHEMA = {
    "type": "object",
    "properties": {
        "turns": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "turn_id": {"type": "integer"},
                    "candidate": {"type": "boolean"},
                    "confidence": {"type": "string",
                                   "enum": ["low", "medium", "high"]},
                },
                "required": ["turn_id", "candidate", "confidence"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["turns"],
    "additionalProperties": False,
}


def host_turns(path):
    """Host turns from a WS6 turns file (ws6_turns.py output), as (turn_id, text).

    Schema is a flat list of {"i", "spk", "text"}; "i" is the turn index
    within the episode and is what Stage 2 and the gold sheets key on, so it
    is carried through rather than re-derived from position here.
    """
    d = json.load(open(path))
    return [(t["i"], t["text"].strip()) for t in d
            if t.get("spk") == "HOST" and t.get("text", "").strip()]


def build_prompt(turns):
    return "\n\n".join(f"[turn {i}] {txt}" for i, txt in turns)


def config_string(sdk_version):
    return (f"anthropic-{sdk_version}/{MODEL}/temp{TEMPERATURE:g}"
            f"/maxtok{MAX_TOKENS}/{STAGE}")


def main(turns_dir, out_dir, *flags):
    import anthropic
    limit = None
    for f in flags:
        if f.startswith("--limit"):
            limit = int(f.split("=", 1)[1] if "=" in f else flags[flags.index(f) + 1])
    dry = "--dry-run" in flags

    client = anthropic.Anthropic()
    cfg = config_string(anthropic.__version__)
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(glob.glob(os.path.join(turns_dir, "*.json")))
    if limit:
        files = files[:limit]

    tot_in = tot_out = 0
    for p in files:
        base = os.path.basename(p).replace(".json", "")
        dest = os.path.join(out_dir, base + ".json")
        if os.path.exists(dest):
            print(f"  skip (done) {base[:44]}")
            continue
        turns = host_turns(p)
        if not turns:
            print(f"  skip (no host turns) {base[:44]}")
            continue
        prompt = build_prompt(turns)
        msgs = [{"role": "user", "content": prompt}]

        if dry:
            n = client.messages.count_tokens(
                model=MODEL, system=SYSTEM, messages=msgs).input_tokens
            tot_in += n
            print(f"  {base[:44]:46} {len(turns):4} host turns  {n:7,} in-tokens")
            continue

        r = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            system=SYSTEM,
            messages=msgs,
            output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
        )
        text = next(b.text for b in r.content if b.type == "text")
        data = json.loads(text)
        tot_in += r.usage.input_tokens
        tot_out += r.usage.output_tokens
        json.dump({"episode": base, "config": cfg,
                   "n_host_turns": len(turns),
                   "usage": {"input_tokens": r.usage.input_tokens,
                             "output_tokens": r.usage.output_tokens},
                   "labels": data["turns"]},
                  open(dest, "w"), indent=1)
        flagged = sum(1 for t in data["turns"] if t["candidate"])
        print(f"  {base[:44]:46} {len(turns):4} turns -> {flagged:3} candidates")

    cost = tot_in / 1e6 * RATE_IN + tot_out / 1e6 * RATE_OUT
    print(f"\nconfig: {cfg}")
    print(f"input tokens : {tot_in:,}")
    if not dry:
        print(f"output tokens: {tot_out:,}")
    print(f"cost {'projected' if dry else 'actual'}: ${cost:.2f} "
          f"(haiku-4-5 @ ${RATE_IN:.2f}/${RATE_OUT:.2f} per MTok)")
    if dry:
        print("DRY RUN — nothing generated, nothing billed beyond token counting.")


if __name__ == "__main__":
    main(*sys.argv[1:])
