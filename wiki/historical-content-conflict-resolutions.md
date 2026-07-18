# How Content-vs-Technology Conflicts Actually Got Resolved

*Wiki entry. Companion to `raw/content-economy-briefing.md` Ch. 1–2, which traces the harm pattern. This entry traces the resolution pattern: what mechanisms ended each conflict, and what they predict for publishers vs. AI. Last updated July 2026.*

## The case studies

### 1. Player pianos → the compulsory license (1908–1909)
Piano-roll makers copied sheet music into perforated rolls without paying composers. In *White-Smith v. Apollo* (1908) the Supreme Court held rolls were not "copies" — **the technology won in court**. Congress responded within a year: the 1909 Copyright Act created the first **compulsory mechanical license** — anyone may mechanically reproduce a song, but must pay a statutory rate. Creators lost the right to say no; they gained a guaranteed price. This mechanism (compulsory license + rate-setting) became the template reused for a century.

### 2. Radio → collective licensing (1920s–1941)
Radio played recorded music to mass audiences; no station could negotiate with thousands of songwriters, and no songwriter could police thousands of stations. Resolution: **collecting societies** (ASCAP, founded 1914) selling **blanket licenses**. When ASCAP overreached on rates in 1940, broadcasters founded a competitor (**BMI**) and boycotted ASCAP — and the DOJ imposed **antitrust consent decrees (1941)** with rate courts that still govern today. Lessons: collective licensing solves the many-to-many negotiation problem; a monopoly collective invites both competition and regulation; the buyers can build their own supply.

### 3. Cable TV retransmission → court loss, then legislative reversal (1968–1992)
Cable systems retransmitted broadcast signals without paying. The Supreme Court ruled **twice** (*Fortnightly* 1968, *Teleprompter* 1974) that this wasn't infringement — again, technology won in court. Congress reversed the outcome: the 1976 Copyright Act created a **compulsory license with royalties**, and the 1992 Cable Act added **retransmission consent** — cable must negotiate for permission to carry a broadcaster. Retrans fees grew from zero to **$15B+/year**, becoming broadcasters' second revenue leg. This is the strongest historical precedent for what publishers want from AI: a statutory *duty to negotiate*. Australia's News Media Bargaining Code (2021) is explicitly this mechanism applied to Google/Facebook.

### 4. Photocopying → the market that changed the law (1973–1994)
Libraries and corporations photocopied journal articles at scale. *Williams & Wilkins* (1973): library copying was fair use — publishers lost. Response: publishers built the **Copyright Clearance Center (1978)**, a transactional licensing market. Then the law flipped: in *American Geophysical Union v. Texaco* (1994), corporate copying was **not** fair use — precisely **because a functioning licensing market now existed**, so unlicensed copying caused cognizable market harm.

**This is the most strategically important precedent for AI.** Fair use's fourth factor (market harm) is partly endogenous: *building the licensing market strengthens the legal case that not using it is infringement.* Every publisher joining PCM, RSL, or a collective license is not just earning revenue — they are constructing the fact pattern that defeats fair use. AI companies signing licenses are, ironically, doing the same to themselves.

