# Pilot Final Report — LLM Adoption and Language Change in Podcast Hosts' Speech

**Study:** Signal-finding pilot for a within-person panel study of whether
documented personal LLM adoption is associated with drift toward
LLM-characteristic language in podcast hosts' spontaneous speech.
**PI:** Sunil Paul (independent researcher).
**Pilot window:** 2026-07-27 → 2026-09-10. **Protocol:** frozen v1.0
(2026-09-10). **External spend:** $0.41 of a $75 pilot cap ($400 study cap).

---

## 1. What this pilot was for

Not to answer the research question — to determine whether the measurement
is *possible and trustworthy*, and to hand a full study a validated
pipeline plus a realistic power picture. The deliverable is a go/no-go on
methodology, not a scientific finding about LLMs and speech. Read against
that bar, the pilot **succeeded for the lexical family and deferred the
relational family** (see §5).

## 2. Corpus

Three hosts taken end-to-end as the technical pilot: **Lex Fridman**
(interview, tech-leaning), **EconTalk / Russ Roberts** (interview,
economics), **MBMBaM** (comedy panel). 48 episodes sampled under a seeded
stratified design across 2019–2025.

- **MBMBaM was dropped** as NOT MEASURABLE: three-brother panel audio cannot
  be diarized with current tooling (DECISIONS.md 2026-08-03). This drove
  eligibility amendment A1 (two-voice formats only).
- **Two Lex episodes excluded** by the implausible-host-share QA gate
  (#134, #478), ratified on the blind V3 audit.
- **Analytic corpus: 30 QA-clean interview episodes, 157,243 host words.**

## 3. Validity gates — all four closed

| Gate | Result |
|---|---|
| **V1 — ASR bias** | **PASS.** 16 EconTalk pairs vs. published human transcripts, 177,898 aligned words: **0 fingerprint insertions, 0 deletions**; placebo symmetric at 1.12/1.12 per 100k. Whisper does not manufacture or erase fingerprint words. |
| **V2 — Reproducibility** | **PASS.** Counts reproduce to **0.39%** single-threaded (1.27% for the chunked config), against a ±2% gate. Root-caused and fixed a CTranslate2 nondeterminism-and-loss bug in the process (see §6). |
| **V3 — Diarization audit** | **PASS.** 20 blind 2-min clips labelled by the PI: QA-clean subset mean absolute error **3.2 pp**, all within ±15 pp, **no era-differential bias** (signed error −2.9 pp pre vs −1.0 pp post — same sign, small gap). The two QA-flagged clips failed unambiguously (+40, +100 pp), independently confirming the QA gate. |
| **V4 — Placebo/coverage** | Counts produced on the ratified denominator; placebo monitor clean. |

The V3 era check is the load-bearing one: era-differential attribution
error would have manufactured a pre/post effect from measurement alone.
It is absent.

## 4. Lexical family (H1-L) — pipeline validated; sole confirmatory family

The lexical instrument is trustworthy end to end. Baseline fingerprint rate
in the QA-clean corpus is **7.6 per 100k host words**.

**Power (WS7 simulation, pilot-measured inputs):** minimum detectable rate
ratio **~1.9 at n=24**, **~2.1 at n=18**. The design **passes the ≤2.0
gate at full size and fails at its own n=18 floor** → the host minimum is
raised to **21** (amendment D1). Expected fingerprint count is only ~1.9
per host-period, so the write-up must report absolute counts beside rate
ratios (C2); RR is unstable at these counts.

**Exploratory pre/post readout (PI-authorized, ballot P1b — NOT
confirmatory).** No exposure classification was applied to the two pilot
hosts, so this is a within-host descriptive readout, not an exposure ×
feature contrast (the §2 peeking rule remains unviolated). Reported once,
here, and stored in `results/exploratory_readout.json`:

| host | pre rate /100k | post rate /100k | within-host RR |
|---|---|---|---|
| Lex Fridman | 4.95 (2 in 40,393 w) | 12.27 (6 in 48,910 w) | 2.48 |
| Russ Roberts | 0.00 (0 in 35,580 w) | 6.18 (2 in 32,360 w) | undefined (0 baseline) |

*Erratum 2026-09-11:* the readout first computed on 2026-09-10 reported
Lex post as 8.63/100k over 162,264 words (RR 1.74). That version silently
included excluded episode #478 — its 113,354 pipeline-mislabelled "host"
words — because the exclusion file carried a hand-abbreviated filename
that name-based lookups did not match. The file is corrected, the readout
recomputed, and the totals now reconcile to the ratified 157,243 host
words. The lesson is recorded in §6 (item 9).

**These numbers carry no evidential weight.** n=2 hosts, no exposure
labels, era-as-proxy, counts in the low single digits (a single word moves
a rate — as the erratum above demonstrates in the other direction). They demonstrate the pipeline emits sensible numbers; they say
nothing about the hypothesis. Consequence of taking the readout: **both
hosts are exploratory-only in any future confirmatory panel** (one-way
door, accepted at ballot).

## 5. Relational family (H1-R) — DEFERRED

The relational instrument was **built and run but never validated.** Stage 1
screening (the recall-tuned pass that flags candidate disagreement turns)
completed on all 30 episodes under a pinned config
(`anthropic-0.122.0/claude-haiku-4-5/temp0/maxtok8192/stage1-v1`):
**1,877 host turns → 199 candidates (10.6%; EconTalk 15.6%, Lex 9.0%)**,
for $0.41.

The **G1/G2 human gold-labelling gate was not run** — the pilot ended
before the rater's ~7–9 hour pass. Under the pre-registered rule, an
unvalidated annotation instrument cannot carry a confirmatory claim, so
H1-R is **deferred to exploratory** (amendment E3). This is *deferred, not
disproven*: the pipeline exists and the flag rate is plausible; what is
missing is the human check that the model's judgments mean what we think.
The gold sheets (499 items, blinded) and the Haiku pin are retained as
Phase 4 assets. Reviving H1-R needs only the rater pass plus a κ≥0.70 gate.

## 6. What the pilot learned that a full study needs (the real value)

Each of these cost real time to discover and changes how Phase 4 must be
built (detail in WS8_FEASIBILITY.md §3):

1. **CTranslate2 multithreading is nondeterministic AND lossy under load**
   (7–96% content silently dropped). Pin `cpu_threads=1`; run N
   single-threaded workers.
2. **Determinism removes Whisper's loop-breaker** — needs a per-chunk
   timeout + no-context retry, flagged for sensitivity analysis (B2).
3. **Co-host/panel formats are not diarizable** with current tooling —
   exclude at sampling (A1).
4. **An implausible-host-share QA gate is mandatory** — embedding
   similarity alone missed a 47%-of-denominator contaminant (B3).
5. **Work units must be « the infrastructure restart interval** (~25
   restarts in 6 days here); chunk + checkpoint atomically.
6. **Persist expensive compute at the boundary it's produced** (a 2h
   diarization run was once lost to a downstream parse bug).
