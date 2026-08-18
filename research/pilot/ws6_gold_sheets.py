#!/usr/bin/env python3
"""WS6: generate the rater's G1/G2 gold-label sheets (RATER_RUBRIC.md).

Design, per the rubric and PROTOCOL §5.2:

G1 (300 items) — "is this a disagreement exchange?" windows: the preceding
GUEST turn plus the HOST turn under judgment. Stratified half candidate /
half non-candidate BY STAGE-1's OWN LABELS, so the sheet measures both the
model's precision (on flagged turns) and its miss rate (on unflagged ones).
The rater never sees which is which.

G2 (200 items) — the four-question turn labelling (concessive opener,
both-sides, bald contradiction, hedges), drawn from Stage-1 CANDIDATES,
because the H1-R features are defined within disagreement turns.

Anonymization: speakers render as HOST/GUEST only; known host names and
guest names (from episode filenames) are replaced with [HOST]/[GUEST] in
the text. Residual name leakage is possible — the rubric instructs the
rater not to guess or look up speakers.

Blinding: item order is seeded-shuffled; the answer key (item -> episode,
turn, stage-1 label) stays PRIVATE with the PI packet. Sheets and key are
NOT committed — they contain transcript text (§9 counts-only posture).
The first 30 rows of each sheet are the calibration block (rubric).

SEED = 20260818.
"""
import csv, glob, json, os, random, re, sys

SEED = 20260818
G1_N, G2_N = 300, 200
CAL = 30  # calibration rows at the top of each sheet

HOST_NAMES = ["Lex Fridman", "Lex", "Fridman", "Russ Roberts", "Russ", "Roberts"]


def guest_names(base):
    """Candidate guest-name tokens from the episode filename."""
    m = re.sub(r"^\d{4}-\d{2}-\d{2}_+(\d+_)?", "", base)
    toks = [t for t in m.split("_") if t and t[0].isupper()]
    # bigrams first so full names match before bare surnames
    names = [" ".join(toks[i:i + 2]) for i in range(len(toks) - 1)] + toks
    return [n for n in names if len(n) > 3]


def anon(text, base):
    for n in HOST_NAMES:
        text = re.sub(rf"\b{re.escape(n)}\b", "[HOST]", text)
    for n in guest_names(base):
        text = re.sub(rf"\b{re.escape(n)}\b", "[GUEST]", text)
    return text


def load(scratch):
    """(episode, show, era, turns list, stage1 labels by turn_id)."""
    labels = {e["episode"]: {t["turn_id"]: t for t in e["labels"]}
              for e in json.load(open(
                  "research/pilot/results/ws6_stage1_labels.json"))["episodes"]}
    eps = []
    for p in sorted(glob.glob(os.path.join(scratch, "ws6_input", "*.json"))):
        base = os.path.basename(p)[:-5]
        turns = json.load(open(p))
        show = "lex" if "__" in base else "econtalk"
        era = "era1" if base[:4] in ("2019", "2020", "2021") else "era2"
        eps.append((base, show, era, turns, labels.get(base, {})))
    return eps


def window(turns, tid):
    """Preceding GUEST turn (if any) + the host turn, rubric-style."""
    idx = {t["i"]: k for k, t in enumerate(turns)}
    k = idx[tid]
    prev = next((turns[j] for j in range(k - 1, -1, -1)
                 if turns[j]["spk"] == "GUEST"), None)
    return prev, turns[k]


def clip(s, n=900):
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " […]"


def main(scratch, outdir):
    rnd = random.Random(SEED)
    eps = load(scratch)
    pool_c, pool_n = [], []
    for base, show, era, turns, lab in eps:
        for t in turns:
            if t["spk"] != "HOST" or t["i"] not in lab:
                continue
            # G1 judges an exchange, so require a preceding guest turn
            prev, _ = window(turns, t["i"])
            rec = (base, show, era, turns, t, lab[t["i"]]["candidate"])
            if prev is None:
                continue
            (pool_c if lab[t["i"]]["candidate"] else pool_n).append(rec)

    # G1: half candidates, half non-candidates, stratified by show x era
    def stratified(pool, n):
        cells = {}
        for r in pool:
            cells.setdefault((r[1], r[2]), []).append(r)
        take, out = n // len(cells), []
        for key in sorted(cells):
            rnd.shuffle(cells[key])
            out += cells[key][:take]
        rest = [r for key in sorted(cells) for r in cells[key][take:]]
        rnd.shuffle(rest)
        return out + rest[:n - len(out)]

    g1_c = stratified(pool_c, min(G1_N // 2, len(pool_c)))
    g1_n = stratified(pool_n, G1_N - len(g1_c))
    g1 = g1_c + g1_n
    rnd.shuffle(g1)

    # G2: candidates only (features are defined within disagreement turns)
    g2 = stratified(pool_c, min(G2_N, len(pool_c)))
    rnd.shuffle(g2)

    os.makedirs(outdir, exist_ok=True)
    key = []

    w1 = csv.writer(open(os.path.join(outdir, "G1_sheet.csv"), "w"))
    w1.writerow(["item", "block", "guest_says", "host_says",
                 "answer_YES_NO-noconflict_NO-excluded_UNSURE", "notes"])
    for i, (base, show, era, turns, t, cand) in enumerate(g1, 1):
        prev, cur = window(turns, t["i"])
        w1.writerow([f"G1-{i:03}", "calibration" if i <= CAL else "main",
                     clip(anon(prev["text"], base)),
                     clip(anon(cur["text"], base)), "", ""])
        key.append({"item": f"G1-{i:03}", "episode": base, "turn_id": t["i"],
                    "show": show, "era": era, "stage1_candidate": cand})

    w2 = csv.writer(open(os.path.join(outdir, "G2_sheet.csv"), "w"))
    w2.writerow(["item", "block", "context_guest", "host_turn",
                 "q1_concessive_opener_YN", "q2_both_sides_YN",
                 "q3_bald_contradiction_YN", "q4_hedges_list", "notes"])
    for i, (base, show, era, turns, t, cand) in enumerate(g2, 1):
        prev, cur = window(turns, t["i"])
        w2.writerow([f"G2-{i:03}", "calibration" if i <= CAL else "main",
                     clip(anon(prev["text"], base), 400),
                     anon(cur["text"], base), "", "", "", "", ""])
        key.append({"item": f"G2-{i:03}", "episode": base, "turn_id": t["i"],
                    "show": show, "era": era, "stage1_candidate": cand})

    json.dump({"seed": SEED, "items": key},
              open(os.path.join(outdir, "gold_answer_key_PRIVATE.json"), "w"),
              indent=1)
    print(f"G1: {len(g1)} items ({len(g1_c)} stage1-candidates, {len(g1_n)} non)")
    print(f"G2: {len(g2)} items (candidates only)")
    print(f"-> {outdir} (sheets + PRIVATE key; not for commit)")


if __name__ == "__main__":
    main(*sys.argv[1:])
