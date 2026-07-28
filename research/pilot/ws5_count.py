#!/usr/bin/env python3
"""WS5: lexical fingerprint counting on host-attributed speech.

Reads diarized transcripts, counts fingerprint- and placebo-candidate
occurrences in HOST-attributed words, applies the section 5.5 meta-mention
rule (flag occurrences within N words of explicit AI-language references;
N=50 primary, 0/20 sensitivity), and emits per-episode counts + context
snippets for every fingerprint hit (for the 5% PI audit and sense checks).

NO exposure contrasts are computed here (pilot hosts carry no exposure
labels; the peeking rule forbids contrasts in the full study anyway).
"""
import glob, json, os, re, sys

FINGERPRINT = {"delve": ["delve", "delves", "delved", "delving"],
               "meticulous": ["meticulous", "meticulously"],
               "intricate": ["intricate", "intricacies", "intricacy"],
               "underscore": ["underscore", "underscores", "underscored", "underscoring"],
               "showcase": ["showcase", "showcases", "showcased", "showcasing"],
               "boast": ["boast", "boasts", "boasted", "boasting"],
               "pivotal": ["pivotal"], "realm": ["realm", "realms"],
               "bolster": ["bolster", "bolsters", "bolstered", "bolstering"],
               "commendable": ["commendable"], "surpass": ["surpass", "surpasses", "surpassed"],
               "adept": ["adept"], "garner": ["garner", "garners", "garnered"],
               "noteworthy": ["noteworthy"], "multifaceted": ["multifaceted"]}
PLACEBO = {"emphasize": ["emphasize", "emphasizes", "emphasized"],
           "highlight": ["highlight", "highlights", "highlighted"],
           "complex": ["complex"], "notable": ["notable", "notably"],
           "remarkable": ["remarkable", "remarkably"], "domain": ["domain", "domains"],
           "strengthen": ["strengthen", "strengthens", "strengthened"],
           "impressive": ["impressive"], "exceed": ["exceed", "exceeds", "exceeded"],
           "skilled": ["skilled"], "gather": ["gather", "gathered", "gathering"],
           "significant": ["significant", "significantly"], "essential": ["essential"],
           "profound": ["profound", "profoundly"]}
AI_REFS = re.compile(r"\b(chatgpt|gpt|claude|gemini|copilot|llm|llms|large language|"
                     r"language model|openai|anthropic|chatbot|chatbots|ai)\b", re.I)

def norm(w): return re.sub(r"[^a-z']", "", w.lower())

def count_episode(path, window=50):
    d = json.load(open(path))
    words = [w for s in d["segments"] for w in s["words"]]
    all_norm = [norm(w["w"]) for w in words]
    ai_idx = [i for i, t in enumerate(all_norm) if AI_REFS.fullmatch(t)]
    lemma = {}
    for fam, forms in list(FINGERPRINT.items()) + list(PLACEBO.items()):
        for f in forms: lemma[f] = fam
    host_words = 0; counts = {}; hits = []
    for i, w in enumerate(words):
        if w["spk"] != "HOST": continue
        host_words += 1
        t = all_norm[i]
        fam = lemma.get(t)
        if not fam: continue
        near_ai = any(abs(i - j) <= window for j in ai_idx)
        kind = "fingerprint" if fam in FINGERPRINT else "placebo"
        key = (kind, fam, "meta" if near_ai else "clean")
        counts[key] = counts.get(key, 0) + 1
        ctx = "".join(x["w"] for x in words[max(0, i-12):i+13]).strip()
        hits.append({"family": fam, "kind": kind, "near_ai": near_ai,
                     "t": w["s"], "context": ctx})
    return {"file": d["file"], "host_words": host_words, "status": d["status"],
            "counts": {f"{k[0]}:{k[1]}:{k[2]}": v for k, v in counts.items()},
            "hits": hits}

def main(scratch):
    out = []
    for p in sorted(glob.glob(os.path.join(scratch, "transcripts_diarized", "*.json"))):
        r = count_episode(p)
        out.append(r)
        fp = sum(v for k, v in r["counts"].items() if k.startswith("fingerprint"))
        pl = sum(v for k, v in r["counts"].items() if k.startswith("placebo"))
        print(f'{r["file"][:55]:57s} host_words={r["host_words"]:6d} fp={fp} placebo={pl}')
    json.dump(out, open(os.path.join(scratch, "ws5_counts.json"), "w"), indent=1)
    hw = sum(r["host_words"] for r in out)
    fp = sum(v for r in out for k, v in r["counts"].items() if k.startswith("fingerprint"))
    pl = sum(v for r in out for k, v in r["counts"].items() if k.startswith("placebo"))
    print(f"\nTOTAL: {hw} host words | fingerprint {fp} ({fp/max(hw,1)*1e5:.1f}/100k) "
          f"| placebo {pl} ({pl/max(hw,1)*1e5:.1f}/100k)")

if __name__ == "__main__":
    main(sys.argv[1])