7. **Completion checks must count outputs, not process exits.**
8. **Using an LLM to detect LLM-like style is the deepest open risk** for
   H1-R; the full study should budget human annotation throughout.
9. **Exclusion lists must be generated, never hand-typed, and every
   consumer must assert its totals against the ratified denominator.** A
   hand-abbreviated filename in the exclusion record let an excluded
   episode leak back into one analysis undetected until a later rebuild
   tripped over it. The 157,243-word total was the tripwire; the fix is to
   make that assertion mandatory in every script that applies exclusions.

## 7. Recommendation for Phase 4

- **Lexical family: GO to design.** The instrument is validated; the
  measurement is trustworthy; the power picture is known (≥21 hosts,
  prefer more episodes/host over more hosts). This pilot cleared the
  methodological path for a full lexical study.
- **Relational family: CONDITIONAL.** Promising and cheap to screen, but
  its instrument is unvalidated. Gate any confirmatory use on the G1/G2
  human validation the pilot deferred; assume human annotation throughout
  at scale.
- **Cost is not the constraint.** Full-study external spend projects to
  ~$95–145 (one GPU + a Haiku-class annotator). The binding constraints
  are PI/rater time and wall-clock, not money.
- **No signal was read.** Per the peeking rule, the pilot computed no
  exposure × feature contrast at any point. Whether the hypothesis is true
  remains open — as intended.

## 8. Data governance at close (§9)

- Pilot audio (3.9 GB) **deleted** — the session container was reclaimed
  during the pause, completing §9 deletion. Transcripts survive only in the
  PI's private backup tarball.
- Committed to the repo: pipeline code, de-identified per-episode counts
  (no verbatim context), the exposure-blind results, this report. No audio,
  no transcripts, no exposure dossiers.
- **Outstanding:** the annotation API key transited the chat and its work
  is done — **revoke at the console.**

## Addendum (2026-09-11): full corpus rebuild — reproducibility and AI-mention density

