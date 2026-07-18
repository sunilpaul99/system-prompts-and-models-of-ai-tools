# IP From First Principles: Copyright, Fair Use, Derivative Works, and the Rights-vs-Technology Bargain

*Wiki entry. The theory layer beneath `raw/content-economy-briefing.md` and the other wiki entries. Last updated July 2026.*

## 1. The problem IP exists to solve

Information is a **public good** in the economist's sense: **non-rival** (your reading an article doesn't use it up) and, once published, **non-excludable** (hard to stop others from using it). Creation is expensive; copying is nearly free. In an open market, competition drives price toward the marginal cost of copying — approximately zero — which can never recoup the fixed cost of creation. Result: systematic underproduction of information goods.

Copyright is the policy instrument that answers this: grant creators a **temporary, artificial excludability** — a limited monopoly — so they can price above copying cost and recoup creation cost. The price society pays is **deadweight loss**: people are priced out of a good that costs nothing to share. Copyright is therefore not a recognition of natural ownership but a **deliberate bargain**: tolerate some monopoly loss to get more creation.

Everything in copyright doctrine is machinery for tuning that bargain — and every technology fight is a fight over re-tuning it.

### Two rival philosophies (and why the difference matters for AI)

- **Utilitarian/incentive theory (US/UK).** The Constitution's IP clause states the purpose: "to promote the Progress of Science and useful Arts." Author reward is the *means*; public benefit is the *end*. The Supreme Court has been explicit that copyright's reward to the owner is "a secondary consideration." Under this theory, the AI question is empirical: does unlicensed AI use reduce the incentive to create, net of the new value created?
- **Natural-rights/personality theory (Continental Europe).** *Droit d'auteur*: the work is an extension of the author's labor (Locke) and personhood (Kant, Hegel). This yields **moral rights** — attribution and integrity — that exist regardless of economic effect and often can't be sold. Under this theory, the AI question is deontological: was the author's will respected? Consent, not consequences.

This is why the US litigates *fair use* while the EU legislates *opt-outs and transparency* (TDM exception with rightsholder opt-out; AI Act disclosure duties). Same technology, different first principles, different remedies. Attribution — economically almost worthless to publishers — is a *moral-rights* demand smuggled into an economic-rights system, which is partly why the debate about it is so confused.

## 2. The architecture of copyright: how doctrine implements the bargain

### 2.1 The idea/expression dichotomy — the load-bearing wall

Copyright protects the **expression** of a work, never the **ideas, facts, methods, or discoveries** in it (§102(b); *Baker v. Selden*, 1880). Anyone may read a copyrighted article and freely restate every fact and idea in it in their own words. This is not a loophole; it is the design. The system deliberately makes the *knowledge* free and monetizes only the *form*, because locking up ideas would strangle the progress the system exists to promote.

Supporting doctrines police the boundary: **originality** requires only a "modicum of creativity" but genuinely excludes facts — *Feist v. Rural* (1991) rejected "sweat of the brow": effort and expense alone earn no protection, no matter how costly the fact-gathering. **Merger** (when an idea can only be expressed a few ways, expression merges with idea and loses protection) and **scènes à faire** (stock elements are free) keep the wall from creeping.

**The AI consequence is severe and under-appreciated:** what news publishers principally sell — timely, verified *facts* — is unprotected by design. An AI system that extracts facts from articles and re-expresses them is doing, at scale, exactly what the dichotomy licenses every human reader to do. Publishers' economic injury is real, but copyright is a poorly fitted instrument for it, because the injury runs through the unprotected layer. This is why publisher claims keep migrating to adjacent theories — hot-news misappropriation (*INS v. AP*, 1918 — mostly dead), DMCA §1202 metadata-removal claims, contract/ToS, unfair competition, and regulatory bargaining codes. The weakness is structural, not tactical.

### 2.2 The bundle of rights

Copyright is not one right but a bundle (§106): **reproduction**, **derivative works**, **distribution**, **public performance/display**. Each stick matters separately for AI:

- **Reproduction** is implicated at *ingestion*: crawling and copying articles into a training corpus is literal copying, regardless of what the model later does. This — not model outputs — is the doctrinally cleanest claim in every training lawsuit, and it's why *how you obtained the copies* matters (*Bartz v. Anthropic*: training on lawfully acquired books was fair use; sourcing from pirate libraries was not — a $1.5B distinction).
- **Derivative works** (§101: a work "recast, transformed, or adapted" from a preexisting one — translations, film adaptations, sequels) exist so authors capture value in *adjacent markets* they could reach. The right presupposes the derivative still embodies the original's protected expression in recognizable form (infringement requires **substantial similarity**). Whether a *model* is a derivative work of its training data is the frontier question: weights encode statistical patterns (idea-like, non-infringing) but demonstrably sometimes memorize expression verbatim (the NYT's regurgitation exhibits). Courts so far treat memorized *outputs* as potential infringements while resisting the claim that the *model itself* is a derivative work. If that ever flips, every model trained on unlicensed data is contraband — the NYT's model-destruction demand is this theory taken seriously.
- **Public performance/display** drove the streaming-era cases; largely peripheral to text AI.

