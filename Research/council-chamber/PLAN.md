# Execution Plan — Study #7: The Council Chamber

**How AI politics arrives in local government**
*Plan drafted 2026-08-19. Status: approved to plan; Phase 0 pending.*

---

## Objective

Produce (a) a peer-reviewable paper on the arrival, diffusion, and framing of AI as a policy
issue in US local government, and (b) a public "AI in Local Government Tracker" dataset/map.

Core hypotheses to test:

- **H1 (diffusion):** AI agenda items diffuse through classic policy-diffusion channels —
  geographic neighbors, peer-city networks, and model-ordinance sponsors — rather than
  appearing independently.
- **H2 (framing):** Local deliberations frame AI in a materially different vocabulary
  (jobs, budgets, kids, water, public safety) than national elite discourse (safety,
  innovation, bias, x-risk) — the local test of our translation-gap thesis.
- **H3 (conflict):** Contested votes and public-comment mobilization concentrate on a small
  subset of AI issues (predictably: policing/surveillance, schools, data centers), while most
  AI items pass without debate.

## Design summary

Panel of the ~300 largest US cities with Legistar/Granicus portals (plus a school-district
sample), 2017–present. Unit of analysis: the *agenda item* (matter), with linked deliberation
text and outcome. Event-history models for first-adoption timing; frame analysis comparing the
local corpus to a national reference corpus; public-comment volume and vote splits as conflict
measures.

## Phases

### Phase 0 — Feasibility probes (gate) — ~1 week

- **0.1 Network access.** This session's egress proxy currently blocks `webapi.legistar.com`
  and general web hosts (verified 2026-08-19). Remedy before any collection: update the Claude
  Code environment's network policy to allow, at minimum:
  `webapi.legistar.com`, `*.legistar.com`, `*.granicus.com`, `www.youtube.com` (captions),
  `archive.org`. Alternative: run collectors on a local machine and commit data to the repo.
- **0.2 API probe.** For 10 pilot cities (Seattle, NYC, Chicago, Austin, Phoenix, Columbus,
  Denver, Nashville, Oakland, Pittsburgh): confirm the Legistar Web API
  (`https://webapi.legistar.com/v1/{client}/matters`) returns matters with full text or
  attachments; document per-city client codes, coverage start dates, and text availability.
- **0.3 Signal check.** Run the keyword seed list (below) on the pilot cities. **Go/no-go
  gate:** ≥ 30 genuine AI agenda items across 10 cities since 2022. If below, AI hasn't
  penetrated agendas enough for the diffusion study; pivot to the school-board corpus first.
- **0.4 School-board probe.** Test BoardDocs/Simbli public portals for 10 large districts.

### Phase 1 — Sampling frame and corpus assembly — ~3–4 weeks

- **1.1 City roster.** Enumerate Legistar clients (the API's client list is discoverable);
  intersect with the Census top-300 cities; record for each: portal type, API coverage window,
  population, region, form of government. Publish the roster as the sampling-frame artifact.
- **1.2 Detection.** Two-stage retrieval: (i) seed keywords on titles/text — *artificial
  intelligence, AI, machine learning, algorithm(ic), facial recognition, automated
  decision(-making), ChatGPT, chatbot, generative, LLM, predictive policing, data center* —
  deliberately over-inclusive; (ii) LLM classifier prunes false positives ("AI" as initials,
  "algorithm" in engineering specs) and assigns each item to an issue category:
  {policing/surveillance, schools, procurement/internal use, data centers/infrastructure,
  workforce, governance/ethics boards, other}.
- **1.3 Deliberation text.** For matched items, pull minutes, attachments, and — where the
  meeting is on YouTube — caption segments around the item (align via agenda timestamps where
  available; otherwise keyword-window extraction).
- **1.4 Outcomes.** Vote results, consent-calendar status, public-comment counts per item.
- **1.5 Validation.** Hand-label 300 randomly sampled candidate items (two coders, report
  agreement). Target: classifier precision ≥ 0.9, recall ≥ 0.85 against this gold set.

### Phase 2 — Analysis — ~3–4 weeks

- **2.1 Descriptives.** First-appearance timeline per city and issue category; the headline
  chart is the cumulative-adoption S-curve by issue.
- **2.2 Diffusion (H1).** Event-history (Cox / discrete-time logit) on first AI agenda item
  and on first *binding* AI policy, with covariates: neighbor adoption, population, region,
  council partisanship (from Ballotpedia mayoral/council data), presence of model-ordinance
  language (detect via text reuse against known templates — e.g., ACLU CCOPS ordinances,
  NLC/league materials).
- **2.3 Framing (H2).** Compare local deliberation text to a national reference corpus
  (congressional AI hearings + major-outlet op-eds) using keyness statistics and
  moral/economic frame classifiers. Deliverable: the "two vocabularies" table.
- **2.4 Conflict (H3).** Vote-split and public-comment analysis by issue category.
- **2.5 Robustness.** Re-run diffusion excluding data-center items (arguably a distinct
  land-use phenomenon); vary detection threshold; placebo keyword ("broadband") diffusion.

### Phase 3 — Deliverables — ~3 weeks, overlaps Phase 2

- **3.1 Tracker.** Public artifact: filterable map/table of every detected AI agenda item
  (city, date, category, outcome, link to source document). Ship v1 as soon as Phase 1 data
  is clean — the tracker builds audience before the paper lands.
- **3.2 Paper.** Target *Urban Affairs Review* or *Policy Studies Journal*; preprint on SSRN
  or SocArXiv immediately on completion.
- **3.3 Data release.** Roster + detected items + gold labels, versioned in this repo (or a
  dedicated repo if size demands).

## Pre-registration

Before Phase 2 begins, freeze and commit: hypotheses H1–H3, the detection pipeline, model
specifications, and the exclusion rules. Registered on OSF; the commit hash is the receipt.

## Division of labor

- **Claude (this session + subagents):** collector scripts, classifier prompts and validation
  harness, statistical analysis, tracker build, paper drafting. Corpus assembly parallelizes
  cleanly across cities (one agent per batch of portals).
- **Sunil:** environment network-policy change (only you can edit it), second coder on a
  validation subsample (or recruit one), judgment calls at the Phase 0 gate and on venue,
  and any outreach (league of cities contacts, potential academic co-author for the
  event-history methodology if we want a domain co-author for venue credibility).

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Egress policy blocks collection | Fix in Phase 0.1 before anything else; it is the single hard blocker |
| Portal heterogeneity balloons scraping work | Legistar-API-first design; Granicus/BoardDocs only in wave 2 |
| "AI item" detection noise | Two-stage retrieval + 300-item gold set with reported precision/recall |
| Selection bias (big cities only) | Own it: frame as "large-city" study; the roster artifact makes the frame explicit |
| Caption quality | Captions are supplementary; minutes and attachments are the primary text |
| Rate limits / scraping etiquette | Public APIs, throttled, cached raw responses committed for reproducibility |

## Timeline

Roughly 10–12 weeks end-to-end: Phase 0 (wk 1) → Phase 1 (wks 2–5) → Phase 2 (wks 5–9) →
Phase 3 (wks 8–11). First public artifact (tracker v1) plausible around week 6.

## Immediate next actions

1. **Sunil:** allow-list the domains in §0.1 in the environment's network settings.
2. **Claude:** on confirmation, run the Phase 0 API probe and signal check; report the
   go/no-go numbers.
