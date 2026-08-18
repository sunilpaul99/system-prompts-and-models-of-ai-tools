# Daily Brief — Pilot Study

_Maintained per PROTOCOL §10. Latest cycle at top._

## 2026-08-18, cycle 83 — V3 AUDIT RETURNED AND SCORED — GATE PASSES

PI returned all 20 blind labels (Numbers file; converted to
`results/v3_audit_labels_PI.csv`). Scored with `ws3_score_audit.py`.
Full write-up in `WS3_V3_report.md`.

**Result — the audit splits exactly on the QA flag:**
- QA-clean clips (n=18): MAE **3.2 pp**, all within ±15 pp, max error 13.3 pp.
- QA-flagged clips (n=2): pipeline claims ~100% host where the PI heard 60%
  (A01, Lex #134) and 0% (A02, Lex #478). Misses of +40 and +100 pp.
- All 20 pooled: 18/20 = **exactly 90%**, i.e. at the gate, not above it.

**No tolerance was pre-specified**, so the report gives the whole tolerance
curve rather than a chosen threshold. The curve is flat above ±11.6 pp — the
verdict turns entirely on whether the 2 flagged episodes are in the
denominator, not on where the line is drawn.

**Era check (the one that could confound the design):** signed error is
negative in all four strata — the pipeline slightly under-credits the host
throughout — with 2019-21 at -2.93 pp and 2023-25 at -1.03 pp. Small,
same-signed, no differential bias by era. This is the result that matters
most, since era-differential measurement error would manufacture a pre/post
effect out of nothing.

PI reported no third voices and no anomalies across all 20 clips.

**V3: PASS on the QA-clean corpus.** The implausible-host-share rule
(amendment B3) is independently confirmed — it caught both failures
automatically before any human listened.

**Decision queue — one item now ripe (§10, not self-ratified):**
Exclude Lex #134 and #478 from analytic totals? Evidence now supports it;
recommendation is to exclude per staged amendment C1. Current QA-clean
totals already exclude them, so ratifying costs nothing; rejecting requires
re-running WS5 with them restored.

**Gates**: V1 PASS · V2 PASS · **V3 PASS** · V4 counts produced.
**Coverage**: 48/48 transcribed and diarized; 30 QA-clean episodes /
157,243 host words. **Spend**: $0 of $75.

**Still PI-blocked**: the exclusion ratification above, rater onboarding for
G1/G2, annotation-model pin.

**Note**: audio (3.9 GB, 48 mp3s) is still held in the scratchpad pending
any audit re-cuts. With V3 scored and no re-cuts requested, §9 deletion is
now appropriate on the PI's word.

## 2026-08-08, cycle 82 — DURABILITY PASS BEFORE PAUSING THE LOOP

PI proposed pausing the scheduled cadence until the V3 audit is done. That
is correct on the work itself — 20+ consecutive cycles have been verified
no-ops — but it exposed a risk the cadence had been masking: **the pilot's
derived artifacts lived only in the ephemeral scratchpad.** A container
reclaim during a multi-day pause would have destroyed `answer_key.json`
(making the audit unscorable), the diarized corpus, and the WS5 counts —
costing days of CPU to rebuild, or making the audit non-reproducible.

**Committed (metadata only, §9-compatible):**
- `audit/answer_key.json` — the 20 audit windows' pipeline labels. Needed to
  score the audit; contains speaker + timestamps, no text.
- `results/ws3_qa_flags.json`, `results/ws4_v1_results.json`,
  `results/ws5_counts.json`, `results/README.md`.

**Deliberately NOT committed:** audio (§9), transcripts (copyright /
transient-copy posture, TOS_NOTES.md), and the 145 verbatim ~150-char hit
excerpts, which were **stripped** from the committed counts. §9 permits
counts to leave the pipeline, not quotations. Hit timestamps are retained,
so any hit stays relocatable in the private transcript.

**Sent to PI:** `pilot_private_backup.tar.gz` (9.8 MB) — diarized
transcripts, turns, host centroids, enrollment spans, the full counts file
with contexts, and a copy of the answer key named to discourage opening it
before labelling.

**Cadence:** scheduled cycles paused at PI request. The loop resumes on PI
input — audit labels, or any new instruction.

**Gates**: V1 PASS · V2 PASS · V3 audit-ready, packet with PI · V4 counts
produced. **Coverage**: 48/48 transcribed and diarized; 30 QA-clean episodes
/ 157,243 host words. **Spend**: $0 of $75.

## 2026-08-05, cycle 81 — V3 AUDIT PACKET DELIVERED TO PI

First substantive change since cycle 80. The PI stated the audit begins
tomorrow (2026-08-06), so the audit materials were packaged and handed off.

**Done this cycle:**
- Re-encoded the 20 audit clips from wav to 64 kbps mono mp3 (77 MB → 16 MB)
  and verified all 20 decode to exactly 120.0 s.
- Wrote `V3_AUDIT_HOWTO.md` — procedure, the blind rule, per-column
  definitions, and what each gate outcome means (including that a FAIL is a
  reportable pilot finding, not a rater error).
- Added `audit_labels_TEMPLATE.csv` — one row per clip, host named per row
  so the PI never has to infer which voice is the host.
- Shipped `v3_audit_packet.zip` (clips + CSV + HOWTO + sheet) directly to
  the PI. **`answer_key.json` was deliberately excluded from the packet** so
  the blind constraint cannot be violated by accident; it stays in the
  session scratchpad.
- Flagged to the PI that the container is ephemeral: the 3.9 GB source audio
  will not survive a reclaim, so the delivered zip is the durable copy.

**Still PI-blocked** (unchanged): V3 labels, the exclusion decision (which
the audit settles empirically), rater onboarding, annotation-model pin.

**Gates**: V1 PASS · V2 PASS · V3 audit-ready, packet with PI · V4 counts
produced. **Coverage**: 48/48 transcribed and diarized; 30 QA-clean episodes
/ 157,243 host words in analytic totals. **Spend**: $0 of $75.

**On return of the filled CSV**, the downstream chain is: score `host_pct`
against `audit/answer_key.json` → V3 report → apply or reject the two
exclusions per the PI's blind labels, recorded in DECISIONS.md.

## 2026-08-03, cycle 80 (~00:12Z) — HOLDING PATTERN

No agent-actionable work remains. No background jobs running, working tree
clean, everything committed and pushed. Per §10 and the loop's own rule, no
busywork changes made this cycle.

**Everything now waits on PI time, not agent time:**
1. V3 audit — ~40 min, ready (V3_AUDIT_SHEET.md, 20 clips). Also settles
   item 2 empirically.
2. Exclusion decision for the 2 implausible-share episodes.
3. Rater onboarding for G1/G2 (rubric + sheet drafted).
4. Annotation-model pin (cost measured: $93 Haiku / $280 Sonnet full study).

**Pilot state at rest:**
- Corpus: 48/48 transcribed under one pinned deterministic config;
  48/48 diarized; 2 QA-flagged.
- Gates: V1 PASS (0 fingerprint ins/del in 178k aligned words), V2 PASS
  (0.39% count reproducibility; chunked config 1.27%), V3 audit-ready,
  V4 counts produced.
- Deliverables complete: WS8 feasibility memo, WS7 power simulation
  (min detectable RR ~1.9 at n=24), protocol amendment list (11 items),
  literature review, decision log.
- Spend: $0 actual of $75 pilot cap.

**Note on future cycles:** to avoid turning this log into noise, subsequent
no-op cycles will NOT add entries. The next brief entry will appear when
something actually changes — PI input, a new instruction, or a job result.

## 2026-08-03, cycle 79 (~22:12Z)

**Protocol amendment list DRAFTED** (PROTOCOL_AMENDMENTS.md) — the
PILOT_PLAN week-3 deliverable. Nothing is applied; each item is
pilot-evidenced and awaits PI accept/modify/reject at the exit review.
11 amendments across eligibility, pipeline config, analysis, power, and
scope — plus an explicit "not amended" section recording that the blinding
and peeking rules, the estimand framing, and the two-family structure all
held and need no change.

The two that most affect the full study's validity:
- **B1**: pin the FULL transcription config, not just the model version —
  thread count alone changes output 7-96% under load. A model version is
  not sufficient to reproduce a corpus, which is the sort of thing a
  replication would discover the hard way.
- **D1**: the design passes §8.2 at n=24 (min detectable RR ~1.9) but
  FAILS at its own n=18 floor (~2.1). The protocol should either raise
  the floor to ~21 hosts or declare that dropping below it converts the
  study to descriptive.

**§5.5 meta-mention rule exercised**: 2 of 12 QA-clean fingerprint hits
were flagged near AI references (one "realm" in a computational-language
discussion, one "intricacies" beside a markets/AI passage) — the rule
fires, at a rate the sensitivity analyses (0/20/50-word windows) can
absorb. Fingerprint words actually occurring in host speech: realm (6),
intricate (4), surpass (2). Nothing else in the frozen candidate list
appeared at all in 157k host words, which is itself an Appendix A finding.

**All agent-doable pilot work is now complete.** Remaining items are PI
time, not agent time: V3 audit (~40 min, ready), exclusion decision
(the audit answers it), rater onboarding, annotation-model pin. Cycles
from here will be no-ops unless something arrives — per §10, no busywork.

**Scorecard**: V1 PASS, V2 PASS, V3 audit-ready, V4 counts produced.
**Spend**: $0 actual of $75 pilot cap.

## 2026-08-03, cycle 78 (~20:12Z)

**WS8 FEASIBILITY MEMO DRAFTED** (WS8_FEASIBILITY.md) — the PROTOCOL §8.3
handoff artifact, and the last major deliverable that needed no PI input.
Every figure is pilot-measured rather than taken from documentation.

Headline: the full study is feasible inside the $400 cap but **not on
CPU-only infrastructure**. Transcription and diarization both run ~1x
realtime per worker (~3,600 worker-hours for 1,800 episodes); one consumer
GPU collapses that to days. Recommended configuration — GPU + Haiku-class
annotator — comes to **~$95-145**, leaving ~75% of the cap unspent. The
binding constraint on this study is PI/rater time and wall-clock, not money.

The memo's most valuable section is §3, the eight non-obvious findings,
each of which cost days here and would cost a future team the same:
CTranslate2 multithreading is nondeterministic AND lossy under load;
determinism removes Whisper's loop-breaker; work units must be much
shorter than the infrastructure restart interval; expensive compute must
be persisted where it is produced; completion checks must count outputs
not process exits; memory caps parallelism, not CPU; co-host formats are
undiarizable; publisher sites rate-limit far below CDN thresholds.

Also recorded: measured decision-queue volume (~1 PI decision per 8-10
agent cycles, clustering at methodological forks) so Phase 4 can staff
for it — 2-4 decisions/week plus the scheduled labelling blocks.

Memo is explicitly DRAFT: three open items (V3 audit result, G1/G2 gates,
Stage-1 flag rate) are listed as pending rather than guessed at.

**Queue (PI, unchanged)**: V3 audit (~40 min, ready); exclusion decision
(the audit answers it); rater onboarding; annotation-model pin.
**Scorecard**: V1 PASS, V2 PASS, V3 audit-ready, V4 counts produced.
**Spend**: $0 actual.

## 2026-08-03, cycle 77 (~18:12Z)

**Annotation-model cost estimate MEASURED** (the input the PI's model-pin
decision was waiting on). Token volumes from the actual pilot corpus, not
assumed:

- pilot interview corpus: 32 episodes, 3,733 turns, 3.71M chars
- Stage-1 screening (30-turn windows, 10-turn overlap -> ~1.5x): **1.39M
  input tokens**, i.e. ~43k per episode
- Stage-2 labelling (assume 15% of windows flagged, +context): 0.27M
- pilot total ~1.66M input tokens; full study (~1,800 episodes, 56x
  scale-up) ~93M input tokens. Output is negligible (JSON labels).

| model class | pilot | full study | vs $400 cap |
|---|---|---|---|
| Haiku-class (~$1/Mtok) | $1.66 | **$93** | fits comfortably |
| Sonnet-class (~$3/Mtok) | $4.98 | **$280** | fits, but 70% of cap |
| Opus-class (~$15/Mtok) | $24.92 | $1,402 | **exceeds cap 3.5x** |

**Recommendation for the pin (PI ratifies):** run the G1/G2 validation on
a Sonnet-class model. Rationale: the pilot spend either way is trivial
($5 vs $2), so the pilot should be run on the model most likely to PASS
the gates — a failed G1/G2 costs a workstream, not $3. Then, if it passes,
re-validate Haiku-class on the same gold sample before committing the full
study to it: if the cheap model also clears κ≥0.70, the full study runs at
$93 and leaves the cap almost intact; if it doesn't, $280 still fits and
the design memo can say exactly what the cheaper option cost in accuracy.
That sequencing buys a real number for the handoff memo instead of a guess.

Caveat stated: the 15% flag-rate for Stage 2 is an assumption, not a
measurement — the pilot's own Stage-1 run will replace it, and the full
figure moves roughly ±10% with it.

**Queue (PI)**: V3 audit (~40 min, ready); exclusion decision (the audit
answers it); rater onboarding; annotation-model pin (recommendation
above). **Spend**: $0 actual.

## 2026-08-03, cycle 76 (~16:12Z)

**WS7 POWER SIMULATION RUN — §8.2 gate PASSES for the lexical family,
narrowly.** (ws7_power.py, committed and runnable; results JSON alongside.)

Inputs are pilot-MEASURED, not assumed: baseline 7.6 fingerprint
occurrences per 100k host words, ~25k host words per host-period (5
episodes x ~5k), 7 pre-periods / 6 post.

**The number that matters: expected count is 1.90 per host-period.** The
lexical outcome is extremely sparse — about 13 pre-period and 11
post-period occurrences per host in total. Everything below follows from
that.

| | RR=1.5 | RR=2.0 | RR=3.0 |
|---|---|---|---|
| n=24, host SD 0.3 | 0.51 | **0.93** | 1.00 |
| n=24, host SD 0.6 | 0.49 | **0.92** | 1.00 |
| n=18, host SD 0.3 | 0.42 | 0.85 | 1.00 |
| n=18, host SD 0.6 | 0.36 | 0.77 | 0.99 |

**Minimum detectable RR (80% power) ~= 1.9 at n=24, ~2.1 at n=18.**
§8.2 requires <=2.0, so the design passes at n=24 and FAILS at the n=18
floor — worth stating plainly, since attrition to 18 hosts is a real risk
and would put the study below its own gate.

**Honest limitation, stated rather than buried:** the pilot has TWO
interview hosts, so between-host variance cannot be estimated from it.
Rather than quote a point estimate from n=2, the simulation sweeps host
SD (0.3 and 0.6) and reports power across it. Reassuringly, power is
insensitive to that choice here (0.93 vs 0.92 at RR=2.0) because sparsity,
not host heterogeneity, dominates.

**Design implications for the memo:** the study can detect a doubling of
fingerprint use but not a 50% increase. Since Yakura et al. report
population-level shifts well below 2x, an individual-level pilot at this
size is powered only for a LARGE personal effect — exactly the "worth a
real study" screening question, and precisely why §8.1 has a GO(weak)
row. Levers if more power is wanted: more episodes per period (words is
the binding constraint, and it is linear), a broader feature list, or
coarser periods.

**Relational family (H1-R) power: still blocked** — needs disagreement-turn
density from the Stage-1 annotator, which needs the model pin + cost
estimate (PI item).

**Queue (PI)**: V3 audit (~40 min, ready); exclusion decision (answered by
the audit); rater onboarding; annotation-model pin. **Spend**: $0.

## 2026-08-03, cycle 75 (~14:12Z)

**V3 AUDIT EXPORT READY — PI action available now** (V3_AUDIT_SHEET.md).
20 two-minute clips, stratified host x era, interview formats only:
14 Lex / 6 EconTalk. Lex is deliberately overweighted because EconTalk
attribution is already externally validated against published human
transcripts (~2pp), while Lex publishes none — the audit is his only
validation route.

Design choices worth noting:
- **Blind labelling**: the sheet carries no pipeline answers; those sit in
  audit/answer_key.json and are scored afterward.
- **The two QA-flagged episodes are included UNMARKED.** The PI labels
  them alongside the rest without knowing which they are, so the pending
  exclusion decision is settled by ears rather than by the same heuristic
  that flagged them.
- Windows skip the first 120s (intros and sponsor reads are host-solo and
  would flatter the pipeline).
- Seeded and reproducible; clips live in scratchpad only (audio is not
  committed, per §9). Say the word and I will send them directly.

**Effort**: ~40 min (20 clips x 2 min), vs the ~1h budgeted.

**Queue (2, both PI):**
1. Exclude the 2 implausible-share episodes? — the audit above answers it
   empirically; no need to decide before labelling.
2. G1/G2 rater onboarding, whenever your rater is ready (rubric and sheet
   already drafted).

**Scorecard**: V1 PASS, V2 PASS, V3 audit-ready, V4 counts produced
(QA-clean: 30 eps, 157k host words, fingerprint 7.6/100k). **Spend**: $0.

## 2026-08-03, cycle 74 (event-driven — DIARIZED CORPUS COMPLETE + first counts)

**48/48 diarized.** WS5 recount and WS6 turn stats ran; a QA problem
surfaced immediately and materially changes the numbers.

**NEW V3 FINDING — implausible-share failures (2/32 interview episodes).**
Weinstein #134 (share 0.999, sim 0.50) and Horton #478 (share 0.996,
sim 0.30) diarized to ~100% HOST. The existing HOST_SIM_MIN=0.30 gate let
them through because it only asks "is the best cluster close enough to the
host?" and never "is the resulting SPLIT plausible?". Horton passed at
sim=0.30 — exactly the threshold.
**These 2 episodes hold 47.4% of all host words**, because a collapsed
diarization sweeps GUEST speech into the host bucket. Any count computed
over them is contaminated at the denominator.
New QA rule implemented (ws3_qa_flags.py): for known two-voice formats a
host share outside [0.15, 0.75] is a failure regardless of similarity.
Flagged, reported, never silently dropped.

