#!/usr/bin/env python3
"""WS1: build per-host episode manifests from saved RSS feeds and draw the
stratified pilot sample (PILOT_PLAN WS1: 8 episodes/host/era-block).

Era blocks: 2019-01-01..2021-12-31 and 2023-01-01..2025-12-31.
Eligibility: duration >= 20 min where duration is known; title-rule
exclusions for rebroadcasts/compilations/guest-host episodes (logged).
Sampling: random.Random(SEED) per host+block, sorted candidate list, so the
draw is reproducible from the committed feed snapshots.
"""
import csv, email.utils, json, random, re, sys, xml.etree.ElementTree as ET
from pathlib import Path

SEED = 20260728
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"

# title-based exclusion rules (case-insensitive), logged per PILOT_PLAN WS1
EXCLUDE_PATTERNS = [
    r"\brebroadcast\b", r"\bre-?release\b", r"\bre-?run\b", r"\bbest of\b",
    r"\bcompilation\b", r"\bhighlights?\b", r"\btrailer\b", r"\bannouncement\b",
    r"\bintroducing\b", r"\bpresents\b", r"\bcrossover\b", r"\bguest host\b",
]

def parse_duration(s):
    if not s: return None
    s = s.strip()
    if re.fullmatch(r"\d+", s):  # seconds
        return int(s)
    parts = s.split(":")
    try:
        parts = [int(p) for p in parts]
    except ValueError:
        return None
    if len(parts) == 3: return parts[0]*3600 + parts[1]*60 + parts[2]
    if len(parts) == 2: return parts[0]*60 + parts[1]
    return None

def load(feed_path):
    root = ET.parse(feed_path).getroot()
    eps = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        pub = item.findtext("pubDate")
        try:
            dt = email.utils.parsedate_to_datetime(pub.strip())
        except Exception:
            continue
        enc = item.find("enclosure")
        eps.append({
            "title": title,
            "date": dt.date().isoformat(),
            "duration_s": parse_duration(item.findtext(f"{ITUNES}duration")),
            "enclosure_url": enc.get("url") if enc is not None else None,
            "enclosure_bytes": enc.get("length") if enc is not None else None,
            "guid": (item.findtext("guid") or "").strip(),
        })
    eps.sort(key=lambda e: (e["date"], e["guid"]))
    return eps

def in_block(date, block):
    return block[0] <= date <= block[1]

BLOCKS = {"era1_2019_2021": ("2019-01-01", "2021-12-31"),
          "era2_2023_2025": ("2023-01-01", "2025-12-31")}

def eligible(ep, log, host):
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, ep["title"], re.I):
            log.append({"host": host, "title": ep["title"], "date": ep["date"],
                        "rule": pat})
            return False
    if ep["duration_s"] is not None and ep["duration_s"] < 20*60:
        log.append({"host": host, "title": ep["title"], "date": ep["date"],
                    "rule": "duration<20min"})
        return False
    if not ep["enclosure_url"]:
        log.append({"host": host, "title": ep["title"], "date": ep["date"],
                    "rule": "no-enclosure"})
        return False
    return True

def main(scratch):
    hosts = {"lex_fridman": "lex.xml", "econtalk": "econtalk.xml",
             "mbmbam": "mbmbam.xml"}
    outdir = Path(__file__).parent
    excl_log, sample = [], []
    for host, fname in hosts.items():
        eps = load(Path(scratch) / fname)
        with open(outdir / f"{host}_manifest.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(eps[0].keys()))
            w.writeheader(); w.writerows(eps)
        for block, rng in BLOCKS.items():
            pool = [e for e in eps if in_block(e["date"], rng)
                    and eligible(e, excl_log, host)]
            rnd = random.Random(f"{SEED}:{host}:{block}")
            picks = sorted(rnd.sample(pool, 8), key=lambda e: e["date"])
            for e in picks:
                sample.append({"host": host, "block": block, **e})
        print(f"{host}: {len(eps)} episodes -> manifest")
    with open(outdir / "pilot_sample_48.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sample[0].keys()))
        w.writeheader(); w.writerows(sample)
    with open(outdir / "exclusion_log.json", "w") as f:
        json.dump({"seed": SEED, "patterns": EXCLUDE_PATTERNS,
                   "excluded": excl_log}, f, indent=1)
    tot = sum(e["duration_s"] or 0 for e in sample)
    print(f"sample: {len(sample)} episodes, ~{tot/3600:.1f} known-duration hours,"
          f" {len(excl_log)} exclusions logged")

if __name__ == "__main__":
    main(sys.argv[1])
