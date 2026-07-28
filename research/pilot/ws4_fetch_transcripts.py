#!/usr/bin/env python3
"""WS4: fetch EconTalk human transcripts for the sampled episodes.

Maps sampled EconTalk episodes to their econtalk.org page via the feed's
<link> element (title match), fetches the page, extracts the transcript as
(speaker, time, text) turns, and saves JSON + raw HTML to scratchpad
(ground truth is not committed to the repo - only derived metrics are).
"""
import csv, html, json, os, re, sys, time, urllib.request
import xml.etree.ElementTree as ET

def feed_links(feed_path):
    root = ET.parse(feed_path).getroot()
    out = {}
    for item in root.iter("item"):
        t = (item.findtext("title") or "").strip()
        l = (item.findtext("link") or "").strip()
        if t and l: out[t] = l
    return out

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research pilot; transcript alignment)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")

SPEAKER_RE = re.compile(r"^([A-Z][A-Za-z.\- ]{2,40}):\s*(.*)$")
TIME_RE = re.compile(r"^\d{1,2}:\d{2}(:\d{2})?$")

def parse_transcript(page_html):
    """Extract speaker turns from an econtalk.org episode page."""
    # transcript paragraphs live after the 'AUDIO TRANSCRIPT' heading
    body = page_html
    m = re.search(r"AUDIO\s+TRANSCRIPT", body, re.I)
    if m: body = body[m.end():]
    # cut at reader comments / related-episodes footer; a marker only counts
    # if it appears well into the body (>5000 chars), else it's nav/sidebar
    cut = len(body)
    for marker in (r"READER\s+COMMENTS", r"COMMENTS\s*\(", r"id=\"comments\"",
                   r"class=\"comments", r"More\s+EconTalk\s+Episodes"):
        mm = re.search(marker, body, re.I)
        if mm and mm.start() > 5000: cut = min(cut, mm.start())
    body = body[:cut]
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S | re.I)
    paras = re.findall(r"<p[^>]*>(.*?)</p>", text, flags=re.S)
    turns, cur = [], None
    for p in paras:
        p = html.unescape(re.sub(r"<[^>]+>", " ", p))
        p = re.sub(r"\s+", " ", p).strip()
        if not p: continue
        m = SPEAKER_RE.match(p)
        if m and not TIME_RE.match(m.group(1)) and len(m.group(1).split()) <= 4 \
                and all(w[0].isupper() for w in m.group(1).split() if w[0].isalpha()):
            if cur: turns.append(cur)
            cur = {"speaker": m.group(1), "text": m.group(2)}
        elif cur:
            cur["text"] += " " + p
    if cur: turns.append(cur)
    return turns

def main(scratch):
    links = feed_links(os.path.join(scratch, "econtalk.xml"))
    outdir = os.path.join(scratch, "ws4_ground_truth"); os.makedirs(outdir, exist_ok=True)
    rows = [r for r in csv.DictReader(open(os.path.join(os.path.dirname(__file__), "manifests", "pilot_sample_48.csv")))
            if r["host"] == "econtalk"]
    report = []
    for r in rows:
        url = links.get(r["title"])
        base = r["date"] + "_" + re.sub(r"[^A-Za-z0-9]+", "_", r["title"])[:60]
        out = os.path.join(outdir, base + ".json")
        if os.path.exists(out):
            report.append((r["title"], "cached")); continue
        if not url:
            report.append((r["title"], "NO-LINK")); continue
        try:
            raw = os.path.join(outdir, base + ".html")
            if os.path.exists(raw):
                page = open(raw).read()
            else:
                page = fetch(url)
                open(raw, "w").write(page)   # keep raw HTML so parser fixes never need refetch
            turns = parse_transcript(page)
            if not turns:
                report.append((r["title"], "PARSE-EMPTY (raw kept)")); continue
            words = sum(len(t["text"].split()) for t in turns)
            json.dump({"title": r["title"], "date": r["date"], "url": url,
                       "turns": turns, "word_count": words}, open(out, "w"))
            report.append((r["title"], f"{len(turns)} turns, {words} words"))
        except Exception as e:
            report.append((r["title"], f"ERR {e}"))
        time.sleep(45)  # polite pacing: 6s tripped econtalk.org's rate limit (403) on 2026-07-28
    for t, s in report: print(f"{t[:55]:57s} {s}")

if __name__ == "__main__":
    main(sys.argv[1])
