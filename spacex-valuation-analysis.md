# SpaceX (NASDAQ: SPCX) Valuation Analysis

**Prepared: August 4, 2026; updated August 5, 2026** after SpaceX's first-ever public earnings report (Q2 2026, reported Aug 4 after close), one day before an in-kind venture distribution of SPCX shares and the first major lockup unlock (both August 6).

> This is an analytical exercise, not investment, tax, or legal advice. All figures are drawn from public reporting and are approximate; private-company history in particular is based on press accounts of the S-1 and tender offers.

---

## 0. UPDATE — Q2 2026 results (reported August 4, after close)

SpaceX's first public earnings report was a **double beat with a violent two-act market reaction**: the stock fell ~8% after hours on capex shock, then reversed to close-in on **~$125 on August 5 (+9% on the day, range $115.72–$126.71)** as the market digested the growth and the guidance raise.

**The quarter:**
- **Revenue $7.81B, up 92% YoY** (vs. ~$6.8–6.9B expected) and up 66% sequentially from Q1's $4.69B.
- **Net loss narrowed to $541M** (−$0.09/share vs. −$0.26 expected), from a $1.0B loss a year ago; **operating loss just $143M**, from −$970M.
- **Connectivity:** revenue **$4.29B (+66% YoY)**, operating income **$1.66B (~39% margin, margin holding)**; **12M subscribers (+17% QoQ, 2× YoY)**; **ARPU $66 — flat sequentially** for the first time after two years of decline (down from $85 a year ago).
- **AI:** revenue **$2.56B, up 247% YoY** — annualizing above $10B — with the implied segment operating loss narrowing to roughly **$1.2–1.3B** (from $2.47B in Q1). The CFO disclosed **$6.7B of new cloud-services contracts** signed in the first weeks of Q3, ramping from October. Backlog across the company hit **$47.5B**.
- **Space:** revenue ~$0.96B; operating loss $542M — the smallest story of the quarter.
- **The shock: capex of $18.37B in a single quarter** (up ~6× YoY), of which **$15.83B was AI**. Musk said data centers will be built exclusively on Nvidia chips, targeting **>2 GW of compute by year-end 2026, scaling toward 10 GW**. Free cash flow is now on the order of **−$15B+ per quarter**.
- **Balance sheet: ~$100B in cash and marketable securities** (largely the IPO raise) — roughly 6–7 quarters of runway at the current burn before new capital is needed.
- SpaceX **raised full-year guidance**, its first raise as a public company.

**What this changes in the analysis below:**
1. **The base case moves up, but less than the stock did.** The two genuinely new fundamental facts are (a) ARPU stabilizing while subscribers grew 17% in a quarter — this de-risks the Starlink base case materially — and (b) AI revenue compounding at a pace that makes the segment's $250B merger mark look less fanciful. I'd revise my sum-of-the-parts base case from ~$65–85 to roughly **$75–95/share**, driven by higher Starlink revenue confidence and a higher probability weight on the AI segment.
2. **But the capex number is the new dominant risk.** $60B+/year of annualized capex means the $100B war chest is a countdown clock: SpaceX has effectively converted itself into a hyperscaler mid-buildout. The bull case now requires those AI data centers to earn hyperscaler-like returns; the bear case is that this is capex-fueled revenue (xAI buying growth) that forces a large dilutive raise by 2028. Note the circularity risk: a company spending $60B/yr on Nvidia chips reporting 247% AI revenue growth is the same pattern the market has begun questioning across the AI capex complex.
3. **At ~$125, the reverse-DCF hurdle got harder, not easier.** Implied equity value is now ~$1.6T, requiring roughly **$110B of 2031 net income** (at 25× exit, 12% return) — the print was good, but one strong quarter does not close a gap of that size. The stock remains priced for the Morgan Stanley trajectory.
4. **The supply event is now, and it's bigger than trailed.** The first unlock releases **~911.5M shares (~$116B, ~7% of the company) on August 6** — the same day as your distribution — with the tranche schedule below unchanged after that. A +9% tape into a $116B unlock is exactly the setup where mechanical distribution-driven selling meets fresh momentum buyers; expect elevated volatility and volume for several sessions rather than a clean directional move.

The original analysis follows; figures there predate the Q2 print except where noted.

---

## 1. Executive summary

