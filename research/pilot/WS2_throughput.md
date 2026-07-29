# WS2 — Transcription Setup & Throughput

Environment: remote session container, **4 CPU cores, no GPU**, 15 GB RAM.
Stack: **faster-whisper 1.2.1** (CTranslate2), compute_type=int8,
vad_filter=on, word_timestamps=on.

**PINNED CONFIG (V2-validated 2026-07-29):**
`faster-whisper-1.2.1/medium/int8/threads1/temp0/beam5` — cpu_threads=1,
temperature=[0.0], beam_size=5, OMP_NUM_THREADS=1. Rationale: CTranslate2
multithreaded inference is nondeterministic (float reduction order) and
under load DROPS 7-96% of content; single-threaded decode reproduces counts
to 0.39% (97.3% token agreement) at full-episode scale and recovers content
the multithreaded runs lost. Throughput recovered by running 4 parallel
single-threaded workers (~1.2x aggregate realtime). Full V2 history in
DAILY_BRIEF cycles 13b-16.

## Measured throughput (10-min slice, EconTalk 2019-05-20)

| Model (int8, 4 threads) | Speed vs realtime | Pilot 79 h (wall) | Full study 1,750 h (wall) |
|---|---|---|---|
| small | 1.72× | ~46 h | ~1,020 h |
| medium | 0.85× | ~93 h | ~2,060 h |
| large-v3 | 0.49× | ~161 h | ~3,570 h |

## Decisions and implications

- **Pilot:** bulk transcription of the 48-episode sample launched with
  **medium/int8** (idempotent job; skips completed episodes so loop cycles can
  relaunch after container recycling). ~4 days wall-clock expected.
- **Model-choice logic:** medium chosen as working candidate — small's accuracy
  on low-frequency fingerprint words (delve, multifaceted, …) is the V1 risk;
  large-v3 likely <0.5× realtime on this hardware (infeasible for pilot
  wall-clock). WS4/V1 measures insertion/deletion rates on medium; if it fails
  the gate, options are large-v3 + more compute, or API fallback.
- **Full study (WS8 memo input):** local transcription in THIS container is
  infeasible (~2,000 wall-hours). Options to price in WS8: (a) GPU machine
  (large-v3 runs ~10-20× realtime on a consumer GPU → ~4-8 days), (b) batch
  ASR APIs — OpenAI whisper-1 at $0.006/min ≈ $630 for 1,750 h (EXCEEDS the
  $400 cap), Groq large-v3-turbo ≈ $0.04/h-audio ≈ $70 (fits), (c) multiple
  parallel cloud sessions. Decision deferred to WS8 feasibility memo.
- HF_TOKEN not set — model downloads worked unauthenticated; note for
  reproducibility that model weights come from HuggingFace (Systran/faster-whisper-*).
