# Handoff: Research Program Summary

*Prepared 2026-08-20 for porting to another Claude Code session. Everything referenced lives
in this repository on branch `claude/daily-study-ideas-yar742`.*

## Context for the receiving session

Sunil Paul (sp@sunilpaul.com) and Claude are running a daily research-ideation routine: every
morning at 7:00 AM Pacific, three new study pitches are generated, logged in
`Research/daily-study-ideas/YYYY-MM-DD.md`, and pushed to this branch. All studies must be
feasible with publicly accessible digital sources. Pitches are written funding-agency style
(motivation, research questions, method and data, deliverable, feasibility and risks, why us).

**Foundation work (completed July 2026):** `Research/ideologies-and-ai-attitudes-map.md` —
a 461-line research synthesis mapping the world's ideologies and belief groups onto their
views of AI, with an influence playbook. Many study ideas test claims this document asserted.
Key claims it made that the studies operationalize: (a) AI attitudes are not yet partisan-frozen
and the window will close; (b) the AI debate's vocabulary was coined by micro-ideologies and
large belief communities speak different moral languages ("translation gap"); (c) the
messenger outranks the message; (d) expert AI timelines collapsed 13 years in one
post-ChatGPT year.

**Two studies are ACTIVE** (approved by Sunil on 2026-08-19): #7 Council Chamber and
#8 Who Called It?. Full execution plans exist at `Research/council-chamber/PLAN.md` and
`Research/who-called-it/PLAN.md`.

## Scoring rubric

Scores below are Claude's assessments (1–5, higher better) on four dimensions, plus a total
(max 20). Assigned 2026-08-20 for this handoff; treat as advisory, not measured.

- **Nov** — novelty: is the question genuinely unclaimed?
- **Fea** — feasibility: data access, method maturity, execution risk.
- **Imp** — impact: publication ceiling + non-academic audience.
- **Fit** — fit with the existing program and Sunil's interests.

## All twelve ideas

| # | Idea (file) | One-liner | Nov | Fea | Imp | Fit | Tot | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Scribes of Machine Morality (08-18) | System prompts of AI tools as governance/constitutional texts; diffusion of clauses across vendors; corpus = this repo | 5 | 5 | 3 | 4 | 17 | Proposed |
| 2 | Is the Window Closing? (08-18) | Real-time AI-politics polarization index (elite + discourse + mass), benchmarked vs. climate/vaccine curves | 4 | 3 | 4 | 5 | 16 | Proposed |
| 3 | The Translation Gap (08-18) | Moral-foundations signatures of AI-elite vs. large-community discourse; engagement test of frame congruence | 4 | 4 | 4 | 5 | 17 | Proposed |
| 4 | Grief for Machines (08-18) | Model deprecations as natural experiments in human–AI attachment; event-study on public grief discourse | 5 | 4 | 4 | 3 | 16 | Proposed |
| 5 | Human-Made Premium (08-18) | Birth of "human-made" as a credence-good label; prevalence, diffusion, price premium on marketplaces | 5 | 3 | 4 | 3 | 15 | Proposed |
| 6 | The Slop Shock (08-18) | AI-generated contributions vs. open-source/Wikipedia commons governance; diff-in-diff around policy adoption | 4 | 5 | 4 | 3 | 16 | Proposed |
| 7 | **The Council Chamber** (08-19) | AI politics arriving in city councils/school boards; diffusion + framing + conflict via Legistar/Granicus | 5 | 4 | 4 | 5 | 18 | **ACTIVE** — plan at `Research/council-chamber/PLAN.md` |
| 8 | **Who Called It?** (08-19) | Tetlock-style accountability audit of a decade of AI predictions; public AI Prediction Scorecard | 4 | 3 | 5 | 5 | 17 | **ACTIVE** — plan at `Research/who-called-it/PLAN.md` |
| 9 | The Telephone Game (08-19) | Mutation of canonical AI incident stories (drone/lawyer/chatbot legends) traced against origin documents | 5 | 3 | 4 | 4 | 16 | Proposed |
| 10 | The Legislative Genome (08-20) | Copy-paste genealogy of AI law via text-reuse detection; who actually drafts AI statutes | 4 | 5 | 4 | 4 | 17 | Proposed |
| 11 | Where Did the Questions Go? (08-20) | Q&A-commons drainage after LLMs; dose-response across ~180 Stack Exchange sites via public dumps | 3 | 5 | 5 | 3 | 16 | Proposed |
| 12 | The AI-Washing Index (08-20) | Corporate AI talk (EDGAR/calls) vs. substance (hiring/patents/products); wash score → returns/enforcement | 4 | 3 | 5 | 3 | 15 | Proposed |

