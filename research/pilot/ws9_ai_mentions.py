#!/usr/bin/env python3
"""WS9 (exploratory): AI-mention density per episode, by speaker.

Candidate cheap exposure proxy (PI idea, 2026-09-10): how much a host TALKS
about AI/LLMs, time-anchored per episode. This is a TOPIC feature, not an
exposure label, so computing it does not touch the §2 peeking rule.

Two tiers, reported separately:
  strict — named LLM products / the term itself (ChatGPT, GPT, Claude,
           Gemini, Copilot, LLM, large language model, OpenAI, Anthropic)
  broad  — strict + generic "AI", "artificial intelligence", "chatbot",
           "machine learning"
Generic "AI" is common in 2019-21 speech (self-driving cars, AlphaGo), so
the strict tier is the one that tracks LLM-era exposure; broad is the
pre-trend check.

Host and guest are counted separately: host density is the candidate
proxy; guest density is the topic-of-conversation control (if a guest
drives all the AI talk, the host's own mention rate still tells you
something, but the episode's topic contamination is high either way).

Outputs COUNTS ONLY (no text) -> results/ws9_ai_mentions.json.

Usage: ws9_ai_mentions.py <turns_dir>   (turns files: list of {i,spk,text})
"""
import glob, json, os, re, sys

STRICT = [r"chat\s?gpt", r"\bgpt[-\s]?\d*\b", r"\bclaude\b", r"\bgemini\b",
          r"\bcopilot\b", r"\bllms?\b", r"large language models?",
          r"language models?", r"\bopen\s?ai\b", r"\banthropic\b"]
BROAD = STRICT + [r"\bai\b", r"artificial intelligence", r"chat\s?bots?\b",
                  r"machine learning", r"\ba\.i\.\b"]

def count(text, pats):
    t = text.lower()
    return sum(len(re.findall(p, t)) for p in pats)

def words(text):
    return len(text.split())

def main(turns_dir):
    ex = {e["file"].replace(".mp3", "") for e in json.load(
        open("research/pilot/results/exclusions_ratified.json"))["episodes"]}
    rows = []
    for p in sorted(glob.glob(os.path.join(turns_dir, "*.json"))):
        base = os.path.basename(p)[:-5]
        if base in ex or "mbmbam" in base.lower():
            continue
        turns = json.load(open(p))
        agg = {"HOST": [0, 0, 0], "GUEST": [0, 0, 0]}   # words, strict, broad
        for t in turns:
            s = t.get("spk")
            if s not in agg:
                continue
            agg[s][0] += words(t["text"])
            agg[s][1] += count(t["text"], STRICT)
            agg[s][2] += count(t["text"], BROAD)
        host = "lex" if "__" in base else "econtalk"
        era = "pre" if base[:4] in ("2019", "2020", "2021") else "post"
        r = {"episode": base, "host": host, "era": era, "year": base[:4]}
        for s, (w, st, br) in agg.items():
            k = s.lower()
            r[f"{k}_words"] = w
            r[f"{k}_strict"] = st
            r[f"{k}_broad"] = br
            r[f"{k}_strict_per1k"] = round(1000 * st / w, 3) if w else None
            r[f"{k}_broad_per1k"] = round(1000 * br / w, 3) if w else None
        rows.append(r)

    # host x era summary
    summ = {}
    for r in rows:
        k = f'{r["host"]}_{r["era"]}'
        s = summ.setdefault(k, {"episodes": 0, "host_words": 0, "host_strict": 0,
                                "host_broad": 0, "guest_words": 0,
                                "guest_strict": 0, "guest_broad": 0,
                                "episodes_with_any_host_strict": 0})
        s["episodes"] += 1
        for f in ("host_words", "host_strict", "host_broad",
                  "guest_words", "guest_strict", "guest_broad"):
            s[f] += r[f]
        if r["host_strict"] > 0:
            s["episodes_with_any_host_strict"] += 1
    for k, s in summ.items():
        s["host_strict_per1k"] = round(1000 * s["host_strict"] / s["host_words"], 3)
        s["host_broad_per1k"] = round(1000 * s["host_broad"] / s["host_words"], 3)
        s["guest_strict_per1k"] = round(1000 * s["guest_strict"] / s["guest_words"], 3)

    print(f'{"cell":14} {"eps":>3} {"host strict/1k":>14} {"host broad/1k":>13} '
          f'{"guest strict/1k":>15} {"eps w/ any":>10}')
    for k in sorted(summ):
        s = summ[k]
        print(f'{k:14} {s["episodes"]:3} {s["host_strict_per1k"]:14.3f} '
              f'{s["host_broad_per1k"]:13.3f} {s["guest_strict_per1k"]:15.3f} '
              f'{s["episodes_with_any_host_strict"]:>4}/{s["episodes"]}')
    print("\nper-episode (host strict/1k, sorted):")
    for r in sorted(rows, key=lambda r: -(r["host_strict_per1k"] or 0)):
        print(f'  {r["host_strict_per1k"] or 0:6.3f}  {r["host_strict"]:3}  '
              f'{r["era"]:4} {r["episode"][:50]}')

    json.dump({"note": "Exploratory topic feature; counts only. Strict = named "
                       "LLM products/terms; broad adds generic AI.",
               "episodes": rows, "summary": summ},
              open("research/pilot/results/ws9_ai_mentions.json", "w"), indent=1)

if __name__ == "__main__":
    main(*sys.argv[1:])