**WS5 counts, both ways (descriptive only — pilot hosts carry NO exposure
labels, so no exposure x feature contrast is computed, per §2):**

| | eps | host words | fingerprint | placebo |
|---|---|---|---|---|
| as computed (contaminated) | 32 | 298,875 | 23 (7.7/100k) | 122 (40.8/100k) |
| **QA-clean** | **30** | **157,243** | **12 (7.6/100k)** | **72 (45.8/100k)** |

QA-clean coverage: econtalk era1 0.0/100k (0 occurrences in 35.6k words),
econtalk era2 6.2, lex era1 5.0, lex era2 16.4. Reported as coverage, not
as a result: n=2 hosts, no exposure labels, and era differences here are
confounded with everything (guest mix, show format changes, episode
length). The pilot's job is variance estimates, not effects.

**WS6 disagreement-density input (the H1-R viability number):** median 36
host turns/episode, 26.3/hour; at 5 episodes per host-half-year that is
**~182 host turns per host-period**. If disagreement episodes run even
5-10% of host turns, that clears the §7 minimum of 5 disagreement turns
per period comfortably — H1-R looks estimable at pilot sampling, pending
G1/G2 validation of the detector itself.

**DECISION QUEUE (PI): 1 item.** Exclude the 2 implausible-share episodes
from analysis (recommended), or attempt re-diarization first? Agent does
not self-ratify exclusions. Note both are Lex episodes and one (Weinstein
#134) is an enrollment reference — its failure is on the full episode, not
the enrollment span, but that coincidence is worth your eye.

**Scorecard**: V1 PASS, V2 PASS, V3 partial (interview validated within
~2pp on EconTalk; 6.2% failure rate now quantified; PI audit pending),
V4 counts produced. **Spend**: $0.

## 2026-08-03, cycle 73 (~10:12Z)

**Restart #25** at 46/48 — two episodes short. Relaunched; ~1h to a
complete diarized corpus.

**On deck the moment 48/48 lands** (all protocol-derivable, no PI input):
1. WS5 recount on the deterministic corpus, MBMBaM excluded per the
   ratified decision (exclusion printed, not silent).
2. WS6 turn reconstruction + disagreement-density estimate on interview
   formats — this produces the number that decides H1-R's viability
   (disagreement turns per host-period at 5-episode sampling; PROTOCOL
   §7 coarsens to host-year if >30% of periods fall under 5 turns).
3. Stratified V3 audit export, interview-only and Lex-weighted, for the
   PI's ~1h.

**Scorecard**: V1 PASS, V2 PASS, V3 partial (pending audit), V4 pending
recount. **Queue**: empty. **Spend**: $0 of $75.

## 2026-08-03, cycle 72 (~08:12Z)

**Interview diarization at 41/48**, running through a ~10h window (best
since the corpus phase). Remaining: 3 EconTalk, 2 Lex, 2 MBMBaM.

Considered skipping the 2 remaining MBMBaM episodes since they will not be
analysed under fallback (c). Decided AGAINST: ~1h of otherwise-idle CPU
buys a complete, symmetric ECAPA diarization set across all 48 episodes,
which makes the retained methods evidence cleaner than a partial set
(the failure is the finding; a full set documents it consistently).

**Next, once 48/48 lands** — all protocol-derivable, no PI input needed:
WS5 recount with the MBMBaM exclusion flag, WS6 turn/disagreement-density
stats on interview formats, then the stratified V3 audit export (interview
only, Lex-weighted) for the PI's ~1h.

**Scorecard**: V1 PASS, V2 PASS, V3 partial (interview within ~2pp of
human transcripts; multi-speaker NOT MEASURABLE, ratified), V4 pending.
**Queue**: empty. **Spend**: $0.

## 2026-08-03, cycle 71b (event-driven — PI ratification)

**Fallback (c) RATIFIED by PI.** Multi-speaker/co-host formats declared
NOT MEASURABLE with available tooling. Full record in DECISIONS.md.
Applied this cycle:
- ws5_count.py gains an exclusion flag; MBMBaM drops out of analytic
  totals while remaining computable and reported separately (the
  exclusion is visible in output, never silent).
- V3 audit sample scope narrowed to interview formats, weighted toward
  Lex (his episodes have no published verbatim transcripts, so the audit
  is their only validation route).
- E-rule amendment (eligibility = interview/two-voice formats) STAGED for
  the freeze amendment pass — protocol text is not edited mid-flight per
  §10; DECISIONS.md is the authority until freeze.
- MBMBaM transcripts and diarization outputs retained in the repo as
  evidence for the methods finding.

**Decision queue: EMPTY.** Remaining PI time is scheduled work, not
decisions: V3 audit (~1h, once the run completes), WS4 spot-verification
(~1h, now confirmatory), G1/G2 gold labeling (6-8h, rater-dependent).

**Coverage**: interview diarization running toward 48/48; WS5 recount,
WS6 turn stats, and the audit export fire behind it.

## 2026-08-03, cycle 71 (~04:12Z)

**Restart #24**; interview-format diarization relaunched (idempotent,
resumes at 20/48). No other action — the multi-speaker question is closed
pending PI ratification, and WS5/WS6/V3-audit all queue behind this run
reaching 48/48 (~1 day at current pace, restart-dependent).

