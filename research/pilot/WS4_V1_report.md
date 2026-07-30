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

- **Insertions <1/100k for fingerprint words: PASS** (0 observed in 176k;
  binomial 95% upper bound ≈ 1.7/100k — below the placebo's observed 1.13
  ins/100k in any case, so no adverse asymmetry).
- **No material fingerprint-vs-placebo asymmetry: PASS in the direction that
  matters** — ASR does not invent fingerprint words more readily than other
  words. Caveat, declared: fingerprint words are so rare in conversational
  speech (2 occurrences in 176k words) that deletion-side asymmetry is
  occurrence-starved; the deletion gate is effectively assessed on the
  placebo side (10.2/100k), which is dominated by era-2 pairs where the
  human transcripts appear more heavily copy-edited (an upper bound, not an
  ASR error rate). PI spot-verification (~1h, planned) adjudicates.

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