- **SpaceX is now public.** It listed on Nasdaq on June 12, 2026 at $135/share (a record ~$75B raise, ~$1.75T implied valuation), spiked to an all-time high of $225.64, and has since fallen roughly 50% from that high to **~$108–114** (Aug 3–4), below the IPO price. Market cap is **~$1.4–1.5T** on roughly 13 billion shares.
- **It is really three companies.** Ahead of the IPO, SpaceX absorbed xAI (including Grok and the X platform) in an all-stock merger that valued the combination at $1.25T ($1T SpaceX + $250B xAI). Reported segments: **Connectivity (Starlink)** — the only profitable segment; **Space (launch/Starship)** — modest operating losses; **AI (xAI/X)** — very large operating losses (~$6.4B in 2025).
- **Analyst dispersion is enormous**: Morningstar fair value **$62**; Goldman Sachs **$205**; Morgan Stanley **$300** (bull $600, bear $75); 22-analyst average **~$223**, range $62–$800. A ~$1T+ of market cap separates the big houses — the disagreement is almost entirely about the AI segment and orbital compute, not about Starlink.
- **My reverse-DCF conclusion: at ~$114 the stock is not cheap on visible cash flows.** The businesses you can underwrite today (Starlink + launch) plausibly support **~$50–75/share**. Everything above that — roughly **$700–800B of today's market cap** — is optionality on xAI competing with OpenAI/Anthropic/Google and on Starship enabling orbital data centers. The current price is roughly "fair" only if you assign near-full private-market marks to xAI *and* assume Starship commercializes on schedule.
- **Your lockup suspicion is well-founded and the timing is acute.** Float was only ~4% at IPO. A staggered unlock begins with a **~20% tranche triggered by tonight's Q2 earnings**, then ~7% tranches every 2–4 weeks through October (public float reaching roughly one-third of the company by Halloween), a Q3-earnings tranche (~28%), the balance on **December 8, 2026**, and Musk's own 6.4B shares (~49%) locked until **June 12, 2027**. Venture distributions like yours are a textbook source of mechanical selling into these windows. Supply pressure is a reasonable base case into year-end, though partially priced in after a 50% drawdown.

---

## 2. How we got here: valuation history

| Date | Event | Implied valuation |
|---|---|---|
| Dec 2024 | Tender offer | ~$350B (~$212/share pre-split terms) |
| Jul 2025 | Tender offer | ~$400B |
| Dec 2025 | Tender offer (~$421/share) | ~$800B |
| Feb 2, 2026 | xAI merger (all-stock) | $1.25T combined ($1T + $250B) |
| Jun 12, 2026 | IPO at $135; first trade $160.95 | ~$1.75T target |
| Mid-Jun 2026 | All-time high $225.64 | ~$2.9T intraday |
| Aug 3–4, 2026 | ~$108–114 | ~$1.4–1.5T |

The valuation quadrupled in roughly 18 months of private marks before the IPO, then the public market took back ~50% from the high within eight weeks. Anyone receiving shares now is receiving them into a falling-knife tape with heavy known supply ahead — but also *after* a major de-rating, not before it.

## 3. The financial reality (from the S-1 and Q1 2026)

**Consolidated 2025:** revenue $18.7B; Adjusted EBITDA $6.6B; operating loss $2.6B; **net loss $4.9B**.
**Q1 2026:** revenue $4.7B; operating loss $1.9B; net loss $4.3B. Reported cash spend on AI infrastructure and the rocket program is running around **$40B/year**.

| Segment (2025) | Revenue | Operating result | Notes |
|---|---|---|---|
| Connectivity (Starlink) | $11.4B (61%) | **+$4.4B (~39% margin)** | 10.3M subs at Q1'26 (11.8M+ now); ARPU compressed from ~$99 (2023) to ~$66/mo; direct-to-cell scaling (650+ satellites, 22 countries, carrier deals covering 400M+ people) |
| Space (launch) | $4.1B | −$0.7B | Falcon dominant in global launch; Starship V3 flew May 2026 and again July 2026 (Flight 13) — promising but **not yet operational**, full reuse not yet demonstrated |
| AI (xAI / X / Grok) | $3.2B | **−$6.4B** | Projected to burn ~$10B in 2026; competing with OpenAI, Anthropic, Google from behind in enterprise/coding |

The essential shape: **one excellent, profitable, decelerating-growth business (Starlink) funding two cash furnaces with enormous theoretical upside.** In Q1 2026 Starlink was 69% of revenue and generated $1.19B of segment operating profit, more than fully consumed by AI (−$2.47B) and Space (−$0.62B).

## 4. What credible analysts are saying