**Queue**: 1 item — ratify fallback (c), the interview-formats-only E-rule
amendment (evidence complete as of cycle 69). **Spend**: $0.

## 2026-08-03, cycle 70 (~02:12Z)

**Interview-format diarization progressing cleanly**: 20/48 (up from 15),
running unattended through a ~6h window. First Lex episodes now landing
with plausible host shares (Lenat 0.299, Hauer 0.435 — interview range,
k=2-3). Note: Lex has no published verbatim transcripts, so his episodes
get plausibility checks rather than the ground-truth comparison EconTalk
allowed; the PI V3 audit is where Lex attribution actually gets verified,
and the audit sample should therefore weight Lex episodes more heavily
than EconTalk's (which are already externally validated within ~2pp).

No other action: the multi-speaker question is closed pending PI
ratification, and everything downstream (WS5 recount, WS6 turn stats, V3
audit export) waits on this run finishing 48/48.

**Queue**: 1 item — ratify fallback (c). **Spend**: $0.

## 2026-08-03, cycle 69 (~00:12Z)

**CONTROL RESULT IN — constraint is affirmatively harmful; the
multi-speaker question is now closed on the evidence.**

| episode | unconstrained | k=3 |
|---|---|---|
| 455 (the one that WORKED) | 0.394 / 0.329 / 0.233 | **0.979 / 0.014 / 0.007** |
| 472 (failure case) | 0.621 / 0.305 / 0.029 | 0.975 / 0.022 / 0.002 |

Forcing three speakers destroyed the single episode that had split
correctly, collapsing it to one 98% cluster. Justin-similarity also fell
on that episode (0.85 -> 0.72), consistent with the surviving cluster
being a BLEND of brothers rather than one voice — an independent
confirmation that the merge is real and not a labelling artifact.

**Final evidence set for the exit review:** unconstrained 1/3 studio
episodes correct, unpredictably; constraining makes both the failures and
the success collapse; identification is sound throughout, so the limit is
segmentation of closely-matched sibling voices. The cycle-68
recommendation (fallback (c)) stands unchanged and now rests on a
complete paired experiment rather than a partial one. pyannote runs
stopped — the remaining episode would add cost, not information.

**Interview-format work RESUMED** (the furthest unblocked workstream, and
unaffected by the pending decision): ECAPA diarization of the 33
remaining EconTalk/Lex episodes relaunched, 15/48 banked.

**Scorecard**: V1 PASS, V2 PASS (both configs), V3 partial (interview
formats within ~2pp of human transcripts; multi-speaker NOT MEASURABLE
pending PI ratification), V4 awaits recount.

**Queue**: 1 item — ratify fallback (c) (E-rule amendment, cycle 68).
Nothing else blocks on it. **Spend**: $0.

## 2026-08-02, cycle 68 (~22:12Z)

**Restart #23** killed the constrained run again before the control
finished; k=3 still 1/3. Relaunched (control first). The MBMBaM test has
now lost four runs to restarts — each attempt needs ~1h uninterrupted
against a ~2h cadence, so completion is luck-dependent.

**RECOMMENDATION QUEUED FOR PI — the evidence no longer requires the
control episode.** Reasoning: even the best case for the constraint does
not rescue the method.
- Unconstrained pyannote: **1 of 3 studio episodes** correctly split
  (0.394/0.329/0.233); the other two collapse to ~0.62/0.31.
- Constrained k=3 on a failing episode: **worse** (0.621 -> 0.975).
- Identification is not the problem (sim 0.83-0.89 throughout);
  segmentation is, and the brothers are closer to each other in embedding
  space than to any non-speech in the audio.
- Decisive point: **there is no way to tell, per episode and without
  ground truth, which outcome you got.** A host-share that lands at 0.39
  or 0.62 unpredictably feeds noise straight into every rate denominator
  in the relational battery. "Sometimes correct, unknowable which" is
  unusable as an outcome measure regardless of how the control resolves.

**Recommended (PI ratifies — this is an E-rule amendment, not agent's to
self-approve):** adopt fallback (c). P3/multi-speaker reported as NOT
MEASURABLE with available tooling; full-study panel restricted to
interview/two-voice formats at freeze; MBMBaM's 16 episodes retained as a
documented methods finding rather than analysed. Episode 455 is preserved
as evidence the ceiling is engineering, not physics — a diarizer that
handles sibling voices (or per-speaker enrollment of ALL co-hosts, an
Appendix C upgrade) would reopen the format.
The control run continues opportunistically for completeness; its result
will be reported either way but does not change the recommendation.

**Queue**: 1 item (fallback (c) ratification). **Spend**: $0.

## 2026-08-02, cycle 67 (~20:12Z)

**Restart #22** killed the constrained run at 1/3. Relaunched with the
CONTROL EPISODE FIRST (455, the one that split correctly unconstrained) —
it is the decisive test, so with ~1h/episode against a 2-6h restart
cadence it should not be queued behind a second failure case. Same
ordering lesson as cycle 63, applied to the experiment rather than the
sweep.

**Standing evidence** (unchanged this cycle):
- unconstrained studio base rate 1/3 correct (455 clean; 472, 478 collapse)
- constrained k=3 on 472: 0.621 -> 0.975 (much worse)
- identification solid throughout (sim 0.83-0.89); segmentation is the
  sole failure mode, and the brothers sit closer to each other in
  embedding space than to any non-speech in the audio

**Pending**: k=3 on the control. If it wrecks 455, the constraint is
affirmatively harmful, the approach is exhausted, and fallback (c)
(interview-formats-only panel) becomes the pilot's recommendation for the
exit review.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 66 (~18:12Z)

**CONSTRAINED (num_speakers=3) MAKES IT WORSE — first paired result.**
Episode 472: unconstrained 0.621/0.305/... -> constrained
**0.975/0.022/0.002**. Forcing three speakers did not split the brothers;
it collapsed them into ONE cluster plus two noise slivers.

**What this reveals (the informative part):** the 9-14 clusters found
unconstrained were never "3 brothers + noise". The brothers were being
split ACROSS those clusters, and music/noise/room-tone are further apart
in embedding space than the brothers are from each other. So the
segmentation isn't over-eager — the sibling voices are genuinely closer to
each other than to anything else in the audio. A count constraint cannot
fix that; it just tells the clusterer to merge the nearest things, which
are the brothers.

Two episodes still running (478 = second failure, 455 = the CONTROL that
worked unconstrained at 0.394/0.329/0.233). The control is now the
decisive test: if k=3 also wrecks 455, the constraint is affirmatively
harmful and the approach is exhausted.

**Direction of travel:** toward fallback (c) — multi-speaker formats NOT
reliably measurable with available tooling, full-study panel restricted to
interview formats. Holding that recommendation until the control lands.
455 remains proof the ceiling is not absolute (pyannote CAN split them,
just not dependably), which makes this a bounded engineering finding
rather than a dead end — the right shape for the handoff memo.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 65b (event-driven — self-inflicted job kill)

