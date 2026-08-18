#!/usr/bin/env python3
"""WS3 / V3 gate: score the PI's blind speaker labels against pipeline output.

Gate (PILOT_PLAN WS3): host-attribution accuracy >= 90%.

The PI estimated host share of speech for each 2-minute window. The pipeline
asserts a speaker for every word. We compare the two on the same window.

IMPORTANT — a tolerance was never pre-specified. The HOWTO said only
"comparing your host_pct against the pipeline's host share, clip by clip".
Choosing a tolerance now, after seeing the data, would let the analyst pick
the threshold that passes. So this script reports the FULL tolerance curve
and the mean absolute error, and leaves the gate call to the PI.

Pipeline host share for a window = HOST run seconds / all run seconds.
(Runs shorter than 3s were dropped at export, so this is approximate; the
error is small relative to the disagreements at issue.)

Usage: ws3_score_audit.py <labels.csv> [answer_key.json]
"""
import csv, json, re, sys

def pipeline_share(entry):
    tot = host = 0.0
    for r in entry["pipeline_runs"]:
        d = r["end"] - r["start"]
        tot += d
        if r["spk"] == "HOST":
            host += d
    return (100.0 * host / tot) if tot else None

def read_labels(path):
    out = {}
    for row in csv.DictReader(open(path)):
        cid = (row.get("id") or "").strip()
        if not re.fullmatch(r"A\d\d", cid):
            continue          # instruction rows ride along; ignore them
        pct = (row.get("host_pct") or "").strip()
        if not pct:
            continue
        out[cid] = {"host_pct": float(pct),
                    "who": (row.get("who_dominates") or "").strip().upper(),
                    "third": (row.get("third_voice") or "").strip().upper(),
                    "notes": (row.get("notes") or "").strip()}
    return out

def main(labels_csv, key_json="research/pilot/audit/answer_key.json"):
    labels = read_labels(labels_csv)
    key = {e["id"]: e for e in json.load(open(key_json))}
    rows = []
    for cid in sorted(labels):
        e = key.get(cid)
        if not e:
            print(f"  ! {cid} has no answer-key entry, skipped"); continue
        p = pipeline_share(e)
        h = labels[cid]["host_pct"]
        rows.append({"id": cid, "episode": e["episode"], "flagged": e["flagged"],
                     "pi": h, "pipe": p, "err": None if p is None else p - h,
                     "third": labels[cid]["third"], "notes": labels[cid]["notes"]})

    print(f"{'id':4} {'flag':5} {'PI%':>6} {'pipe%':>7} {'diff':>7}  episode")
    for r in rows:
        pipe = "n/a" if r["pipe"] is None else f'{r["pipe"]:.1f}'
        diff = "n/a" if r["err"] is None else f'{r["err"]:+.1f}'
        print(f'{r["id"]:4} {"FLAG" if r["flagged"] else "":5} '
              f'{r["pi"]:6.0f} {pipe:>7} {diff:>7}  {r["episode"][:44]}')

    scored = [r for r in rows if r["err"] is not None]
    n = len(scored)
    mae = sum(abs(r["err"]) for r in scored) / n
    bias = sum(r["err"] for r in scored) / n
    print(f"\nn = {n} scored clips")
    print(f"mean absolute error : {mae:.1f} pp")
    print(f"mean signed error   : {bias:+.1f} pp  (positive = pipeline claims MORE host than the PI heard)")

    print("\nagreement rate by tolerance (none was pre-specified — reported as a curve):")
    for tol in (5, 10, 15, 20, 25, 30):
        k = sum(1 for r in scored if abs(r["err"]) <= tol)
        print(f"  within +/-{tol:2} pp : {k:2}/{n}  = {100*k/n:5.1f}%")

    fl = [r for r in scored if r["flagged"]]
    if fl:
        print("\nQA-flagged episodes (the pending exclusion question):")
        for r in fl:
            print(f'  {r["id"]}  PI heard {r["pi"]:.0f}% host, pipeline claims {r["pipe"]:.1f}%  '
                  f'-> gap {r["err"]:+.1f} pp   {r["episode"][:44]}')

    third = [r["id"] for r in rows if r["third"] == "Y"]
    print(f"\nclips where the PI heard a third voice: {third or 'none'}")
    notes = [(r["id"], r["notes"]) for r in rows if r["notes"]]
    if notes:
        print("PI notes:")
        for cid, nt in notes:
            print(f"  {cid}: {nt}")

    json.dump(rows, open("research/pilot/results/v3_audit_scored.json", "w"), indent=1)
    return rows

if __name__ == "__main__":
    main(*sys.argv[1:])