- **Morningstar — $62 fair value (~$780–800B).** Sum-of-the-parts: launch + Starlink ≈ **$611B**; AI segment probability-weighted at ≈ **$170B**; adjustments for cash, expected capital raises (~$86B assumed), and debt. They call xAI a *"material threat of value destruction"* with an *"indeterminate"* moat, and consider the IPO price roughly twice fair value.
- **Goldman Sachs — $205.** Constructive middle: credits Starlink scale, launch near-monopoly, and partial AI value.
- **Morgan Stanley (Adam Jonas) — $300 base / $600 bull / $75 bear.** The bull thesis is explicitly about **orbital AI compute** ("Starmind" AI-satellite constellation): orbital data centers reaching cost parity with terrestrial by ~2031; Starship operational in Q4 2026 with launch cost falling to ~$500/kg by 2030 and <$150/kg by 2040; company revenue scaling from **$45B (2026) → $319B (2030) → $3.3T (2040)** at ~59% operating margins. Note that even Jonas's *bear* case ($75) is below today's price relative context — i.e., the largest bull on the Street concedes a downside scenario ~35% below the current quote.
- **Consensus:** ~$223 average target across 22 analysts (range $62–$800), 27 buy / 1 sell. Treat the buy skew with suspicion: most initiations came from IPO syndicate banks after the July 7 quiet-period expiry, and the stock has fallen *through* those targets — a "wall of bullish price targets" the market is visibly ignoring.

The spread itself is the message: **there is no analytical consensus on what half this company is worth.** Starlink's value is broadly agreed within ±30%; xAI's value estimates span roughly $0–$2T+.

## 5. My valuation framework

Working numbers: ~13.0B shares fully diluted, so **every $100B of value ≈ $7.70/share**, and share price × 13B = implied market cap. Discounting at 11–12% equity cost; where I use exit multiples they are on 2030–2031 results, discounted back ~5 years (factor ≈ 0.57–0.62).

### 5a. Sum-of-the-parts, three scenarios

**Connectivity (Starlink).** 2026E revenue ~$15.5B growing ~35–45% but decelerating; the core tension is subscriber growth (doubling year-over-year) vs. ARPU compression ($99 → $66/mo as growth shifts to price-sensitive geographies) and eventual fixed-broadband saturation. Direct-to-cell is the credible second act (carrier deals already cover 400M+ people).

| | Bear | Base | Bull |
|---|---|---|---|
| 2030 revenue | $30B | $50B | $80B |
| EBITDA margin | 38% | 42% | 45% |
| Exit EV/EBITDA (growth embedded) | 14× | 18× | 22× |
| 2030 EV | $160B | $380B | $790B |
| **PV today** | **~$100B** | **~$230B** | **~$470B** |

