# WS4 — ASR Bias Check (V1): Ground-Truth Sourcing

Status: SOURCED 2026-07-28. Implementation next.

**Source:** EconTalk episode pages (econtalk.org) publish human-made
transcripts with speaker names and timestamps, verified present and verbatim-
formatted for both eras (checked: Hirschfeld 2019-05, Cowen 2024-11 — both
open with labeled speaker turns + timestamps).

**Plan:**
- Corpus: the 16 sampled EconTalk episodes (8 per era, ~20+ h total) —
  exceeds the ≥10 h / ≥4 h-per-era gate requirement. All are already in the
  pilot audio sample with Whisper transcripts being produced (medium/int8).
- Fetch each episode's transcript HTML; parse to (speaker, time, text).
- Alignment: token-level alignment (difflib/rapidfuzz anchor alignment on
  normalized tokens) between human transcript and Whisper output; compute
  insertion AND deletion rates separately for fingerprint-candidate and
  placebo-candidate word lists (word lists from PROTOCOL §5.1/§5.4).
- Gate: insertions <1/100k words; no material fingerprint-vs-placebo asymmetry.

**Declared caveats:**
1. Human transcripts may be lightly copy-edited (disfluencies removed) —
   PI spot-verification of sampled segments against audio (~1 h, per
   PILOT_PLAN §3) decides whether they count as verbatim; deletions measured
   against edited text are an upper bound.
2. Single-show ground truth (one voice/mic/register per era) — declared
   limitation for V1 generality; Appendix C notes the full study should add a
   second source (broadcast archives).
3. ToS: transcripts are openly published web pages; fetched for alignment
   only, not redistributed.
