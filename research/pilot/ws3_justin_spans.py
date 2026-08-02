#!/usr/bin/env python3
"""WS3: harvest Justin McElroy enrollment spans from MBMBaM det2 transcripts.

Justin's reliable solo material is the show opener ("...welcome to My
Brother, My Brother and Me... I'm your oldest brother, Justin McElroy") —
only ~5-8s per episode, so spans are harvested across ALL sampled episodes
and pooled. Spans are text-anchored: located by matching the opener line in
the transcript, so each is automatically verified and PI-auditable (the
matched text is stored). Live "Face 2 Face" episodes are skipped (crowd
noise + atypical openings; logged).

Span rule: from the start of the segment containing "welcome to my brother"
(case-insensitive, fuzzy on punctuation) through the END of the segment
containing "oldest brother" — i.e., through Justin's self-introduction,
stopping before Travis speaks.
"""
import glob, json, os, re, sys

def harvest(scratch):
    spans, skipped = [], []
    for p in sorted(glob.glob(os.path.join(scratch, "transcripts_det2", "*MBMBaM*"))):
        t = json.load(open(p))
        base = os.path.basename(p).replace(".json", "")
        if re.search(r"face_?2_?face", base, re.I):
            skipped.append((base, "live episode")); continue
        segs = t["segments"]
        start_i = end_i = None
        for i, s in enumerate(segs):
            if s["start"] > 180: break
            txt = s["text"].lower()
            if start_i is None and re.search(r"welcome to my brother|everybody and welcome", txt):
                start_i = i
            if start_i is not None and re.search(r"oldest brother", txt):
                end_i = i; break
        if start_i is None or end_i is None:
            skipped.append((base, "opener not matched")); continue
        # guard: if welcome->self-intro spans >15s, banter (other brothers)
        # intervenes — use ONLY the self-intro segment (pure Justin)
        if segs[end_i]["end"] - segs[start_i]["start"] > 15:
            start_i = end_i
        spans.append({
            "file": base,
            "start": round(segs[start_i]["start"], 1),
            "end": round(segs[end_i]["end"], 1),
            "verified": "text-anchored: " + " / ".join(
                segs[j]["text"].strip()[:60] for j in range(start_i, end_i + 1)),
        })
    return spans, skipped

def main(scratch):
    spans, skipped = harvest(scratch)
    repo = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(repo, "enrollment_spans.json")
    d = json.load(open(p))
    d["mbmbam"] = spans
    json.dump(d, open(p, "w"), indent=1)
    tot = sum(s["end"] - s["start"] for s in spans)
    print(f"harvested {len(spans)} spans, {tot:.0f}s Justin-solo total")
    for s in spans: print(f'  {s["file"][:45]} [{s["start"]}-{s["end"]}]')
    for b, r in skipped: print(f"  SKIP {b[:45]}: {r}")

if __name__ == "__main__":
    main(sys.argv[1])
