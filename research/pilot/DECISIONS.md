# PI Decision Log

Per PROTOCOL §10: every queued decision, its resolution, date, and where it
took effect. Latest first.

## 2026-08-02 — multi-speaker diarization (V3 structural failure)

**PI decision: option (b) — adopt pyannote/speaker-diarization-3.1.**
Context: ECAPA+agglomerative clustering pools the three McElroy brothers
into one speaker (DAILY_BRIEF cycle 59); interview formats unaffected.
Implementation staged this cycle (ws3_diarize_pyannote.py): pyannote
supplies speaker turns; host identification still uses the ECAPA
enrollment centroid, so enrollment_spans.json and the interview-format
path stay authoritative; output schema unchanged so WS5/WS6 consume it
unmodified. PI has accepted the model terms on Hugging Face
(2026-08-02). **Remaining: an HF read token in the session environment**
(website acceptance alone yields 401). Token is a credential: stored
outside the repo, never committed, never logged.
Fallbacks if pyannote underperforms on sibling voices: (c) declare
multi-speaker NOT MEASURABLE and restrict the full-study panel to
interview formats at freeze.

## 2026-07-29 — batch resolution (PI, in-session)

1. **Second rater: RESOLVED.** PI's adult children (25, blind to the
   hypotheses) will be asked first; PI's wife is the fallback. Applies to
   both roles: G1/G2 gold labeling (~6-8h, week 2) and exposure-label
   ratification (Phase 3). Rater independence rule recorded: no discussion
   of hypotheses or of the PI's own labels during rating; disagreements
   resolve to UNKNOWN (exposure) / excluded (gold). Rater identity is
   recorded here but reported in the write-up only as "one independent
   second rater (family member, blind to hypotheses)" with the relationship
   declared as a limitation.
2. **History-genre frame substitution: ACCEPTED.** The §3.1 History cell
   uses Chartable 2019-09-22 + Apple Podcasts History genre-page captures
   (2020-04/2020-12/2021-06/2021-12). Declared frame deviation stands as
   documented in frame/FRAME.md.
3. **MBMBaM primary host: JUSTIN McELROY.** Applies to E1 (one host per
   show), WS3 voice enrollment, and all host-level pilot measures for P3.
   Enrollment spans to be drafted from his show-opening monologues once
   MBMBaM transcripts land, transcript-verified as with other hosts.
4. **EconTalk courtesy email: DECLINED.** Pilot proceeds under the
   TOS_NOTES.md posture (transient copies, delete after extraction,
   counts-only release) with no publisher contact.

Slate ratification (2026-07-28) predates this log: P1 Lex Fridman /
P2 EconTalk / P3 MBMBaM, ratified by PI in-session.