### 5. VCR/Betamax → the harm that became the market (1976–1984)
Hollywood sued Sony to kill the VCR. *Sony v. Universal* (1984): time-shifting is fair use; technology with substantial non-infringing uses is lawful. Then home video revenue **exceeded box office** within a few years. Lesson: incumbents can misjudge which side of the ledger a technology lands on. (Applicability to AI is limited — VCRs created a new distribution channel for studios' own product; AI answers substitute for the publisher's product. But it's the cautionary tale against pure blocking strategies.)

### 6. Music sampling → bright-line liability creates a clearance market overnight (1991)
*Grand Upright v. Warner* (1991) declared sampling without a license infringement ("Thou shalt not steal"). A clearance market materialized almost immediately. Lessons: legal certainty — in either direction — creates a market fast; but transaction costs reshaped the art itself (dense collage sampling like the Bomb Squad's became economically impossible; only stars can clear samples). Metric/legal regimes reshape what gets created.

### 7. Napster → litigation kills the company, a product kills the behavior (1999–2015)
The industry won every lawsuit (Napster, Grokster) and lost half its revenue anyway; piracy was resolved not by law but by **superior licensed products** — iTunes, then Spotify. Industry revenue eventually recovered to growth via streaming, but **redistributed**: labels and the top 1–2% of artists capture most of it; the per-stream long tail earns nothing. This is the briefing's "Scenario B (Spotify model)" precedent in full: *aggregate* recovery, *individual* immiseration, and the platform (Spotify ~30%, Apple/Google app-store cuts) inserted permanently into the value chain.

### 8. Google Books → substitution decides fair use (2004–2015)
Google scanned 20M+ books without permission. A negotiated global settlement was **rejected by the court** (2011, as exceeding class-action power — a warning about settling structural questions privately). Then *Authors Guild v. Google* (2015): scanning to enable search is **transformative fair use** — because snippets **do not substitute** for buying the book. The controlling variable was substitution. AI answers are on the other side of that line: they are engineered to be a complete substitute for the visit. This is the single most important legal distinction between AI and every aggregation case the platforms previously won.

### 9. YouTube/Viacom → attribution technology dissolves the conflict (2007–2014)
Viacom sued YouTube for $1B. The lawsuit fizzled (DMCA safe harbor), but the real resolution was **Content ID**: fingerprinting that detects copyrighted audio/video and lets rightsholders **monetize instead of remove**. It now routes billions of dollars a year and converted adversaries into supply partners. This is the optimistic analog for AI attribution — and the reason for pessimism is precise: Content ID works because *exact matching of media files is computationally trivial*. Measuring semantic influence inside a transformer is not. The economics of Content ID await an attribution technology that doesn't yet exist for LLMs (see `wiki/attribution-deep-dive.md`).

### 10. News aggregation → link taxes fail, bargaining codes work (2013–2023)
- **Hot news doctrine** (*INS v. AP*, 1918): misappropriation of fresh news held unlawful — an early recognition that facts have time-value; largely preempted/dormant today but conceptually resurrected by AI substitution arguments.
- **Link taxes failed** where Google could walk away: Germany 2013 (publishers waived fees to keep traffic), Spain 2014 (Google News shut down; publishers lost traffic and got nothing).
- **Bargaining codes worked** where walking away was barred or costly: Australia's News Media Bargaining Code (2021) — final-offer arbitration as the stick — moved ~A$200M/year without ever being formally invoked. Canada's C-18 (2023) split the difference: Google paid $100M/yr; **Meta blocked news entirely and suffered no measurable harm** — proving the code only works on platforms that actually need news.

## The resolution playbook: seven lessons

1. **Courts set bargaining positions; they almost never produce the final regime.** In piano rolls, cable, and photocopying, creators *lost* in court and won afterward — through legislation (compulsory licenses, retrans consent) or market construction (CCC). The NYT case matters less for its verdict than for the bargaining position it creates.
2. **The recurring end-state is collective/compulsory licensing with rate-setting.** Mechanical royalties, ASCAP/BMI blanket licenses, cable compulsory license, CCC, streaming's CRB rates. Individual negotiation never scales past the top few dozen rightsholders; everything else flows through a collective with a tariff. Expect the same for AI: bilateral deals for the NYT tier, collective licensing (RSL, CLA, CCC, VG WORT) for everyone else.
3. **Building the licensing market changes the law** (the Texaco principle). Fair use's market-harm factor rewards the side that constructs a functioning market. PCM, RSL, and every signed deal are legal ammunition, not just revenue.
4. **Substitution is the pivotal fact.** Platforms won when their use pointed demand back at the original (search, snippets, Google Books). They lost or paid when the use replaced the original (ROSS, retransmission, sampling). AI answers are the most substitutive technology in this entire history — which is why publishers' legal position is stronger than it was against Google search, even under the same fair use doctrine.
5. **Detection technology determines deal structure.** Content ID made per-use monetization possible because matching was cheap. Absent reliable attribution, AI deals default to lump sums and flat pools — which favor the platform and the biggest brands. Whoever ships credible attribution tech doesn't just earn fees; they determine which deal structures are even possible.
6. **Aggregate recovery, individual redistribution.** Music revenue recovered; the middle class of musicians did not. Retrans fees saved broadcasters; local news died anyway. Expect AI licensing to "work" at industry level while hollowing out the middle — unless the rate structure (like statutory mechanicals, which pay every song the same rate) is deliberately designed against power-law concentration.
7. **Walk-away power decides who pays.** Spain vs. Australia; Google (needs news for freshness) vs. Meta (doesn't). The uncomfortable question for publishers: as models improve and grounding needs shrink, AI companies' walk-away power *grows over time*. Publishers' leverage is a depreciating asset — which argues for locking in structural mechanisms (codes, compulsory licenses, collective rates) now, while the leverage exists.

## Mapping to the AI conflict, mid-2026

| Historical mechanism | AI-era instance | Status |
|---|---|---|
| Compulsory license (1909, 1976) | Proposed statutory AI training license | Discussed, not enacted anywhere |
| Duty to negotiate (retrans consent, Australia) | UK CMA conduct requirements on Google (June 2026); EU leverage | Beginning |
| Collective licensing (ASCAP, CCC) | RSL Collective, CLA/PLS GenAI licence, CCC AI rights, VG WORT | Building |
| Market construction → fair-use flip (CCC/Texaco) | PCM, ~20 OpenAI deals, Google's ~20-publisher negotiations | Actively accumulating |
| Detection tech → per-use monetization (Content ID) | Attribution research (counterfactual RAG, etc.) | Not production-ready |
| Superior licensed product (iTunes/Spotify) | Licensed grounding marketplaces (PCM) | Pilot stage |
| Walk-away asymmetry (Meta/Canada) | Model improvement reducing grounding dependence | The long-term threat |