Both background jobs died instantly with exit 144, no output, no restart.
**Cause: `pkill -f "ws3_diarize_pyannote.py"` matched its OWN shell
wrapper** (the wrapper's command line contains the pattern string), so it
killed itself and the job it had just spawned in the same command. No data
lost (turn caches intact; the constrained run had produced nothing yet),
~15 min of wall-clock lost.

Practice rule adopted (and a WS8 note, since Phase 4 will orchestrate many
jobs): never `pkill -f` on a pattern that appears in the killing command
itself — resolve PIDs first (`pgrep -f ... | grep -v $$`) or kill by
recorded PID. Constrained test relaunched cleanly with nothing else
running, so no kill was needed at all.

## 2026-08-02, cycle 65 (~16:12Z)

**Studio base rate now 1 of 3.** Episode 478 also collapsed (0.646/0.315),
matching 472 (0.621/0.305); 455 remains the lone clean three-way split
(0.394/0.329/0.233). Identification stays strong throughout (sim
0.85-0.89) — segmentation is the sole failure mode, and 9-14 detected
speakers against a cast of 3 confirms it is OVER-segmentation.

**Paired experiment launched** (ws3_pyannote_constrained.py): the two
failing episodes plus the working one, re-run with num_speakers=3.
Same attribution code, only segmentation differs — the working episode
is the control, so the constraint must not break it. Outputs go to
separate directories, leaving unconstrained results intact for
comparison. The unconstrained sweep was stopped to give this the CPU;
its 4 completed episodes are banked and it resumes afterward.

Rationale recorded for Appendix A: constraining the count encodes a KNOWN
fact about the show's cast, not a preference about the outcome, and would
apply only to formats with fixed known casts. If it works, this becomes a
declared handling rule; if not, fallback (c) stands.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 64 (~14:12Z)

**STUDIO VERDICT (2 episodes): pyannote PARTIALLY solves the
three-brother case — real improvement, not yet reliable.**

| episode | type | speakers | Justin sim | word shares |
|---|---|---|---|---|
| 455 Fear Sponging | studio | 9 | 0.853 | **0.394 / 0.329 / 0.233** + noise |
| 472 LASIK Voicemails | studio | 9 | 0.886 | 0.621 / 0.305 + noise |
| 450 Face 2 Face | live | 13 | 0.792 | 0.587 / 0.330 + noise |

- **455 is a textbook three-way split** (39/33/23) — pyannote separated
  all three brothers, which ECAPA could never do (0.94-1.00 single
  cluster). Proof the problem is tractable.
- **472 collapses to 62/31** — two brothers still merged.
- Justin identification is strong and stable everywhere (sim 0.79-0.89,
  clean margins), so the 39s enrollment centroid is adequate; the
  variance is in SEGMENTATION, not identification.

**Read:** "sometimes correct" is not usable as-is for a within-person
outcome measure — a host-share that swings 39%->62% by episode would
inject noise directly into every rate denominator. Two paths, in order:
1. **Constrained run (agent, next):** pyannote accepts num_speakers /
   min-max. MBMBaM studio episodes have a KNOWN speaker count (3 brothers,
   + a scripted announcer in the cold open). Forcing 3-4 is principled
   rather than fitted, and 9 detected speakers means over-segmentation is
   the failure mode. Test on 472 (the failing case) — ~1h, invalidates
   that episode's turn cache only.
2. **PI V3 audit arbitrates** the final call, on a stratified sample that
   should now oversample MBMBaM.
If the constrained run does not stabilize shares, fallback (c) —
interview-formats-only panel — becomes the recommendation, and 455 stands
as evidence that the limit is engineering, not physics.

**Queue**: empty (no PI decision needed yet; audit comes after the
constrained test). **Spend**: $0.

## 2026-08-02, cycle 63 (~12:12Z)

**Restart #21** killed the pyannote run mid-studio-episode. Episode 450's
turns survived (the cycle-60b cache doing its job); the in-flight studio
episode was lost.

**Scheduling change**: episodes now processed STUDIO-FIRST (live
"Face 2 Face" shows deferred to the end). Rationale: the
measurable-or-not verdict depends on studio episodes, each costs ~1h, and
the restart cadence is 2-6h — so processing order directly determines how
fast the pilot learns anything. Alphabetical order had spent the first
(and so far only completed) run on the atypical live case.
Bug caught pre-launch: the new sort used `re` without importing it —
would have crashed at first use.

**Status**: pyannote 1/16 (the live episode), studio verdict ~1h out.
ECAPA interview run still parked at 15/48 by design.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 62 (~10:12Z)

**First pyannote MBMBaM episode complete — INTERIM, not the verdict.**
The alphabetically-first episode is 450 "Face 2 Face", a LIVE show with
audience noise — the hardest case in the sample and one already excluded
from enrollment by rule. Result: 13 speakers detected; time shares
SPEAKER_12 0.588 (36.5 min), SPEAKER_11 0.312 (19.4 min), remainder in
11 micro-clusters (audience/noise, <2.2% each). Justin identified
confidently (sim 0.792 vs next-best 0.451 — a clean margin, so the ECAPA
enrollment centroid IS discriminative). Diagnostic: 98.9% of words fall
inside a real pyannote turn, so the nearest-turn fallback is NOT inflating
shares — the 59/31 split is genuine.

**Read:** pyannote clearly beats ECAPA (which produced one all-brothers
cluster at 0.94-1.00 host share) — it is separating speakers. But 59/31
on a three-brother show suggests two brothers still merged into the
"Justin" cluster, OR that Justin genuinely dominates this live episode.
Cannot distinguish yet. **The verdict needs a STUDIO episode** (455, next
in queue, ~1h). Reporting this now rather than waiting, with the caveat
attached, because the interim number is easy to over-read in either
direction.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 61 (~08:12Z)

**pyannote**: first episode mid-run (~30 min wall, 191% CPU); turn cache
writes on pipeline return, so the next verdict-or-bug cycle is cheap.
ECAPA interview run remains parked at 15/48 by design. No other action
this cycle — the machine is deliberately dedicated to the P3 test, and
nothing else is unblocked without it.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 60b (event-driven)

**pyannote run completed its ~2h diarization then threw the result away**
on a downstream parse error: pyannote 4.x returns a `DiarizeOutput`
wrapper, not the classic `Annotation`, so `.itertracks()` failed AFTER all
the expensive work. Two fixes:
1. Correct parse: use `exclusive_speaker_diarization` (overlap resolved to
   one speaker per instant — exactly what word attribution needs), falling
   back to `speaker_diarization`.
2. **Structural fix (the real lesson): raw speaker turns are now CACHED to
   pyannote_turns/<ep>.turns.json immediately after the pipeline returns,
   before any downstream processing.** Any later bug now costs seconds, not
   hours. This mirrors the chunk-checkpoint principle from WS2 and is a
   WS8 rule: expensive irreversible compute must be persisted at the
   boundary where it is produced, not at the end of the enclosing job.

Relaunched. ECAPA interview-format run stays parked at 15/48 until the
first pyannote verdict lands.

## 2026-08-02, cycle 60 (~06:12Z)

**Two diarization jobs were contending for 4 cores**: ECAPA interview-format
run (15/48) and the pyannote MBMBaM test (first episode still in flight
after ~65 min wall). Since the pyannote result unblocks a protocol
decision (P3 measurable or not) and the ECAPA run is routine throughput,
the ECAPA job is PAUSED with SIGSTOP (resumable in place, no episode work
lost — per-episode idempotence plus a stopped process keeps its state) and
pyannote now has the machine. ECAPA resumes (SIGCONT) once the first
pyannote verdict is in.

**Note on pyannote cost**: ~65+ min wall for a ~1.3h episode on 4 CPU
cores, i.e. roughly realtime. For WS8: 16 MBMBaM episodes ~= 20h of
compute here; a full study using pyannote across ~1,800 episodes would
need GPU (pyannote is ~20-50x realtime on a consumer GPU) — this is a
concrete argument for the full study budgeting one GPU box rather than
CPU fleets.

**Scorecard**: V1 PASS, V2 PASS (both configs), V3 pending (interview
formats validating within ~2pp; multi-speaker under test), V4 pending
recount.

**Queue**: empty (PI cleared the multi-speaker item by choosing option b
and completing all four HF gates). **Spend**: $0.

## 2026-08-02, cycle 59d (event-driven — pyannote RUNNING)

**All four gates cleared; pyannote pipeline loads.** Gate chain in full
(for the WS8 catalog, since a full study will hit this too):
speaker-diarization-3.1 -> segmentation-3.0 ->
speaker-diarization-community-1 (4.x redirect), each a separate
acceptance form; ~15 min of PI time total. Token authenticates as the
PI's HF account, stored 0600 outside the repo.

**pyannote diarization of the 16 MBMBaM episodes LAUNCHED**
(ws3_diarize_pyannote.py, 2 threads, idempotent per episode). This is the
decisive test for the P3/multi-speaker question: can a purpose-built
diarizer separate three sibling voices where ECAPA+agglomerative could
not? Read on the FIRST completed episode: speaker count (expect 3-4:
three brothers + announcer) and host_word_share (expect ~0.30-0.40 for
Justin; the ECAPA failure produced 0.94-1.00).

**Interview formats** unaffected and continuing on the ECAPA path (which
validated within ~2pp of human transcripts) — no plan to re-diarize them
with pyannote unless the V3 audit motivates it, and any such switch would
be a declared, documented change rather than a silent one.

## 2026-08-02, cycle 59c (event-driven — pyannote auth, cont.)

segmentation-3.0 now accessible (PI accepted). Next gate surfaced:
**pyannote/speaker-diarization-community-1**. Cause identified: the
installed pyannote.audio is 4.x, and 4.x REDIRECTS the
"speaker-diarization-3.1" identifier to the newer community-1 pipeline,
which carries its own gate. So the gate chain is a property of the 4.x
client, not of our request. Two paths:
  (i) PI accepts community-1 (recommended — it is the current pipeline
      and generally outperforms 3.1); OR
  (ii) pin pyannote.audio 3.1.x, which uses segmentation-3.0 +
      wespeaker directly (both already accepted) — but 3.x is
      incompatible with this container's torchaudio (AudioMetaData
      removed), so it would need a torchaudio downgrade and revalidation.
Recommendation: (i). Honest caveat recorded: gate chains cannot be
enumerated ahead of time (metadata probes are false greens), so the agent
cannot promise this is the last form — though community-1 bundles its
own weights, so it should be.

## 2026-08-02, cycle 59b (event-driven — pyannote auth)

**HF token installed** (stored 0600 at ~/.cache/huggingface/token, outside
the repo; never committed/logged). Authentication CONFIRMED — whoami
resolves, and the error moved 401 -> 403 (authenticated but not
authorized).

**Remaining gate:** pyannote/speaker-diarization-3.1 is a meta-pipeline
that downloads two separately gated models. Terms are accepted for the
pipeline repo but NOT for **pyannote/segmentation-3.0**, whose weight
download 403s. NOTE for the record: an api.model_info() probe returned OK
for all three repos — that check reads metadata and does NOT test
file-download authorization, so it was a false green; the authoritative
test is a weight fetch (or the model page showing no pending form).
PI action queued: accept terms at huggingface.co/pyannote/segmentation-3.0
(and huggingface.co/pyannote/wespeaker-voxceleb-resnet34-LM if it also
prompts). No other work is blocked; interview-format diarization
continues.

## 2026-08-02, cycle 59 (~04:12Z)

**V3 STRUCTURAL FINDING — multi-speaker diarization FAILS on MBMBaM
(the pre-registered P3 stress test).** All 8 MBMBaM episodes diarized so
far: k=2 with one cluster = ALL THREE BROTHERS pooled (sibling voices too
similar for ECAPA embeddings at 1.5s windows; silhouette prefers the
speech-vs-music split), host_share 0.94-1.00 (nonsense). Interview shows
(EconTalk/Lex) diarize correctly — the failure is format-specific,
exactly as PILOT_PLAN WS3 anticipated ("P3 is the expected failure
point").

**DECISION QUEUE (PI) — multi-speaker handling, options:**
(a) Cheap retry: force k>=3 + finer windows (0.75s) for known-3-speaker
    shows — agent will test on one episode next cycle; sibling similarity
    may defeat it anyway.
(b) Better diarizer: pyannote speaker-diarization-3.1 — needs a free
    HuggingFace account token with model terms accepted (PI action:
    ~5 min; token pasted into session env). Most likely real fix.
(c) Declare multi-speaker formats unmeasurable with this pipeline: pilot
    reports P3 as NOT MEASURABLE; full-study panel restricted to
    interview formats (protocol E-rule amendment at freeze).
Recommendation: (a) now, (b) if PI provides token, (c) as the honest
fallback for the exit review. No action blocks interview-format work.

**Also this cycle**: restart #19 absorbed; diarization relaunched
(13/48 done; interview episodes unaffected and validating normally).

**Queue**: 1 item (above). **Spend**: $0.

## 2026-08-02, cycle 58 (~02:12Z)

**V2 CHUNKED-CONFIG PROBE: PASS** — full-pipeline A/B on the Lomborg
episode, 1.27% count delta (gate ±2%). The production configuration is
formally reproducibility-validated end to end. All V-gates that can be
machine-checked are now green: V1 PASS, V2 PASS (both configs).

**Enrollment QA catch:** the final Justin harvest pulled 3 long spans
whose welcome→self-intro stretch contained multi-brother banter — a
contaminated centroid (211 windows, implausibly high). Caught by
plausibility check before ANY MBMBaM episode was diarized. Harvest rule
hardened (span >15s → use self-intro segment only); clean re-harvest:
7 spans / 39s pure Justin → 41-window centroid. Thin but pure — Munch
Squad fallback remains if the V3 audit shows weak separation.

**Diarization** relaunched with clean centroids: 48 episodes, sequential
(~a day with restart overhead). WS5 recount + V3 audit export follow.

**Queue**: empty. **Spend**: $0.

## 2026-08-02, cycle 57 (~00:12Z)

**DETERMINISTIC CORPUS COMPLETE: 48/48.** All episodes transcribed under
the pinned config (faster-whisper-1.2.1/medium/int8/threads1/temp0/beam5/
chunk1500); Horton chunks 1+5 carry the loopguard_no_context flag (2 of
~210 chunks, as predicted). Corpus took ~3 days wall including 18
container restarts, one full config redo, and the V2 investigation — all
of which is exactly the WS8 material a full study needs.

**Post-corpus chain FIRED at 23:53Z** and is running: (1) chunked-config
V2 A/B probe (in progress), (2) 3-host enrollment, (3) deterministic
diarization x48, (4) WS5 recount. Note: diarization is single-process
sequential (~20-40min/episode → ~a day with restart overhead); if it
becomes the bottleneck, parallelize by host next cycle.

**Queue**: empty. **Spend**: $0 of $75 pilot cap.

## 2026-08-01, cycle 56 (~22:12Z)

**Subprocess timeout also failed to fire** (child at 235 CPU-min, parent
wedged in the wait — cause under investigation, but moot). Three
independent attempts confirm chunks 1/5 loop under with-context decode,
which IS the loop-guard criterion — so the with-context attempt is now
skipped by evidence: both chunks running DIRECTLY in no-context mode
(flagged loopguard_no_context per the Appendix A rule), then assembly +
post-corpus chain, all in one background sequence (~1h).

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 55 (~20:12Z)

**Restart #18** killed the v3 finisher mid-run; relaunched (idempotent —
the subprocess-timeout design survives restarts trivially since chunks
write atomically). Still 47/48 + chunks 1,5 of Horton. Note: chunk 1's
timeout budget is ~80min, so a completed run needs an uptime window of
~3h; windows today have been 2-6h — should fit.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 54 (~18:12Z)

