# WS4 — V1 ASR Bias Report (EconTalk block complete)

Date: 2026-07-30 (SUPERSEDES 2026-07-29 run — deterministic corpus). Corpus: all 16 sampled EconTalk episodes, both eras
(8 × 2019-2021, 8 × 2023-2025), 177,898 aligned human-transcript words.
Transcriber: faster-whisper-1.2.1/medium/int8/threads1/temp0/beam5/chunk1500 (V2-validated pinned config).
Method: ws4_align.py — token alignment vs verbatim human transcripts;
insertions/deletions counted inside the aligned overlap only.

## Results

| List | Genuine occurrences (matched) | Insertions | Deletions | Ins/100k | Del/100k |
|---|---|---|---|---|---|
| Fingerprint (§5.1 candidates) | 2 | **0** | **0** | **0.00** | 0.00 |
| Placebo (provisional) | 71 | 2 | 2 | 1.12 | 1.12 |

## Gate assessment (§6.1)

- **Insertions <1/100k for fingerprint words: PASS** (0 observed in 178k;
  binomial 95% upper bound ≈ 1.7/100k; placebo insertions 1.12/100k — no
  adverse asymmetry).
- **No material fingerprint-vs-placebo asymmetry: PASS** — and on the
  deterministic corpus the placebo side is symmetric (ins 1.12 = del 1.12
  per 100k), removing the earlier deletion-side concern entirely. Remaining
  caveat, declared: fingerprint words are so rare in conversational speech
  (2 occurrences in 178k words) that fingerprint-specific deletion rates
  are occurrence-starved; the placebo side stands in for them. PI
  spot-verification (~1h) is now confirmatory rather than adjudicative.

## Era note (RESOLVED)

On the nondeterministic corpus, placebo deletions ran 10.2/100k and
concentrated in era-2 — initially hypothesized as transcript copy-editing.
On the deterministic corpus the excess vanished (1.12/100k, symmetric with
insertions, both eras): the signal was content dropped by nondeterministic
multithreaded transcription (see V2 investigation, DAILY_BRIEF cycles
13b-16b). No evidence of era-dependent ASR bias or meaningful ground-truth
editing remains.

## Baseline-rate corollary (feeds WS7)

Fingerprint composite in spontaneous speech ≈ 1.1/100k words (2/176k, both
speakers, both eras pooled) — an extremely sparse outcome. In host-attributed
speech alone: 0 occurrences in 36k words so far. The §8.2 power simulation
must model near-zero baselines.

## Residual limitations (Appendix C material)

Single-show ground truth; possible copy-editing of human transcripts
(deletion rates are upper bounds); medium model only (large-v3 not
V1-tested — infeasible wall-clock on this hardware).
