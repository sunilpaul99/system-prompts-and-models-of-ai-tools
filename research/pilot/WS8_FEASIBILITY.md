# WS8 — Feasibility & Cost Memo (full study)

Status: DRAFT, 2026-08-03. All figures are **measured in the pilot**, not
estimated from documentation. Pending inputs are marked. Companion to
PILOT_PLAN WS8 and PROTOCOL §8.3 (the handoff deliverable).

---

## 1. Verdict in one paragraph

A full study of 24 hosts × 15 half-year periods × 5 episodes (~1,800
episodes, ~1,500–2,000 audio-hours) is **feasible within the $400 external
cap, but not on CPU-only infrastructure**. Transcription and diarization
are the binding constraints, and both are ~1× realtime per worker on
4 CPU cores — roughly 3,600 worker-hours for the full corpus. One consumer
GPU collapses that to days. The analysis pipeline itself (counting,
alignment, turn reconstruction) is trivial by comparison. The costed
recommendation is: **one GPU machine + a Haiku-class annotator ≈ $93
external spend**, leaving ~75% of the cap unspent.

## 2. What the pilot actually measured

| Stage | Measured throughput | Full-study projection |
|---|---|---|
| Feed/manifest | 6 feeds, seconds | negligible |
| Audio download | 48/48 episodes, 3.9 GB, ~15 min | ~150 GB, ~10 h |
| Transcription (CPU, medium/int8, 1 thread) | ~1.0× realtime/worker | ~1,750 worker-hours |
| Transcription (CPU, 4 threads) | 0.85× realtime — **and nondeterministic** | unusable (see §3) |
| Diarization ECAPA (CPU) | ~20–40 min/episode | ~900 h |
| Diarization pyannote (CPU) | ~1× realtime | ~1,750 h |
| Counting / alignment / turns | seconds per episode | < 1 h total |
| Annotation (Stage 1+2) | 43k input tokens/episode | ~93M tokens |

Storage: 3.9 GB audio for 48 episodes → ~150 GB for 1,800, but audio is
deleted after feature extraction (§9), so **peak** storage governs, not
total: ~10 GB with a rolling delete.

## 3. Non-obvious findings that change how Phase 4 must be built

These are the pilot's real value; each cost days to discover.

1. **CTranslate2 multithreading is nondeterministic AND lossy under load.**
   Multi-threaded decode dropped 7–96% of content depending on machine
   load, silently. Single-threaded decode reproduces word counts to 0.39%.
   *Rule: pin `cpu_threads=1`, run N single-threaded workers for
   throughput.* A study that transcribes on shared machines without this
   bakes load-correlated measurement error into every count.
2. **Determinism removes Whisper's loop-breaker.** `temperature=[0.0]`
   eliminates the fallback ladder that escapes repetition loops; two
   chunks (of ~210) burned 227 CPU-minutes each before a hard timeout.
   *Rule: per-chunk subprocess timeout at ~3× realtime, retry with
   `condition_on_previous_text=False`, and FLAG those chunks so they can
   be excluded in sensitivity analysis.* In-process guards do not work —
   the loop stalls inside a single decode call.
3. **Work-unit duration must be « infrastructure restart interval.** This
   environment restarted ~25 times in 6 days (2–10 h windows). Episode-level
   units could not complete for 3–4 h episodes. *Rule: chunk at ~25 min,
   checkpoint atomically per chunk, reconcile claims at launch.*
4. **Persist expensive compute at the boundary where it is produced.** A
   2 h diarization run was discarded by a downstream parse bug. *Rule:
   cache the raw model output immediately, before any post-processing.*
5. **Completion checks must count outputs, not process exits.** A worker
   pool that OOM-died still reported success, claiming a complete corpus
   at 14/48.
6. **Memory, not CPU, caps parallelism.** Each worker holds the model plus
   a decoded-audio buffer; a 4 h episode is ~1.8 GB. *Rule: workers =
   RAM / (model + longest-episode buffer), and cache audio per worker,
   not per chunk.*
7. **Co-host/panel formats are not diarizable with current tooling** (see
   DECISIONS.md 2026-08-03). Eligibility must exclude them, or the study
   must budget per-speaker enrollment of every co-host.
8. **Publisher sites rate-limit far below CDN thresholds.** Transcript
   fetching tripped a 403 at 6 s spacing; 45 s worked. *Rule: fetch once,
   slowly, and cache raw HTML so parser fixes never re-hit the network.*

## 4. Recommended Phase 4 configuration

- **Compute**: one GPU machine (consumer-grade suffices). Whisper
  large-v3 runs ~10–20× realtime and pyannote ~20–50× realtime there,
  turning ~3,600 CPU-hours into a few days. If GPU is unavailable, the
  CPU path works but needs ~4–6 weeks of wall-clock with N parallel
  single-threaded workers, which the restart-resilience rules above make
  survivable.
- **Transcription**: pin the full config string, including chunking:
  `faster-whisper/<model>/int8/threads1/temp0/beam5/chunk1500`. Re-run V2
  after any change to model, threads, or chunk size — all three alter output.
- **Diarization**: ECAPA + enrollment for two-voice formats (validated
  within ~2pp against human transcripts); do not attempt co-host formats.
- **Annotation**: validate on a Sonnet-class model, then re-validate a
  Haiku-class model on the same gold sample; commit the full study to the
  cheaper one if it clears κ≥0.70. Cost $93 vs $280.
- **QA gates that must be automated** (each caught a real failure here):
  V2 reproducibility probe per batch; implausible-host-share detector;
  loop-guard flags surfaced in the analysis dataset.

## 5. Budget against the $400 cap

| Item | Cost |
|---|---|
| Transcription (local, GPU or CPU) | $0 |
| Diarization (local) | $0 |
| Annotation, Haiku-class | $93 |
| Annotation, Sonnet-class (alternative) | $280 |
| GPU rental, if not owned (~$0.5/h × ~100 h) | ~$50 |
| **Recommended total** | **~$95–145** |

Comfortably inside the cap. The binding constraint on this study is
**PI/rater time and wall-clock**, not money.

## 6. Expected decision-queue volume

Measured from this pilot's own queue: ~1 PI decision per 8–10 agent
cycles, clustered at methodological forks (slate ratification, frame
substitution, multi-speaker fallback, model pin). Phase 4 should assume
**2–4 PI decisions per week**, each needing 5–30 minutes, plus the
scheduled labelling blocks (V3 audit ~1 h; WS4 spot-check ~1 h; G1/G2 gold
6–8 h).

## 7. Open items before this memo is final

- V3 audit result (PI, ready now) → attribution accuracy number.
- G1/G2 gates → whether the relational family survives, and its power.
- Stage-1 flag rate → replaces the 15% assumption in the token estimate.