**Loop-guard v1 didn't fire** — the repetition loop stalls INSIDE a single
decode window, so the segment generator never yields and an in-process
per-segment check never runs. Guard rebuilt as a HARD per-chunk subprocess
timeout (3x realtime + 300s; kill; fresh subprocess with
condition_on_previous_text=False; flag; escalating budget). Finisher v3
running. Appendix A rule text updated accordingly (subprocess-timeout
semantics). ~2h of compute lost to the unguarded attempt — logged.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 53 (~16:12Z)

**ROOT CAUSE of the unfinishable chunks found: decode repetition loops.**
Horton chunks 1 and 5 (sponsor/music-adjacent content) send the pinned
temperature=[0.0] decode into repetition loops — the fallback ladder that
normally breaks loops was removed for determinism. 227 CPU-minutes on one
25-min chunk before the kill. Every earlier "worker attrition" event on
these chunks now re-attributed to this, not OOM.
**Fix (Appendix A rule, deterministic + declared):** loop-guard — a chunk
exceeding 3x realtime wall-clock aborts and re-runs with
condition_on_previous_text=False (6x budget), output flagged
loopguard_no_context. Finisher relaunched with the guard; post-corpus
chain queues behind it. V2 note: the loop-guard rule is itself
deterministic (wall-clock-triggered — declared as the one
non-bit-reproducible trigger; the FLAG makes affected chunks auditable
and excludable in sensitivity analysis; expected incidence <=2 chunks in
~210).

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 52 (~14:12Z)

**Horton endgame.** All chunks but 1 and 5 complete — those two workers
died mid-chunk (OOM attrition) leaving stale claims the surviving worker
couldn't take, so it exited at 47/48. Claims cleared; a single chained job
now transcribes the 2 missing chunks (~60-80min), assembles the episode,
and FIRES THE POST-CORPUS CHAIN (V2 chunked probe → enrollment →
diarization of all 48 → WS5 recount) in one uninterrupted sequence.
WS8 note (final form): claim staleness needs heartbeats; every stall in
the corpus's last 10% traced to exactly this gap.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 51 (~12:12Z)

**Restart #17** stalled Horton at 15/20 for the inter-cycle window;
relaunched. 5 chunks (~1.5h at 3 workers) to corpus completion.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 50 (~10:12Z)

**Restart #16**; relaunched. Horton at 15/20 chunks — 5 remain (~1.5-2h).
Corpus completion this morning; post-corpus chain fires on 48/48.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 49 (~08:12Z)

**Horton**: 11/20 chunks; 2 workers steady through a 6h window. ~9 chunks
(~3h) to corpus completion, then the post-corpus chain fires.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 48 (~06:12Z)

**Horton**: 6/20 chunks. Worker attrition mechanism identified: 3 workers
x full-4h decoded-audio cache (~1.8GB each) + models exceeds RAM on this
one episode -> OOM reaper trims to 2. Two workers IS the RAM-fit for this
episode; no more relaunch churn. ~4-5h remaining. WS8 note: audio-cache
memory should scale with episode length (cap or mmap) when multiple
workers share one long episode.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 47 (~04:12Z)

**Horton grind**: 3/20 chunks after 2h at 2 workers (worker attrition
again; 4h-episode chunks run ~40min each). Relaunched to restore 3
workers (in-flight loss < gain with ~5h of tail remaining). Revised
completion: ~4-5h, then post_corpus chain fires.

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 46 (~02:12Z)

**Final episode push.** Corpus at 47/48; the holdout is the 4h Scott
Horton Lex episode (20 chunks). Two fixes landed between cycles: a stale
chunk-claim released, and a queue-logic bug patched (a claimed todo[0]
made workers skip the whole episode — now they iterate all unclaimed
chunks, so 3 workers share the final episode in parallel). Restart #15
absorbed; workers relaunched. ETA ~2.5-3h, then post_corpus.sh fires
(guarded on 48/48).

**Queue**: empty. **Spend**: $0.

## 2026-08-01, cycle 45 (~00:12Z)

**Redo**: 45/48; final 3 episodes in flight (2 workers). Post-corpus
analysis chain staged (post_corpus.sh): guards on 48/48, then runs (1)
chunked-config V2 A/B probe (<=2% gate), (2) Justin harvest + full
3-host enrollment, (3) deterministic diarization of all 48, (4) WS5
recount. Fires next cycle if the corpus is done. Tooling patched to be
directory-parametric (ws3_diarize, ws5_count).

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 44 (~22:12Z)

**Redo**: 43/48; 5 episodes remain. One worker exited on a benign
tail-race ("no more work" while the others held the only claimable
chunks — a small queue-logic wart at the tail, harmless; noted for WS8:
workers should sleep-and-retry rather than exit while unfinished episodes
exist). Claims verified clean (0 stale). 2 workers finishing, ~3-4h.

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 43 (~20:12Z)

**Restart #14**; relaunched with 3 workers for the final 7 episodes.

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 42 (~18:12Z)

**Redo**: 41/48; 7 episodes remain (~20 chunks, ~3-4h at 2 workers — one
worker died again; not restarting since relaunch cost ≈ gain this close to
the end). Justin harvest rerun on new episodes.

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 41 (~16:12Z)

**Restart #13**; redo relaunched. MBMBaM tail in progress.

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 40 (~14:12Z)

**Restart #12**; redo relaunched. ~10 episodes remain (MBMBaM tail).

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 39 (~12:12Z)

**Redo**: 196 chunks / 37 of 48; ~14h uptime; ~11 episodes remain
(MBMBaM tail). Justin span harvest at 4 spans / 27s; two 2019 episodes
skipped (opener derailed by bits — a 2019-era show habit, apparently).
Watch item: if 2019 episodes systematically fail the opener match,
Justin's enrollment pool skews late-era; acceptable for voice ID (voices
are stable) but noted for the V3 audit.

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 38 (~10:12Z)

**Redo**: 182 chunks / 35 of 48 (MBMBaM 5); 12h uptime — record window.
ETA for corpus completion: ~4-6h.

**WS3 Justin enrollment harvest built + first run** (ws3_justin_spans.py):
text-anchored opener spans, auto-verified by matched transcript text.
First pass: 3 spans / 22s Justin-solo (ep 515, 690, 701); 1 live episode
skipped by rule; 1 skipped where the opener was derailed by a comedy bit
(correctly unmatched — the pattern requires his actual self-intro).
Reruns automatically as remaining episodes assemble; expect ~10-12 usable
spans (~70-90s, ~60-80 embedding windows). If the pooled centroid proves
too thin at V3 audit, declared fallback: harvest Justin's "Munch Squad"
solo press-release readings (longer solo stretches, locatable by text).

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 37 (~08:12Z)

**Redo**: 169 chunks / 32 of 48 (EconTalk 16, Lex 13, MBMBaM 3); one
worker had died (claim-race exception) — launcher restarted, 3 workers
restored. ~10h uptime window.

