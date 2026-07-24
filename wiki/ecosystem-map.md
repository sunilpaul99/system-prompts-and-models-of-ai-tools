# The Ecosystem Map: Who's Who in Publishers and AI, and How to Engage

*A map of the positions, people, companies, institutions, and entry points in the publishers-and-AI conversation. Last updated July 2026.*

## 1. The five positions

Nearly everyone in this debate occupies one of five camps. Knowing which camp someone is in predicts their arguments better than their industry does.

### A. Rightsholder maximalists — "consent and compensation, or it's theft"
Training and grounding without a license infringe; the remedy is litigation plus legislation. Strongest where the natural-rights intuition runs deep (authors, artists) and where subscription brands have leverage.
**Who**: News/Media Alliance (~2,000 publishers; CEO Danielle Coffey), Authors Guild (Mary Rasenberger; the Grisham/Martin class action), Copyright Alliance (Keith Kupferschmid), NYT (the defining lawsuit), Condé Nast (CEO Roger Lynch testified to Congress for licensing mandates), Dotdash Meredith (CEO Neil Vogel: "fair use is not fair" — though he signed an OpenAI deal anyway), UMG and the music industry, Getty Images.

### B. Deal-makers — "courts are a lottery; take the cash while leverage exists"
Same diagnosis as camp A, opposite tactic: sign now, litigate never (or only as leverage). Implicitly accepts the depreciating-leverage clock.
**Who**: News Corp (Robert Thomson; $250M+ OpenAI deal), Axel Springer (Mathias Döpfner — deal-maker *and* loud AI-threat rhetorician), AP (first OpenAI deal, now Google Gemini real-time deal), FT, The Guardian, Washington Post, Vox Media, Hearst, People Inc. — the PCM/OpenAI cohort. The NYT itself straddles A and B: suing OpenAI/Microsoft while licensing to Amazon (~$20–25M/yr).

### C. Infrastructure builders — "make the market work, whatever the doctrine says"
The Texaco play, deliberate or not: build the licensing rails so unlicensed use becomes both unnecessary and legally indefensible. The most consequential camp right now.
**Who**:
- **Cloudflare** (CEO Matthew Prince) — the most aggressive mover. Pay-per-crawl launched July 1, 2026 (block-by-default toggle, $0.01/crawl minimum); evolving to "pay per use" with Ceramic.ai and You.com; **from September 15, 2026, Cloudflare blocks mixed search/agent/training crawlers from ad-supported sites by default**. Cloudflare sits in front of ~20% of the web — this is unilateral, infrastructure-level rate-setting, no legislation required.
- **Microsoft PCM** (VP Nikhil Kolar, under Microsoft AI CEO Mustafa Suleyman) — the marketplace bet; see briefing Ch. 5.
- **RSL Collective** (Doug Leeds, ex-Ask.com/IAB Publishing; Eckart Walther, RSS co-creator) — nonprofit collective rights organization + the open RSL standard (machine-readable licensing terms in robots.txt); ~1,500 endorsing orgs incl. Yahoo, AP, Medium, Reddit, BuzzFeed, USA Today, Vox. This is the ASCAP-of-the-web attempt.
- **TollBit** (Toshit Panigrahi) — metered per-crawl/per-use access, 5,000+ publishers. **ProRata.ai** (Bill Gross) — attribution-based answer engine + 50/50 ad revenue share, 700+ publishers. **Human Native** (UK) and **Created by Humans** — licensing marketplaces for datasets and books respectively. **Copyright Clearance Center** — the photocopying-era collective, now selling AI reuse licenses.
- **Fairly Trained** (Ed Newton-Rex, ex-Stability AI, resigned over training ethics) — certifies models trained only on licensed data; the "fair trade" label play.
- Provenance/attribution tech: **C2PA/Content Authenticity Initiative** (Adobe-led, Microsoft/Google members), **Encypher** (text credentials), **Bria** (image attribution royalties), **Spawning** (opt-out infrastructure).

