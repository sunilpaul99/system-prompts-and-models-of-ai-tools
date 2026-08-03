# Protocol Amendments — staged for the exit review / freeze

Per PILOT_PLAN week 3 ("protocol amendments drafted; exit review") and
PROTOCOL §10 (the protocol text is not edited mid-flight). Each item below
is a pilot-evidenced change for the PI to accept, modify, or reject at
freeze. Nothing here is applied yet.

---

## A. Eligibility (§3.2, E-rules)

**A1. Restrict to interview / two-voice conversational formats.**
*Evidence:* co-host diarization fails unrecoverably (DECISIONS.md
2026-08-03; 1/3 studio episodes correct, unpredictably, and a speaker-count
constraint made it worse). *Status:* PI-ratified 2026-08-03; needs the
protocol text updated at freeze.

**A2. Add a format screen for live/audience-recorded episodes.**
*Evidence:* the live episodes in the pilot produced 13-14 spurious speaker
clusters from audience noise. Even in two-voice shows, live recordings
should be excluded at sampling, not discovered at diarization.

## B. Pipeline configuration (§6, Appendix A)

**B1. Pin the FULL transcription config, not just the model.**
Required string: `faster-whisper-<ver>/<model>/int8/threads1/temp0/beam5/
chunk1500`. *Evidence:* thread count alone changes output by 7-96% under
load (V2 investigation, cycles 13b-16b). Model version is not sufficient
to reproduce a corpus.

**B2. Add the loop-guard rule as a declared, flagged fallback.**
A chunk exceeding ~3× realtime is killed and re-run with
`condition_on_previous_text=False`; affected chunks carry
`loopguard_no_context` and are excludable in sensitivity analysis.
*Evidence:* determinism removes Whisper's loop-breaker; 2 of ~210 chunks
looped indefinitely. *Note:* this is the one wall-clock-triggered (hence
not bit-reproducible) rule in the pipeline — declared as such.

**B3. Add an implausible-host-share QA gate.**
For two-voice formats, host share outside [0.15, 0.75] is a diarization
failure regardless of embedding similarity. *Evidence:* 2/32 interview
episodes passed the similarity gate at ~99.9% host share and held 47% of
all host words — a denominator contaminant that the existing gate could
not see (cycle 74).

## C. Analysis (§7)

**C1. Pre-specify handling of QA-failed episodes.**
The protocol currently has no rule for episodes that fail diarization QA.
Proposed: excluded from analytic totals, reported with counts, and their
host-periods marked missing rather than zero-filled (consistent with the
existing §3.4 minimum-word rule).

**C2. State the sparsity regime explicitly.**
Expected fingerprint count is ~1.9 per host-period (7.6/100k × ~25k words).
§7's Poisson-with-offset model is appropriate, but the write-up should
report absolute counts alongside rate ratios, since RR is unstable at
these counts. *Evidence:* WS7 simulation, cycle 76.

## D. Power and design (§8.2)

**D1. Record the measured minimum detectable effect.**
~RR 1.9 at n=24; ~RR 2.1 at n=18. The design passes the §8.2 gate (≤2.0)
at full size and **fails at its own n=18 floor** — the protocol should
either raise the floor to ~21 hosts or declare that dropping below 21
converts the study to descriptive.

**D2. Note that words-per-period is the binding lever.**
Power scales with host words, not host count, in this sparsity regime.
More episodes per period is the cheapest route to sensitivity.

## E. Scope and reporting

**E1. Related-work update.** Yakura et al. now includes an 824k-episode
synthetic control plus an N=496 entrainment experiment; the Science
sycophancy paper supplies H1-R's causal mechanism; a Communications
Psychology "norm leakage" piece predicts effects in BOTH directions
(softening and blunting), which bears directly on R5's predicted sign.
*Action:* §1 and §5.2 rationale need revision; R5's directional prediction
should be stated as two-sided or explicitly justified.

**E2. Report the pilot's own failures as findings.** Multi-speaker
non-measurability, transcription nondeterminism, and the QA-gate gap are
Appendix C / WS8 content, not omissions.

---

## Not amended (deliberately)

- The blinding and peeking rules (§2) — held throughout; no exposure ×
  feature contrast has been computed at any point.
- The estimand and its "association, not cause" framing (§1) — unchanged.
- The two-family co-primary structure (§5) — H1-R's fate rests on the
  G1/G2 gates, which have not run; no basis yet to amend.