**MBMBaM structure findings (first det2 transcripts):**
- Cold-open disclaimer voice is an ANNOUNCER, not a brother — must be
  excluded from any host-attribution assumptions (and from R-family
  denominators; it's scripted).
- Justin's solo opener is only ~5-8s/episode ("...I'm your oldest
  brother, Justin McElroy"), and live "Face 2 Face" episodes have atypical
  openings + crowd noise. Enrollment plan: text-anchored harvest of the
  opener span across ALL 16 sampled episodes (~100s Justin-solo total,
  each span auto-located by transcript text match and PI-auditable),
  skipping live episodes. Live-episode handling itself goes to the WS8
  failure/handling catalog (crowd noise will also stress diarization).

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 36 (~06:12Z)

**Restart #11**; redo relaunched (workers confirmed). Progress held at
~150 chunks / 28 of 48 assembled — Lex block nearly done.

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 35 (~04:12Z)

**Redo**: 148 chunks / 27 of 48; workers healthy, ~6h uptime. 5 Lex + 16
MBMBaM remain. No other action this cycle (transcription-dedicated CPU;
nothing else unblocked; queue empty).

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 34 (~02:12Z)

**Redo**: 135 chunks / 25 of 48 (EconTalk 16 + Lex 9); workers healthy,
~4h uptime. Remaining: 7 Lex + 16 MBMBaM. At current pace (~3.5
chunks/h aggregate on Lex material) the Lex block finishes ~mid-day;
MBMBaM (shorter, 3-voice episodes) should run faster. Diarization of
assembled episodes stays deferred until transcription is done (CPU
dedication rule).

**Queue**: empty. **Spend**: $0.

## 2026-07-31, cycle 33 (~00:12Z)

**Redo**: 119 chunks / 23 of 48 assembled; 3 workers healthy. Restart #10
occurred and was absorbed WITHOUT agent intervention (harness auto-restarted
the launcher; launch-time claim reconciliation did its job) — the pipeline
is now fully self-healing. Lex block continuing; MBMBaM not yet reached.

**Between-cycles**: literature review completed at PI request
(LITERATURE.md): 4 must-reads pre-freeze, theory tier, gap analysis.
Key updates: Yakura et al. v4 now includes an 824k-episode podcast
synthetic-control + N=496 entrainment experiment; a Science paper
establishes sycophantic-AI effects on conflict behavior (mechanism for
H1-R). Gap analysis confirms both our hypotheses sit in open territory —
protocol's related-work section should be updated before freeze
(action queued for the amendment pass).

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 31 (~20:12Z)

**Restart #9** ended the 8h window; no chunk progress lost beyond the
in-flight chunks (chunked design working as intended). Workers relaunched
and confirmed. Status: 105 chunks / 20 of 48 assembled; Lex block
continuing, MBMBaM after.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 30 (~18:12Z)

**Redo**: 105 chunks / 20 assembled / ~8h uptime (best window yet).
**All three Lex enrollment spans now det2-verified** (Sinek, Weinstein
#134, Huberman — solo intro+sponsor reads in each). The existing
lex_fridman voice centroid was computed from exactly these spans on
unchanged audio, so it stands without re-enrollment. Lex deterministic
diarization is now fully unblocked — deliberately deferred until
transcription workers free up (CPU contention lesson from V2).

**Milestones remaining in corpus**: rest of Lex block, then MBMBaM →
draft Justin's enrollment spans from his show-opening monologues →
3-speaker diarization stress test (the pilot's hardest V3 case).

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 29 (~16:12Z)

**Redo**: 96 chunks / 19 assembled / ~6h uptime. Both Weinstein episodes
assembled; Weinstein #134 enrollment span det2-verified (Lex solo
0-103s+). Huberman reference still pending -> Lex re-enrollment fires
when it lands. Note for WS5: pre-era Lex uses "realm" unprompted
(#134, 0:95, "the realm of conversation") - a genuine host-attributed
fingerprint-word baseline occurrence; the counting pipeline will pick it
up on the det2 recount.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 28 (~14:12Z)

**Redo pace assessment (revised, honest).** Affinity+cache patch holds
(workers sticky to episodes, no redundant decodes), but Lex chunks run
~0.6x/worker regardless — content-dependent decode cost (longer/denser
episodes make beam search slower), not an infra fault. EconTalk chunks ran
0.85-0.95x; Lex is simply slower material. Revised ETA: ~80 chunks remain
(~165 total for 48 eps) → ~1-1.5 days including restart overhead. No
further optimization planned — the pipeline is correct, deterministic, and
restart-proof; remaining time is intrinsic compute.

**Status**: 85 chunks / 17 assembled / 3 workers / ~4h uptime.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 27 (~12:12Z)

**Throughput fix.** Pace had dropped to ~0.6x/worker on the Lex block: all
three workers crowded the same long episode, each re-decoding the full
3-4h audio for every 25-min chunk under RAM pressure. Patched: (a) worker-
episode affinity (worker w prefers episodes where index%3==w, falls back
to any), (b) per-worker decoded-audio cache reused across chunks of the
same episode. Workers restarted under the patched launcher. Expected
recovery to ~0.9-1x/worker. Determinism unaffected (decode is
bit-identical; caching changes nothing in the compute path).

**Status**: 81 chunks / 17 assembled; Weinstein #134 nearly done.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 26 (~10:12Z)

**Restart #8** — workers dead since shortly after cycle 25 (~2h idle; no
chunk progress). Relaunched; stale-claim reconciliation handled by the
launcher. Status: 77 chunks / 17 of 48 assembled; Lex block in progress
(Weinstein and Huberman reference episodes not yet assembled — their span
verification and Lex re-enrollment wait on them).

Observed restart pattern for WS8: uptime windows today ranged 2-8h;
compute loses the tail of the window each time. Chunked design caps the
loss at ~25min/worker; without it the corpus would be unfinishable.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 25 (~08:12Z)

**V1 FORMAL RERUN — GATE PASS on freeze-quality data.** All 16 EconTalk
pairs, deterministic corpus, 177.9k aligned words: fingerprint ins/del
0/0; placebo 1.12/1.12 per 100k (symmetric, both eras).
WS4_V1_report.md updated (supersedes the provisional 07-29 run; era note
RESOLVED — the old deletion excess was V2's transcription loss).

**Corpus**: 17/48 assembled (EconTalk complete + Sinek); ~8h uptime.
Lex block in progress. Sinek enrollment span det2-verified (Lex solo
0-100s+ incl. ad reads — his voice throughout).

**Next**: Lex refs (Weinstein/Huberman) verify as they assemble → Lex
re-enrollment + diarization on det2; then MBMBaM + Justin enrollment.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 24 (~06:12Z)

**Redo**: 56 chunks, 12/48 assembled (EconTalk era-1 complete, era-2 half
done), ~6h uptime, workers healthy.

**V1 on 12 deterministic pairs (136k words): fingerprint 0/0; placebo
0.73 ins / 0.73 del per 100k — including 4 era-2 pairs.** The era-2
deletion excess is GONE on the deterministic corpus: the "heavier
transcript editing in era-2" hypothesis is effectively closed — it was
transcription loss all along. V1 gate comfortably passing on
freeze-quality data; final formal rerun when all 16 EconTalk pairs
assemble.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 23 (~04:12Z)

**Redo steady**: 33 chunks, 6/48 assembled, 3 workers, ~4h uptime (no
restart since cycle 21).

**Incremental V1 on the deterministic corpus (6 EconTalk pairs, 75.5k
aligned words): fingerprint ins/del 0/0; placebo deletions 1.33/100k vs
10.2/100k on the old corpus.** Reading: most of the old deletion signal
was content LOST by the nondeterministic transcription, not transcript
copy-editing and not ASR word-misses. The deterministic corpus is
measurably more complete; the era-2 "transcript editing" hypothesis will
be re-tested on det2 era-2 pairs as they assemble (if deletions stay low
there too, that flag closes entirely). PI's WS4 spot-verification hour may
shrink accordingly.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 22 (~02:12Z)

**Chunked redo running cleanly** — no restart in ~2h (longest uptime today);
17 chunks done, 3/48 episodes assembled, 3 workers healthy. Chunk pace ~1x
realtime/worker as expected. ETA still governed by restart luck, but every
chunk is now permanent progress.

**WS6:** rater rubric drafted (RATER_RUBRIC.md) — plain-language G1
(episode detection, 300 items) and G2 (turn labels, 200 items)
instructions with UNSURE option, calibration block, and no-discussion
rule. Ready for the PI's raters; sheet generator queues behind Stage-1
screening on the finished corpus.

**Queue**: empty. **Spend**: $0.

## 2026-07-30, cycle 21 (~00:12Z)

**Restarts #6 and #7 within the cycle; redo architecture upgraded to
CHUNKED.** Restart cadence has accelerated to ~2h, below the runtime of
long Lex episodes (1-4h single-threaded) — un-chunked, those episodes
could NEVER complete. New pipeline (ws2_bulk_det_chunked.sh):
- Episodes split at VAD-silence-aligned boundaries near 1500s marks —
  deterministic (VAD is deterministic), so the chunking is part of the
  pinned config: .../threads1/temp0/beam5/chunk1500.
- Each chunk is an atomic checkpoint + claim; a restart costs <=25 min of
  work per worker instead of a whole episode.
- Launch-time stale-claim reconciliation built in (the restart-#5 lesson).
- The 14 unchunked deterministic transcripts will be superseded by chunked
  versions for config consistency across the corpus (uniform pinned
  config; redo cost ~5h aggregate, absorbed by restart resilience).
- V2 note: chunked config needs its own A/B reproducibility probe once the
  corpus lands (chunk boundaries deterministic in principle; verify).

**WS8**: infra restart cadence is a first-class design parameter; work-unit
duration must be << restart interval.

**Queue**: empty. **Spend**: $0.

## 2026-07-29, cycle 20 (~22:12Z)

**Container restart #5** hit mid-cycle; the harness auto-restarted the
queue launcher, which re-ran its embedded `rm -rf claims` — wiping live
claim markers. Agent initially misread the fresh claims as stale and
deleted them, then caught the error and restored them (workers unaffected;
output writes are idempotent so worst case was duplicate compute, not
corruption). Launcher lesson for WS8 + immediate practice: claim hygiene
on restart-prone infra needs heartbeats (claim mtime refresh) rather than
launch-time wipes; for the pilot's scale, manual reconciliation at each
cycle (claims vs outputs vs live processes) suffices and is now the
documented procedure.

**Status:** 14/48 deterministic; 3 workers healthy on the first Lex
episodes post-restart. Restarts cost ~1-1.5h of worker progress each when
they land mid-episode; ETA drifts accordingly (~afternoon tomorrow).

**Queue**: empty. **Spend**: $0.

## 2026-07-29, cycle 19 (~20:12Z)

**Redo OOM cascade caught and fixed.** The 4-worker layout (incl. the
shard-0 relaunch, which restored the 4-model footprint) was progressively
OOM-killed; the launcher's `wait` then returned cleanly and printed a FALSE
"corpus complete" at 14/48. Two fixes: (a) workers cut to 3, sized to RAM;
(b) sharding replaced with an atomic-claim WORK QUEUE so any worker picks up
any remaining episode and a dead worker's unclaimed files are never
stranded. WS8 lessons: false-success on partial completion is a real
failure mode - completion checks must count OUTPUTS, not process exits
(the new launcher reports N/48 explicitly); OOM sizing = RAM / (model
footprint + longest-episode decode buffer), which for 3-4h Lex episodes
is ~4GB/worker.

**Status:** 14/48 deterministic; 3-worker queue confirmed running (3 procs,
14G available RAM). ETA ~15-16h for the remaining ~50h of audio.

**Queue**: EMPTY (PI cleared all four items — see DECISIONS.md).
**Spend**: $0.

## 2026-07-29, cycle 18b (event-driven — PI decisions)

**Decision queue CLEARED by PI** (full log: DECISIONS.md):
1. Second rater: PI's adult children (blind to hypotheses), wife as
   fallback — covers G1/G2 gold labeling and exposure ratification.
   Next agent action: prepare rater rubric + labeling sheets in week-2
   window; record rater onboarding date when known.
2. History frame substitution: ACCEPTED as documented.
3. MBMBaM primary host: JUSTIN — enrollment spans queue behind MBMBaM
   transcripts (redo in progress).
4. EconTalk courtesy email: DECLINED — proceed under existing ToS posture.

Open PI items remaining: NONE decision-shaped. Scheduled PI time: V3 audit
(~1h), WS4 spot-verification (~1h), G1/G2 gold labeling (rater-dependent).

## 2026-07-29, cycle 18 (~18:12Z)

**Redo status: 3/48 done, and a big schedule surprise.** Single-threaded
workers run ~0.9-1.1x realtime EACH (CT2's multithreading was near-useless
on this CPU) → aggregate ~3.6x realtime → corpus completes in ~18h, not
2.5 days. The deterministic fix costs nearly nothing in wall-clock.

**Anomaly:** shard 0 OOM-killed at startup (4 models + decode buffers vs
15GB RAM). Relaunched; RAM at 10G used with 4 workers live. Contingency:
drop to 3 workers on any repeat OOM. WS8 note: memory, not CPU, is the
binding constraint for parallel single-threaded transcription; full study
should size workers to RAM/2.5GB or stream decode.

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 17 (~16:12Z)

**Container restart #4** killed the redo before any episode completed
(restart landed within the first episodes' ~60-90min processing window —
single-threaded episodes are longer-lived checkpoints, so restarts hurt
more now; WS8 note: deterministic redo on restart-prone infra wants
smaller work units or mid-episode checkpointing... accepted as-is for the
pilot, ~2 episode-slots lost per restart worst case). Redo relaunched.

**Status**: deterministic corpus 0/48 after relaunch; ~2.5 days to
completion at 4x single-threaded workers. All downstream reruns
(V1/WS5/WS3) queue behind it. Machine dedicated to the redo.

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 16b (event-driven)

**V2 GATE: PASS under pinned config.** Full-episode A/B at cpu_threads=1:
count delta 0.389% (gate: ±2%), token agreement 97.3%. Config pinned into
WS2_throughput.md (Appendix A material):
faster-whisper-1.2.1/medium/int8/threads1/temp0/beam5, OMP_NUM_THREADS=1.
**Deterministic corpus redo LAUNCHED** — 4 parallel single-threaded workers,
all 48 episodes, ~65-70h audio at ~1.2x aggregate → ~2.5 days. Old
transcripts retained until V1/WS5/WS3 rerun on the deterministic corpus,
then retired. Residual 2.7% token disagreement (boundary effects) is
declared in the V2 report as the irreducible floor of this stack; counts
(the analysis quantity) reproduce well inside gate.

## 2026-07-29, cycle 16 (~14:12Z)

**V2 full-episode validation in flight**: run A complete at threads=1 —
6,435 words, vs 4,595/5,997 from the two nondeterministic runs of the SAME
episode: the multithreaded configuration was not just irreproducible, it was
DROPPING real content (~7-28%). The deterministic config is more complete,
not merely more stable. Run B in progress (~2h); machine kept otherwise
idle. Deterministic 4-worker redo script staged (ws2_bulk_det.sh), fires on
a passing A-vs-B comparison.

**Downstream implications once corpus is redone**: V1 realignment, WS5
baseline recount, diarization re-run (word timestamps shift), host-share
revalidation. Human-transcript ground truth and enrollment spans unaffected.

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 15b (event-driven)

**V2 root cause isolated + fix candidate validated at clip scale.**
Chain: audio decode bit-identical (md5 x3); VAD deterministic; divergence
begins at the first tokens -> CTranslate2 multi-threaded float-reduction
nondeterminism, cascaded by condition_on_previous_text. Load sensitivity is
the same mechanism (scheduling variance), unifying all prior probe results.
5-min A/B: cpu_threads=4 -> word counts differ (688 vs 669);
cpu_threads=1 -> word counts IDENTICAL (715 vs 715; text near- but not
bit-identical). V2's +/-2% gate is on COUNTS, so threads=1 is gate-passing
at clip scale. Full-episode validation running (2 solo runs, threads=1,
OMP pinned). If <=2%: Appendix A pins {medium/int8, cpu_threads=1,
temperature=[0.0], beam_size=5}; corpus redo runs as 4 PARALLEL
single-threaded workers (aggregate ~1.2x realtime — faster than the old
single 4-thread job, and load-robust by construction).

## 2026-07-29, cycle 15 (~12:12Z)

**V2 verdict from probe #3: BOTH factors real.**
- Solo, exact settings: 5.02% delta (vs 96% under load) — load corruption
  is the dominant effect and is CONFIRMED (transcription must run
  exclusively; likely audio-decode underruns feeding VAD).
- But 5% > the ±2% gate even solo, and segmentation still differs (932 vs
  1,703 segments) — residual nondeterminism from the temperature-fallback
  sampling ladder.

**Action (pre-registered in cycle 13b):** old-settings bulk transcription
STOPPED (no more compute on to-be-discarded transcripts). Determinism test
running: two solo runs of one episode with fully pinned decode
(temperature=[0.0], beam_size=5) compared to each other. If identical/±2%:
adopt pinned settings into Appendix A (with exclusive-execution rule),
REDO the 17-episode corpus (~1 day solo compute), rerun V1 + baselines.
Existing V1/host-share/baseline numbers are provisional until then —
directionally informative (attribution validated against human transcripts
independently) but not freeze-quality.

**Queue / spend**: unchanged / $0. Schedule impact: ~1.5 days.

## 2026-07-29, cycle 14 (~10:12Z)

**V2 isolation experiment in progress — machine deliberately idle.**
Probe #2 (exact settings, loaded machine) collapsed to 533 words/79 segments:
VAD kept only ~9 min of a 77-min episode. Emerging hypothesis: CONCURRENT
CPU LOAD corrupts pipeline output (likely audio-decode underruns feeding
VAD), which would also explain probe #1's 13.5% delta. Probe #3 (exact
settings, SOLO) is running now; bulk transcription paused and auto-resumes
when it completes. No other compute launched this cycle to keep the
experiment clean. If probe #3 reproduces ±2%: Appendix A gains an
exclusive-execution rule + re-audit of any episode transcribed under
contention (transcripts 5-17 all ran while diarization/other jobs shared
the CPU — the V1 alignment numbers themselves may need a redo pass).
If probe #3 fails: decode re-pinned deterministic, corpus redone.

**Other jobs**: bulk transcription paused (auto-resumes); diarization
deferred one cycle (would contaminate probe).

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 13b (~09:00Z, event-driven)

**V2 RED FLAG — reproducibility probe FAILED at 13.5% word delta (target
±2%).** Re-transcription of Hirschfeld produced 11,098 words vs 12,836
original; identical time coverage but radically different segmentation
(753 vs 1,703 segments) and 2,476 tokens unique to the original run.
CONFOUND in probe #1: rerun used cpu_threads=2 vs 4 (thread count changes
float reduction order -> can flip decode paths); faster-whisper's default
temperature-fallback ladder also samples nondeterministically at T>0.
Probe #2 with EXACT original settings is running. Outcomes:
- If probe #2 reproduces ±2%: pin cpu_threads in Appendix A alongside model
  version; V2 passes with a sharpened settings-pin lesson.
- If probe #2 also fails: decode params must be re-pinned (temperature=[0],
  fixed beam) and the transcribed corpus REDONE under deterministic
  settings before any confirmatory counting. Cost: ~1 day compute. This
  is a freeze-blocking issue and exactly what V2 exists to catch.

## 2026-07-29, cycle 13 (~08:12Z)

**Container restart #3** — transcription relaunched from checkpoint (17/48;
EconTalk block 16/16 COMPLETE, Lex block begun).

