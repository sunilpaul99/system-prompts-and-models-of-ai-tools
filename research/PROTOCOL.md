# Study Protocol: LLM Adoption and Language Change in Podcast Hosts' Speech — A Signal-Finding Pilot

**Working title:** Is personal LLM adoption associated with drift toward LLM-characteristic language in one's own spontaneous speech? A blinded within-person pilot study of podcast hosts, 2019–2026.

**Status:** DRAFT v0.2 — not yet frozen.
**Principal investigator:** Sunil Paul (independent researcher)
**Drafted:** 2026-07-27 (v0.1); revised 2026-07-27 (v0.2)
**Freeze date:** _(to be stamped when ratified)_

---

## 0. Purpose and decision framing

This is a **pilot study**, not the definitive study. Its purpose is to determine whether an individual-level signal exists that would justify recommending a full-scale academic study, and to produce a validated methodology (pipeline, feature lists, exposure rubric, measured effect-size and variance estimates) that an academic team could inherit.

The output is one of three recommendations, per the decision table in Section 8:

- **GO** — a credible individual-level signal exists; encourage academic replication at scale.
- **NO-SIGNAL** — a clean pipeline found no individual-level differential; the population-level trend likely reflects ambient transmission, composition, or assisted production. Still worth communicating; changes what the "real" study should be.
- **INCONCLUSIVE** — pipeline or classification problems prevent a read; report what broke, which is itself useful to academics.

Scope discipline: wherever a design choice trades rigor against feasibility, this protocol chooses the option adequate for a *screening decision*, and records the upgrade a full study should make (Appendix C, "Handoff notes").

## 1. Research question and estimand

**Question.** Among long-running podcast hosts, is documented personal adoption of LLM tools associated with a larger increase in LLM-characteristic language in the host's own spontaneous speech, relative to hosts with documented non-use or rare use?

**Estimand (honest version).** The differential pre-to-post change in fingerprint-feature rates between hosts with direct evidence of regular LLM use and hosts with direct evidence of rare/non-use, under conditional parallel trends. This is an **association**. "Unconscious absorption" is one candidate mechanism; LLM-assisted show preparation (outlines, questions, talking points that shape nominally spontaneous speech) is another, and this design cannot fully separate them. Speech as the outcome medium rules out verbatim copy-paste only.

**H1 (primary).** The fingerprint-rate increase (composite lexical rate, Section 5.1) is larger among CONFIRMED-USE hosts than CONFIRMED-NONUSE hosts.

**Negative-control analyses (not "hypotheses to confirm"):**
- **NC1 — placebo words:** the same contrast on matched non-LLM words should show no comparable differential.
- **NC2 — pseudo-intervention:** the H1 model re-run with a fake adoption date of 2020-07 inside the pre-period should show no effect.
- **NC3 — guest speech:** guest-attributed speech processed by the identical pipeline serves as a pipeline-artifact detector (guests vary; pipeline is constant).

**Exploratory (clearly labeled, no confirmatory weight):** discourse-level features (Section 5.2); adoption-date event-time alignment; per-word contribution; LIGHT-by-absence hosts.

## 2. Design overview

Within-person panel. For each host, feature rates are measured per calendar half-year, 2019-H1 through 2026-H1. Pre period: 2019-H1–2022-H1. Washout (excluded): 2022-H2–2023-H1. Post period: 2023-H2–2026-H1.

**Blinding rules:**
- Exposure classification for a host is completed and frozen before any of that host's feature data is viewed.
- No one (PI or agent) computes any exposure × feature-rate contrast until data collection is declared complete ("peeking rule"). Interim reporting is limited to coverage and exposure-blind pooled rates.

## 3. Panel selection

### 3.1 Sampling frame (survivorship-aware)

The frame is built from **archived pre-treatment charts**: Wayback Machine captures of Apple Podcasts US top-200 charts (or Chartable equivalents) dated 2020–2021, for genres Technology, Society & Culture, History, Comedy, Sports, Business, Science. Shows are then followed *forward*. The frame snapshot (URLs, capture dates, full list) is committed to the repo before eligibility screening. Target population, stated honestly: hosts of popular, long-running, English-language conversational podcasts active by 2020–2021 — not podcast hosts in general.

### 3.2 Eligibility (assessed before exposure is examined)

