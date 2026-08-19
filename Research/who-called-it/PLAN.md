# Execution Plan — Study #8: Who Called It?

**An accountability audit of a decade of AI predictions**
*Plan drafted 2026-08-19. Status: approved to plan; Phase 0 pending.*

---

## Objective

Score the resolved AI predictions of four cohorts — (a) surveyed AI researchers, (b) prediction
markets/platform forecasters, (c) prominent public commentators, (d) AI lab leadership — and
publish (i) a peer-reviewable calibration study and (ii) a public, maintained
**AI Prediction Scorecard**.

Core questions:

- **Q1 (calibration):** Which cohort is most accurate on resolvable AI claims (Brier scores,
  calibration curves)?
- **Q2 (signatures):** Do error directions cluster by ideology (accelerationist vs. skeptic vs.
  safety-focused, using our ideologies-map taxonomy), proximity to the technology, or incentive?
- **Q3 (lead/lag):** Did prediction markets anticipate expert-survey updates or trail them?

## The methodological spine: no cherry-picking

The study lives or dies on claim selection. Three rules, frozen before scoring:

1. **Pre-registered sampling frames** (below) define which claims enter; no claim added after
   its resolution is known to us *unless* it comes through a frame.
2. **Operationalizability filter:** a claim enters only if two coders independently agree on a
   resolution criterion *before* looking up the outcome. Report the exclusion rate and a
   taxonomy of what got excluded (this is itself a finding — how much AI punditry is
   unscoreable in principle).
3. **Blind resolution:** claims are resolved by a coder who sees the claim text with claimant
   identity masked.

## Sampling frames

- **F1 — Expert surveys:** AI Impacts / ESPAI 2016, 2022, 2023 item-level results (published);
  Grace et al. milestone timelines with explicit resolution criteria. Score every item whose
  window has closed by 2026.
- **F2 — Platforms:** All Metaculus AI-category questions resolved by cutoff (public API);
  Manifold AI markets above a liquidity floor (public API). Community prediction at fixed
  horizons (question midpoint; 6 months before resolution).
- **F3 — Pundits/executives:** Every AI prediction published 2015–2024 in a fixed outlet set
  (NYT, WSJ, WaPo, FT, Economist, Wired, MIT Tech Review op-ed/columns) by a fixed speaker
  roster (top-100 most-cited AI commentators, roster built from citation frequency in those
  outlets *before* any scoring) — plus lab-leadership claims from earnings calls, keynotes,
  and published interviews. Timestamped via outlet archives and the Wayback Machine.
- **F4 — Documented-forecast sets others assembled** (e.g., contest archives, "AGI timeline"
  compilations) used only as *pointers* back to primary timestamped sources.

## Phases

### Phase 0 — Feasibility probes (gate) — ~1 week

- **0.1 Network access.** Session egress currently blocks `www.metaculus.com` and general web
  (verified 2026-08-19). Required allow-list: `www.metaculus.com`, `api.manifold.markets`,
  `web.archive.org`, `aiimpacts.org`, plus outlet archive domains as needed. Alternative:
  local collection.
- **0.2 API probes:** pull 20 resolved Metaculus AI questions and 20 Manifold markets; confirm
  fields (resolution, community prediction time series, close dates).
- **0.3 Survey data:** confirm item-level ESPAI data is downloadable (AI Impacts publishes
  summaries; item-level may require the published appendix or author contact — flag early).
- **0.4 Pilot pundit sweep:** one outlet (Wired), one year (2019): extract candidate
  predictions, run the operationalizability filter. **Go/no-go gate:** if < 25% of extracted
  pundit claims are scoreable, narrow the paper to F1+F2 cohorts and reframe the pundit
  section as "the unscoreability of AI punditry" (still publishable, arguably spicier).

### Phase 1 — Claims database — ~4 weeks

