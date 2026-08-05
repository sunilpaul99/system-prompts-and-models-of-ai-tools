# V3 Audit — how to run it (PI instructions)

Companion to `V3_AUDIT_SHEET.md`. Everything you need is in the packet
`v3_audit_packet.zip`: 20 mp3 clips, a CSV to fill in, and this file.

**Time:** ~40 minutes for the listening, ~10 for the notes. One sitting is
better than two — your calibration for "how much is the host talking"
drifts between sessions.

## What you are checking

The pipeline decides, word by word, whether the HOST or the GUEST said it.
Every downstream count depends on that being right, because the rate we
measure is fingerprint-words *per host word* — if guest speech leaks into
the host's column, the denominator is wrong and so is the rate.

You are not transcribing and you are not judging content. You are the
ground truth for one question: **how much of this clip is the host?**

## Procedure

1. Unzip the packet. Play `clips/A01.mp3` … `A20.mp3` in order.
2. Each clip is exactly 2 minutes, taken from the middle of an episode
   (the first 120 s of every episode is skipped, because intros and
   sponsor reads are host-solo and would flatter the pipeline).
3. For each clip fill one row of `audit_labels.csv`:

   | column | what to put |
   |---|---|
   | `host_pct` | your estimate of the host's share of the *talking*, 0–100. Eyeball it; nearest 10 is fine, nearest 5 if it's close. |
   | `who_dominates` | `HOST`, `GUEST`, or `EVEN`. Use `EVEN` for roughly 40–60. |
   | `third_voice` | `Y` if you hear anyone who is neither host nor guest — audience, a producer, a clip being played, a co-host. Otherwise `N`. |
   | `notes` | anything odd: music, ad read, heavy crosstalk, phone-quality audio, long silence. |

   The host is named per row in the CSV — Lex Fridman for the Lex clips,
   Russ Roberts for EconTalk. If you can't tell which voice is the host,
   write that in `notes` rather than guessing; "indistinguishable" is a
   real and useful finding.

4. Send me the filled CSV. I score it against the pipeline's answers.

## The one rule that matters

**Do not open `answer_key.json` before you finish.** It contains the
pipeline's labels. This audit is only worth running blind — if you've seen
the machine's answer, your estimate stops being independent evidence and
the gate becomes unfalsifiable. The key stays in the session scratchpad,
not in the packet, for exactly that reason.

Same reason you shouldn't try to guess which clips are the "suspicious"
ones. Two of the twenty are episodes an automated QA rule flagged as
implausible, and they're unmarked deliberately. Your blind labels on those
two are what settle whether they get excluded from the analysis — a
decision I'm not allowed to make for you (PROTOCOL §10).

You also don't know the hypothesis-relevant grouping here, and that's
fine: era (2019–21 vs 2023–25) is in the CSV only so I can check that
accuracy doesn't differ systematically between the two. Don't let it
influence your listening.

## What happens with your numbers

- **Gate:** host-attribution accuracy ≥90% (PILOT_PLAN WS3). I compute it
  by comparing your `host_pct` against the pipeline's host share on the
  same window, clip by clip.
- **Pass** → V3 clears, and the diarized corpus is validated for analysis.
- **Fail** → diarization is not fit for purpose and the pilot reports that
  as its finding. That is a real possible outcome, not a failure of yours.
- **The two flagged clips** → if you hear a normal two-person conversation
  where the pipeline claims ~99.9% host, they're excluded and I record the
  exclusion in `DECISIONS.md` with your labels as the basis.

## If something goes wrong

- A clip won't play → tell me the ID, I'll re-cut it.
- A clip is mostly music or an ad → label it anyway and note it; I'll
  decide whether to drop it from the denominator (and say so explicitly).
- You want to stop halfway → partial is usable. 12 clips gives a usable
  accuracy estimate, just a wider interval. Send what you have.