(For reference, Morningstar's DCF — which runs the tail much longer — gets to ~$500–600B for Starlink + launch combined. My base-to-bull range brackets theirs.)

**Space (launch/Starship).** Falcon is a profitable-at-gross-level near-monopoly (~$4B revenue) but the segment loses money as Starship consumes capital. Value hinges entirely on Starship: V3 has now flown twice; full recovery/reuse of both stages is the unproven gate.

| | Bear | Base | Bull |
|---|---|---|---|
| Starship outcome | Delays persist; Falcon economics only | Operational 2027; cadence scales; NASA/defense (incl. Golden Dome-type programs) + constellation self-launch | Jonas path: $500/kg by 2030, external commercial market expands |
| **PV today** | **~$80B** | **~$200B** | **~$450B** |

**AI (xAI / X / Grok).** The swing factor. The merger marked it at $250B in Feb 2026. Comparable private AI labs carry marks in the several-hundred-billion range, but xAI monetizes least well of the majors, burns ~$10B/year, and its access to SpaceX's balance sheet was the stated rationale for the merger — i.e., it exists inside SpaceX partly *because* it could not fund itself indefinitely alone.

| | Bear | Base | Bull |
|---|---|---|---|
| Outcome | Sub-scale; continued burn destroys value net of any salvage; effectively $0 net of future funding needs | Survives as a top-4 lab; worth roughly its merger mark plus growth | Top-2 lab + orbital compute works; AI becomes majority of company value |
| **PV today** | **~$0** | **~$350B** | **~$1.5T+** |

**Corporate:** net cash from the $75B IPO raise less debt and the ~$40B/yr spend rate; assume ongoing dilution of ~3–5%/yr in base case (Morningstar assumes ~$86B of future raises). Call it **+$50B bear / +$80B base / +$100B bull** of net balance-sheet value today, offset by dilution in the per-share math.

### Sum-of-the-parts totals

| Scenario | Total equity value | Per share (~13B sh, dilution-adjusted) |
|---|---|---|
| **Bear** | ~$650–800B (see note below) | **~$50–60** |
| **Base** | ~$850B–1.1T | **~$65–85** |
| **Bull** | ~$2.5T+ | **~$180–200+** |

Note on the bear case: a strict PV-of-visible-cash-flows bear lands uncomfortably low (~$25–35/share) because Starlink's terminal value is genuinely sensitive to ARPU trajectory. A more defensible "everything disappoints but Starlink is still Starlink" floor, closer to Morningstar's method with longer tails, is **~$50–60/share**. I'd treat **$50–75** as the fundamental-support zone and my sum-of-the-parts **base case lands at ~$65–85/share** — materially below today's ~$114. The current price requires giving the AI segment close to full private-market credit ($400B+) *and* a successful Starship on roughly the announced schedule.

### 5b. Reverse DCF — what today's price implies

Equity value $1.48T at $114. To earn a 12% return holding five years, with an exit at 25× earnings in 2031, SpaceX must produce **~$100B of net income in 2031** — at a strong 30–35% net margin, that's **~$300B of revenue**, i.e., ~16× 2026 revenue, a ~65%/yr compound growth rate for five years. That is essentially Morgan Stanley's model ($319B by 2030). Relax to a 10% return and a 35× exit multiple and you still need **~$70B of net income / ~$200B+ revenue by 2031**.

**Translation: today's price already embeds the bull narrative's first five years.** You are not paying for Starlink; you are paying for Starlink *and* pre-paying for orbital AI compute.

## 6. What you have to believe at each price

| Price | Implied cap | What you must believe |
|---|---|---|
| **$62** (Morningstar) | ~$0.8T | Starlink executes to ~$40–50B revenue with margins intact; Falcon stays dominant; Starship eventually works but only replaces/extends launch economics; xAI is a probability-weighted lottery ticket (~$170B) more likely to burn cash than to win. No orbital compute. |
| **$75–90** | ~$1.0–1.2T | The above, plus either Starship commercializing on schedule *or* xAI holding its $250B merger mark — one of the two options pays off, not both. |
| **~$114** (today) | ~$1.5T | Starlink to ~$50B+ revenue; Starship operational by 2027 with scaling cadence; xAI retains near-full private-lab marks (~$400B+) despite the burn; dilution stays modest; ~$300B revenue by early 2030s *or* you accept a sub-10% expected return. |
| **$205** (Goldman) | ~$2.7T | All of the above *plus* early orbital-compute/Starmind revenue is real by ~2028, direct-to-cell becomes a 100M+ endpoint business, and defense launch/constellation spending expands the Space TAM. |
| **$300** (Morgan Stanley) | ~$3.9T | $319B revenue by 2030 at ~59% operating margins (richer than Nvidia's); orbital data centers hit cost parity with terrestrial by 2031; Starship on a path from 46 launches (2027) toward thousands/yr; near-monopoly economics persist without regulatory or competitive interruption. |
| **$600** (MS bull) | ~$7.8T | AI is >60% of company value: xAI is a top-2 lab beating OpenAI/Google in key markets, *and* space-based compute becomes the world's marginal AI datacenter, *and* Starship hits ~$150/kg. Multiple miracles, each individually possible, jointly required. |

## 7. The lockup / supply picture — your specific concern

Your suspicion is structurally correct, with important nuance:

**The supply schedule** (per lockup trackers and IPO documents as reported):
- IPO float was tiny — roughly **4%** of shares (~$75B sold at $135).
- **First earnings-triggered tranche: ~911.5M shares (~$116B, ~7% of the company) unlock August 6** — confirmed post-earnings; the same day as your distribution.
- **~7% tranches every 2–4 weeks, August through October**; public float reaches roughly **one-third of the company by October 31**.
- **~28% tranche after Q3 earnings** (early November).
- **Remainder of the 180-day pool on December 8, 2026.**
- **Musk's 6.4B shares (~49%) locked until June 12, 2027** — the largest single overhang, one year out.

**Why venture distributions amplify this:** funds like the one distributing to you typically distribute in-kind precisely at unlock windows, and a large fraction of LPs (especially institutions with no mandate to hold single stocks) sell immediately and mechanically, price-insensitively. Multiply your Thursday distribution by every SpaceX fund investor since 2008 and you have months of programmatic supply meeting a still-small float.

**The counterweights:** (1) the stock has already fallen ~50% from its high — unlock schedules are public, and sophisticated buyers front-run known supply, so some of this is priced; (2) index inclusion (Nasdaq-100 already; MSCI and eventually S&P 500 eligibility as float grows) creates mechanical *demand* tranches against the mechanical supply; (3) historically, lockup expirations produce low-single-digit abnormal negative returns on average — but the drawdowns are much larger for low-float, high-valuation, VC-heavy IPOs, which is exactly this profile.

**Net judgment:** supply pressure dominating through the December 8 full unlock is the sensible base case, with the June 2027 Musk unlock as a second overhang. If you intend to hold long-term regardless, this is noise; if you are valuation-driven, the market is unlikely to run away to the upside while two-thirds of the company is still queued to hit the float — patience is cheap here.

## 8. Key risks in both directions

**Downside risks beyond supply:** tonight's first earnings print (a $40B/yr spend rate meeting public-market scrutiny for the first time); ARPU compression outrunning subscriber growth; a Starship failure or reuse-economics disappointment; xAI burn accelerating (forcing dilutive raises); governance concentration (Musk ~49%, multi-class structure, related-party complexity across Tesla/X); regulatory and geopolitical exposure (spectrum, FAA cadence approvals, defense dependence); Amazon Kuiper and Chinese constellations attacking Starlink pricing.

**Upside risks (why the bears can be wrong):** Starlink direct-to-cell converts carrier deals covering 400M+ people into a wholesale revenue stream with no terrestrial analog; Starship V3 has now flown twice and is trending toward operational status — if full reuse lands, launch cost collapses in a way no competitor can answer this decade; xAI's compute buildout plus SpaceX's launch/power vertical integration is a genuinely unique asset if orbital compute economics work even half as well as Morgan Stanley models; and index inclusion flows are large and mechanical.

## 9. Bottom line

1. **Is it significantly overvalued or undervalued?** On visible, underwritable cash flows, **overvalued**: fundamental support is roughly **$50–75/share** against a ~$114–125 price, and my sum-of-the-parts base case is **~$65–85** (revised to **~$75–95** after the Q2 print — see Section 0). The current price is defensible only with near-full credit for the AI segment and on-schedule Starship commercialization. It is simultaneously far below the Street's syndicate-bank targets — but those targets require believing in a 2030 income statement that does not yet exist.
2. **Will lockup supply pressure the stock?** More likely than not, through at least December 8, 2026, with a second overhang at Musk's June 2027 unlock. The effect is partially priced after a 50% drawdown, but the float math (4% → ~33% by Halloween → ~50%+ by year-end) is unusually extreme even by mega-IPO standards.
3. **Timing note for Thursday:** your shares now arrive on the *same day* as the first big unlock tranche (~$116B of stock), one day after a +9% post-earnings rally — into maximum-supply, maximum-volatility conditions. Whatever you decide, decide it on the valuation framework above rather than on the tape of the next few weeks, which will be dominated by supply mechanics rather than fundamentals.
4. **On cost basis** (verify with your tax advisor): for in-kind distributions from a venture fund (partnership), your basis is generally the *fund's carryover basis* in the shares (often very low, dating to early rounds), not the value on distribution day, and the holding period tacks — meaning a sale would likely realize a large long-term gain. This materially changes the sell-vs-hold calculus versus a fresh purchase, and is worth resolving before Thursday.

---

## Sources

- [CNBC — Morningstar: SpaceX worth less than half its $1.75T IPO target](https://www.cnbc.com/2026/06/03/morningstar-spacex-ipo-target-price-nasdaq.html)
- [Morningstar — Why We Think the SpaceX IPO Is Overvalued](https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued)
- [Morningstar — 6 Charts on SpaceX's Pre-IPO Financials](https://www.morningstar.com/stocks/6-charts-spacexs-s-1-financials)
- [Motley Fool — Morningstar's $62 fair value vs. the market](https://www.fool.com/investing/2026/06/26/morningstars-fair-value-of-spacex-stock-is-62-spcx/)
- [Yahoo Finance — Morgan Stanley's Street-high $300 target](https://finance.yahoo.com/markets/stocks/article/spacex-snags-street-high-300-price-target-from-morgan-stanley-as-rocket-company-enters-nasdaq-100-160316317.html)
- [Motley Fool — Morgan Stanley $300 target details](https://www.fool.com/investing/2026/07/19/morgan-stanley-set-a-300-price-target-on-elon-musk/)
- [Fortune — SpaceX falls below IPO price despite bullish targets](https://fortune.com/2026/07/18/wall-street-analysts-spacex-outlook-stock-predictions/)
- [CNBC — SpaceX heavily reliant on Starlink for growth and profit](https://www.cnbc.com/2026/05/21/spacex-starlink-growth-profit-nasdaq-ipo.html)
- [CNBC — SpaceX acquiring xAI ahead of IPO](https://www.cnbc.com/2026/02/02/elon-musk-spacex-xai-ipo.html)
- [SEC — Space Exploration Technologies Corp. Form S-1](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)
- [SatNews — "Only 7% of That Is Real": inside the S-1](https://satnews.com/2026/05/21/inside-spacexs-s-1-three-companies-one-profit-1-75-trillion/)
- [Fast Company — Q2 earnings preview and stock drop](https://www.fastcompany.com/91584302/spacex-q2-2026-earnings-update-stock-drop-today-ai-spending-results-come-due-investors-first-glimpse)
- [Yahoo Finance — Q2 earnings date triggers insider share unlock](https://finance.yahoo.com/markets/stocks/articles/spacex-q2-2026-earnings-date-170755440.html)
- [StockAlarm — SPCX lockup expiration schedule](https://pro.stockalarm.io/blog/spacex-ipo-lockup-financials)
- [BiyaPay — SPCX lockup schedule, float, and Musk lockup explained](https://www.biyapay.com/en/blogdetail/4087-spacex-spcx-lockup-expiration-schedule-20262027-fl)
- [CNBC — SPCX real-time quote](https://www.cnbc.com/quotes/SPCX)
- [NASASpaceflight — Starship V3 debut and follow-up](https://www.nasaspaceflight.com/2026/05/starship-flight-12-v3-follow/)
- [CNBC — Starship Flight 13, first test since IPO](https://www.cnbc.com/2026/07/24/spacex-launches-massive-starship-rocket-in-first-test-flight-since-ipo.html)
- [The Next Web — Starlink's cash-machine math is getting harder](https://thenextweb.com/news/starlink-is-spacexs-cash-machine-but-the-maths-is-getting-harder)
- [ValueAdd VC — Starlink revenue, subscribers, ARPU](https://valueaddvc.com/blog/starlink-revenue-2025-2026-subscriber-count-arpu-and-the-path-to-profitability)
- [Roic — Starlink ARPU falls 18% as base quadruples](https://www.roic.ai/news/starlinks-revenue-per-user-falls-18-as-customer-base-quadruples-signaling-shift-to-volume-over-pricing-04-29-2026)

**Q2 2026 earnings update (Aug 4–5):**
- [SpaceX — Q2 2026 results press release (PDF)](https://s21.q4cdn.com/184289198/files/doc_financials/2026/q2/SpaceX-Reports-Second-Quarter-2026-Results.pdf)
- [Fortune — Revenue surges 92% to $7.8B, ~$1B beat](https://fortune.com/2026/08/04/spacex-revenue-surges-92-to-7-8-billion-blowing-past-wall-street-expectations-by-nearly-1-billion/)
- [Benzinga — Double beat, backlog $47.5B](https://www.benzinga.com/markets/earnings/26/08/60931182/spacex-q2-highlights-double-beat-revenue-up-92-backlog-hits-47-5-billion)
- [TradingKey — AI revenue +247%, capex spike, after-hours drop](https://www.tradingkey.com/analysis/stocks/us-stocks/262074436-spacex-q2-revenue-92-percent-ai-income-247-percent-capex-double-stock-drop-tradingkey)
- [Investing.com — Earnings call transcript coverage](https://www.investing.com/news/transcripts/earnings-call-transcript-spacex-beats-revenue-estimates-in-q2-2026-shares-swing-93CH-4836052)
- [TechTimes — First-ever guidance raise as $116B lockup looms](https://www.techtimes.com/articles/323056/20260804/spacex-q2-beat-raises-full-year-guidance-first-time-116b-lock-looms.htm)
- [StartupHub — Aug 6 unlock: 911.5M shares, ~$116B](https://www.startuphub.ai/ai-news/ipo-watch/2026/spacex-spcx-earnings-lockup-august-2026)
- [CNBC — Q2 earnings live updates](https://www.cnbc.com/2026/08/04/spacex-spcx-earnings-live-updates-q2-2026.html)