### 2.3 The public's side of the bargain

Limited terms, exhaustion (**first sale**), **compulsory licenses** (mechanical, cable, webcasting — where Congress decided negotiation would fail and set the price administratively), and **fair use**. These aren't exceptions grudgingly carved from ownership; in the utilitarian frame they are half of the deal — the mechanism ensuring the monopoly stays a servant of diffusion.

## 3. Fair use: the system's adaptation mechanism

Fair use (§107) exists because a literal-enforcement copyright would defeat its own purpose: criticism, teaching, parody, and follow-on creation all require using existing works, and transaction costs would block countless socially valuable uses no author would rationally refuse. Structurally, fair use is **common-law flexibility inside a statutory monopoly** — the interface where new technologies get absorbed without waiting for Congress. Photocopying, home taping, search engines, thumbnails, plagiarism-detection databases, and book scanning were all metabolized here.

The four factors, and what each actually probes:

1. **Purpose and character of the use** — since *Campbell v. Acuff-Rose* (1994), the core question is **transformativeness**: does the use add new purpose, meaning, or function, or does it merely supersede the original? *Warhol v. Goldsmith* (2023) narrowed this: new aesthetic meaning is not enough if the use serves the **same commercial purpose** as the original (both were magazine licensing of a Prince image). Warhol is the publishers' best recent weapon: an AI answer *about the news* arguably shares the exact commercial purpose of the article it draws from.
2. **Nature of the work** — factual works get thinner protection than creative ones (the idea/expression wall again). Cuts *for* AI companies on news, *against* them on fiction.
3. **Amount and substantiality** — but copying *everything* can be fair if necessary to a transformative purpose (Google Books copied every word of every book), while copying a small "heart" can be unfair (*Harper & Row*, 1985 — 300 words of Ford's memoir). Quantity matters less than what the taking does.
4. **Effect on the market** — historically the dominant factor, and the one with two properties everything turns on:
   - **Substitution is the pivot.** Uses that point demand back at the original (search, snippets, indexing) win; uses that capture the original's demand lose (*Thomson Reuters v. ROSS*). Google Books won *because* snippets can't replace the book. AI answers are engineered to fully replace the visit — the most substitutive technology copyright has ever confronted.
   - **The factor is endogenous** (the *Texaco* principle). Harm includes harm to *licensing markets* — but only markets that exist or are likely to develop. Photocopying was fair use in 1973 and infringement by 1994 because publishers built the CCC in between. Every AI licensing deal signed today strengthens tomorrow's argument that unlicensed use harms a real market. Fair use is partly a race to construct facts.

Also live: **market dilution** — the *Kadrey* court's suggestion that flooding markets with AI-generated competing works could itself be factor-four harm, even without copying-specific substitution. If that theory matures, it partially patches the facts problem from §2.1.

## 4. Economic rights vs. new technological capability: the underlying structure

### 4.1 Why the conflict recurs

Every major copying technology creates the same gap: the statute allocated rights against the *last* technology's economics, and the new technology makes uses possible that the allocation never priced. Two symmetric errors are available:

- **Over-protection**: incumbents get a veto over the new technology → innovation strangled, deadweight loss, the public loses capabilities it could have had (the world where the VCR lost).
- **Under-protection**: the new technology free-rides on the corpus → creation incentives collapse → the technology eventually starves its own input supply.

The second error has a distinctive AI form: models need a continuing supply of fresh, high-quality human text (news especially — grounding exists because parametric knowledge goes stale). If AI destroys the revenue that funds that supply, it consumes its seed corn; "model collapse" research is the literal, technical version of the incentive argument. This gives AI companies a *self-interested* reason to fund content that previous free-riding platforms never had — a genuinely new element in the pattern.

### 4.2 The honest cases, both directions

**For economic rights (publishers/creators):**
- *Incentive preservation* — the entire point of the system; if answers substitute for visits, the funding model of the corpus dies.
- *Dynamic efficiency* — today's underpayment is invisible now and shows up as tomorrow's missing journalism.
- *Fairness/labor* — the Lockean intuition that value extracted from someone's work owes them a share (this is the moral engine of public and jury sentiment, whatever doctrine says).
- *Bargaining asymmetry* — "consent" is fictional when the counterparty can take the content anyway and litigation costs eight figures.

**For technological capability (AI developers/public):**
- *Knowledge diffusion is the system's purpose* — ideas and facts are free by design; a technology that dramatically lowers the cost of access to knowledge is delivering exactly the "Progress" the clause names.
- *Learning is not infringement* — humans lawfully read, internalize patterns, and re-express; a rule that machines may not learn from what they lawfully read has no principled stopping point.
- *Transaction-cost impossibility* — clearing rights over billions of works individually cannot be done; demanding it means either no models or models owned only by whoever can pay (see below).
- *Competition* — strict licensing regimes are a moat: only Big Tech can afford the corpus, and only big publishers capture the fees. The rule meant to protect the little creator entrenches the giants on both sides.
- *The historical record* — accommodation usually grew the pie (radio made the music industry; the VCR made Hollywood's biggest revenue line).

### 4.3 Why "learning vs. copying" is genuinely hard, not confused

The AI training question sits precisely on copyright's deepest fault line. Training is *like reading*: the model extracts statistical patterns — idea-layer material the system deliberately leaves free. Training is *like copying*: it requires literal reproduction at ingestion, occasionally memorizes expression, and operates at a scale no human analogy survives. **Scale is a qualitative variable, not a quantitative one**: fair use was calibrated to individual acts by individual users; a "reader" that reads everything ever published and can serve every human's information needs simultaneously breaks the background assumptions under which the idea/expression bargain was tolerable to creators. Both sides' analogies are correct; that's why the doctrine can't settle it and why three judges have already split.

### 4.4 How these conflicts actually end (and the institutional lesson)

The historical record (see `wiki/historical-content-conflict-resolutions.md`) shows courts almost never produce the final regime; they set bargaining positions. The stable end-state, repeatedly, is **administered access**: compulsory or collective licensing in which the technology gets *certainty of access* (no veto, no injunction risk) and creators get *certainty of payment* (a rate, set administratively or by collective bargaining, not by individual negotiation or by market power). Piano rolls (1909), radio (ASCAP/BMI + consent decrees), cable (1976/1992), photocopying (CCC), streaming (CRB rates). The bargain's tuning knob moves from courts to rate-setters.

The deep reason this design wins: it converts a *property rule* (owner can refuse; price set by veto) into a *liability rule* (user can use; price set by tribunal) exactly where transaction costs make property rules fail — Calabresi and Melamed's framework, applied. AI, with billions of works and millions of users, is the most extreme transaction-cost environment copyright has ever faced, which is why the theoretical prediction and the historical pattern point the same direction: some form of statutory or collective license for training and grounding, with bilateral deals surviving only at the premium tier.

### 4.5 The political economy just flipped

For two centuries, copyright expanded monotonically (term extensions, new rights) because the beneficiaries were concentrated (studios, labels, publishers) and the cost-bearers diffuse (the public) — classic public-choice ratchet. AI reversed the alignment for the first time: **the deep pockets are now on the users' side.** Trillion-dollar companies want *narrow* copyright; fragmented, shrinking publishers want it *broad*. Predictions built on copyright's historical expansion bias should be discounted accordingly — and creator interests now depend more on regulatory bargaining leverage (competition law, AI acts, codes of conduct) than on copyright doctrine itself, which is exactly what the UK CMA and EU AI Act developments show.

## 5. Mapping the principles to the live disputes

| Principle | Live AI dispute it governs |
|---|---|
| Public-good economics / incentive bargain | Whether unlicensed AI use is underproduction-causing free-riding or welfare-enhancing diffusion |
| Idea/expression + *Feist* (facts free) | Why fact-extraction answers are hard to reach with copyright; why publishers add DMCA/misappropriation/contract claims |
| Reproduction right at ingestion | Scraping claims; *Bartz* lawful-acquisition bright line |
| Derivative works / substantial similarity | "Is the model itself infringing?"; regurgitation exhibits; model-destruction remedies |
| Transformativeness (*Campbell*, narrowed by *Warhol*) | "Training is transformative" vs. "same commercial purpose as the news itself" |
| Factor 4 substitution | Zero-click harm; *ROSS*; why AI differs from Google Books |
| Factor 4 endogeneity (*Texaco*) | Every licensing deal and marketplace (PCM, RSL) strengthens the infringement case against holdouts |
| Market dilution (*Kadrey* dicta) | AI-content flood as cognizable harm without direct copying |
| Moral rights vs. economic rights | Attribution demands; EU opt-out/transparency regime vs. US fair-use litigation |
| Property vs. liability rules (Calabresi–Melamed) | The case for compulsory/collective AI licensing as the end-state |
| Public choice / concentrated interests | Why the copyright ratchet may reverse; why creator leverage now runs through regulators |

## 6. The synthesis

The question is never "rights vs. technology." Both over- and under-protection destroy value; the design problem is institutional: **which mechanism preserves the incentive to create while letting the new capability diffuse?** History's answer is administered access — liability rules, collective rates, certainty on both sides. The AI-specific twists are three: the injury runs substantially through copyright's deliberately unprotected layer (facts), the technology has a self-interested stake in its input supply surviving (seed corn), and the lobbying asymmetry that always expanded copyright now points the other way. Any strategy for publishers — including Tenni's — should be built on those three structural facts, not on the hope that copyright doctrine alone will deliver the verdict.
