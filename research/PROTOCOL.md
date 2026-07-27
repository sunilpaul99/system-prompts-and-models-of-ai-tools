# Study Protocol: Individual-Level Absorption of LLM Style in Spontaneous Speech

**Working title:** Does personal LLM use predict drift toward LLM-characteristic language in one's own unassisted speech? A within-person panel study of podcast hosts, 2019–2026.

**Status:** DRAFT v0.1 — not yet frozen. All sections open for revision.
**Principal investigator:** Sunil Paul (independent researcher)
**Drafted:** 2026-07-27
**Freeze date:** _(to be stamped when ratified)_

---

## 1. Research question and hypotheses

**Question.** Is the documented population-level rise of LLM-characteristic language in spontaneous human speech (Yakura et al. 2024, arXiv:2409.01754; Anderson, Galpin et al., AIES 2025) driven by *individual absorption proportional to personal LLM exposure*, or is it uniform ambient cultural transmission independent of personal use?

**H1 (primary — dose-response).** Hosts classified as heavy LLM users show a larger pre-to-post-ChatGPT increase in fingerprint-feature rates in their own spontaneous speech than hosts classified as light/non-users.

**H2 (validity — placebo null).** Neither group shows a comparable increase in placebo features (register- and frequency-matched words with no LLM overrepresentation). A placebo increase in either group indicates pipeline artifact or general register drift, and weakens any H1 interpretation.

**H3 (exploratory — discourse-level transfer).** Discourse/pragmatic fingerprint features (Section 5.2) increase post-ChatGPT; whether they show dose-response is exploratory, not confirmatory.

**All three primary outcomes are publishable:** dose-dependent drift (absorption), uniform drift (ambient transmission), or no individual-level signal (population trend reflects composition or assisted text, not changed speakers).

---

## 2. Design overview

Within-person panel design. For each host in a fixed panel, we measure feature rates in their own speech in each calendar half-year from 2019-H1 through 2026-H1, then compare within-host change across exposure groups (difference-in-differences with host fixed effects). Spontaneous *speech* is the outcome medium because it cannot be copy-pasted, eliminating the assisted-authorship confound.

Key blinding rule: **exposure classification (Section 4) is completed and frozen for each host before that host's language data is analyzed.** Evidence gathering for exposure must not include reading/listening for fingerprint features.

---

## 3. Panel selection

### 3.1 Enumeration (anti-cherry-picking)

Candidate podcasts are enumerated mechanically, not from memory:

1. Take the top 250 shows in each of Apple Podcasts' US charts for these genres as of the enumeration date: Technology, Society & Culture, History, Comedy (Interviews), Sports, Business, Science.
2. Supplement with Podchaser/Listen Notes "long-running" filters for the same genres.
3. Record the full enumerated list with timestamps before applying any inclusion criteria.

### 3.2 Inclusion criteria (all required)

- **I1.** English-language.
- **I2.** Predominantly unscripted conversational format (interview, co-host banter, call-in). Shows that are read essays, audio dramas, or narrated documentaries are excluded. Operational test: spot-check 3 random episodes; if host speech is evidently read from a script in ≥2, exclude.
- **I3.** Continuous run: ≥12 published episodes per calendar year in every year 2019–2025, with the same primary host throughout.
- **I4.** Primary host speaks an estimated ≥30% of airtime (verified in pilot diarization on 3 episodes).
- **I5.** Audio or official transcripts retrievable for ≥70% of episodes in both the pre period (2019-01 to 2022-06) and post period (2023-07 to 2026-06).

### 3.3 Exclusion criteria

- **E1.** Podcast's core topic is AI/LLMs (e.g., shows *about* machine learning). Rationale: topic-driven vocabulary would mechanically inflate fingerprint words. Tech shows are eligible only if AI is not the dominant recurring subject pre-2022. Borderline cases go to the decision queue.
- **E2.** Host is a professional voice actor or the show has heavy post-production editing of speech.
- **E3.** Host's exposure classification comes back "unclassifiable" (Section 4.4) — retained in the dataset but excluded from H1 confirmatory analysis.

### 3.4 Panel size and balance

Target: **48 hosts** (minimum acceptable: 36), with targets of ≥16 likely-heavy and ≥16 likely-light exposure, and ≥40% of the panel from non-technology genres. If enumeration cannot fill these cells, the shortfall is logged and reported, not silently rebalanced.

