# Technical Pilot Plan

Companion to `PROTOCOL.md` v0.3. The pilot's job: prove the pipeline end-to-end on 3 hosts, populate Appendix A, run validity checks V1/V3 and validation gates G1/G2, produce the inputs for the §8.2 power simulation, and price the full study accurately. Everything here is pre-freeze: findings feed protocol revisions, and that's the point.

**Duration target:** 2–3 weeks. **Spend cap for pilot:** $75 of the $400 total.

---

## 0. Pilot host selection (and a blinding rule)

Three hosts chosen to stress different pipeline conditions, NOT sampled from the study frame:

- **P1:** a technology-adjacent interview show (long episodes, 2 speakers, likely AI mentions — stresses sense-filtering and meta-mention rules).
- **P2:** a non-tech interview show, e.g. history or culture (stresses genre generality).
- **P3:** a co-host banter/panel show, 3+ speakers (stresses diarization hardest).

Each must have episodes retrievable from 2019 and from 2024–2025 (era contrast for V1/G1 sampling). Candidates are proposed by the agent with feed-health evidence; PI picks the three.

**Blinding rule:** pilot hosts are permanently excluded from the confirmatory panel — the pilot necessarily looks at their feature data before exposure classification, which would break the §2 blinding order.

## 1. Workstreams

### WS1 — Corpus access (agent)
Resolve RSS/archive feeds for P1–P3; enumerate all episodes with dates/durations; download a stratified sample: 8 episodes per host per era-block (2019–2021, 2023–2025) ≈ 48 episodes ≈ 50–70 hours. Log every failure mode encountered (dead feeds, CDN blocks, re-uploads, ad-injected copies) — these become the Phase 4 handling rules. Record per-source terms-of-service notes (§9).

**Output:** episode manifest + failure-mode catalog.

### WS2 — Transcription (agent)
Stand up local Whisper (pin one model version; record it in Appendix A). Benchmark: hours of audio per hour of compute in this environment; decide local-vs-API for the full study from measured throughput, not guesses. Transcribe all WS1 audio.

**Output:** transcripts; throughput/cost table; pinned version string.

### WS3 — Diarization + host attribution (agent, PI audits)
Speaker diarization on all WS1 episodes; host voice enrollment from 3 reference episodes per host. Compute host-attributed word share per episode. **V3 audit:** agent selects 24 stratified segments (host × era × format), PI labels speaker identity for ~2 minutes each against pipeline output; attribution accuracy target ≥90%. P3 (multi-speaker) is the expected failure point — if it fails there, the fix options (interview-only panel; better diarizer) go to the decision queue.

**Output:** V3 accuracy table; go/no-go on multi-speaker formats.

### WS4 — ASR bias check V1 (agent, PI spot-verifies)
Locate conversational audio with trustworthy verbatim transcripts in BOTH eras (candidates: shows publishing human-made transcripts; broadcast interview archives; the pilot's own audio with PI hand-verification of sampled segments). Target ≥10 hours total, ≥4 per era. Measure Whisper insertion AND deletion rates separately for fingerprint-candidate words and placebo-candidate words. Gate: insertions <1/100k words, no material fingerprint-vs-placebo asymmetry.

**Output:** V1 report. Fail → try alternate transcriber before any protocol surgery.

### WS5 — Lexical battery construction (agent, PI ratifies)
For each §5.1 candidate word: (a) pre-2022 trend in spoken references (COCA-spoken, subtitle corpora, any accessible podcast-era corpus — document what was actually usable); (b) LLM-vs-human overrepresentation check in speech-register text (generate matched-topic LLM text, compare); (c) ASR stability from WS4; (d) draft sense-disambiguation rules for ambiguous words, validated on 100 pilot-corpus instances each. Same matching table for placebo candidates. Run the full counting pipeline on the pilot corpus, including the meta-mention flagger (P1 will exercise it).

**Output:** draft Appendix A word tables with per-gate pass/fail; baseline rate estimates per host-period (feeds WS7).

### WS6 — Relational battery build + gates G1/G2 (agent builds, PI labels)
1. Agent drafts Stage 1 (screening) and Stage 2 (labeling) prompts; freezes annotation model version; implements metadata stripping.
2. Stage 1 runs over the pilot corpus → candidate disagreement windows.
3. **Gold sample construction:** 300 windows for G1 (stratified era × host, mixing Stage-1 positives and random negatives so recall is measurable), 200 host disagreement turns for G2. Agent prepares a labeling sheet with context, stripped of dates/show names, randomized order.
4. **PI labels** (and second rater if recruited — decide by end of week 1). Budget ~6–8 hours of PI time. Rubric written before labeling starts; first 30 items double-labeled by PI and agent-prompt for rubric debugging, then discarded from the gold set.
5. Compute G1 (precision/recall ≥0.75) and G2 (κ ≥0.70 for R2/R5). One round of prompt/rule revision allowed on a held-out split, per §5.2.4.
6. Measure the sparsity number that decides H1-R's fate: disagreement turns per host-period at 5-episode sampling.

**Output:** G1/G2 results; frozen prompts (draft Appendix A); disagreement-density estimates (feeds WS7).

### WS7 — Power simulation §8.2 (agent, PI reviews)
Simulation using WS5/WS6 estimates: baseline rates, host heterogeneity (3 hosts is thin — inflate variance conservatively and say so), serial correlation, words and disagreement-turns per period. Report minimum detectable rate ratio per family at n=24 and n=18. Committed as runnable code.

**Output:** power memo. Detectable RR >2.0 in a family → design revision options to the decision queue.

### WS8 — Feasibility & cost report (agent)
Manifest-based projection for the full study: eligible-episode availability, storage, wall-clock, external spend vs. the $400 cap, expected decision-queue volume per week (measured from the pilot's own queue), and the Phase 4 handling rules derived from WS1's failure catalog.

**Output:** one-page feasibility memo + recommended Phase 4 parameters.

## 2. Sequencing

Week 1: WS1 → WS2 → WS3 start; WS6 prompt drafting in parallel; second-rater decision.
Week 2: WS4, WS5, WS6 gold labeling (PI's main time commitment), V3 audit (PI, ~1 hour).
Week 3: WS7, WS8; protocol amendments drafted; exit review.

Daily cadence per §10 of the protocol starts on day 1: scorecard, coverage, decision queue, spend.

## 3. PI time budget

- Pick pilot hosts from agent's shortlist: 15 min
- V3 diarization audit: ~1 hour
- WS4 spot-verification: ~1 hour
- G1/G2 gold labeling: 6–8 hours (the big one; can split across days)
- Ratify Appendix A word gates + prompts: ~1 hour
- Exit review: ~1 hour

Total ≈ 10–12 hours across 3 weeks.

## 4. Exit criteria (pilot → Phase 3)

The pilot ends with an **exit review** producing one of:

- **PROCEED:** V1 passed; V3 ≥90% on at least interview formats; G1/G2 outcome known (pass → H1-R stands; fail after one revision → relational family demoted per §5.2.4); both power gates resolved (≤2.0 or design revised); feasibility within budget. → Amend protocol with pilot-derived values, populate Appendices A/B, freeze, begin Phase 3.
- **REVISE & RERUN:** a fixable gate failure (e.g., swap transcriber, drop multi-speaker formats) → targeted re-run of the affected workstream only.
- **STOP:** pipeline fundamentally infeasible within budget — written up honestly as a feasibility finding.

Every gate result and revision lands in the protocol changelog before freeze.
