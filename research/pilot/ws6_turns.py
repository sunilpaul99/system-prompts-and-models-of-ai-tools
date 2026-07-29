#!/usr/bin/env python3
"""WS6 prep: reconstruct speaker turns from diarized transcripts and report
conversation statistics (turn counts, host turns/hour, mean turn length).

Turn = maximal run of same-speaker words, closing when >= GAP_S seconds of
another speaker's speech intervenes (brief backchannels below MIN_TURN_WORDS
do not break a turn). These turns are the input units for Stage 1 screening
and the denominator machinery for R1-R5. Also emits a turn-formatted,
metadata-stripped rendering per episode (HOST/GUEST + text only) — the exact
input format the Stage 1/2 annotation prompts will consume.
"""
import glob, json, os, sys

MIN_TURN_WORDS = 5   # runs shorter than this are backchannels: absorbed, don't split
GAP_S = 1.0

def turns_from(diar):
    words = [w for s in diar["segments"] for w in s["words"]]
    # 1. maximal same-speaker runs
    runs, cur = [], None
    for w in words:
        spk = "HOST" if w["spk"] == "HOST" else "GUEST"
        if cur and cur["spk"] == spk:
            cur["words"].append(w)
        else:
            if cur: runs.append(cur)
            cur = {"spk": spk, "words": [w]}
    if cur: runs.append(cur)
    # 2. a short run sandwiched between two runs of the same OTHER speaker is a
    #    backchannel: it does not open a turn boundary. Its words stay
    #    attributed to their real speaker (recorded in the enclosing turn's
    #    backchannel list) so word counts remain correct.
    turns = []
    i = 0
    while i < len(runs):
        r = runs[i]
        if (turns and len(r["words"]) < MIN_TURN_WORDS
                and i + 1 < len(runs)
                and turns[-1]["spk"] == runs[i+1]["spk"] != r["spk"]):
            turns[-1].setdefault("backchannels", []).append(
                {"spk": r["spk"], "text": "".join(w["w"] for w in r["words"]).strip()})
            turns[-1]["words"] += runs[i+1]["words"]
            i += 2
            continue
        if turns and turns[-1]["spk"] == r["spk"]:
            turns[-1]["words"] += r["words"]
        else:
            turns.append({"spk": r["spk"], "words": list(r["words"])})
        i += 1
    for t in turns:
        t["start"] = t["words"][0]["s"]; t["end"] = t["words"][-1]["e"]
        t["text"] = "".join(w["w"] for w in t["words"]).strip()
        t["n_words"] = len(t["words"])
        del t["words"]
    return turns

def main(scratch):
    outdir = os.path.join(scratch, "turns"); os.makedirs(outdir, exist_ok=True)
    rows = []
    for p in sorted(glob.glob(os.path.join(scratch, "transcripts_diarized", "*.json"))):
        d = json.load(open(p))
        ts = turns_from(d)
        dur_h = max(t["end"] for t in ts) / 3600
        host_turns = [t for t in ts if t["spk"] == "HOST"]
        json.dump([{"i": i, "spk": t["spk"], "text": t["text"]} for i, t in enumerate(ts)],
                  open(os.path.join(outdir, os.path.basename(p)), "w"))
        rows.append((d["file"][:50], len(ts), len(host_turns),
                     len(host_turns)/dur_h, sum(t["n_words"] for t in host_turns)/max(len(host_turns),1)))
        print(f"{rows[-1][0]:52s} turns={rows[-1][1]:4d} host_turns={rows[-1][2]:4d} "
              f"host_turns/h={rows[-1][3]:5.0f} mean_host_turn_words={rows[-1][4]:5.0f}")

if __name__ == "__main__":
    main(sys.argv[1])
