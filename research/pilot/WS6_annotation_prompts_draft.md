# WS6 — Relational Battery Annotation Prompts (DRAFT for Appendix A)

Status: DRAFT v1, 2026-07-28. Freezes into Appendix A only after G1/G2
validation. Annotation model: to be pinned at freeze — recommendation to PI:
a fixed-snapshot small model (cost: two passes over ~1,800 transcripts must fit
inside the $400 cap; estimate in WS8 once token volumes are measured on the
pilot corpus). Temperature 0; JSON-schema-constrained output.

## Metadata stripping (PROTOCOL §5.2.3)

Annotation input contains ONLY: speaker roles (HOST / GUEST / OTHER), turn
index, and turn text. Stripped before the annotation context: dates, show
name, episode title/number, guest name (replaced with GUEST), any URLs, and
any sponsor-read spans. Stripping is mechanical (from the diarized transcript
JSON), implemented in the pipeline, and verified by a 20-transcript audit.

## Stage 1 — screening (recall-tuned)

System prompt (draft):

> You screen podcast transcript windows for possible disagreement between
> HOST and GUEST. A candidate is ANY span where GUEST states a position,
> preference, or judgment and HOST's response could be read as expressing a
> different position — even partially, even politely, even if softened to
> near-invisibility. When in doubt, flag it: false positives are acceptable;
> misses are not.
> Not candidates: pure factual Q&A, HOST asking devil's-advocate questions
> explicitly labeled as such, topic changes, backchannels ("right", "mm-hmm"),
> and disagreements about scheduling/logistics of the show itself.
> Input: numbered turns, roles HOST/GUEST/OTHER. Output JSON:
> `{"windows": [{"start_turn": int, "end_turn": int, "guest_stance_turn": int,
> "host_response_turns": [int], "confidence": "high|medium|low"}]}`
> Include low-confidence windows.

Windowing: 30-turn sliding windows, 10-turn overlap; windows merged on overlap.

## Stage 2 — episode confirmation + turn labeling

System prompt (draft):

> You are annotating a candidate disagreement episode between HOST and GUEST.
> Step 1 — CONFIRM: is this a genuine disagreement episode? HOST's turn(s)
> must express a contrary or partially contrary stance on the same proposition
> GUEST advanced. Exclude: trivia/factual-lookup conflicts; scripted debate
> formats; exchanges whose TOPIC is AI language or chatbots (set
> `ai_topic_flag` instead of excluding, with the span).
> Step 2 — for EACH host disagreement turn, label:
> - `concessive_preface` (R2): does the turn OPEN with an explicit
>   validation/agreement token before the contrary stance? (e.g. "That's a
>   great point, and…", "I hear you, but…", "Totally fair — though…").
>   The token must precede the disagreement content. Mid-turn concessions
>   do not count.
> - `hedge_tokens` (R3): list epistemic hedges present ("I think", "maybe",
>   "sort of", "it could be argued", "to some extent", "kind of", "perhaps",
>   "arguably", "in some ways").
> - `both_sides` (R4): does the turn present balanced dual framing without
>   committing? ("there's merit on both sides", "it depends how you look at
>   it" as the turn's resolution).
> - `bald_directness` (R5): does the turn contain unmitigated contradiction
>   ("No.", "I disagree", "That's wrong", "Not true") NOT softened within the
>   same sentence?
> Output JSON: `{"confirmed": bool, "exclusion_reason": str|null,
> "ai_topic_flag": bool, "host_turns": [{"turn": int,
> "concessive_preface": bool, "preface_text": str|null,
> "hedge_tokens": [str], "both_sides": bool, "bald_directness": bool}]}`

## Rule-based backstops (PROTOCOL §5.2.3)

R3 hedge lexicon and R5 contradiction lexicon are ALSO counted by plain
regex over host disagreement turns, reported alongside LLM labels — a drift
detector for the annotator. Lexicons frozen in Appendix A.

## Open items before G1/G2

1. Pin annotation model + snapshot (PI ratifies; cost estimate from pilot corpus).
2. Gold-sample construction (300 windows G1, 200 turns G2) after WS3
   diarization produces role-attributed transcripts.
3. Concessive-token lexicon: seeded from R2 examples above; expanded from
   pilot-corpus concordance BEFORE gold labeling (so the rubric, not the
   annotator, defines the boundary).
4. PI labeling sheet generator (randomized order, stripped context) — build
   after gold-sample draw.
