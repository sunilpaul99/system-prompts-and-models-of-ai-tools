# Daily Brief — Pilot Study

_Maintained per PROTOCOL §10. Latest cycle at top._

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