**Milestones**
- **V1 GATE: PASS** on the full EconTalk corpus — WS4_V1_report.md. Zero
  fingerprint insertions/deletions in 176k aligned words. Deletion-side
  caveats declared (occurrence starvation; copy-editing upper bound).
- V2: first reproducibility probe RUNNING (Hirschfeld re-transcription,
  2 threads; word-count and count deltas vs ±2% target on completion).
- V3: 15/16 EconTalk diarized + validated (Pinker queued next cycle).

**Next**: Lex transcripts → verify his enrollment spans → Lex diarization;
V3 audit-sample export once Lex episodes accumulate (host x era strata).

**Queue / spend**: unchanged / $0. Second-rater decision due in ~4 days.

## 2026-07-29, cycle 12 (~06:12Z)

**Era-differential update (softening):** episodes 11-13 validate at 2-4pp
gaps — the era-2 differential is driven by two outliers (Yudkowsky, Betts),
episode-specific causes more likely than an era-wide shift. Flag stays open
for the stratified audit but the confounder scenario weakened.

**Scorecard**
- V1: 15 pairs / 164k words; fingerprint ins/del still 0/0 (2 genuine
  occurrences, both correct). Placebo ins 1.22/100k — slightly above the
  <1/100k gate line IF it were the fingerprint list (it isn't; fingerprint
  is what the gate governs, and it's at 0). Placebo del 10.4/100k, era-2
  driven (transcript-editing artifact, upper bound).
- V3: 13/13 diarized-and-validated; 14-15 diarizing now.
- V2: first reproducibility probe DEFERRED until main transcription is off
  the critical path (avoids CPU contention); planned: re-transcribe 1
  EconTalk episode, counts must reproduce ±2%.

**Coverage**: WS2 15/48 — Pinker finishing the EconTalk block; Lex block
next (his enrollment spans get transcript-verified when his first eps land).

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 11 (~04:12Z)

**Priority methodological flag (for stratified V3 audit)**
Era-2 host-attribution gaps are wider than era-1: Yudkowsky human 39.2% vs
pipeline 32.4% (-6.8pp), Betts 19.6% vs 25.2% (+5.6pp), vs ~2pp gaps on all
era-1 episodes. If attribution error differs by ERA it is a within-person
trend confounder — exactly what NC3 and the era-stratified V3 audit exist to
catch. Candidates: more produced segments/ads post-2021, remote-guest audio,
or heavier transcript editing (Betts GT is short for 64 min). Quantify across
all 16 EconTalk pairs when the block completes; V3 audit sample must
oversample era-2.

**Scorecard**
- V1: 13 pairs / 145.6k words. Fingerprint ins/del still 0/0. Placebo ins
  0.69/100k, del 9.6/100k (deletion rate creeping up in era-2 pairs —
  consistent with the transcript-editing hypothesis above, and why deletions
  are measured against an upper bound).
- V2/V4: unchanged.

**Coverage**: WS2 13/48 (EconTalk block nearly done — 3 remain). Era-2 runs
~1.6x realtime. Diarization of 11-13 in background.

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 10 (~02:12Z)

**Scorecard**
- V1: now 10 pairs / 116k aligned words. Fingerprint: 1 genuine occurrence,
  correctly transcribed; insertions 0, deletions 0 → the fake-signal
  direction (ASR inventing fingerprint words) is clean at <0.9/100k upper
  bound. Placebo: ins 0.86/100k, del 6.9/100k. Note: fingerprint words are
  so rare in speech that the ins-vs-del asymmetry comparison is
  occurrence-starved — V1's meaningful gate here is the insertion rate, and
  it passes.
- V3: 8/8 EconTalk episodes diarized, host share within ~2pp of human
  transcripts on 7/8. WS5 baseline now 36k host words, fingerprint still 0.

**Coverage**: WS2 10/48 (era-2 EconTalk in progress; Yudkowsky 78min in
39min — era-2 audio transcribes faster). Diarization relaunched for 9-10.

**Queue / spend**: unchanged / $0.

## 2026-07-29, cycle 9 (~00:12Z)

**Anomaly: second container restart** mid-cycle (the first was cycle 6).
Both compute jobs relaunched from checkpoints; no data loss. Restart cadence
(~2 per day) is now an expected operating condition — WS8 will model it.

**Turn-segmentation calibration (WS6)**
- Backchannel-absorption logic rewritten (short interjections no longer
  bridge/split turns incorrectly; their words keep true attribution).
- Fair comparison is human SPEAKER-CHANGES (collapsing editorial paragraph
  splits), not raw paragraph count: pipeline captures 75/104, 39/81, 69/105,
  55/67 speaker changes (65-85%). Root cause of the misses: 1.5s embedding
  windows can't resolve sub-1.5s interjections — they never get their own
  window. Implication: R1 (disagreement initiation rate) undercounts short
  sharp interjections ("No."), which is exactly R5's material. Options for
  the decision queue AFTER quantification on more episodes: (a) finer
  windows (0.75s/0.375s hop, ~2x compute), (b) accept + declare as
  measurement floor, (c) word-level re-segmentation using Whisper word
  probabilities at boundaries. Recommendation deferred until MBMBaM (the
  stress case) is diarized.

**Coverage**: WS2 8/48 transcribed; diarization catching up on eps 5-8.

**Scorecard / queue / spend**: otherwise unchanged.

## 2026-07-28, cycle 8 (~22:12Z)

**Coverage / progress**
- WS2: 6/48 transcribed (Newstok took 116 min — CPU was shared with
  diarization; Shortland back to 67 min once diarization idled).
- WS6 prep: turn reconstruction implemented (ws6_turns.py) and run on 4
  episodes; emits the metadata-stripped HOST/GUEST turn format that Stage 1/2
  prompts consume. First conversation stats: 17-30 host turns/hour, mean host
  turn 141-182 words.
- **Calibration flag:** pipeline turn counts run 2x low vs human transcripts
  (Lomborg 39 vs 82) — backchannel absorption is over-merging. Needs tuning
  against human-transcript turn boundaries before G1 gold-sample construction
  (the 16 EconTalk human transcripts are the free calibration target).
  Stage 1's 30-turn sliding windows tolerate this meanwhile.

**Scorecard**: V1/V3/V4 unchanged from cycle 7. V2 will use the completed
EconTalk block for its first 1% reproducibility probe.

**Decision queue**: items 1-5 unchanged.

**Spend**: $0 external.

## 2026-07-28, cycle 7 (~20:12Z)

**Scorecard**
- V1: clean rerun on decontaminated ground truth (4 pairs, 54.5k words):
  fingerprint ins=del=0; placebo 1 deletion (1.8/100k). Gate passing so far.
- V3 (pre-audit evidence): pipeline host word-share matches human-transcript
  host share within ~1pp on 3/4 episodes (29.6→30.7, 32.5→32.9, 32.2→33.4);
  Hirschfeld off 5pp (47.4→42.5) — flagged for the formal audit. Known
  intro spans 100% HOST in all 4. k=3 selections are a junk micro-cluster
  (0.1-0.2% of words), not speaker splits; consider min-cluster-size floor.
- V4 seeded: WS5 counting pipeline live (ws5_count.py).

**Key quantitative finding (feeds WS7 power sim)**
Pre-era EconTalk host speech, 18.5k host words: fingerprint composite = 0
occurrences (0/100k); placebo = 6 (32/100k). ASR ground truth (54.5k words,
both speakers): fingerprint also 0. The lexical outcome is EXTREMELY sparse
at baseline — the power simulation must model near-zero baselines, and the
"increase from ~0" regime may favor absolute-rate over rate-ratio framing.
Host words/episode 3.6-5.5k → ~20-25k per host-period at 5 eps (>5k minimum).

**Coverage / progress**
- WS2: transcription resumed post-restart, 5/48 in progress.
- WS3: all 4 available episodes diarized; job idles until new transcripts.
- WS4: 16/16 ground-truth parses clean (speaker allowlist fix; layout with
  comments BEFORE transcript documented in failure catalog).
- WS5: counting pipeline built + first baseline rates (above).

**Decision queue**: items 1-5 unchanged; nothing new blocking.

**Spend**: $0 external.

## 2026-07-28, cycle 6 (~18:12Z)

**Anomaly: container restart.** The session container recycled between cycles
(~18:12Z); all background compute died mid-task. Scratchpad disk, all audio,
transcripts, and installed packages survived. All three jobs relaunched from
their idempotent checkpoints — this is exactly the failure mode the loop
design anticipated; no data lost. WS8 note: long-running compute in this
environment must checkpoint per-episode (it does).

**Coverage / progress**
- WS2: relaunched (4/48 done). Pace estimate unchanged.
- WS3: relaunched (1 episode diarized so far).
- WS4: econtalk.org cooldown over (200 OK); refetch running at 45s pacing
  with raw-HTML caching. V1 rerun once fetches land.

**Scorecard / queue / spend**: unchanged from cycle 5.

## 2026-07-28, cycle 5 (~16:12Z)

**Scorecard**
- V1 first pass ran on 4 episode pairs (~63k aligned words): fingerprint
  insertions 0, deletions 0 — the words are near-absent from pre-era EconTalk
  speech (matters for WS7 power sim: sparse-outcome regime). Provisional
  placebo: 0 ins, 5 del. NOTE: results are provisional — one pair (Lomborg)
  was contaminated (see anomaly) and the run will be redone cleanly.
- V3: unchanged from cycle 4 (diarization continuing in background).

**Anomaly (WS8 failure catalog + process lesson)**
1. EconTalk page parser scooped READER COMMENTS + footer into ground truth
   (fake speakers, +9k words on one episode). Parser fixed (comment-section
   cutoff, speaker-name filter, offset-guarded markers).
2. Agent process error, logged honestly: the cached good fetches were deleted
   before the re-parse was verified, and raw HTML had not been saved despite
   the script's docstring claiming it. Both fixed (raw HTML now cached;
   refetch never needed after parser changes).