### D. Fair-use and open-innovation camp — "learning is not infringement; strong copyright entrenches giants"
Training is transformative pattern-learning; licensing mandates would hand AI to the deepest pockets and kill open-source models. Note their strongest argument is *competition*, not convenience.
**Who**: EFF, Public Knowledge, Authors Alliance (Dave Hansen — authors *for* fair use), Engine and startup advocacy groups, a16z and most AI investors; scholars Pamela Samuelson (Berkeley), Matthew Sag (Emory; coined the "Snoopy problem" — style vs. expression), Mark Lemley (Stanford; nuanced, briefly repped Meta), James Grimmelmann (Cornell). The AI labs' litigation positions live here (OpenAI, Meta, Google, Anthropic pre-settlement), though their *dealmaking* behavior increasingly lives in camp C.

### E. Structural reformers — "the frame itself is wrong"
Data is labor; provenance should be foundational; the goal is redesigned institutions, not better deals under the old ones.
**Who**: Jaron Lanier and E. Glen Weyl (data dignity, "mediators of individual data"; Lanier's provenance research sits inside Microsoft's CTO office), Tim O'Reilly (disclosure and value-flows arguments), Creative Commons (CC Signals — preference signaling for AI reuse), Mozilla Foundation, Data Provenance Initiative (Shayne Longpre, MIT — audits training-dataset licensing at scale), plus the journalism-sustainability funders: Knight Foundation, Lenfest Institute, **Press Forward** (~$500M for local news), Rebuild Local News (Steven Waldman), American Journalism Project.

### The referees
Not a camp but the deciders: **Judge Sidney Stein** (SDNY, the NYT MDL), the **US Copyright Office** (its May 2025 Part 3 report cast doubt on blanket fair-use claims for training — followed by leadership turmoil that itself became a story), the **UK CMA** (June 2026 conduct requirements on Google, incl. publisher opt-outs), the **UK IPO** (AI/copyright consultation), the **EU AI Office** (GPAI Code of Practice; transparency rules live August 2, 2026), and Australia's ACCC (the bargaining-code precedent).

## 2. The key ideas (the vocabulary of the debate)

