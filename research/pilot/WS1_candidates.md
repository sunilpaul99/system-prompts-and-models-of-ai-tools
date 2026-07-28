# WS1 — Pilot Host Candidate Shortlist

Status: DRAFT — candidates identified; **feed-depth verification blocked by session network policy** (see "Blocker" below). No candidate is confirmed until its RSS archive is verified to reach 2019.

Selection criteria (PILOT_PLAN §0): episodes retrievable from both 2019 and 2024–2025; unscripted conversational; same host throughout; slot-specific stress properties. Pilot hosts are excluded from the confirmatory panel.

## Slot P1 — tech-adjacent interview show (stresses AI-mention/meta-mention filtering)

| Candidate | Evidence for fit | Risks to verify |
|---|---|---|
| **Lex Fridman Podcast** | Interview format since 2018; very long unscripted episodes; AI is discussed constantly (maximal stress for the meta-mention rule); self-hosted feed (lexfridman.com/feed/podcast) historically carries the full archive | AI-topic density is *extreme* — good for stressing filters, but confirm enough non-AI segments exist; feed depth to 2019 |
| **The Changelog** | Developer interviews since 2009; changelog.com historically serves complete archives with transcripts | Guest pool is developer-only; confirm same-host continuity 2019–2025 |

## Slot P2 — non-tech interview show (stresses genre generality)

| Candidate | Evidence for fit | Risks to verify |
|---|---|---|
| **EconTalk (Russ Roberts)** | Weekly one-on-one interviews since 2006, same host throughout; Econlib publishes feeds and *human-made transcripts* for many episodes — which also feeds WS4's verbatim ground-truth needs ([econlib feed page](https://www.econlib.org/library/rss-feeds-for-econtalk/)) | Main simplecast feed may start at 2015 (fine) but confirm items aren't truncated to recent N; economics guests skew academic |
| **The Tim Ferriss Show** | Interviews since 2014; art19 feed historically complete; host publishes transcripts | Host is a productivity-tools enthusiast — fine for pilot (exposure irrelevant), but episodes are heavily produced; verify unscripted rubric |

## Slot P3 — multi-speaker banter (stresses diarization hardest)

| Candidate | Evidence for fit | Risks to verify |
|---|---|---|
| **Accidental Tech Podcast** | Three co-hosts, weekly since 2013, fully unscripted; feed at [atp.fm/rss](https://atp.fm/rss) | Tech topic overlaps P1 (acceptable for pilot); verify feed depth — some independent feeds truncate |
| **My Brother, My Brother and Me** | Three co-hosts, comedy advice, weekly since 2010, non-tech ([Maximum Fun](https://maximumfun.org/podcasts/my-brother-my-brother-and-me/)) | Network feeds (Maximum Fun/Simplecast) sometimes truncate archives; comedy register may stress the disagreement annotator in useful ways |

## Recommended picks pending verification

**P1: Lex Fridman** (maximal meta-mention stress), **P2: EconTalk** (transcripts double as WS4 ground truth — a two-for-one), **P3: MBMBaM** (non-tech banter, so the pilot trio spans three genres). Fallbacks: Changelog / Tim Ferriss / ATP respectively.

## Blocker: session network policy

This session's environment allows the web-search API but returns 403 on all direct HTTPS fetches (podcast domains, feed CDNs, and web.archive.org — the last also matters for the §3.1 sampling frame). Verified 2026-07-28 via proxy status log: `connect_rejected` for lexfridman.com, feeds.simplecast.com, changelog.com, rss.art19.com, atp.fm.

**Fix options (pick one):**
1. Adjust this Claude Code environment's network policy to allow broader egress (Settings → environment → network policy; docs: code.claude.com/docs/en/claude-code-on-the-web). Domains needed at minimum: podcast feed/CDN hosts (varied), web.archive.org, plus transcript sites.
2. Run WS1–WS4 in a local Claude Code session on a machine with normal internet access, committing results to this repo.

**Next actions once unblocked:** verify each candidate feed's item count and earliest pubDate; confirm 8×2 era episode samples are downloadable; snapshot the archived 2020–2021 Apple charts for the §3.1 frame; then PI picks the three pilot hosts.
