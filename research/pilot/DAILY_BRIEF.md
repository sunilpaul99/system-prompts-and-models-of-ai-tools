# Daily Brief — Pilot Study

_Maintained per PROTOCOL §10. Latest cycle at top._

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