| Idea | One-line version | Camp that wields it |
|---|---|---|
| Grounding vs. training | Per-use retrieval vs. baked-into-weights; different economics, different legal claims | C (it's their product architecture) |
| Zero-click / substitution | The answer replaces the visit — the core harm and the pivotal fair-use fact | A, B |
| Idea/expression dichotomy | Facts are free by design; publishers' product is thinly protected | D |
| Texaco endogeneity | Building the licensing market builds the infringement case against holdouts | C (often unknowingly) |
| Attribution / Shapley problem | Fair payment requires measuring influence, which is intractable; splits are policy | All (usually confused) |
| The redundancy trap | Fair attribution pays unique info and zeroes commodity coverage | (rarely acknowledged) |
| Administered access / collective licensing | The historical end-state: liability rules, blanket licenses, rate-setting | C, E |
| Pay-per-crawl | Infrastructure-level tolls on bots; unilateral rate-setting by CDNs | C (Cloudflare) |
| GEO/AEO | Optimizing content to be retrieved/cited by AI — the new SEO | Publishers' ops teams |
| Data dignity | Data as labor deserving payment and provenance | E |
| Seed corn / model collapse | AI destroying its own input supply; the self-interested case for funding content | A→ aimed at AI cos |
| Agentic web | Agents, not humans, consume the web; needs an economic layer (MCP, NLWeb, RSL) | C |
| Provenance (C2PA) | Cryptographic content credentials; necessary but not sufficient for attribution | C, E |

## 3. Who to read and follow

**Trade press and newsletters** (where this conversation actually happens week to week):
- **Press Gazette** (platform-publisher data, deal tracking), **Digiday** (Media Briefing; the deal scorecards), **Nieman Lab** (Joshua Benton and staff; predictions series), **CJR/Tow Center** reports (Klaudia Jaźwińska on AI citations), **Reuters Institute** (Nic Newman's Digital News Report — the canonical audience data).
- Independents: **A Media Operator** (Jacob Cohen Donnelly — publisher business models), **The Rebooting** (Brian Morrissey), **The Media Copilot** (Pete Pachal — AI×media specifically), Simon Owens's Media Newsletter, Ben Thompson's Stratechery (aggregation theory — the framework half this debate borrows).

**Academic/legal commentary**: Pamela Samuelson's writing for a skeptic's view of infringement claims; Matthew Sag's congressional testimony for the middle; the Copyright Alliance blog for the rightsholder view; Authors Alliance for the pro-fair-use author view; ChatGPT Is Eating the World (blog tracking all ~70 cases); McKool Smith and Mishcon case trackers.

## 4. How to get engaged

**Follow the live proceedings** (free, high-signal):
- The NYT MDL docket (CourtListener: *NYT v. Microsoft*, 1:23-cv-11195) — the sanctions fight and summary judgment briefing are where doctrine is being made.
- EU AI Act GPAI transparency enforcement from Aug 2, 2026; UK IPO consultation outputs; CMA conduct reviews.

**Public comment and policy input**: US Copyright Office proceedings, UK IPO consultations, EU AI Office codes of practice, and US state-level AI bills all take public submissions — trade associations (NMA, DCN, MPA) aggregate publisher voices; EFF/Public Knowledge aggregate the other side.

**Fellowships and programs**:
- **Tarbell Fellowship** (AI journalism; $60–110K stipend, newsroom placement — 2026 closed, next cycle late 2026)
- **Pulitzer Center AI Accountability Fellowships** (2026–27 cohort, ~$20–25K project funding)
- **JournalismAI** at LSE/Polis (free academy + fellowship, Google News Initiative-backed)
- Reynolds Journalism Institute fellowships; Nieman; Knight-Wallace; the Bell AI Fellowship (the briefing's own workshop context).

**Standards and working groups** (open to participants): C2PA / Content Authenticity Initiative membership; RSL standard adoption and the RSL Collective; IPTC (news metadata); IAB Tech Lab's AI working efforts; W3C discussions on AI preference signals; open-source attribution tooling (OpenAttribution, RAGonite, pyDVL, TRAK — see briefing Ch. 9.11).

**Conferences and rooms where this is debated**: INMA World Congress, WAN-IFRA World News Media Congress, ONA (Online News Association), ISOJ (UT Austin), International Journalism Festival (Perugia), Digiday Publishing Summits, Semafor/Axios media events, Aspen Digital roundtables.

**Build or fund**: the open research bridge (citation-validated uniqueness → attribution — see the attribution deep dive); GEO/AEO analytics for publishers; collective-licensing tooling for the long tail; local-news sustainability via Press Forward/Lenfest if the motivation is civic rather than commercial.

## 5. Reading the map strategically

Three observations for anyone entering this conversation now:

1. **The center of gravity has moved from courtrooms to infrastructure.** The most consequential 2026 actors are Cloudflare, RSL, and the marketplaces — parties that can set de facto rates without waiting for verdicts. Camp C is where the leverage compounds (and, via Texaco, it quietly does camp A's legal work).
2. **Every camp is missing something.** A underestimates the facts problem and the leverage clock; B is pricing a wasting asset without structural protection; C hasn't solved attribution and may be building the Spotify model; D underweights the seed-corn problem; E has the right diagnosis and no deployment at scale. The valuable contributor is whoever can hold all five honestly.
3. **The long tail is unrepresented.** Every mechanism above works best for the top 50 publishers. The ASCAP-shaped institutions (RSL Collective, CCC, national collecting societies) are the only vehicles pointed at everyone else — and they are the least funded and least discussed. That's both the gap and the opportunity.
