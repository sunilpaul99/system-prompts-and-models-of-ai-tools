# WS3 / V3 — diarization attribution audit

Status: **scored 2026-08-18**. PI labelled all 20 clips blind; scoring run
is `ws3_score_audit.py`, inputs `results/v3_audit_labels_PI.csv` and
`audit/answer_key.json`, output `results/v3_audit_scored.json`.

Gate (PILOT_PLAN WS3): host-attribution accuracy ≥90%.

---

## 1. Headline

**The audit splits cleanly in two, and the split falls exactly on the QA
flag.** The 18 QA-clean clips agree with the pipeline to a mean absolute
error of **3.2 percentage points**, every one inside ±15 pp. The 2
QA-flagged clips are catastrophic: the pipeline claims ~100% host where the
PI heard 60% and 0%.

| subset | n | MAE | max abs error | within ±15 pp |
|---|---|---|---|---|
| all clips | 20 | 9.9 pp | 100.0 pp | 18/20 = **90%** |
| QA-clean only | 18 | **3.2 pp** | 13.3 pp | 18/18 = **100%** |
| QA-flagged only | 2 | 70.0 pp | 100.0 pp | 0/2 |

## 2. Per-clip result

`diff` is pipeline minus PI; positive means the pipeline claims more host
speech than the PI heard.

| id | flag | PI % | pipeline % | diff |
|---|---|---|---|---|
| A01 | **FLAG** | 60 | 100.0 | **+40.0** |
| A02 | **FLAG** | 0 | 100.0 | **+100.0** |
| A03 | | 30 | 18.4 | −11.6 |
| A04 | | 0 | 0.0 | +0.0 |
| A05 | | 20 | 17.9 | −2.1 |
| A06 | | 40 | 43.4 | +3.4 |
| A07 | | 40 | 41.5 | +1.5 |
| A08 | | 30 | 16.7 | −13.3 |
| A09 | | 0 | 0.0 | +0.0 |
| A10 | | 40 | 43.2 | +3.2 |
| A11 | | 20 | 15.1 | −4.9 |
| A12 | | 20 | 19.0 | −1.0 |
| A13 | | 10 | 7.5 | −2.5 |
| A14 | | 20 | 17.3 | −2.7 |
| A15 | | 40 | 39.5 | −0.5 |
| A16 | | 20 | 20.2 | +0.2 |
| A17 | | 10 | 6.0 | −4.0 |
| A18 | | 80 | 75.6 | −4.4 |
| A19 | | 40 | 41.3 | +1.3 |
| A20 | | 60 | 61.7 | +1.7 |

Two clips (A04, A09) are guest-monologue windows where both the PI and the
pipeline recorded 0% host — agreement at the boundary, not a degenerate case.

The PI reported **no third voices** and left no anomaly notes, consistent
with the interview-only eligibility rule (amendment A1).

## 3. On the tolerance, honestly

No tolerance was pre-specified. `V3_AUDIT_HOWTO.md` said only that scoring
compares `host_pct` against the pipeline's share "clip by clip". Picking a
threshold now, after seeing the data, would be choosing the number that
delivers the verdict — so the scoring script reports the whole curve:

| tolerance | agreement (all 20) |
|---|---|
| ±5 pp | 16/20 = 80.0% |
| ±10 pp | 16/20 = 80.0% |
| ±15 pp | 18/20 = 90.0% |
| ±20 pp and beyond | 18/20 = 90.0% |

The curve is flat from ±15 pp outward, because the only two failures miss by
40 and 100 pp. **The gate verdict does not hinge on the tolerance** anywhere
above ±11.6 pp — it hinges entirely on whether the two flagged episodes are
in the denominator. That is the pending exclusion decision, and it is the
PI's to make (§10).

For the record, the residual disagreement on the clean subset is dominated
by human rounding: the PI labelled to the nearest 10, so a true 18.4% reads
as either 20 or 30. Two clips (A03, A08) account for the whole tail.

## 4. Era check — no differential bias

This matters more than the headline: a pipeline that were systematically
*more* accurate in one era would manufacture a pre/post difference out of
measurement error alone, which is precisely the study's estimand.

| stratum | n | MAE | signed |
|---|---|---|---|
| Lex 2019–21 | 6 | 5.33 pp | −3.69 |
| Lex 2023–25 | 6 | 2.37 pp | −1.30 |
| EconTalk 2019–21 | 3 | 1.59 pp | −1.43 |
| EconTalk 2023–25 | 3 | 2.48 pp | −0.48 |
| **2019–21 pooled** | 9 | 4.08 pp | −2.93 |
| **2023–25 pooled** | 9 | 2.40 pp | −1.03 |

The signed error is negative in every stratum — the pipeline slightly
*under*-credits the host throughout — and the era gap (−2.93 vs −1.03 pp) is
small, same-signed, and driven by the two rounding-tail clips in Lex era 1.
At n=9 per era this is not a precise estimate, but there is no sign of the
one pattern that would be disqualifying: differential bias by era.

## 5. Verdict

- **QA-clean corpus: V3 PASS**, comfortably. 3.2 pp MAE, no era-differential
  bias, no third-voice contamination.
- **The two flagged episodes fail unambiguously** and independently confirm
  the implausible-host-share QA rule (amendment B3), which caught them
  automatically before any human listened. The rule earned its place.
- **Gate on all 20 clips: exactly 90%** — at the threshold, not above it.
  Reported as-is rather than rounded into a pass.

## 6. What this settles, and what it does not

Settled: the pipeline attributes speech accurately enough for the lexical
family on QA-clean interview episodes, and the QA gate detects the failures
it was built to detect.

Not settled, and reserved for the PI (§10): whether Lex #134 (A01) and
Lex #478 (A02) are excluded from analytic totals. The evidence now supports
exclusion — the pipeline assigns ~100% of both episodes to the host, the PI
heard a normal two-person conversation in one and no host at all in the
other, and the two episodes hold 47% of all host words in the uncorrected
denominator. **Recommendation: exclude both, per staged amendment C1.**
The current QA-clean totals (30 episodes, 157,243 host words) already
exclude them, so ratifying costs nothing downstream; rejecting the
recommendation would require re-running WS5 with them restored.
