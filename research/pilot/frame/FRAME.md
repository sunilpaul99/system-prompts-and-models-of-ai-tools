# §3.1 Sampling Frame — Archived Chart Snapshots

Committed per PROTOCOL §3.1 **before eligibility screening**. Raw HTML in
`raw/`; CDX capture listings in `cdx_*.txt`; retrieval log in
`snapshot_log.txt`. Retrieved 2026-07-28 from web.archive.org (id_ raw-content
endpoint), User-Agent identifying the project.

## Primary frame: Chartable "Apple Podcasts: United States" genre top-200 charts

Verified content: each capture is a full US top-200 chart for its genre
(sanity check: tech 2020-11-11 capture titled "Apple Podcasts : United States
of America : Technology Podcast — Chartable", 201 show links).

| Genre | Captures (timestamps) |
|---|---|
| Technology | 2020-11-11, 2021-01-16, 2021-04-11, 2021-06-14, 2021-10-19 |
| Society & Culture | 2021-04-19, 2021-10-28 |
| Comedy | 2020-11-12 |
| Sports | 2020-10-03, 2020-11-11, 2021-12-03 |
| Business | 2020-11-26, 2021-02-26, 2021-08-19, 2021-10-25 |
| Science | 2021-02-05, 2021-05-06, 2021-12-06 |
| History | 2019-09-22 (only Chartable capture in 2019–2022; see supplement) |

## History-genre supplement (declared frame deviation)

Chartable's US-History chart has a single archived capture (2019-09-22, just
before the 2020–2021 window). Supplement: Apple Podcasts' own History genre
page (popular-shows list, not a ranked top-200), 4 captures: 2020-04-04,
2020-12-18, 2021-06-30, 2021-12-01 (`raw/apple-us-history_*.html`).
**Queue item for PI:** ratify this substitution (Chartable 2019-09 +
Apple-popular 2020–2021) for the History cell, or drop History from the frame.
This is exactly the kind of §3.1 deviation the protocol requires be recorded —
it is recorded here before any eligibility screening has begun.

## Not obtained

- Chartable `us-all-podcasts` (overall top-200): zero archived captures
  2019–2022. Not required — the frame is defined per-genre.

## Next step (Phase 3, NOT pilot)

Parse show names + ranks from each capture into `frame_list.csv` — the
frozen frame list — before eligibility screening begins. No eligibility or
exposure work has been done as of this commit.
