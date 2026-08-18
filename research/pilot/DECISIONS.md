# PI Decision Log

Per PROTOCOL §10: every queued decision, its resolution, date, and where it
took effect. Latest first.

## 2026-08-18 — annotation model: PINNED to Haiku 4.5 via API

**PI decision: run WS6 annotation through the metered API on
`claude-haiku-4-5` with temperature=0, not through the agent session.**
Ratified in-session 2026-08-18.

Rationale (recorded because the cheaper-looking option was rejected):
- Session-based annotation would cost no extra dollars (subscription), but
  the serving model can change mid-run and cannot be pinned or recorded —
  the same unpinned-config failure class that V2 exposed in transcription.
- API cost is trivial at pilot scale: Stage 1 reads 1,877 host turns
  (~244k input tokens) ≈ **$0.30**; full-study Stage 1 ≈ $93 on Haiku.
- Haiku 4.5 over Sonnet-class: it is the model the full study would use,
  AND it still accepts temperature=0 — Sonnet 5/Opus 5 reject sampling
  parameters, so pinned sampling is not expressible there.
- **Escalation rule:** if Haiku fails κ≥0.70 against the PI's gold labels,
  re-validate a Sonnet-class model on the same gold sample; that switch is
  a PI decision.

Effects: `ws6_stage1.py` (pinned config string written into every output),
spend drawn from the $75 pilot cap once the PI supplies an API key.

## 2026-08-18 — QA-flagged episodes: EXCLUDED

**PI decision: exclude Lex #134 and Lex #478 from analytic totals.**
Ratified 2026-08-18 in-session, on the completed blind V3 audit.

Evidence base (WS3_V3_report.md, `results/v3_audit_scored.json`):
- The implausible-host-share QA rule flagged both episodes automatically
  (~99.9% host share) before any human listened — staged amendment B3.
- Both were placed in the 20-clip audit **unmarked**, so the PI labelled
  them blind alongside 18 clean clips.
- PI heard **60%** host on #134 (A01) and **0%** host on #478 (A02); the
  pipeline asserts **100%** on both. Misses of +40 and +100 pp.
- The other 18 clips agreed to 3.2 pp MAE, all within ±15 pp, so the
  failure is specific to these two episodes and not a general attribution
  problem.
- Between them the two episodes held **141,632 of 298,875 host words —
  47.4% of the uncorrected denominator.**

**Effects:**
1. Analytic totals: **30 episodes / 157,243 host words** (verified:
   298,875 − 28,278 − 113,354 = 157,243). These are the totals already
   used for the V4 fingerprint rate of 7.6/100k, so no recount is needed.
2. Their host-periods are marked **MISSING, not zero-filled**, per staged
   amendment C1.
3. Recorded machine-readably in `results/exclusions_ratified.json`.
   `ws5_counts.json` is left as raw per-episode output — exclusion is
   applied by consumers, so the raw record stays auditable.
4. Amendment C1 (pre-specified handling of QA-failed episodes) now has a
   worked precedent for the freeze pass; B3 (the QA gate itself) is
   confirmed by an independent human check.

## 2026-08-03 — multi-speaker formats: fallback (c) ADOPTED

**PI decision: multi-speaker/co-host formats are NOT MEASURABLE with
available tooling.** Ratified 2026-08-03 on the completed paired
experiment (DAILY_BRIEF cycles 59, 64-69).

Evidence base:
- ECAPA + agglomerative clustering: all three brothers pooled into one
  cluster (host share 0.94-1.00) on 8/8 episodes.
- pyannote speaker-diarization (community-1): correct three-way split in
  **1 of 3** studio episodes (0.394/0.329/0.233); the other two collapsed
  to ~0.62/0.31.
- num_speakers=3 constraint: made things WORSE everywhere, including
  destroying the one working episode (0.394 -> 0.979). Host-similarity
  fell on that episode (0.85 -> 0.72), consistent with the surviving
  cluster being a blend of voices.
