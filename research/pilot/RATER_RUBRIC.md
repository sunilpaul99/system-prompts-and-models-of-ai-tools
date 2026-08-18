# Gold-Sample Labeling Instructions (G1 + G2)

## Your role

You are the **human reference judge** for this study. A computer program has
read the same conversations and made its own judgments about them. We need
an independent human answer for the same items so we can measure how often
the program gets it right. **Your answers are the standard the program is
graded against** — you are not being graded, and there is no answer key you
are supposed to match.

Because of that, three ground rules:

1. **You must not know what the program said**, and you don't — nothing on
   your sheets reveals it. Please don't ask.
2. **Judge only what is on the page.** If the text doesn't show it, the
   answer is No — don't fill in what a speaker "probably meant."
3. **Work alone.** Don't discuss items or answers with anyone (including
   the PI) until a whole sheet is submitted. The first 30 rows of each
   sheet are the exception — those are practice, reviewed together.

You'll see short podcast transcript excerpts with speakers marked **HOST**
and **GUEST**. Show names, dates, and real names have been removed on
purpose; please don't try to guess or look up who is speaking. There are no
quotas — some stretches may be nearly all Yes, others nearly all No.

## Two words used throughout

- A **turn** is everything one speaker says before the other speaker talks.
  If the host speaks three sentences, the guest replies, and the host
  speaks again, that's three turns: HOST turn, GUEST turn, HOST turn.
- A **host turn** is simply a turn where the HOST is the one speaking.
  On your sheets, host turns are always in the column labeled `host_says`
  (G1) or `host_turn` (G2).

## Time budget

| | items | pace | time |
|---|---|---|---|
| G1 sheet | 300 | ~45–60 sec each | **3.5–4.5 h** |
| G2 sheet | 199 | ~60–90 sec each | **2.5–3.5 h** |
| Calibration review with PI (both sheets) | 60 | — | **~0.5–1 h** |
| **Total** | | | **≈ 7–9 hours** |

Split it across days however you like — the sheets save wherever you save
them, and the random order is intentional (don't reorder or batch by
similarity). Two asks: do each sheet's first 30 rows (the calibration
block) in **one sitting** before the review, and try to finish any sitting
at a row boundary rather than mid-item.

---

## G1 — "Is this a disagreement exchange?" (300 items)

Each row shows two boxes: `guest_says` (what the guest said) and
`host_says` (how the host responded, immediately after). Answer **one
question** about the pair:

> Does the guest state a position or judgment, and does the host then
> express a *different* position on the *same* issue — even partially,
> even politely?

**There are FOUR possible answers. Two of them are flavors of No — pick
the one that fits:**

| answer | write in the sheet | when |
|---|---|---|
| Yes | `YES` | the host pushes back on the guest's position, in any style |
| No — no conflict | `NO-noconflict` | question, agreement, summary, topic change, or filler |
| No — excluded type | `NO-excluded` | there IS a conflict, but it's about a checkable fact, or it's a scripted debate segment |
| Unsure | `UNSURE` | still torn after reading twice |

`UNSURE` exists so you never have to flip a coin — but it's for genuine
ties, not a fast lane. If more than roughly 1 item in 10 is coming out
`UNSURE`, flag it at the next check-in.

### Examples (invented, not from your sheets)

**YES — polite pushback still counts:**
> GUEST: I think remote work has basically made offices obsolete.
> HOST: That's fair for some jobs, but I keep coming back to how much
> apprenticeship happens in person. I'm not sure a junior engineer can
> learn the same way over Zoom.

The host grants something, then takes a different position on the same
issue. Style doesn't matter — soft disagreement is still `YES`.

**YES — disagreement phrased as a challenge:**
> GUEST: Markets always price in this kind of risk.
> HOST: Always? 2008 seems like a pretty big counterexample.

A pointed question that carries a contrary position counts.

**NO-noconflict — interest is not disagreement:**
> GUEST: We found the effect was twice as large in older adults.
> HOST: Fascinating. What do you think drives that difference?

