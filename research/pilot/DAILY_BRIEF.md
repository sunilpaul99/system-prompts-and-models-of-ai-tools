# Daily Brief — Pilot Study

_Maintained per PROTOCOL §10. Latest cycle at top._

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