- **1.1 Schema:** claim_id, speaker, cohort, ideology tag (from our ideologies-map taxonomy,
  assigned by coders blind to accuracy), claim text, source URL + archive snapshot, statement
  date, horizon, resolution criterion, resolution (true/false/partial/unresolvable),
  resolution evidence URL, coder ids.
- **1.2 Platform ingest** (scripted, from F2). **1.3 Survey ingest** (F1).
- **1.4 Pundit corpus:** LLM-assisted extraction of prediction-shaped sentences from the F3
  outlet/speaker sweep, then human operationalizability coding (two coders; disagreements
  adjudicated; kappa reported).
- **1.5 Blind resolution** of all operationalized claims; second-coder check on a 20% sample.
- Target scale: 300–600 scored claims outside the platform set (platforms add thousands).

### Phase 2 — Analysis — ~3 weeks

- **2.1** Brier scores and calibration curves by cohort; bootstrap CIs; difficulty adjustment
  by matching claims on topic and horizon.
- **2.2** Error-direction models: over-optimism/pessimism vs. ideology tag, employment
  (lab-affiliated vs. not), and incentive proxies.
- **2.3** Lead/lag: for milestones covered by both surveys and markets, compare update timing.
- **2.4** The 13-year timeline collapse (our prior study's finding): decompose into accuracy
  gain vs. herding using post-collapse resolutions.
- **2.5** Robustness: alternative scoring rules (log score), exclude partial resolutions,
  vary the pundit roster cutoff.

### Phase 3 — Deliverables — ~3 weeks, overlapping

- **3.1 Scorecard:** public artifact — sortable per-person and per-cohort scorecard, each
  score linking to the claim, source, and resolution evidence. Every cell must be
  receipt-backed; this artifact will be attacked by everyone who scores badly, so the
  evidence chain is the defense.
- **3.2 Paper:** target *PNAS Nexus* or *International Journal of Forecasting*; preprint
  immediately.
- **3.3 Right-of-reply:** before public launch, email each named individual their entries and
  a 2-week window to dispute resolution coding (not scores). This is both ethics and armor.

## Pre-registration

Freeze frames F1–F4, the roster, the operationalizability rule, scoring rules, and models on
OSF before Phase 1 scoring begins; commit hash in this repo.

## Division of labor

- **Claude:** ingest scripts, extraction prompts, the claims database, scoring/analysis code,
  scorecard build, paper draft. Extraction and resolution-evidence gathering parallelize well
  across subagents (per-outlet, per-year).
- **Sunil:** network allow-list; serve as (or recruit) the second human coder for
  operationalizability and the 20% resolution audit; decisions on naming individuals vs.
  cohort-only reporting in v1 (recommend: name public figures, they're public claims — but
  this is a judgment call you should own); right-of-reply outreach comes better from a human.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Cherry-picking accusation | Pre-registered frames, blind resolution, published exclusions — the whole spine |
| Resolution disputes | Right-of-reply window; publish evidence per claim; report disputed cells |
| Pundit claims mostly unscoreable | Phase 0.4 gate with a planned pivot that is itself a finding |
| Legal/reputational pushback from named figures | Public claims, public record, receipts; cohort-only fallback exists |
| ESPAI item-level data unavailable | Use published milestone tables; author contact; worst case F1 shrinks, F2 carries Q3 |
| Archive paywalls for F3 | Wayback Machine snapshots; library access if needed |

## Timeline

Roughly 10–11 weeks: Phase 0 (wk 1) → Phase 1 (wks 2–6) → Phase 2 (wks 6–9) → Phase 3
(wks 8–11). The two studies (#7 and #8) share infrastructure (archive fetching, claim/item
databases, coder workflow) and can run in parallel, staggered by a week.

## Immediate next actions

1. **Sunil:** allow-list the §0.1 domains in the environment network settings.
2. **Claude:** run Phase 0 probes for both studies the moment access lands; report go/no-go
   numbers for the two gates in one memo.