- **I1.** English-language; predominantly unscripted conversational format (spot-check 3 random episodes against a written rubric; borderline → decision queue).
- **I2.** Same primary host from 2019 through 2025, ≥12 episodes/year each year.
- **I3.** Host speaks ≥30% of airtime (pilot diarization on 3 episodes).
- **I4.** Audio retrievable for ≥70% of sampled periods in both pre and post.
- **E1.** Excluded: shows whose dominant recurring topic pre-2022 is AI/ML (topic confound); shows with heavy speech post-production; at most one host per show (co-hosts share production environments — the primary host only).

### 3.3 Panel size (pilot-scaled)

Target **24 hosts**: 12 CONFIRMED-USE, 12 CONFIRMED-NONUSE (minimum acceptable 9 per arm), with ≥40% of the panel from non-technology genres, balanced across arms as evenly as the frame allows. If eligible hosts exceed need, selection is by fixed random seed from the eligible pool, recorded in the repo. Cell shortfalls are reported, not rebalanced silently.

Rationale: 24 hosts cannot detect a subtle effect; they can detect the *moderate-to-large* effect that would make a full study clearly worthwhile, and can estimate the variance components a real power analysis needs. That matches the pilot's decision purpose. A post-pilot simulation (Section 8.3) converts observed variance into "the full study needs N hosts" — a key handoff deliverable.

### 3.4 Episode sampling

**5 episodes per host per half-year**, fixed random seed, minimum duration 20 minutes; rebroadcasts, compilation episodes, and guest-host episodes excluded by rule. ≈ 24 × 15 × 5 = 1,800 episodes ≈ 1,500–2,000 audio-hours. Minimum analyzable host-period: 5,000 host-attributed words; below that, the period is marked missing (not zero-filled).

## 4. Exposure classification

### 4.1 Categories (time-anchored)

- **CONFIRMED-USE:** direct self-report of regular LLM use (≈weekly or more, for any purpose), with an **adoption interval** [earliest evidence date, latest "not yet using" date if any]. The label applies only from the adoption interval forward.
- **CONFIRMED-NONUSE:** direct self-report of non-use or rare use, valid over the period the statements cover; re-checked for later adoption statements through 2026.
- **UNKNOWN:** everything else — including hosts with *no* statements found (absence of evidence is not classified as non-use in the confirmatory analysis; such hosts are exploratory only).

**Professional AI involvement** (works at/founded an AI company, ships AI products) is recorded as a **covariate**, not exposure evidence.

Each dossier records: verbatim quotes, source URLs, statement dates, the date the statement refers to, evidence strength (direct/indirect), and search-checklist completion.

### 4.2 Procedure, blinding, reliability

The agent assembles dossiers using the fixed search checklist (Appendix B), gathering exposure evidence only — never reading transcripts for language features. Labels are ratified by the PI, and **by one independent second rater** (a recruited collaborator following the written rubric, blind to all language data) if available; agreement is reported. If no second rater can be recruited, single-rater status is a declared limitation. Disagreements → UNKNOWN.

### 4.3 Declared limitations

Exposure is from public statements: measurement error is certain, and may be *differential* (tech hosts more searchable and more disclosure-prone). Mitigations: non-tech genre quota, professional-involvement covariate, and honest framing of the estimand. No claim is made about the direction of misclassification bias.

## 5. Outcome measures

Rates are computed from counts per host-period with host-attributed word count as denominator.

### 5.1 Primary endpoint: composite lexical fingerprint rate

One primary endpoint: the summed count of the frozen lexical fingerprint list per host-period. Candidate list (from Yakura et al. 2024; Anderson & Galpin AIES 2025; Kobak et al.):

> delve, meticulous(ly), intricate/intricacies, underscore [verb], showcase [verb], boast [="features"], pivotal, realm, bolster, commendable, surpass, adept, garner, noteworthy, multifaceted

**Pre-freeze validation gates for each candidate word (Appendix A records pass/fail):**
1. Not already trending upward 2015–2021 in a **spoken** reference (Spotify/TAL podcast corpora, COCA-spoken, subtitle corpora — not Google Books alone).
2. Overrepresented in LLM output vs. matched human *speech-register* text (verified by generating matched-topic LLM text and comparing, not assumed from academic-text studies).
3. ASR-stable: Whisper sensitivity/specificity for the word checked on audio from both eras (Section 6.1).
4. Sense-disambiguation rule defined where needed ("boast," "underscore," "realm," "showcase"): LLM-based sense filter with a 100-instance human-audited sample per ambiguous word.

Lemmatization, contraction, and disfluency handling rules are fixed in Appendix A. Words failing any gate are dropped and logged. **Aggregation rule:** the composite is the sum of counts; per-word rates are reported descriptively, and a leave-one-out sensitivity shows whether any single word drives the result (if so, that is stated in the write-up — a one-word effect is a different finding than general style transfer).