Sampling within host: up to 24 episodes per host per half-year, selected by fixed random seed; episodes shorter than 20 minutes excluded.

---

## 4. Exposure classification rubric

### 4.1 Evidence sources (in scope)

Public statements only: the host's own remarks on their podcast (located via keyword search of transcripts for AI-related terms, NOT by listening broadly), their public social media, newsletters, interviews, bylined articles, and product/company affiliations (e.g., host founded an AI startup; host's employer mandates AI tools).

### 4.2 Categories

- **HEAVY:** Direct self-report of regular LLM use (weekly or more) for writing, research, show prep, or work, OR sustained professional immersion (works at/founded an AI company, ships AI products) with no disclaimers of non-use.
- **LIGHT:** Direct self-report of non-use or rare use, OR expressed avoidance/skepticism plus absence of any use evidence, OR (weakest tier) no evidence of use found after the full search checklist is completed — flagged as "LIGHT-by-absence" and reported separately in sensitivity analysis.
- **UNCLASSIFIABLE:** Contradictory evidence, or evidence only about their *team's* use, not their own.

Classification also records **adoption date** where determinable (earliest evidence of regular use), for exploratory lag analysis.

### 4.3 Procedure and blinding

The agent assembles a per-host evidence dossier (verbatim quotes, links, dates). The PI personally ratifies every label. Both agent and PI complete classification for a host **before** any feature data for that host is viewed. The dossier search checklist and queries are fixed in Appendix B before Phase 3 begins.

### 4.4 Known limitation (declared)

Exposure is measured with error (self-report, public evidence only). Misclassification is plausibly nondifferential and would bias H1 toward null — making a positive H1 finding conservative. This is stated, not solved.

---

## 5. Outcome measures

All rates computed as occurrences per 10,000 host-spoken words, per host per half-year.

### 5.1 Lexical fingerprint (confirmatory, H1)

Drawn from words empirically overrepresented in LLM output and used in prior studies (Yakura et al.; Anderson & Galpin; Kobak et al. on academic abstracts), restricted to words that were NOT already trending upward 2015–2021 (verified against Google Books Ngrams / GloWbE before freeze):

> delve (delves, delving), meticulous(ly), intricate / intricacies, underscore(s, -ing) [verb], showcase (-s, -ing) [verb], boast(s, -ing) [in the sense "features/offers"], pivotal, realm, bolster(ing), commendable, surpass(es, -ing), adept, garner(ed), noteworthy, multifaceted

Final list frozen in Appendix A after the pre-trend verification; candidates failing the pre-trend test are dropped and logged.

### 5.2 Discourse/pragmatic fingerprint (exploratory, H3)

Detected via pattern rules + LLM-assisted annotation with human-validated precision ≥0.85 on a 200-instance gold sample per feature:

- The contrastive reframe: "It's not (just) X — it's Y."
- Balanced triplet lists in speech ("clear, concise, and compelling").
- Preemptive both-sidesing / hedge stacks ("While X has merit, it's important to consider…").
- Summarizing meta-turns ("So, to recap…", "The key takeaway is…").
- Sycophantic acknowledgment before disagreement ("That's a great point, and…" → contradiction).

### 5.3 Placebo features (H2)

Words matched to the lexical fingerprint on register and 2015–2021 spoken-corpus frequency, with **no** LLM overrepresentation in published lists:

> accentuate, sturdy, immense, clever, quarrel, tidy, gloomy, brisk, drawback, hearty, keen [adj], swiftness-matched candidates finalized in Appendix A

Placebo list is frozen simultaneously with the fingerprint list and never revised after freeze.

### 5.4 Meta-mention exclusion rule

An occurrence is excluded when the word/pattern is *mentioned rather than used* — i.e., within 50 words of an explicit reference to AI language ("ChatGPT always says delve", "that sounds like AI"). Detection: rule-based flag + LLM adjudication; all exclusions logged with context windows and audit-sampled by the PI (5% random sample).

---

## 6. Data pipeline

1. **Fetch:** RSS/feed resolution and audio download. Official transcripts used where published *and* verified verbatim (spot-check vs. audio); otherwise transcribe.
2. **Transcribe:** Whisper (single pinned model version for the entire study; version recorded).
3. **Diarize:** speaker separation; host identified by voice enrollment from 3 reference episodes. Episodes with diarization confidence below threshold go to the exclusion queue, never silently dropped.
4. **Extract:** tokenize, count features on host-attributed speech only.
5. **Delete audio** after extraction; retain transcripts of host speech, feature counts, and logs.