3. econtalk.org rate-limited the refetch burst (403) — 32 fetches at 6s
   pacing. Pacing raised to 45s; refetch scheduled next cycle after cooldown.
   Failure-mode catalog entry: publisher sites rate-limit far below CDN
   thresholds; transcripts should be fetched once, slowly, with raw caching.

**Coverage / progress**
- WS2: 5/48 transcribed. WS3: diarization continuing.
- WS4: fetch+parse+align pipeline implemented (ws4_fetch_transcripts.py,
  ws4_align.py); blocked ~1 cycle on the 403 cooldown.

**Decision queue**: items 1-5 unchanged.

**Spend**: $0 external.

## 2026-07-28, cycle 4 (~14:12Z)

**Scorecard**
- V3: first diarized episode PASSES internal sanity check — intro 100% HOST
  (165/165 words), guest first-reply correctly non-HOST, known host turn 21/21;
  k=2, host-cluster sim 0.892, host word-share 42.5%. Formal PI audit still
  pending (needs more episodes + stratified export).
- V1: ground truth SOURCED — EconTalk human transcripts verified verbatim
  w/ speaker labels + timestamps in BOTH eras (WS4_ground_truth.md). ~20 h
  available vs. ≥10 h gate requirement.
- V2/V4: unchanged (await counting pipeline).

**Coverage / progress**
- WS2: 4/48 transcribed (pace dipped to ~1.25x wall/audio-hour with
  diarization sharing CPU — acceptable).
- WS3: diarization running through completed episodes in background.
- WS4: sourcing done (above); alignment implementation next cycle.

**Decision queue**: items 1-5 unchanged. Upcoming PI time commitments now
visible: V3 audit (~1 h) once ~10 episodes diarized; WS4 spot-verification
(~1 h) once alignment runs.

**Spend**: $0 external.

## 2026-07-28, cycle 3 (~12:12Z)

**Scorecard**: V3 in motion — enrollment done, first diarizations running.
V1/V2/V4 unchanged.

**Coverage / progress**
- WS2: 3/48 transcribed (all three EconTalk enrollment references). Pace ~1.0x
  wall/audio-hour with diarization now sharing CPU.
- WS3: enrollment spans transcript-verified for all 3 EconTalk references
  (guest-entry timestamps logged in enrollment_spans.json); Lex spans
  provisional pending his transcripts. Host centroids built (econtalk 211
  windows, lex_fridman 315). Diarization of completed episodes launched
  (background); first V3 numbers next cycle.
- Bug fixed: enroll() choked on JSON "_note" key.

**Decision queue**: unchanged (items 1-5 open; none blocking current work).

**Spend**: $0 external.

## 2026-07-28, cycle 2 (~10:12Z)

**Scorecard**: V1/V2/V4 unchanged (not started). V3: pipeline built this cycle,
audit pending diarized output.

**Coverage / progress**
- Frame snapshot COMPLETE (between cycles): 18 Chartable top-200 genre-chart
  captures 2020-2021 + History supplement committed (frame/FRAME.md). WS1 fully
  done.
- WS2 transcription: 2/48 episodes done, on pace (~1.0x wall clock/audio-hour,
  ~4 days remaining). Disk 21G free.
- WS3 built this cycle: ECAPA-embedding diarizer + host-attribution pipeline
  (ws3_diarize.py) - speechbrain/spkrec-ecapa-voxceleb (un-gated; pyannote
  models are HF-gated, no token in env), agglomerative clustering with
  silhouette K-selection, host enrollment from intro-monologue spans
  (enrollment_spans.json). Smoke-tested on real audio. Runs as transcripts
  accumulate; V3 audit export hook included.

**Decision queue (PI)** — additions:
4. History-genre frame substitution (frame/FRAME.md) — ratify or drop History.
5. MBMBaM primary-host designation for diarization enrollment + all host-level
   analysis (protocol E1: one host per show). Options: Justin (eldest,
   traditionally opens the show), Griffin ("sweet baby brother", frequent
   segment-driver), or Travis. Recommendation: whoever the V3 audit shows is
   most acoustically separable — deferred until first MBMBaM diarization, but
   the PI may pre-empt with a preference.

**Spend**: still $0 external.

## 2026-07-28, cycle 1 (06:12Z trigger; run ~08:12Z)

**Scorecard**
- V1 (ASR bias): NOT STARTED — awaits WS4 ground-truth sourcing; transcriber candidate benchmarked.
- V2 (reproducibility): N/A until counting pipeline exists.
- V3 (diarization audit): NOT STARTED — WS3 next after transcription.
- V4 (placebo monitor/coverage): N/A until counting starts.

**Coverage / progress**
- WS1: COMPLETE except frame snapshot. Slate ratified by PI (Lex Fridman /
  EconTalk / MBMBaM). Manifests committed; 48/48 sample episodes downloaded
  (3.9 GB); ToS notes recorded. Frame snapshot: web.archive.org became
  reachable this cycle after ~40 min of connection resets — snapshot job
  re-armed and running (Chartable CDX discovery + 2020/2021 captures for 7
  genres + all-podcasts).
- WS2: throughput measured (small 1.72× / medium 0.85× / large-v3 0.49×
  realtime on 4 CPU cores). Bulk transcription of 48 episodes running with
  medium/int8 (idempotent; ~4 days wall). Full-study local transcription
  infeasible in-container; costed options in WS2_throughput.md.
- WS6: Stage 1/2 annotation prompts drafted (WS6_annotation_prompts_draft.md)
  with metadata-stripping spec and rule-based backstops.

**Decision queue (PI)**
1. EconTalk courtesy note to econlib@libertyfund.org — optional; proceeding
   without unless PI objects (TOS_NOTES.md).
2. Second-rater decision (PILOT_PLAN: by end of week 1).
3. Annotation-model pin for WS6 — recommendation + cost estimate will
   accompany the pilot-corpus token measurement (not yet actionable).

**Spend**: $0 external of $75 pilot cap ($400 total). All compute local so far.

**Anomalies**: web.archive.org egress-IP throttling (documented in
frame/snapshot_log.txt); no data anomalies.