### 5.2 Exploratory: discourse features (trimmed)

Two features only, chosen for detectability: (a) the contrastive reframe ("It's not just X — it's Y"); (b) summarizing meta-turns ("So, to recap…"). Detection by pattern rules + LLM annotation; validated for **precision and recall** on a 200-instance human-labeled sample balanced across pre/post periods, annotators blind to period. Reported as exploratory regardless of outcome.

### 5.3 Placebo words (NC1)

Matched to fingerprint words on: spoken-corpus baseline frequency (2015–2021), part of speech, and flat pre-trend; and checked for comparable ASR error rates (Section 6.1). Candidate list refined during Appendix A construction; frozen simultaneously with the fingerprint list. Topic-sensitivity matching is approximate — declared as such.

### 5.4 Meta-mention rule

Occurrences within 50 words of explicit AI-language references ("ChatGPT always says delve") are flagged. Primary analysis excludes flagged occurrences; **pre-registered sensitivity analyses run with no exclusion and with a 20-word window.** All exclusions logged with context; 5% audited by PI.

## 6. Pipeline

Fetch (RSS/archived feeds) → transcribe (Whisper, single pinned version) → diarize (host voice enrolled from 3 reference episodes) → sense-filter and count on host-attributed speech → delete audio, retain host-speech transcripts, counts, logs.

### 6.1 Validity checks

- **V1 — ASR bias, both eras and both lists:** on ≥10 hours of audio with verbatim ground-truth transcripts drawn from both pre-2021 and post-2023 sources, measure Whisper insertion *and* deletion rates for fingerprint and placebo words separately. Gate: insertion <1/100k words and no material fingerprint-vs-placebo asymmetry; else change transcriber before freeze.
- **V2 — Reproducibility:** 1% of episodes re-processed each cycle; counts must reproduce ±2%.
- **V3 — Diarization audit:** stratified manual check (by era × genre) of 40 episode segments against human labeling; host-attribution accuracy ≥90%, reported.
- **V4 — Placebo monitor + coverage ledger:** continuous, in every daily brief.

## 7. Analysis plan

**Primary model:** Poisson regression of the composite fingerprint count with host fixed effects, half-year fixed effects, host-period word-count offset, and the CONFIRMED-USE × post interaction. Overdispersion assessed; quasi-Poisson as the pre-specified fallback. Episode-level data retained; primary model at host-period level.

**Inference:** randomization inference — permute exposure labels across hosts (respecting arm sizes) 10,000 times; report the permutation p-value for the interaction. This is the primary test (24 clusters is too few for asymptotic cluster-robust inference).

**Negative controls:** NC1 (placebo composite, same model — and a single pre-specified contrast test: interaction(fingerprint) − interaction(placebo) via permutation); NC2 (pseudo-date 2020-07); NC3 (guest speech, descriptive).

**Pre-trend assessment:** event-study-style plot of per-half-year arm differences with CIs across the pre-period; and a declared substantive bound — a pre-period differential trend exceeding 50% of the observed post effect renders H1 INCONCLUSIVE regardless of p-value. (No reliance on a low-powered nonsignificance test.)

**Pre-specified sensitivities:** leave-one-word-out; meta-mention windows (0/20/50); excluding tech-genre hosts; excluding hosts with professional AI involvement; minimum-word-count threshold doubled.

**Covariate:** professional AI involvement × post, as a robustness specification.

## 8. Decision rules (the point of the pilot)

### 8.1 Interpretation table

| H1 (permutation p, effect direction) | NC1 placebo | Pre-trend bound | Recommendation |
|---|---|---|---|
| p<0.05, positive | clean | ok | **GO** — encourage full academic study |
| 0.05≤p<0.20, positive, rate ratio ≥1.3 | clean | ok | **GO (weak)** — signal plausible; full study with proper N justified |
| p≥0.20 or rate ratio <1.15 | clean | ok | **NO-SIGNAL** — report; recommend academics study ambient/population mechanisms instead |
| any | placebo differential comparable to H1 | — | **INCONCLUSIVE** — artifact suspected; report diagnosis |
| any | — | violated | **INCONCLUSIVE** — differential trends; report |

The GO(weak) row exists because a pilot of 24 hosts is designed to detect *large* effects; a moderate positive estimate with p≈0.1 is exactly the "worth a real study" outcome. A null here does NOT establish absence — the write-up states the minimum rate ratio the pilot could plausibly have detected (from 8.3) and bounds the claim accordingly.

