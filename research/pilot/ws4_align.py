#!/usr/bin/env python3
"""WS4/V1: ASR insertion/deletion measurement for candidate word lists.

For each episode with BOTH a human transcript (ws4_ground_truth) and a Whisper
transcript (transcripts), align token streams (difflib on normalized tokens)
and count, for each target word: matches, whisper-only occurrences
(insertions), human-only occurrences (deletions). The opening/closing
unmatched blocks (human transcripts start at the guest intro; audio starts at
0:00) are excluded from counting - only the aligned overlap region counts.

Word lists: fingerprint candidates are PROTOCOL section 5.1 verbatim.
Placebo list here is PROVISIONAL (WS5 freezes the real one with matching
tables); used only to check for gross fingerprint-vs-placebo ASR asymmetry.
"""
import difflib, glob, json, os, re, sys

FINGERPRINT = ["delve", "meticulous", "meticulously", "intricate", "intricacies",
               "underscore", "underscores", "underscored", "showcase", "showcases",
               "boast", "boasts", "pivotal", "realm", "realms", "bolster",
               "bolsters", "commendable", "surpass", "surpasses", "adept",
               "garner", "garners", "garnered", "noteworthy", "multifaceted",
               "delves", "delved", "delving"]
PLACEBO_PROVISIONAL = ["emphasize", "emphasizes", "highlight", "highlights",
                       "complex", "notable", "remarkable", "domain", "domains",
                       "strengthen", "strengthens", "impressive", "exceed",
                       "exceeds", "skilled", "gather", "gathered", "significant",
                       "essential", "profound"]

def norm_tokens(text):
    return [t for t in re.findall(r"[a-z']+", text.lower()) if t]

def episode_tokens_whisper(path):
    tr = json.load(open(path))
    toks = []
    for seg in tr["segments"]:
        toks += norm_tokens(seg["text"])
    return toks

def episode_tokens_human(path):
    gt = json.load(open(path))
    toks = []
    for turn in gt["turns"]:
        toks += norm_tokens(turn["text"])
    return toks

def align_counts(human, whisper, targets):
    sm = difflib.SequenceMatcher(a=human, b=whisper, autojunk=False)
    ops = sm.get_opcodes()
    # drop leading/trailing non-equal blocks (structural head/tail mismatch)
    while ops and ops[0][0] != "equal": ops.pop(0)
    while ops and ops[-1][0] != "equal": ops.pop()
    counts = {t: {"match": 0, "ins": 0, "del": 0} for t in targets}
    aligned_h = aligned_w = 0
    for tag, i1, i2, j1, j2 in ops:
        aligned_h += i2 - i1; aligned_w += j2 - j1
        if tag == "equal":
            for t in human[i1:i2]:
                if t in counts: counts[t]["match"] += 1
        else:
            for t in human[i1:i2]:
                if t in counts: counts[t]["del"] += 1
            for t in whisper[j1:j2]:
                if t in counts: counts[t]["ins"] += 1
    return counts, aligned_h, aligned_w

def merge(a, b):
    for k, v in b.items():
        d = a.setdefault(k, {"match": 0, "ins": 0, "del": 0})
        for kk in v: d[kk] += v[kk]

def main(scratch, tdir="transcripts"):
    targets = set(FINGERPRINT + PLACEBO_PROVISIONAL)
    tot_f = {"match": 0, "ins": 0, "del": 0}; tot_p = {"match": 0, "ins": 0, "del": 0}
    per_word, aligned_words = {}, 0
    pairs = 0
    for gt_path in sorted(glob.glob(os.path.join(scratch, "ws4_ground_truth", "*.json"))):
        base = os.path.basename(gt_path)[:10]  # date prefix
        wh = glob.glob(os.path.join(scratch, tdir, base + "*.json"))
        if not wh: continue
        human = episode_tokens_human(gt_path)
        whisper = episode_tokens_whisper(wh[0])
        counts, ah, aw = align_counts(human, whisper, targets)
        merge(per_word, counts)
        aligned_words += ah; pairs += 1
        print(f"{base}: aligned {ah} human tokens vs {aw} whisper tokens")
    for w, c in sorted(per_word.items()):
        if any(c.values()):
            tgt = tot_f if w in FINGERPRINT else tot_p
            for k in c: tgt[k] += c[k]
    print(f"\npairs={pairs}, aligned human words={aligned_words}")
    for name, tot in [("FINGERPRINT", tot_f), ("PLACEBO(prov)", tot_p)]:
        ins_rate = tot["ins"] / max(aligned_words, 1) * 100000
        del_rate = tot["del"] / max(aligned_words, 1) * 100000
        print(f"{name}: match={tot['match']} ins={tot['ins']} del={tot['del']} "
              f"-> ins/100k={ins_rate:.2f} del/100k={del_rate:.2f}")
    nz = {w: c for w, c in per_word.items() if c["ins"] or c["del"]}
    print("\nper-word nonzero ins/del:", json.dumps(nz, indent=1))
    json.dump({"pairs": pairs, "aligned_words": aligned_words,
               "per_word": per_word}, open(os.path.join(scratch, "ws4_v1_results.json"), "w"))

if __name__ == "__main__":
    main(sys.argv[1], *sys.argv[2:3])
