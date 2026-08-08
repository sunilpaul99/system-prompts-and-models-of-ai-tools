# Derived results — durable copies

These files were produced in the session scratchpad, which is ephemeral.
They are committed here so the pilot survives a container reclaim.

| file | what it is |
|---|---|
| `../audit/answer_key.json` | pipeline speaker labels for the 20 V3 audit windows. **Do not read before the audit is labelled** — it is the answer key. Committed only so the audit remains scorable. |
| `ws3_qa_flags.json` | per-episode host share, host-centroid similarity, cluster count, QA flags (32 interview episodes). |
| `ws4_v1_results.json` | V1 ASR-bias alignment result: 16 pairs, 177,898 aligned words, per-word insertion/deletion counts. |
| `ws5_counts.json` | WS5 lexical counts per episode: host words, status, per-family counts, and hit timestamps. |

## What is deliberately NOT here

- **Audio.** Deleted after feature extraction (PROTOCOL §9).
- **Transcripts.** These are derived from copyrighted podcast audio and the
  project holds a transient-copy posture (TOS_NOTES.md). They are not
  published; the durable copy is held privately by the PI.
- **Verbatim context snippets.** `ws5_counts.json` carried a ~150-character
  excerpt around each of the 145 hits, as reviewable evidence. Those were
  stripped for the committed copy — §9 permits counts to leave the
  pipeline, not quotations. The full version with contexts is in the PI's
  private packet, which is where hit-level review should happen.

Timestamps are retained, so any hit can be relocated in the private
transcript without the excerpt travelling with the public record.
