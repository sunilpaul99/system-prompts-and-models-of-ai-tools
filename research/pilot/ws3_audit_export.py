#!/usr/bin/env python3
"""WS3 / V3 audit export: stratified segments for PI speaker-labelling.

PILOT_PLAN WS3: "agent selects 24 stratified segments (host x era x format),
PI labels speaker identity for ~2 minutes each against pipeline output;
attribution accuracy target >=90%."

Stratification (interview formats only, per the 2026-08-03 decision):
  host (econtalk / lex) x era (2019-21 / 2023-25), plus a deliberate
  oversample of the two QA-flagged episodes so the PI's ears directly
  settle the pending exclusion question.

Lex is weighted higher than EconTalk: EconTalk attribution is already
externally validated against published human transcripts (within ~2pp),
whereas Lex publishes none, so the audit is his only validation route.

Segment choice is seeded and reproducible. Windows avoid the first 120s
(intros/sponsor reads are host-solo and would flatter the pipeline).

Outputs:
  audit/clips/<id>.wav          2-min excerpts (scratchpad; audio not committed per §9)
  audit/V3_AUDIT_SHEET.md       the labelling sheet (committed; contains no audio)
  audit/answer_key.json         pipeline labels, for scoring AFTER the PI labels
"""
import glob, json, os, random, sys, wave
import numpy as np

SEED = 20260803
SR = 16000
CLIP_S = 120
SKIP_HEAD_S = 120

def decode(mp3, t0, t1):
    import av
    c = av.open(mp3); s = c.streams.audio[0]
    r = av.AudioResampler(format="s16", layout="mono", rate=SR)
    buf = []
    c.seek(int(t0 / s.time_base), stream=s)
    for fr in c.decode(s):
        t = float(fr.pts * s.time_base)
        if t < t0 - 1: continue
        if t > t1: break
        for rf in r.resample(fr): buf.append(rf.to_ndarray())
    if not buf: return np.zeros(0, dtype=np.int16)
    return np.concatenate(buf, axis=1)[0].astype(np.int16)

def pipeline_labels(diar, t0, t1):
    """Speaker timeline the pipeline asserts for this window, as runs."""
    runs, cur = [], None
    for s in diar["segments"]:
        for w in s["words"]:
            mid = (w["s"] + w["e"]) / 2
            if not (t0 <= mid <= t1): continue
            if cur and cur["spk"] == w["spk"]:
                cur["end"] = w["e"]
            else:
                if cur: runs.append(cur)
                cur = {"spk": w["spk"], "start": w["s"], "end": w["e"]}
    if cur: runs.append(cur)
    return [r for r in runs if r["end"] - r["start"] >= 3.0]

def main(scratch, n_total="24"):
    n_total = int(n_total)
    rnd = random.Random(SEED)
    flags = {r["episode"]: r["flags"] for r in
             json.load(open(os.path.join(scratch, "ws3_qa_flags.json")))}
    eps = []
    for p in sorted(glob.glob(os.path.join(scratch, "transcripts_diarized_det2", "*.json"))):
        b = os.path.basename(p).replace(".json", "")
        if "mbmbam" in b.lower(): continue
        host = "lex" if "__" in b else "econtalk"
        era = "era1" if b[:4] in ("2019", "2020", "2021") else "era2"
        eps.append({"base": b, "path": p, "host": host, "era": era,
                    "flagged": bool(flags.get(b))})
    # quota: lex weighted 2:1 over econtalk; flagged episodes always included
    flagged = [e for e in eps if e["flagged"]]
    quota = {("lex", "era1"): 6, ("lex", "era2"): 6,
             ("econtalk", "era1"): 3, ("econtalk", "era2"): 3}
    picks = list(flagged)
    for (h, er), q in quota.items():
        pool = [e for e in eps if e["host"] == h and e["era"] == er and not e["flagged"]]
        picks += rnd.sample(pool, min(q, len(pool)))
    # one window per picked episode, up to n_total
    picks = picks[:n_total]
    outdir = os.path.join(scratch, "audit"); clips = os.path.join(outdir, "clips")
    os.makedirs(clips, exist_ok=True)
    sheet, key = [], []
    for i, e in enumerate(picks, 1):
        d = json.load(open(e["path"]))
        words = [w for s in d["segments"] for w in s["words"]]
        if not words: continue
        last = words[-1]["e"]
        t0 = rnd.uniform(SKIP_HEAD_S, max(SKIP_HEAD_S + 1, last - CLIP_S - 60))
        t1 = t0 + CLIP_S
        mp3 = glob.glob(os.path.join(scratch, "audio", "*", e["base"] + ".mp3"))
        cid = f"A{i:02d}"
        if mp3:
            a = decode(mp3[0], t0, t1)
            w = wave.open(os.path.join(clips, f"{cid}.wav"), "wb")
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes(a.tobytes()); w.close()
        runs = pipeline_labels(d, t0, t1)
        sheet.append({"id": cid, "episode": e["base"], "host": e["host"],
                      "era": e["era"], "start_s": round(t0, 1), "end_s": round(t1, 1),
                      "n_runs": len(runs)})
        key.append({"id": cid, "episode": e["base"], "flagged": e["flagged"],
                    "window": [round(t0, 1), round(t1, 1)],
                    "pipeline_runs": [{"spk": r["spk"], "start": round(r["start"], 1),
                                       "end": round(r["end"], 1)} for r in runs]})
    json.dump(key, open(os.path.join(outdir, "answer_key.json"), "w"), indent=1)
    print(f"exported {len(sheet)} audit segments to {clips}")
    for s in sheet:
        print(f'  {s["id"]} {s["host"]:8s} {s["era"]} {s["start_s"]:8.1f}s '
              f'{s["episode"][:40]}')
    return sheet

if __name__ == "__main__":
    main(*sys.argv[1:])
