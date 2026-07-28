# WS1 — Candidate Feed Archive-Depth Verification

Verified: 2026-07-28, from the remote session (network blocker in `WS1_candidates.md` is resolved — direct HTTPS fetches now succeed; see note at bottom).
Method: full RSS fetch of each candidate feed; `<item>` count and pubDate parsing (`scratchpad/feedcheck.py`, stdlib only). Channel titles confirmed for the two Simplecast feed IDs.

**Requirement (PILOT_PLAN §0):** episodes retrievable from both 2019 and 2024–2025. **All six candidates pass.**

| Candidate | Feed URL | Items | Earliest pubDate | Latest pubDate | 2019 items | 2024 / 2025 items |
|---|---|---|---|---|---|---|
| Lex Fridman Podcast (P1) | https://lexfridman.com/feed/podcast/ | 499 | 2018-08-26 | 2026-06-30 | 50 | 48 / 33 |
| The Changelog (P1 fallback) | https://changelog.com/podcast/feed | 1,012 | 2009-11-19 | 2026-07-21 | 49 | 153 / 146 |
| EconTalk (P2) | https://feeds.simplecast.com/wgl4xEgL | 1,060 | 2006-03-16 | 2026-07-27 | 52 | 53 / 52 |
| The Tim Ferriss Show (P2 fallback) | https://rss.art19.com/tim-ferriss-show | 880 | 2014-04-18 | 2026-07-22 | 52 | 71 / 58 |
| Accidental Tech Podcast (P3 fallback) | https://atp.fm/rss → cdn.atp.fm/rss/public | 703 | 2013-02-07 | 2026-07-27 | 52 | 53 / 52 |
| My Brother, My Brother And Me (P3) | https://feeds.simplecast.com/wjQvYtdl | 839 | 2010-04-12 | 2026-07-27 | 51 | 53 / 51 |

Notes / observed failure modes (feeds WS8 catalog):

- **No truncation observed anywhere** — every feed serves its complete archive, including both network-hosted Simplecast feeds (the truncation risk flagged in `WS1_candidates.md` did not materialize).
- **ATP** redirects `atp.fm/rss` → `cdn.atp.fm/rss/public?<token>`; the token may be rotating — Phase 4 downloader should follow redirects fresh each run rather than caching the CDN URL.
- **Tim Ferriss (art19)** feed is 30 MB (verbose per-item HTML); parse streaming in Phase 4.
- **Changelog** volume jumps 2023+ (71→127→153/yr) — likely feed consolidation of multiple shows into the master feed; episode sampling must filter to the flagship interview show and confirm host continuity.
- Per-source ToS review (§9) still pending — required before bulk audio download, which has not started.

## Confirmed slate (pending PI ratification per PILOT_PLAN §0)

- **P1: Lex Fridman Podcast** — 2019 coverage confirmed (50 eps); maximal AI-mention stress.
- **P2: EconTalk** — 2019 coverage confirmed (52 eps); weekly cadence rock-steady since 2006; human transcripts double as WS4 ground truth.
- **P3: My Brother, My Brother And Me** — 2019 coverage confirmed (51 eps); 3-speaker non-tech banter; slate spans tech / economics-academia / comedy.

All three fallbacks also verified viable.

## Network-access note

Podcast feed hosts (lexfridman.com, changelog.com, feeds.simplecast.com, rss.art19.com, atp.fm/cdn.atp.fm) are all reachable directly. **web.archive.org remains problematic from this egress**: TLS connections reset, and archive.org APIs intermittently 429 — see `frame/snapshot_log.txt` for the sampling-frame snapshot attempt (§3.1).
