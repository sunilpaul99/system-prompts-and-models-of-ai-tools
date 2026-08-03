#!/usr/bin/env python3
"""WS3 QA: flag structurally implausible diarization.

Motivation (2026-08-03): two interview episodes came through with
host_word_share ~0.999 — impossible for a two-person interview, and both
had weak host-cluster similarity (0.50, 0.31). The existing HOST_SIM_MIN
gate (0.30) passed them because it only asks "is the best cluster close
enough to the host?", never "is the resulting SPLIT plausible?".

Rule: for a known two-voice interview format, a host share outside
[0.15, 0.75] is a diarization failure regardless of similarity. Flagged
episodes are reported, never silently dropped; whether they are EXCLUDED
from analysis is a PI decision (exclusions are never self-ratified).
"""
import glob, json, os, sys

SHARE_MIN, SHARE_MAX = 0.15, 0.75
SIM_WARN = 0.55

def audit(scratch, ddir="transcripts_diarized_det2", skip="mbmbam"):
    rows = []
    for p in sorted(glob.glob(os.path.join(scratch, ddir, "*.json"))):
        b = os.path.basename(p)
        if skip and skip in b.lower(): continue
        d = json.load(open(p))
        share, sim = d["host_word_share"], d["host_cluster_sim"]
        flags = []
        if not (SHARE_MIN <= share <= SHARE_MAX): flags.append("IMPLAUSIBLE_SHARE")
        if sim < SIM_WARN: flags.append("WEAK_SIM")
        rows.append({"episode": b.replace(".json", ""), "host_share": round(share, 3),
                     "host_sim": round(sim, 3), "k": d["k"], "flags": flags})
    return rows

def main(scratch, ddir="transcripts_diarized_det2"):
    rows = audit(scratch, ddir)
    bad = [r for r in rows if r["flags"]]
    print(f"WS3 QA: {len(rows)} interview episodes audited, {len(bad)} flagged")
    for r in bad:
        print(f'  {r["episode"][:46]:48s} share={r["host_share"]:.3f} '
              f'sim={r["host_sim"]:.2f} k={r["k"]} {",".join(r["flags"])}')
    out = os.path.join(scratch, "ws3_qa_flags.json")
    json.dump(rows, open(out, "w"), indent=1)
    hw_bad = len(bad) / max(len(rows), 1)
    print(f"\nflagged fraction: {hw_bad:.1%} — PI decides exclusion "
          f"(agent does not self-ratify exclusions)")

if __name__ == "__main__":
    main(*sys.argv[1:])