The private transcript backup was lost, so the 30-episode analytic corpus
was **rebuilt end to end from re-downloaded audio** under the identical
pinned config, in a fresh environment (`results/rebuild_environment.json`).
This turned into the corpus-level reproducibility test the pilot's V2 probe
could not provide. Per-episode pairs are in `results/reproducibility_rebuild.json`.

**Inputs were the same.** 28/30 re-downloaded files match the RSS-declared
byte length exactly, so the drift below is pipeline-side, not audio-side.

**What reproduced tightly:** speaker attribution — host share within
±0.021 on every episode (host similarity within ~0.003); the QA gate flagged
0/30 in both runs; Durov's host-turn count was 135 in both. Corpus totals:
host words **157,243 → 159,303 (+1.3%)**; placebo rate 43.9 → 45.2 /100k.

**What did not:** per-episode transcription. Total transcribed words drift
by a **median 1.6%, max 6.3%**; host-attributed words by a **median 2.2%,
max 9.0%**, with 15/30 episodes outside the ±2% V2 gate. The pilot's V2
probe (0.39%) re-processed identical decoded audio *within one
environment*; this rebuild crosses environments — a fresh CTranslate2
(4.8.2), a freshly downloaded checkpoint (revision `08e178d…`), new torch.
The pin string `faster-whisper-1.2.1/medium/int8/threads1/temp0/beam5/
chunk1500` did not capture whatever changed. **Finding 10: the config pin
must include the CTranslate2 version and the model-checkpoint hash, and
audio checksums must be recorded at download** so that a reproducibility
failure can be attributed to inputs or to the pipeline. Staged as
post-freeze amendment F1 (not applied to the frozen text).

**Sparsity in action:** the clean fingerprint count moved **10 → 12** on
two single-word differences (Wolfram 1→2, Gibson 1→2); the exploratory
within-host readout for Lex moves from RR 2.48 to **3.3** on the rebuild
(pre 4.9 → post 16.2 /100k; EconTalk 0 → 6.0). Two words, a 30% swing in
the rate ratio — exactly the C2 warning, now demonstrated.

**AI-mention density (`results/ws9_ai_mentions.json`, exploratory).** The
PI-proposed exposure proxy — how much a host *talks about* AI, per 1,000
host words — was computed on the rebuilt turns. Strict tier (named LLM
products/terms): EconTalk pre **0.00 → post 0.57**; Lex pre **0.10 →
post 1.72**. Broad tier (adds generic "AI"): EconTalk 0.00 → 1.27; Lex
1.57 → 3.62. Guests move the same way (Lex guests 0.02 → 1.00). The
measure works mechanically and separates eras sharply — but that
separation is largely trivial: the strict terms barely existed before
late 2022, so **the strict tier cannot run the pre-2022 personality test;
only the broad tier can** (Lex's pre-period generic-AI rate is non-zero).
The distribution is heavily topic-driven: one ChatGPT-titled episode
(Wolfram) carries 57 of the corpus's mentions at 7.8/1k; 13/30 episodes
have any host mention at all. Consequences for the full study: (a) the
segment-separation design — measure outcomes away from AI-talk — is
mandatory, not optional; (b) an episode-level AI-topic screen is needed in
addition to the show-level E1 rule; (c) as a dose measure it is heavy-tailed
and should enter as log-density or presence, not raw rate; (d) it is a
screener and covariate, not a confirmatory exposure variable.

## 9. Artifact index

| Artifact | File |
|---|---|
| Frozen protocol | `research/PROTOCOL.md` (v1.0) |
| Exit-review ballot + votes | `research/pilot/EXIT_REVIEW_BALLOT.md` |
| Decision log | `research/pilot/DECISIONS.md` |
| Amendments (ratified) | `research/pilot/PROTOCOL_AMENDMENTS.md` |
| Feasibility / cost memo | `research/pilot/WS8_FEASIBILITY.md` |
| Power simulation | `research/pilot/ws7_power.py`, `ws7_power_results.json` |
| V1 report | `research/pilot/WS4_V1_report.md` |
| V3 audit report | `research/pilot/WS3_V3_report.md` |
| Lexical counts | `research/pilot/results/ws5_counts.json` |
| Exclusions (ratified) | `research/pilot/results/exclusions_ratified.json` |
| Exploratory readout | `research/pilot/results/exploratory_readout.json` |
| Stage-1 relational labels | `research/pilot/results/ws6_stage1_labels.json` |
| Literature review | `research/pilot/LITERATURE.md` |
| Rater rubric (Phase 4 asset) | `research/pilot/RATER_RUBRIC.md` |