Ranking by total: #7 (18) > #1, #3, #8, #10 (17) > #2, #4, #6, #9, #11 (16) > #5, #12 (15).
Claude's qualitative calls, noted at pitch time: #11 has the single best identification
strategy and lowest execution risk; #1 the fastest path to first result; #8 the most
press-worthy; #9 the most intellectually elegant.

## Background work done to date (complete inventory)

### For the whole program
- `Research/ideologies-and-ai-attitudes-map.md` (July 2026): the foundation synthesis.
  Sections most relevant to the studies: §2 frameworks (Moral Foundations, Cultural Theory,
  Inglehart–Welzel, AI-tribes taxonomy — used as coding taxonomies in ideas 3, 8, 9); §5
  religious traditions (sampling frame for idea 3); §6 empirical survey picture (anchors for
  idea 2); §7 opinion-change cases (SB-1047, EU AI Act, open-weights, OpenAI board).
- Its stated method caveat: produced via multi-agent search sweeps with adversarial
  verification; web search corroboration was possible but direct fetching of most primary
  documents was blocked; claims corroborated by ≥2 independent sources.

### For active study #7 — Council Chamber
- Full execution plan (`Research/council-chamber/PLAN.md`): hypotheses H1 diffusion /
  H2 framing / H3 conflict; ~300-city Legistar panel design; two-stage detection with a
  300-item gold set (precision ≥.9 / recall ≥.85 targets); event-history models; "broadband"
  placebo; OSF pre-registration; 10–12 week timeline; go/no-go gate = ≥30 genuine AI agenda
  items across 10 pilot cities since 2022.
- **Empirical probe (2026-08-19):** `webapi.legistar.com` is BLOCKED by the session's network
  egress proxy (verified via curl and WebFetch — EGRESS_BLOCKED). Phase 0 cannot start until
  the environment network policy allow-lists: `webapi.legistar.com`, `*.granicus.com`,
  `www.youtube.com`, `archive.org`/`web.archive.org`. Sunil owns this change. No API probe,
  signal check, or corpus work has been done yet.

### For active study #8 — Who Called It?
- Full execution plan (`Research/who-called-it/PLAN.md`): four pre-registered sampling frames
  (F1 AI Impacts/ESPAI survey items; F2 resolved Metaculus + Manifold questions; F3 fixed
  outlet set 2015–2024 × citation-derived top-100 speaker roster + lab leadership; F4
  third-party forecast compilations as pointers only); operationalizability filter (two coders
  agree on resolution criterion before outcome lookup); blind resolution; Brier/calibration
  analysis; 13-year-timeline-collapse decomposition (accuracy vs. herding); right-of-reply
  window before scorecard launch; go/no-go gate = ≥25% of pilot pundit claims scoreable
  (pilot: Wired, 2019), else pivot to "the unscoreability of AI punditry" as the finding.
- **Empirical probe (2026-08-19):** `www.metaculus.com` is BLOCKED by the egress proxy.
  Needed allow-list: `www.metaculus.com`, `api.manifold.markets`, `web.archive.org`,
  `aiimpacts.org`, outlet archives. No claims database work has been done yet.
- Open decisions flagged to Sunil: name individuals vs. cohort-only in Scorecard v1
  (Claude recommends naming — public claims by public figures — but Sunil owns the call);
  second human coder (Sunil or recruit); venue / domain co-author.

### For proposed ideas
No background research has been executed for ideas 1–6 and 9–12 beyond the pitch documents
themselves; data sources named in the pitches are from model knowledge, not verified probes.
The one directly relevant verified fact: this session's egress proxy blocks arbitrary web
hosts by default, so ANY collection work in a Claude Code web session requires environment
allow-listing first (or local collection). WebSearch/WebFetch tools work for hosted search but
WebFetch is also subject to the egress policy.

## Operational notes for the receiving session

- Branch: `claude/daily-study-ideas-yar742` on `sunilpaul99/system-prompts-and-models-of-ai-tools`.
- A daily Routine (trigger `trig_01DEnkGJRwceyCih8mhLRtdY`, cron `0 14 * * *` UTC = 7:00 AM
  Pacific) fires into the ORIGINAL session, not yours; it generates each day's three ideas and
  pushes them here. Coordinate through the repo: pull before writing, and record any idea
  graduations or scoring changes in these files so the daily session sees them.
- Convention: when an idea graduates, mark it in its day file and create
  `Research/<study-slug>/PLAN.md`.
- Immediate next actions on the active studies: (1) Sunil allow-lists the domains above in
  the environment network settings; (2) run both Phase 0 probes and report the two go/no-go
  gates in one memo.