### 8.2 Power realism (pre-freeze gate)

Before freeze, run a simulation using pilot-phase estimates (baseline rates, host heterogeneity, serial correlation, words per period from the Phase 2 technical pilot): report the minimum detectable rate ratio at n=24 (and n=18 floor). **If the detectable rate ratio exceeds 2.0, the design is revised (more hosts, more episodes, or narrower feature set) before freezing.** Simulation code committed to the repo.

### 8.3 Handoff deliverable

Regardless of outcome: frozen protocol + changelog, open pipeline code, per-host-period feature dataset (see 9), variance-component estimates, and a one-page "design memo for the full study" (required N from simulation, exposure-rubric lessons, pipeline failure modes) — written for an academic audience. This memo is the artifact used to recruit academic interest.

## 9. Ethics and data governance

- Subjects are public figures analyzed via publicly published speech and public statements; no contact, no private data.
- **Exposure dossiers are private** (not released — they aggregate personal statements in a way hosts didn't anticipate). Released data: de-identified per-host-period feature counts (random host IDs, genre kept, show names withheld). True anonymity among well-known hosts is imperfect; the release contains no exposure labels linked to identifiable hosts.
- Host-identifiable results appear in the write-up only if (pre-declared rule) the finding cannot be communicated otherwise AND the disclosed fact is something the host has stated publicly themselves.
- Informal ethics consult: at least one person with IRB experience reads this protocol before freeze; their comments logged.
- Terms-of-service check for each audio source before bulk download; official transcripts used only where verified verbatim; audio deleted after feature extraction; retention: transcripts and counts for 3 years, then review.
- Sensitive incidental material in transcripts (health disclosures etc.) is not extracted, quoted, or released; only word counts leave the pipeline.

## 10. Agent operating rules

Unchanged in substance from v0.1: the deviation rule (protocol-derivable actions proceed; interpretation/extension/exclusion decisions queue for the PI with a recommendation); always-queued items (every exposure label, every exclusion, every anomaly, budget ≥80% of cap); never-done items (peeking, post-freeze edits to Appendices A/B, contacting anyone, publishing); daily brief = scorecard (V1–V4) + coverage + decision queue + spend. Full text in Appendix D.

## 11. Budget and schedule

- ~1,800 episodes ≈ 1,500–2,000 audio-hours. Transcription: local Whisper preferred (≈$0, slower) with API fallback; hard cap **$400** total external spend, set at freeze.
- Phases: Technical pilot (3 hosts end-to-end, feeds V1/V3 and the 8.2 simulation) ~1–2 weeks → Frame + eligibility + exposure dossiers ~2–3 weeks → Freeze → Collection ~4–6 weeks → Analysis ~1 week → Write-up + design memo ~2 weeks.

## 12. Outputs

Public write-up (essay and/or arXiv preprint), open code and de-identified dataset, and the Section 8.3 design memo. The protocol is posted publicly (OSF) at freeze.

---

## Appendix A — Frozen feature lists and text-processing rules
_(Populated during technical pilot; frozen at freeze date: final fingerprint list with per-word gate results, placebo list with matching table, lemmatization/sense rules.)_

## Appendix B — Exposure evidence search checklist
_(Fixed queries and sources per host; frozen before dossier work begins.)_

## Appendix C — Handoff notes for a full study
_(Running list of rigor upgrades deliberately deferred: staggered-adoption estimator, larger panel, dual human raters throughout, full topic adjustment, formal measurement-error model, formal equivalence bounds.)_

## Appendix D — Agent operating rules (full text)
_(Carried from v0.1 §8.)_

## Changelog

- **2026-07-27 v0.1 → v0.2** (pre-freeze revision, responding to external methods review): reframed as decision-oriented pilot with GO/NO-SIGNAL/INCONCLUSIVE rules; estimand narrowed to association, assisted-preparation pathway acknowledged; exposure rebuilt as time-anchored confirmed-use/confirmed-nonuse with professional involvement as covariate and absence-of-evidence demoted to exploratory; sampling frame moved to archived 2020–2021 charts; panel cut 48→24 hosts, sampling cut to 5 episodes/host-half-year (fixing v0.1's budget inconsistency); primary model changed to Poisson FE with offset and permutation inference; placebo recast as negative control with a single pre-specified contrast; pseudo-date and guest-speech negative controls added; ASR check extended to both eras and both lists; discourse features trimmed to two, exploratory; power-realism gate (8.2) and interpretation table (8.1) added; ethics section expanded (private dossiers, de-identified release, consult requirement).