### 6.1 Pipeline validity checks (standing, run throughout)

- **V1 — Transcriber-bias check:** before Phase 4, transcribe ≥10 hours of pre-2020 audio with published verbatim transcripts; confirm Whisper does not insert fingerprint words (insertion rate must be <1 per 100k words, else transcriber is reconsidered — this is a freeze-level gate).
- **V2 — Reproducibility probe:** each cycle, re-process a random 1% of completed episodes; feature counts must reproduce within ±2%.
- **V3 — Placebo monitor:** placebo rates computed continuously; sustained placebo drift triggers a red flag to the PI.
- **V4 — Coverage ledger:** attempted/completed/excluded episode counts per host per period, reported in every daily brief.

---

## 7. Analysis plan (pre-registered)

**Primary (H1):** Difference-in-differences on log fingerprint rate: host fixed effects, half-year fixed effects, interaction of post-period × HEAVY. Standard errors clustered by host. Pre period: 2019-H1–2022-H1. Washout (excluded): 2022-H2–2023-H1. Post period: 2023-H2–2026-H1. Significance threshold α=0.05, two-sided; effect size reported with 95% CI regardless of significance.

**H2:** identical model on placebo rates; the H1 interpretation requires the H1 interaction to significantly exceed the placebo interaction (seemingly-unrelated estimation or bootstrap contrast).

**Pre-trend check:** the HEAVY×half-year interactions within the pre period must be jointly null; if violated, H1 is reported with this caveat prominent.

**Sensitivity analyses (all pre-declared):** excluding LIGHT-by-absence hosts; excluding technology-genre hosts; per-word leave-one-out on the fingerprint list; guest-speech contamination check (re-run on episodes with diarization confidence in top tercile).

**Exploratory (labeled as such):** H3 discourse features; adoption-date lag alignment; per-feature transfer ranking.

**Peeking rule:** no one — PI or agent — computes any exposure × feature-rate cross-tabulation before Phase 4 data collection is declared complete. Interim reporting is limited to per-host coverage and pooled (exposure-blind) feature rates.

---

## 8. Agent operating rules and decision queue

**Deviation rule:** any action derivable from this protocol proceeds autonomously; anything requiring interpretation, deviation, or extension is queued for the PI with a recommendation. Unanswered queue items block only the hosts/episodes they concern.

**Always queued:** every exposure label; every host or episode exclusion; every protocol ambiguity; anomalies (V1–V4 failures, fingerprint spikes co-occurring with AI-topic discussion); any budget-cap approach (≥80% of cap).

**Never done by the agent:** computing the H1 correlation before completion; modifying Appendix A/B post-freeze; contacting any person; publishing or posting anything.

**Daily brief format:** scorecard (V1–V4 green/yellow/red) → coverage numbers → decision queue with recommendations → spend vs. cap. Nothing else.

**Changelog:** every post-freeze amendment is recorded here with date, reason, and PI ratification. An empty changelog section is maintained from freeze day.

---

## 9. Ethics and data handling

Public, published audio only; no private data; no contact with subjects; hosts analyzed in aggregate, with per-host results anonymized by default in any publication (host-identifiable results only with a specific PI decision at write-up). No IRB is available to an independent researcher; this section stands in its place and errs conservative. Audio deleted post-extraction; transcripts retained are of publicly published material.

## 10. Budget and schedule

- Transcription: ~2,000 audio-hours ≈ $200–500 (API) or ~$0 (local Whisper, slower). Hard cap set at freeze.
- Agent compute: capped daily; cap set at freeze.
- Schedule: Pilot (Phase 2) ~1 week → Panel & exposure (Phase 3) ~2–3 weeks → Collection (Phase 4) ~4–8 weeks → Analysis ~1–2 weeks → Write-up ~2–3 weeks.

## 11. Outputs

Frozen protocol (this document, publicly posted at freeze — OSF.io), open code, per-host per-period feature dataset, and a write-up (public essay and/or arXiv preprint; venue decision deferred to Phase 6).

---

## Appendix A — Frozen feature lists

_(Populated and frozen after pre-trend verification; includes final lexical fingerprint, discourse patterns with detection rules, placebo list.)_

## Appendix B — Exposure evidence search checklist

_(Fixed queries and source list per host; frozen before Phase 3.)_

## Changelog

_(Empty until freeze.)_