The host asks a follow-up. No position of the host's own → `NO-noconflict`.

**NO-noconflict — agreement, even enthusiastic:**
> GUEST: Nobody reads the terms of service.
> HOST: Exactly, and honestly I think that's rational — life is short.

The host adds to the guest's point rather than opposing it.

**NO-excluded — factual correction, not judgment:**
> GUEST: The law passed in 2003.
> HOST: Small correction — 2005, I looked it up this morning.

There is a conflict, but it's about a checkable fact. That's the kind of
conflict this study deliberately sets aside → `NO-excluded`.

**The devil's-advocate rule:** if the host says "let me play devil's
advocate" and asks ONE contrary question, that's `NO-noconflict`. It
becomes `YES` only if the host owns the contrary position ("honestly, I
think that objection is right") or keeps pressing it over multiple turns —
in your window, judge what you can see.

---

## G2 — Four features of a host turn (199 items)

Each row shows `context_guest` (what the guest had just said — context
only, you don't judge it) and `host_turn` (one host turn — this is what
you judge). These turns were selected because the host appears to be
pushing back; you're describing **how** the pushback is worded.

Answer **four questions about the host turn**, plus notes:

### Q1 — Concessive opener (`q1`, write Y or N)

Does the turn **open** — first thing, before any pushback — by validating
or agreeing with the guest?

- **Y:** "That's a great point, and yet I wonder if…" / "I hear you.
  But here's my problem with it…"
- **N:** "I disagree — though I get why people like the idea." *(the
  agreement comes after the pushback, not first)*
- **N:** "Well, the data says otherwise." *(no validation at all)*

### Q2 — Both-sides framing (`q2`, write Y or N)

Does the turn **end up refusing to pick a side**, as its conclusion?

- **Y:** "…so honestly, I think there's merit on both sides and it depends
  on the case." *(that's where the turn lands)*
- **N:** "There are decent arguments both ways, but I come down firmly on
  the side of disclosure." *(both sides presented, then a side picked)*

### Q3 — Bald contradiction (`q3`, write Y or N)

Does the turn contain a **flat, unsoftened** contradiction anywhere in it?

- **Y:** "No. That's just not what happened."
- **Y:** "I disagree." *(as its own sentence, nothing softening it)*
- **N:** "I disagree, though I see why you'd read it that way." *(softener
  in the same sentence)*
- **N:** "I'm not sure that's right." *(hedged, so not bald)*

### Q4 — Hedges (`q4`, list them, or leave blank)

Copy into the box **every** phrase from this checklist that appears in the
host turn (list each once, comma-separated; blank = none):

> I think · maybe · sort of · kind of · perhaps · it could be argued ·
> to some extent · arguably · in some ways

Count them wherever they appear and whatever the sentence is doing — a
hedge inside a supportive sentence still counts.

### A worked example (invented)

> **context_guest:** …so in my view the acquisition was a clear success.
> **host_turn:** That's a totally fair way to frame it. But I think the
> integration was, sort of, a mess for two years — no, actually I'd go
> further: the culture never recovered. Though maybe I'm biased, I was
> there for part of it.

- q1 = **Y** (opens by validating: "That's a totally fair way to frame it")
- q2 = **N** (the turn picks a side and stays there)
- q3 = **N** ("no, actually I'd go further" escalates, but there's no flat
  unsoftened contradiction of the guest as its own statement — the turn is
  wrapped in "I think," "sort of," "maybe")
- q4 = **I think, sort of, maybe**

---

## If something's wrong with an item

- Garbled or unreadable text (transcription errors happen): answer
  `UNSURE` (G1) or leave the q's blank (G2), and write "garbled" in notes.
- The `host_turn` box seems to contain the guest speaking, or the excerpt
  cuts off mid-thought: same — note it, don't reconstruct it.
- Never skip a row silently; a note is what makes the row recoverable.