- Host IDENTIFICATION was reliable throughout (sim 0.83-0.89); the limit
  is SEGMENTATION of closely-matched sibling voices, which sit nearer to
  each other in embedding space than to any non-speech in the audio.
- Decisive: no per-episode way to know which outcome occurred without
  ground truth, so host-share noise would propagate into every rate
  denominator in the relational battery.

**Effects (staged for the freeze amendment pass; protocol is not edited
mid-flight per §10):**
1. E-rule amendment: eligibility restricted to interview / two-voice
   conversational formats. Co-host and panel shows excluded from the
   full-study panel, with this finding cited as the reason.
2. Pilot P3 slot reported as **NOT MEASURABLE**, itself a WS8/Appendix C
   deliverable rather than a gap.
3. MBMBaM's 16 episodes: retained as a documented methods case; NOT
   analysed for H1-L/H1-R. Their transcripts and diarization outputs stay
   in the repo as evidence.
4. V3 audit sample: interview formats only, weighted toward Lex (no
   published verbatim transcripts, so the audit is his only validation).
5. WS5/WS6 recounts: MBMBaM excluded from analytic totals, reported
   separately if at all.

**Appendix C (upgrade path, not a permanent limit):** episode 455 proves
separation is achievable. A diarizer trained for closely-matched voices,
or per-speaker enrollment of ALL co-hosts rather than the primary only,
would reopen co-host formats for a better-resourced study.

## 2026-08-02 — multi-speaker diarization (V3 structural failure)

**PI decision: option (b) — adopt pyannote/speaker-diarization-3.1.**
Context: ECAPA+agglomerative clustering pools the three McElroy brothers
into one speaker (DAILY_BRIEF cycle 59); interview formats unaffected.
Implementation staged this cycle (ws3_diarize_pyannote.py): pyannote
supplies speaker turns; host identification still uses the ECAPA
enrollment centroid, so enrollment_spans.json and the interview-format
path stay authoritative; output schema unchanged so WS5/WS6 consume it
unmodified. PI has accepted the model terms on Hugging Face
(2026-08-02). **Remaining: an HF read token in the session environment**
(website acceptance alone yields 401). Token is a credential: stored
outside the repo, never committed, never logged.
Fallbacks if pyannote underperforms on sibling voices: (c) declare
multi-speaker NOT MEASURABLE and restrict the full-study panel to
interview formats at freeze.

## 2026-07-29 — batch resolution (PI, in-session)

1. **Second rater: RESOLVED.** PI's adult children (25, blind to the
   hypotheses) will be asked first; PI's wife is the fallback. Applies to
   both roles: G1/G2 gold labeling (~6-8h, week 2) and exposure-label
   ratification (Phase 3). Rater independence rule recorded: no discussion
   of hypotheses or of the PI's own labels during rating; disagreements
   resolve to UNKNOWN (exposure) / excluded (gold). Rater identity is
   recorded here but reported in the write-up only as "one independent
   second rater (family member, blind to hypotheses)" with the relationship
   declared as a limitation.
2. **History-genre frame substitution: ACCEPTED.** The §3.1 History cell
   uses Chartable 2019-09-22 + Apple Podcasts History genre-page captures
   (2020-04/2020-12/2021-06/2021-12). Declared frame deviation stands as
   documented in frame/FRAME.md.
3. **MBMBaM primary host: JUSTIN McELROY.** Applies to E1 (one host per
   show), WS3 voice enrollment, and all host-level pilot measures for P3.
   Enrollment spans to be drafted from his show-opening monologues once
   MBMBaM transcripts land, transcript-verified as with other hosts.
4. **EconTalk courtesy email: DECLINED.** Pilot proceeds under the
   TOS_NOTES.md posture (transient copies, delete after extraction,
   counts-only release) with no publisher contact.

Slate ratification (2026-07-28) predates this log: P1 Lex Fridman /
P2 EconTalk / P3 MBMBaM, ratified by PI in-session.
