# The Content Economy: From Clay Tablets to AI

**Prepared: April 2026**

17 chapters tracing how content has been created, distributed, and monetized across every major technology transition - from clay tablets to AI - with deep dives on attribution technology, the legal landscape, economics, and forward projections for 2026-2030. Most chapters are industry-level. Microsoft-specific chapters: 3 (Agentic Web Narrative), 4 (MSN), 5 (PCM), 10.2 (Microsoft's C2PA implementations), 12 (NYT v. OpenAI/Microsoft).

## Table of Contents

1. [From Clay Tablets to AI: How Content Has Always Worked](#1-from-clay-tablets-to-ai-how-content-has-always-worked)
2. [The Pattern](#2-the-pattern)
3. [The Agentic Web Narrative](#3-the-agentic-web-narrative)
4. [MSN and the Publisher Pipeline](#4-msn-and-the-publisher-pipeline)
5. [PCM - Product and Technical Details](#5-pcm---product-and-technical-details)
6. [How LLMs Actually Generate Answers (And Where Attribution Breaks)](#6-how-llms-actually-generate-answers-and-where-attribution-breaks)
7. [Can Attribution Work?](#7-can-attribution-work)
8. [The Shapley Value Problem](#8-the-shapley-value-problem)
9. [Beyond Shapley: Emerging Attribution Approaches](#9-beyond-shapley-emerging-attribution-approaches)
10. [Content Provenance and C2PA](#10-content-provenance-and-c2pa)
11. [The Legal Landscape](#11-the-legal-landscape)
12. [NYT v. OpenAI/Microsoft: The Defining Case](#12-the-new-york-times-v-openaimicrosoft-the-defining-case)
13. [The Economics Under Stress](#13-the-economics-under-stress)
14. [The Blockchain Question](#14-the-blockchain-question)
15. [What This All Means](#15-what-this-all-means)
16. [Where This Is Going](#16-where-this-is-going)
17. [Content Business Models in the AI Era](#17-content-business-models-in-the-ai-era)

---

# 1. From Clay Tablets to AI: How Content Has Always Worked

Every technology transition in media follows the same arc: new distribution excites creators, the platform consolidates power, creators get commoditized. Understanding this pattern is essential context for anyone working in content, publishing, or AI - because AI is the latest chapter in a story that's 5,000 years old.

## 1.1 Writing as Technology (3400 BCE - 1440 CE)

Writing itself was the first content platform - and the first to concentrate power.

**The invention of writing (roughly 3400 BCE)** didn't emerge from literature or storytelling. It emerged from accounting. The earliest known writing - Sumerian cuneiform on clay tablets in Mesopotamia - tracked grain shipments, livestock counts, and tax receipts. Writing was invented to solve an information management problem: how do you record economic transactions across a complex society? The very first "content" was spreadsheets.

**Who controlled writing controlled power.** For most of human history, literacy was deliberately restricted. In ancient Egypt, scribes were an elite class - fewer than 1% of the population could read or write. The Egyptian scribal schools (the "House of Life") trained writers who became administrators, tax collectors, and priests. A famous Egyptian text, "The Satire of the Trades" (roughly 2000 BCE), told students that every profession was miserable except the scribe's - because scribes controlled the information layer of civilization. This is the earliest recorded version of "content is king."

**The alphabet democratized writing - partially.** The Phoenician alphabet (roughly 1050 BCE) was revolutionary because it reduced writing from hundreds of hieroglyphs or cuneiform symbols to roughly 22 letters. This made literacy accessible to merchants and traders, not just temple elites. The Greek and Latin alphabets descended from Phoenician, spreading literacy across the Mediterranean. But even with simpler writing systems, literacy rates in the Roman Empire peaked at maybe 10-15% of the population.

**Medieval monasteries as content platforms.** After Rome fell, monasteries became the primary institutions preserving and copying written knowledge in Europe. Monks hand-copied manuscripts - a single Bible took roughly 15 months of full-time work. The monastery controlled what got copied (mostly religious texts), what got preserved, and what was lost. Scholars estimate that less than 1% of all classical Greek and Roman literature survived to the present - the rest was lost through deliberate selection, neglect, or destruction. The monks were the first content curators, and their curation was absolute.

**The Islamic Golden Age (8th-14th century)** preserved much of what Europe lost. The House of Wisdom in Baghdad (founded roughly 830 CE) systematically translated Greek, Persian, and Indian texts into Arabic. Paper manufacturing (learned from Chinese prisoners of war after the Battle of Talas in 751 CE) made copying dramatically cheaper than European parchment. At its peak, Cordoba's library held 400,000 volumes when the largest European libraries had a few hundred. The Arab world's content infrastructure - translation houses, paper mills, lending libraries - was centuries ahead of Europe's.

**The key pattern**: In every pre-print era, the institution that controlled copying controlled knowledge. Sumerian temples, Egyptian scribal schools, Roman publishing houses (which used slaves to hand-copy texts for sale), medieval monasteries, Islamic translation houses - the platform that controlled reproduction controlled the content economy. Sound familiar?

## 1.2 The Gutenberg Disruption (1440-1800): The First Platform Shift

**The printing press was the original content distribution revolution** - and it followed exactly the same arc that every subsequent technology shift would follow.

Johann Gutenberg's movable type press (roughly 1440) reduced the cost of producing a book by roughly 80% within 50 years. Before printing, a single book cost the equivalent of a laborer's annual wages. By 1500, roughly 20 million volumes had been printed across Europe. By 1600, that number was 150-200 million.

**Who benefited first: the incumbents.** The earliest printed books were Bibles, classical texts, and legal codes - the same content monasteries had been hand-copying. The Catholic Church initially embraced printing as a way to distribute standardized religious texts. Indulgences (printed certificates of divine forgiveness) became a mass-produced revenue stream.

**Then the disruptors arrived.** Martin Luther's 95 Theses (1517) went viral because of the printing press - an estimated 300,000 copies circulated within three years. Luther understood the platform: he wrote in German (not Latin), kept his pamphlets short and cheap, and published prolifically (roughly one new work every two weeks during peak years). The Church, which had controlled the content layer for a millennium, suddenly faced competition it couldn't suppress.

**Governments tried to control the platform.** England's Licensing Act (1662) required all books to be approved by the government before printing. The Stationers' Company held a monopoly on printing - you couldn't publish without their permission. This was the first "terms of service" for a content platform. When the Licensing Act lapsed in 1695, it unleashed an explosion of newspapers, pamphlets, and periodicals - the 18th-century equivalent of user-generated content.

**Copyright was invented to solve the attribution problem.** The Statute of Anne (1710), the world's first copyright law, wasn't primarily about protecting authors - it was about breaking the Stationers' Company's monopoly and establishing that creators (not printers or guilds) owned their work. The core question it addressed - who gets paid when content is reproduced at scale by a distribution technology the creator doesn't control - is precisely the question AI content marketplaces exist to answer 316 years later.

**The newspaper emerges.** The first regular newspapers appeared in the early 1600s (Relation in Strasbourg, 1605; the London Gazette, 1665). By 1800, newspapers were established commercial enterprises funded primarily by subscriptions and notices (early classified ads). The business model that would dominate for 200 years - bundle news with advertising, use content to attract eyeballs, sell the eyeballs to advertisers - was born.

## 1.3 The Print Era (Pre-2000): The Bundled Monopoly

Newspapers operated a three-legged revenue stool: subscriptions, display advertising, and classified advertising. As the sole surviving newspaper in most communities (consolidation killed off competitors), they were de facto local monopolies generating **20-40% annual profit margins**.

**Classified ads were the profit engine.** They contributed **40% of total newspaper revenue**, and some papers depended on classifieds for up to 70% of ad revenue. Classifieds were almost pure profit - no editorial effort, just order-taking and typesetting. In Western Europe, newspapers collected 93% of all classified advertising as late as 2003.

**Peak revenue**: US newspaper advertising revenue peaked at approximately **$49 billion nominal** in 2000 ($65.8B in 2013 dollars, $89B in 2020 dollars). Recruitment/help-wanted revenue alone peaked at $8.7 billion.

**Broadcast didn't kill print.** Surprisingly, radio and television did not financially disrupt newspapers. TV competed for national ad dollars, but newspapers adapted by focusing on local retail and classified advertising. Print newspaper ad revenue grew almost continuously from 1950 to 2000 despite television's rise. The real disruption came from the internet.

**Sources**:

- [Statista: 50 Years of Growth Wiped Out](https://www.statista.com/chart/612/newspaper-advertising-revenue-from-1950-to-2012/)
- [AEI: Newspaper Ad Revenue Free Fall](https://www.aei.org/carpe-diem/chart-of-the-day-newspaper-advertising-revenue-will-likely-continue-its-decade-long-free-fall-to-below-1950-levels/)
- [CJR: Reader Revenue and the Great Newspaper Ad Bubble](https://www.cjr.org/the_audit/newspaper_subscription_revenue.php)

## 1.4 The Early Web (1995-2005): Free Content and the CPM Crash

**The portal era**: Yahoo, AOL, and MSN built walled gardens that aggregated publisher content behind their own branded front pages. The portal controlled the ad inventory and monetization - publisher content drove engagement, but the platform captured the value. Yahoo received 95 million page views per day by 1998. This was the first instance of the platform pattern.

**Banner ad economics collapsed.** The first banner ad (AT&T on HotWired, 1994) had a 44% click-through rate at $100 CPM. By 2002, run-of-network banners were available for $2 CPM or less - a 95%+ decline. Click-through rates cratered from 44% to 0.1%. "Banner blindness" became the term of art.

**"Information wants to be free"** - Stewart Brand's 1984 half-quote became a rallying cry that justified giving away content online. Publishers, terrified of being left behind, put their content online for free. Most never recovered.

**Craigslist killed classifieds.** Craig Newmark offered free listings vs. newspapers' premium rates. Classified revenue plunged from $19.6 billion (2000) to $4.6 billion (2012) - a 77% drop. A Management Science study found Craigslist cost US newspapers $5 billion from 2000-2007. In markets where Craigslist entered, newspapers saw a 20.7% drop in classified rates, and downstream effects included slashed local political coverage - Stanford research linked this directly to increased partisan polarization.

**Sources**:

- [MinnPost: How Craigslist Killed the Newspapers' Golden Goose](https://www.minnpost.com/business/2014/02/how-craigslist-killed-newspapers-golden-goose/)
- [MediaPost: Craigslist Costs Newspapers $5 Billion](https://www.mediapost.com/publications/article/206729/craigslist-costs-local-newspapers-5-billion-in-lo.html)
- [Stanford GSB: Craigslist and Political Polarization](https://www.gsb.stanford.edu/insights/surprising-link-between-craigslist-classified-ads-political-polarization)

## 1.5 The Search Era (2005-2015): Google Redirects the Ad Dollar

Google's innovation was intent-based advertising - ads shown to people actively searching for something, fundamentally more valuable than display ads shown to passive readers.

**The revenue shift**: Google's ad revenue from its own properties grew from 55% (2005) to 77% (2015) to 90% (2025). The share flowing to publishers through Google's network shrank correspondingly. The "ad tech tax" meant publishers kept only 30-40 cents of every dollar spent to advertise on their sites.

**The decline timeline**:

- 2000: $49B (peak)
- 2006: $49B (briefly held)
- 2008: $37.6B (recession)
- 2011: ~$20B
- 2020: $8.8B (newspapers' share of total ad spending: 5%, down from 53% in 2000)
- 2023: ~$6B (92% decline from peak)

**Google News controversy**: Launched 2002. Google aggregated headlines and snippets, keeping users in Google's ecosystem. Google said it sent traffic back. Publishers said Google profited from their content without paying. The News Media Alliance estimated Google earned $4.7B from news content (2018). A Columbia University study estimated fair payment at $10-12 billion annually. Google's concession: a $1 billion News Showcase fund (2020), widely seen as inadequate.

**The European link tax battles**: Germany (2013) - publishers demanded EUR 1B, then backtracked when they realized they'd lose traffic. Spain (2014) - made fees non-waivable; Google shut down Google News Spain entirely, costing publishers an estimated EUR 10M/year. France - fined Google EUR 500M for bad-faith negotiation. Australia (2021) - News Media Bargaining Code forced negotiations, injecting hundreds of millions into news. Canada (2023) - passed similar legislation.

**SEO dependency**: By the 2010s, 53% of all trackable website traffic came from organic search. Publishers built editorial strategies around Google's algorithm, creating a power asymmetry with no recourse when rankings changed.

**Sources**:

- [Stanford Law: Why Google Dominates Advertising Markets](https://law.stanford.edu/wp-content/uploads/2020/12/Srinivasan-FINAL-Why-Google-Dominates-Advertising-Markets.pdf)
- [CJR: Google and Meta Owe Publishers](https://www.cjr.org/the_media_today/google_meta_owe_publishers_columbia_study.php)
- [EFF: Google News Shuts Shop in Spain](https://www.eff.org/deeplinks/2014/12/google-news-shuts-shop-spain-thanks-ancillary-copyright-law)

## 1.6 The Social Era (2012-2020): The Platform Bait-and-Switch

### Facebook's Pivot to Video (2015-2018)

One of the most destructive episodes in publisher-platform history:

- 2016: Facebook VP told publishers "We're seeing a year-on-year decline on text... Video, video, video."
- September 2016: Facebook admitted it had inflated video viewing metrics by 60-80% for two years
- October 2018: Court documents revealed actual inflation was 150-900%. Average video duration inflated from 2.0 to 17.5 seconds (775%).
- Casualties: Mic, Vice, Mashable, LittleThings (shut down entirely), CollegeHumor - all fired writers, hired video teams, then collapsed
- Settlement: Facebook paid advertisers $40 million. Publishers got nothing.

### Facebook Instant Articles (2015-2023)

- 2015: Launched with NYT, BuzzFeed, The Atlantic, Washington Post. Articles loaded "4x faster."
- The trade-off: Publishers hosted content on Facebook's servers, surrendering URLs, reader relationships, and most monetization.
- 2017: The Guardian pulled out citing "woeful" financial returns.
- 2018: More than half of Facebook's 72 original partners had abandoned the format.
- April 2023: Meta finally shut it down.

### Facebook News Tab (2019-2024)

- 2019: Launched with licensing deals, paying select publishers.
- 2024: Deprecated in US and Australia. Usage had dropped 80%+. Meta stated it "will not enter into new commercial deals for traditional news content."

### The 2018 Algorithm Cliff

January 11, 2018: Facebook announced it would "prioritize posts from friends and family":

- Publishers suffered 28% average traffic decrease from Facebook
- Some categories lost 60-70%+
- LittleThings shut down entirely citing the change
- Long-term: Facebook referrals to news sites fell 58% (2018-2024), from 1.3B visits to 561M. Facebook's share of publisher referrals collapsed from 30% to 7%.

### Twitter/X

Never a major traffic driver (3-4% of referrals) but disproportionately influential. Under Musk: referral traffic fell 24-49% for major outlets. NPR and PBS left entirely. Ad revenue fell 60% in 2023.

**Sources**:

- [Nieman Lab: Facebook's Faulty Data](https://www.niemanlab.org/2018/10/did-facebooks-faulty-data-push-news-publishers-to-make-terrible-decisions-on-video/)
- [Gizmodo: RIP Facebook Instant Articles](https://gizmodo.com/facebook-meta-news-instant-articles-1849660590)
- [Slate: Facebook's Retreat from News](https://slate.com/technology/2018/06/facebooks-retreat-from-the-news-has-painful-for-publishers-including-slate.html)

## 1.7 The Subscription Era (2015-Present): The Paywall Bet

The NYT is the definitive proof that subscription models work - for dominant brands:

- 2011: Launched metered paywall
- 2015: 1 million digital subscribers
- 2020: ~7 million
- End of 2025: **12.21 million** digital-only subscribers across 234 countries
- Digital subscription revenue up 14% in 2025; digital advertising up 20%

But the NYT is the exception. Across 20 wealthy countries, the share of users paying for news has plateaued at ~18%. When readers hit a paywall, 57% leave entirely. Most households have 1-2 news subscriptions, meaning dominant brands capture most of the market.

Apple News+ economics are brutal: Apple takes 50% of the $12.99/month subscription. The remaining 50% is split among all publishers. One publisher told Business Insider revenue was "one-twentieth of what Apple promised." The NYT pulled out entirely.

**Sources**:

- [Yahoo Finance: NYT Reports Strong 2025 Growth](https://finance.yahoo.com/news/york-times-reports-strong-2025-165700176.html)
- [Digital Content Next: State of Subscriptions 2025](https://digitalcontentnext.org/blog/2025/09/25/state-of-subscriptions-2025-pushing-past-the-paywall-plateau/)
- [Digiday: Apple News Ad Monetization Abysmal](https://digiday.com/media/media-briefing-apple-news-ad-monetization-still-abysmal-for-some/)

## 1.8 The AI Era (2023-Present): The Zero-Click Extinction Event

AI answers questions directly, eliminating the need to click through to publishers:

- Zero-click searches increased from 56% to 69% (May 2024 to May 2025)
- Google organic search traffic to publishers down 33% globally, 38% in the US (Nov 2024-Nov 2025)
- Business Insider: organic search traffic down 55%. HuffPost lost half of search referrals.
- Small publishers (1K-10K daily pageviews): down 60%, some losing 90-95% of Google traffic

AI chatbot referrals are not a replacement: despite 200% growth in ChatGPT referrals, chatbots account for less than 1% of all pageview referrals. Not remotely close to offsetting losses.

AI licensing has emerged as a new revenue hope. Total commitments: ~$2.92B across all deals. Average deal: ~$24M. News Corp + OpenAI: $250M+ over 5 years. Financial Times + OpenAI: $5-10M/year.

**But the math doesn't add up.** Columbia study estimates fair payment from Google alone: $10-12B/year. Actual AI licensing across ALL companies: ~$817M in 2024. That's 7-8% of what one study says Google alone owes. Publishers expect traffic to decline another 43% over the next three years.

**Sources**:

- [Press Gazette: Google Traffic Down a Third](https://pressgazette.co.uk/media-audience-and-business-data/google-traffic-down-2025-trends-report-2026/)
- [AdExchanger: AI Search Reckoning](https://www.adexchanger.com/publishers/the-ai-search-reckoning-is-dismantling-open-web-traffic-and-publishers-may-never-recover/)
- [Digiday: Timeline of Publisher-AI Deals 2025](https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/)

## 1.9 The Demand Side: How People Actually Find Information Now

Everything above tells the supply side - what happened to publishers and platforms. But any content strategy ultimately needs to reach people. Here's where those people actually are, and how they discover information in 2026. The answer is not what most corporate content strategies assume.

### The Fragmented Discovery Journey

Consumers no longer follow a linear path from search to content to action. The average consumer bounces between **3.6 platforms** before making a decision, taking up to 10 weeks and 97 interactions. A typical journey: discover on TikTok, research on Reddit, check with ChatGPT, read a review on a publisher site, watch a YouTube video, buy on Amazon. The "funnel" is dead. Discovery is non-linear, multi-platform, and increasingly happens by accident.

### Where People Get News (2025-2026)

**Social media dominates**, especially for younger demographics:


| Platform  | % of US adults who regularly get news there | Trend                             |
| --------- | ------------------------------------------- | --------------------------------- |
| Facebook  | 38%                                         | Declining slowly                  |
| YouTube   | 35%                                         | Stable/growing                    |
| Instagram | 20%                                         | Growing                           |
| TikTok    | 20%                                         | Fastest-growing (from 3% in 2020) |
| X/Twitter | 12%                                         | Declining                         |
| Reddit    | 9%                                          | Growing fast                      |


**Among adults under 30**: 43% regularly get news on TikTok (up from 9% five years ago), surpassing YouTube (41%) and Facebook (41%). Social media beats every other format for news consumption among young adults - 76% get news from social, vs. 60% from news websites and 28% from email newsletters.

**The critical insight**: 52% of TikTok users look at news, but only 14% follow news accounts. They're encountering news through the algorithm, not by seeking it out. News finds them; they don't find news. This is fundamentally different from every previous distribution model - and it means traditional content distribution (publish, optimize for search, hope people click) misses the majority of how younger audiences encounter information.

### TikTok as a Search Engine

TikTok is no longer just entertainment. It's now a primary search tool, especially for Gen Z:

- **64% of Gen Z** use TikTok as a search engine (Adobe)
- **Google confirmed** that over 40% of Gen Z prefer TikTok or Instagram over Google for search
- **Google usage among Gen Z** has dropped nearly 25% compared to Gen X
- **41% of Gen Z** now turn to social media first for information, surpassing the 32% who default to traditional search engines (Sprout Social Q2 2025)

This represents the most significant shift in information-seeking behavior since Google displaced Yahoo in the early 2000s. For any content team: if your target audience is under 35, they may encounter your content on TikTok before they ever see it in a search engine or AI chatbot.

### Reddit: The Stealth Search Engine

Reddit has become an under-the-radar information powerhouse:

- **80 million weekly search users** (Q4 2025), up from 60 million the prior year
- **Reddit Answers** (AI-powered search) queries jumped from 1M to 15M in Q4 2025
- Reddit posts appear in **20%+ of Google search results**. For product and review queries, Reddit appears **97% of the time**
- Reddit became the **#1 source for AI-generated search results** in June 2025 - 40.1% of all LLM citations came from Reddit (Statista), ahead of Wikipedia (26.3%) and YouTube (23.5%)
- Two-thirds of US consumers use Reddit like a search engine weekly. 41% think Reddit gives better answers than Google for certain questions

**Why this matters for AI content**: Reddit is where real humans share real opinions. LLMs are trained on it. AI search cites it more than any other source. If your content reads like corporate marketing and Reddit threads read like authentic human experience, the AI will prefer Reddit. This is not hypothetical - it's already happening.

### AI Chatbots as Information Sources

AI is emerging as a distinct information channel, especially for younger users:

- **64% of US teens** (13-17) have used AI chatbots, with 28% using them daily (Pew, February 2026)
- **57% of teen chatbot use** is for information search (ahead of schoolwork at 54% and entertainment at 47%)
- **ChatGPT dominates**: 59% of teen chatbot users use ChatGPT, vs. 23% Gemini, 20% Meta AI. Microsoft Copilot lags behind.
- **50% of consumers** now use AI-powered search, but 60% of those searches result in zero clicks to external websites

AI is compressing the discovery and research stages into a single conversation. Instead of searching "best winter boots" and clicking through 10 results, users ask ChatGPT a detailed question and get a single synthesized answer. This is the zero-click problem at its most extreme - and it's the behavior content marketplaces are designed to monetize.

### The Trust Crisis

The audience that content teams are trying to reach doesn't trust institutional media:

- **28% of Americans** trust mass media (Gallup 2025) - an all-time low, down from 68% in 1972
- Trust has hit record lows across all groups: Republicans (8%), Democrats (51%), Independents (27%)
- Among adults under 65, trust is **below 28%** in every age bracket
- Globally, trust in news held at about **40%** for the third straight year (Reuters Institute 2025), with the US among the lowest
- **72% of Gen Z** hold negative or cautious views toward AI-generated content
- **56% of Gen Z** are more likely to trust brands committed to publishing content created by humans
- Paradox: 60% of Gen Z still place their ultimate trust in traditional newspapers, even while getting most of their news from TikTok. They view social platforms as "rapid awareness engines," not definitive sources

**The implication for content strategy**: Any organization writing for a broad audience faces the same problem - institutional content competes against an audience that distrusts corporate messaging, prefers social discovery, and trusts Reddit more than brand blogs. The corporate blog post optimized for enterprise SEO reaches IT decision-makers, but it doesn't reach the consumer audience that lives on TikTok, YouTube, and Reddit.

### The Budget Mismatch

The industry hasn't caught up to consumer behavior:

- Brands spend **$74.9 billion/year** on SEO, with **90%+ going to Google optimization**
- TikTok, YouTube, Pinterest, Reddit, and ChatGPT combined get **10% of the budget** but drive **over 60% of discovery** in a 2026 consumer journey
- Creators and influencers are driving a shift toward personality-led information, at the expense of institutional media. Politicians, executives, and celebrities increasingly bypass traditional media entirely, giving interviews to podcasters and YouTubers instead.

### What This Means for the Briefing

The rest of this document focuses heavily on the supply side - how content is created, licensed, attributed, and monetized. But every decision about content strategy should be pressure-tested against the reality of how people actually consume information:

- **A grounding citation** reaches the user inside an AI answer - but the largest AI chatbot has 440M DAU while TikTok has 1B+
- **A corporate blog post** ranks on Google - but Gen Z is 25% less likely to use Google than Gen X
- **An enterprise whitepaper** reaches CIOs - but the developers those CIOs manage get their information from Reddit, YouTube, and GitHub
- **A carefully attributed AI response** addresses the legal problem - but the user who asked the question may not care about or even notice the attribution

The supply-side infrastructure matters. But the demand side determines whether anyone sees it.

**Sources**:

- [Pew Research: 1 in 5 Americans regularly get news on TikTok](https://www.pewresearch.org/short-reads/2025/09/25/1-in-5-americans-now-regularly-get-news-on-tiktok-up-sharply-from-2020/)
- [Pew Research: 8 Facts About Americans and TikTok (March 2026)](https://www.pewresearch.org/short-reads/2026/03/02/8-facts-about-americans-and-tiktok/)
- [Pew Research: Social Media and News Fact Sheet](https://www.pewresearch.org/journalism/fact-sheet/social-media-and-news-fact-sheet/)
- [Gallup: Trust in Media at New Low of 28%](https://news.gallup.com/poll/695762/trust-media-new-low.aspx)
- [Reuters Institute: Digital News Report 2025](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025)
- [Reuters Institute: Journalism Trends and Predictions 2026](https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026)
- [Sprout Social: Social Media Search 2026](https://sproutsocial.com/insights/social-media-search/)
- [Sprout Social: How Gen Z Uses Social Media](https://sproutsocial.com/insights/gen-z-social-media/)
- [HBR: How Gen Z Uses Gen AI - And Why It Worries Them](https://hbr.org/2026/01/how-gen-z-uses-gen-ai-and-why-it-worries-them)
- [Search Engine Land: Social Search Visibility](https://searchengineland.com/social-search-visibility-evolution-471685)
- [ALM Corp: Where People Search in 2026](https://almcorp.com/blog/where-people-search-online-2026/)
- [Rise at Seven: How People Search in 2026](https://riseatseven.com/blog/how-people-search-2026/)

---

# 2. The Pattern

Every transition follows the same playbook:


| Platform                             | Promise                                 | Outcome                                                                                            |
| ------------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **AOL/Yahoo Portals (1995)**         | "We'll bring you massive audience"      | Portals controlled ad inventory; publishers became content suppliers                               |
| **Google Search (2000s)**            | "We send you traffic for free"          | Publishers became SEO-dependent; Google kept 77%+ of ad revenue                                    |
| **Google News (2002)**               | "We drive clicks to your articles"      | Aggregated without payment; showed enough info users didn't click                                  |
| **Facebook Instant Articles (2015)** | "4x faster, access to our audience"     | Stripped identity, cannibalized monetization; shut down 2023                                       |
| **Facebook Pivot to Video (2016)**   | "Video is the future"                   | Inflated metrics 150-900%; publishers bankrupted; Facebook paid $0                                 |
| **Facebook News Tab (2019)**         | "We'll pay to license your content"     | Killed 2024; deals not renewed; "no new commercial deals for news"                                 |
| **Apple News+ (2019)**               | "Access to millions of iPhone users"    | Apple takes 50%; publishers get "one-twentieth" of promised revenue                                |
| **TikTok/Short-Form (2020s)**        | "The algorithm will find your audience" | Creators bypass publishers entirely; 43% of under-30s get news here; no revenue flows to newsrooms |
| **AI Licensing (2024)**              | "We'll pay for your content"            | $817M/year total vs. $2B+/year destroyed in traffic                                                |


Each transition concentrated power in fewer hands: thousands of local newspaper monopolies -> ~5 portals -> 1 search engine (90% share) -> 2 companies (Google + Facebook, 60% of digital ad dollars) -> TikTok/YouTube/Reddit (algorithm-driven, creator-led, no publisher in the loop) -> 3-4 AI companies controlling the interface between publishers and readers.

The revenue arc: $49B (2000) -> $6B (2023) in newspaper advertising. Meanwhile Google's own ad revenue: $300B+ (2025).

**The question**: Are AI content marketplaces genuinely different from every previous platform promise, or is this Google News 3.0? The rest of this document explores that question.

---

# 3. The Agentic Web Narrative

## 3.1 What Microsoft Means by "Agentic Web"

Microsoft introduced the concept at Build 2025 (May 2025). Nadella: "In 2025, we're building out this open agentic web at scale."

The idea: just as the original web was built on open protocols (HTTP, HTML) that let browsers navigate pages, the agentic web will be built on open protocols that let AI agents navigate, reason about, and take actions across services. Instead of humans clicking through search results, AI agents retrieve information, synthesize it, and act on your behalf.

**The key pillars**:

1. **Open protocols**: Microsoft joined the MCP (Model Context Protocol) Steering Committee, pushing open standards for agent interoperability. MCP lets agents connect to external tools and data sources through a standardized interface.
2. **NLWeb**: Microsoft's open-source project positioned as "HTML for the agentic web." Created by R.V. Guha (creator of RSS, RDF, and Schema.org). NLWeb lets any website expose a natural language interface that AI agents can query, using existing structured data (Schema.org, RSS). Each NLWeb implementation is an MCP server. Key components: AskAgent (core query agent), AgentFinder (discovery service), DataFinder (NL-to-SQL), ModelRouter (LLM routing). Early adopters: Common Sense Media, Eventbrite, O'Reilly Media, Shopify, Tripadvisor.
3. **PCM as the economic layer**: If NLWeb is how agents access content, PCM is how content owners get paid. The agentic web needs an economic model.
4. **Platform play**: Just as Windows + Office dominated the desktop era, Microsoft is positioning Copilot + Azure + M365 as the backbone of the agent era. 230,000+ organizations have used Copilot Studio to build agents.

**The content narrative**: "As AI shifts from search results to conversational answers, content quality becomes mission-critical." Microsoft is positioning itself as building the responsible version of the AI-powered web. The framing: premium, licensed content is required for AI agents to function reliably in high-stakes domains (healthcare, finance, legal).

**The Gartner reality check**: Jason Wong, distinguished VP analyst: the agentic web "paints a compelling vision for open interoperability, but we are still very early in the primordial soup of agentic standards."

**Sources**:

- [Microsoft Build 2025: The age of AI agents and the open agentic web](https://blogs.microsoft.com/blog/2025/05/19/microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/)
- [Microsoft: Introducing NLWeb](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/)
- [NLWeb GitHub repository](https://github.com/microsoft/NLWeb)
- [VentureBeat: Microsoft announces 50+ AI tools for the agentic web](https://venturebeat.com/ai/microsoft-announces-over-50-ai-tools-to-build-the-agentic-web-at-build-2025/)

---

# 4. MSN and the Publisher Pipeline

MSN is the third-largest English-language news website in the world. Microsoft claims reach of up to **1 billion users** across its consumer properties: Edge (which drives 60% of MSN volume as the default new tab page), Windows taskbar/widgets, Bing, Outlook, Xbox, and the MSN app. Monthly visits to msn.com alone were ~982 million in February 2026.

This is Microsoft's largest consumer content surface and it's been **AI-edited since 2020**. Video consumption grew 40% overall in 2025, with 80% growth among Gen Z viewers.

The key insight: **Microsoft already has massive consumer content distribution. The problem isn't reach - it's what gets distributed through it.**

MSN has a direct precedent for PCM: MSN used to require individually negotiated contracts with publishers. They switched to click-to-sign and now have 18,000 brands. PCM is designed to follow the same arc.

**Sources**:

- [Semrush: msn.com traffic overview](https://www.semrush.com/website/msn.com/overview/)
- [Press Gazette: Top 50 US news websites](https://pressgazette.co.uk/media-audience-and-business-data/media_metrics/most-popular-websites-news-us-monthly-3/)
- [Microsoft Ads Blog: Valuable consumers at Microsoft media](https://about.ads.microsoft.com/en/blog/post/april-2025/psst-the-valuable-consumers-are-over-at-microsoft-medias-ai-powered-experiences)

---

# 5. PCM - Product and Technical Details

## 5.1 What It Is

The Publisher Content Marketplace launched February 3, 2026. Led by **Nikhil Kolar, VP at Microsoft AI**. It's a platform that pays publishers when their content powers AI services like Copilot.

**The problem it solves**: Every AI answer engine was individually negotiating with publishers, often for months. Low trust, high friction, not scalable. Kolar: "What is a low-friction, high-trust, scalable way to make content available for AI engines and a way for content publishers to get compensated for the premium content?"

## 5.2 How It Works

**Supply side (publishers)**: Publishers define licensing terms, usage parameters, and pricing. They retain ownership and editorial independence. Participation is voluntary with clear opt-in/opt-out.

**Demand side (AI builders)**: Microsoft's first-party demand comes from two Copilots - M365 Copilot (enterprise) and MAI Copilot (consumer). External demand partners like Yahoo are being onboarded. Long-term vision: "any AI builder. Anyone building an agent. And it can be used on Azure."

**Grounding vs. training** - this is the single most important technical distinction in AI content licensing:

- **Training** is when content gets absorbed into the model's weights during the learning process. Millions of articles are fed through the neural network over weeks of computation, and the model learns statistical patterns from them. Once training is complete, the content is "baked in" - it exists as distributed numerical weights, not as retrievable text. This is what the NYT lawsuit is primarily about: OpenAI scraped Times articles to train GPT. The content is now inseparable from the model itself. You can't "un-train" on specific articles without retraining from scratch.
- **Grounding** (also called retrieval-augmented generation / RAG) is when content is fetched at query time and placed into the model's context window alongside the user's question. The model reads the retrieved content and synthesizes a response from it, but the content never becomes part of the model's permanent weights. It's more like an open-book exam than memorization. When the query is done, the retrieved content leaves the context window.

**Why this matters for PCM:**

- **Legally**: Training without a license is the core claim in every AI copyright lawsuit. Grounding from licensed sources avoids that claim entirely - the content was never scraped into training data. (Though the legal distinction between training and grounding has not yet been directly adjudicated by any court.)
- **Commercially**: Training deals are one-time lump sums (News Corp's $250M/5yr with OpenAI). Grounding deals can be per-use, creating recurring revenue that scales with actual consumption - the model PCM is built on.
- **For content quality**: Grounded responses can cite specific, current sources. Trained knowledge goes stale the moment training ends and can't point back to where it learned something. Grounding enables attribution; training makes attribution nearly impossible.
- **The unsolved overlap**: If a model was pre-trained on a publisher's content AND retrieves that same content at inference time via grounding, how much of the response came from each? This is the "training vs. grounding blur" problem (see Section 7.2), and nobody has solved it.

**Pricing**: Still experimental. Guiding principle: pay for demonstrated value. Kolar: "Sometimes, the value may be: 'I just need to know the score.' In some cases, the value will be associated with a particular source." Illustrative analyst models (not confirmed by Microsoft):

- Mid case: 10M tokens/month, $0.02/token, 25% royalty = ~$50K/month
- High case: 100M tokens/month = approaching $6M/year
- Long tail: 500K tokens = ~$12K/year

**Bring-your-own-license**: Publishers with existing deals can use PCM as infrastructure to deliver those agreements.

**Current partners**: Supply - AP, Business Insider, Conde Nast, Hearst Magazines, People, USA TODAY, Vox Media. Demand - Microsoft Copilot, Yahoo (onboarding).

**Publisher sentiment**: According to Digiday, Microsoft is "the unexpected darling of AI licensing deals." Top score among AI companies for collaboration, willingness to pay, and well-behaved crawlers.

## 5.3 Open Questions

- Attribution accuracy for composite responses (see Chapter 7)
- Pricing power concentration risk (see Chapter 11)
- No actual payout data yet
- Geographic complexity (EU AI Act, Digital Markets Act)
- Book publishers excluded - currently news/magazine focused
- Ongoing litigation (NYT, The Intercept, others - see Chapter 10)

**Sources**:

- [Microsoft Ads Blog: Building Toward a Sustainable Content Economy for the Agentic Web](https://about.ads.microsoft.com/en/blog/post/february-2026/building-toward-a-sustainable-content-economy-for-the-agentic-web)
- [Digiday Q&A: Nikhil Kolar on scaling PCM](https://digiday.com/media/qa-nikhil-kolar-vp-microsoft-ai-scales-its-click-to-sign-ai-content-marketplace/)
- [Digiday: Publishers rate Big Tech's AI licensing deals](https://digiday.com/media/publishers-scorecard-for-big-techs-ai-licensing-deals/)
- [Windows Central: Publisher Content Marketplace announcement](https://www.windowscentral.com/microsoft/microsoft-publisher-content-marketplace-announcement)

---

# 6. How LLMs Actually Generate Answers (And Where Attribution Breaks)

Understanding attribution requires understanding how every major AI answer engine works under the hood. The architecture is remarkably similar across products - ChatGPT, Copilot, Gemini, Perplexity, and Claude all follow the same pattern. The details differ, but the pipeline is universal - and so are the places where attribution fails.

## 6.1 The Core Architecture: Retrieval-Augmented Generation (RAG)

Every major AI product that answers questions with citations uses some version of RAG. The idea is simple: instead of relying solely on what the model memorized during training, fetch relevant documents at query time and give the model fresh context to work with.

RAG has three components:

1. **A content index** - a searchable database of documents, web pages, or enterprise files. Content is pre-processed: crawled, cleaned, split into chunks (typically 256-1,024 tokens each), and stored with metadata (source URL, title, author, date).
2. **An embedding model** - a smaller neural network that converts text into numerical vectors (arrays of ~768-3,072 numbers). Semantically similar text maps to nearby points in vector space. "inflation rate" and "consumer price index" would be close together; "inflation rate" and "tire pressure" would not. Every chunk in the index gets embedded. Every user query gets embedded. Retrieval = finding the chunks whose vectors are closest to the query vector.
3. **A large language model (LLM)** - the model that reads the retrieved chunks alongside the user's question and generates a response. This is GPT-4 (OpenAI/Microsoft), Gemini (Google), Claude (Anthropic), etc. The LLM has two knowledge sources: its parametric knowledge (what it learned during training, baked into weights) and the retrieved context (what was fetched for this specific query). It blends both when generating a response.

## 6.2 The Retrieval Pipeline: How Sources Get Selected

When you ask an AI a question, here's what happens before the model writes a single word:

**Step 1 - Query understanding:** The system analyzes your question to determine intent. Complex queries may be decomposed into sub-queries ("What's the best laptop for video editing under $1,500?" becomes searches for laptop specs, video editing requirements, and pricing).

**Step 2 - Query rewriting:** The LLM or a specialized model rewrites your natural language question into optimized search queries. "Why is inflation still high?" might become multiple retrieval queries like "inflation rate 2026 causes," "Federal Reserve interest rate policy," "consumer price index trends."

**Step 3 - Hybrid search:** Modern systems don't rely on a single retrieval method. They run two searches in parallel:

- **Keyword search (BM25):** Traditional text matching. Fast, good at exact terms and names.
- **Vector/semantic search:** Embedding-based similarity. Good at meaning, bad at exact terms.
- Results from both are merged using algorithms like **Reciprocal Rank Fusion (RRF)**, which combines rankings without needing to compare scores directly.

**Step 4 - Reranking:** The initial search returns dozens or hundreds of candidates. A **cross-encoder reranker** (a smaller transformer model) takes the top 20-50 results and rescores them. Unlike embedding search, the reranker processes the query and each document together, capturing fine-grained relevance. This is the most accurate but most expensive retrieval step.

**Step 5 - Context assembly:** The top 5-15 reranked chunks are assembled into the LLM's context window alongside the user's query and system instructions. This assembled prompt is what the model actually sees.

**What gets lost in this pipeline:** Metadata degrades at every step. A full article with author name, publication date, section, and copyright notice gets chunked into fragments. The fragment might retain a source URL as bookkeeping, but the rich metadata - who wrote it, when, under what license, how it relates to other content - is typically stripped or simplified. By the time content reaches the LLM's context window, it's anonymous text with a URL attached.

## 6.3 How the LLM Generates a Response

Once the context window is assembled, the LLM generates a response token by token:

1. **All input tokens are processed simultaneously** through the model's layers (GPT-4 class models have ~200 billion parameters across 120+ layers). Each token attends to every other token through "attention" mechanisms - this is where the model decides which parts of the retrieved context are relevant to which parts of the question.
2. **Tokens are generated one at a time.** The model outputs one token, feeds it back in as input, and generates the next. A 500-word response is roughly 650 tokens, each requiring a pass through the network.
3. **The model blends parametric and retrieved knowledge** with no explicit tracking of which is which. There is no internal mechanism that labels "this sentence came from retrieved chunk 3" vs. "this came from training data." The transformer's attention weights offer some signal, but they're distributed, noisy, and don't cleanly map to source attribution.

**What a single inference costs:** At GPT-4 scale, a standard query (input + output) costs roughly **$0.01-0.03** depending on context length and model size. This baseline cost is critical context for the attribution problem - every additional inference pass to measure source contribution multiplies this cost.

## 6.4 How Citations Are Generated - The Critical Finding

**There is no dedicated attribution engine in any major AI product.** Citations are generated by the LLM itself during the response synthesis step. The model receives retrieved chunks with metadata (source URL, title) and is instructed via prompt engineering to cite sources in its response. Citation is a text generation task, not a measurement.

This means:

- The model can cite a source it barely used, because the source was in the context window
- The model can fail to cite a source it heavily relied on, because citation is probabilistic
- The model can hallucinate citations - generating plausible-looking URLs or attributing claims to sources that don't support them
- There is no ground truth for "which source contributed what" - only the model's self-report, which is unreliable

**The invisible usage problem**: Otterly.AI found content was "used" by AI **44,469 times** but visibly cited only **169 times** - meaning **99.6% of AI content usage is invisible and unattributed**. This isn't a bug in one product - it's structural to how RAG citation works across the industry.

## 6.5 How Different Products Implement This

The architecture above is universal. The implementations vary:


| Product           | Retrieval Source                                                | LLM                              | Citation Approach                             |
| ----------------- | --------------------------------------------------------------- | -------------------------------- | --------------------------------------------- |
| Microsoft Copilot | Bing index (web), Microsoft Graph (enterprise), Azure AI Search | OpenAI GPT-4 class               | LLM-generated from retrieved metadata         |
| ChatGPT           | Bing index (via browsing tool), uploaded files                  | OpenAI GPT-4o/GPT-5              | LLM-generated, inline links                   |
| Google Gemini     | Google Search index                                             | Gemini Pro/Ultra                 | LLM-generated, "Google it" verification links |
| Perplexity        | Custom web index + Bing                                         | Multiple (GPT-4, Claude, custom) | LLM-generated, numbered inline citations      |
| Claude            | No built-in web search (tool use for retrieval)                 | Anthropic Claude                 | LLM-generated when retrieval tools are used   |


**Microsoft-specific details:** Copilot uses Azure AI Search with hybrid search (BM25 + vector) and a two-stage reranker adapted from Bing's web search models. M365 Copilot accesses enterprise content through Microsoft Graph's Semantic Index. Consumer Copilot grounds from Bing's pre-built web index - it does not crawl live. File grounding cap: 20 files maximum.

## 6.6 Why This Architecture Makes Attribution So Hard

The RAG pipeline creates three distinct attribution problems:

**Problem 1 - Ingestion gap:** Content is chunked, stripped of rich metadata, and embedded. Provenance information degrades. C2PA cryptographic credentials (if they existed on the source) are discarded. By the time content is in the vector store, it's anonymous.

**Problem 2 - Retrieval != contribution:** A document can be retrieved (placed in the context window) without contributing anything to the final answer. Conversely, a document might heavily shape the response despite ranking low in retrieval. The retriever measures relevance to the query; what matters for attribution is influence on the output. These are different things.

**Problem 3 - Generation is opaque:** The transformer blends retrieved context with parametric knowledge through distributed attention patterns. There is no internal log of "this token was generated because of chunk 3." Attribution after the fact is inference about inference - using heuristics to guess what the model actually did. Current approaches (Chapter 9) are all different flavors of this guesswork, at different levels of sophistication and cost.

**The fundamental problem:** Attribution requires knowing contribution at the generation stage, but we only have reliable tracking at the ingestion stage. The middle - retrieval through generation - is opaque by design. This isn't a limitation of current implementations that better engineering will fix. It's inherent to how transformer-based language models work.

**Sources**:

- [Microsoft Learn: RAG in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [Microsoft Cloud Blog: Common RAG Techniques Explained](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/02/04/common-retrieval-augmented-generation-rag-techniques-explained/)
- [Zenity Labs: Inside Microsoft Copilot's RAG System](https://labs.zenity.io/p/a-look-inside-copilot-rag-system)
- [Otterly.AI: Bing AI Performance Report Analysis](https://otterly.ai/blog/bing-webmaster-tools-ai-performance-report/)
- [Bing Blog: AI Performance in Webmaster Tools](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- [Lewis et al.: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (NeurIPS 2020)](https://arxiv.org/abs/2005.11401)
- [Pinecone: What is Retrieval-Augmented Generation](https://www.pinecone.io/learn/retrieval-augmented-generation/)

---

# 7. Can Attribution Work?

## 7.1 The CJR Study (March 2025)

The Tow Center for Digital Journalism tested eight AI search tools (including Copilot) on citation accuracy:

- **Over 60% of queries produced incorrect citations across all platforms**
- Premium/paid chatbots were more confidently wrong than free versions
- Fabricated URLs were persistent - Gemini and Grok produced more fake links than real ones
- **Content licensing deals provided no guarantee of accurate citation**
- Chatbots directed users to syndicated versions rather than original sources
- Chatbots rarely declined to answer questions they couldn't answer accurately

## 7.2 The Core Technical Challenges

**Retrieval vs. influence**: RAG systems log which documents were retrieved as context. But "retrieved" is not "used." An LLM might retrieve five articles and meaningfully use two. Current systems can't distinguish between documents that shaped the response and those that were retrieved but ignored.

**Composite responses**: Most answers synthesize multiple sources. Apportioning credit is an active research problem (see Chapter 8).

**Hallucination with citations**: The AI confidently generates a response with a footnote pointing to a source that doesn't support the claim. The source is real but misrepresented.

**Training vs. grounding blur**: If a model was pre-trained on a publisher's content AND retrieves that same content at inference time via grounding, how much of the response came from each? Unsolved. This affects every AI product that uses RAG on top of a broadly trained model.

## 7.3 The Bottom Line

Every major AI product's attribution is retrieval-based, not influence-based. They can tell you which documents were in the context window. They cannot reliably tell you which ones shaped the answer. Revenue allocation across the industry will be a policy decision (business rules about splitting), not a technical measurement - for the foreseeable future. Anyone claiming otherwise is ahead of the science.

For the commercial landscape of companies attempting to solve this (ProRata, TollBit, Geodesix, Bria, Perplexity, Encypher), see Chapter 9.6.

**Sources**:

- [CJR/Tow Center: AI Search Has a Citation Problem](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)
- [Fortune: AI search engines are confidently wrong](https://fortune.com/2025/03/18/ai-search-engines-confidently-wrong-citing-sources-columbia-study/)

---

# 8. The Shapley Value Problem

## 8.0 A Quick Primer on Inference (What Happens When You Ask an AI a Question)

Before the Shapley cost numbers make sense, you need to understand what "inference" means - because the entire attribution cost problem is measured in multiples of it.

**Inference** is the act of running a query through a trained AI model to get a response. When you type a question into any AI chatbot, here's what happens at the hardware level:

1. **Your query gets tokenized** - broken into tokens (roughly word-pieces). "What are the latest unemployment numbers?" becomes something like 8 tokens.
2. **Retrieved content gets added** - The RAG pipeline (Chapter 6) fetches relevant documents and places them in the context window alongside your query. A typical grounded response might have 2,000-4,000 tokens of retrieved context.
3. **The model processes the full context** - All those tokens flow through the neural network's layers (GPT-4 class models have roughly 200 billion parameters across 120+ layers). Each token interacts with every other token through "attention" mechanisms. This is the expensive part - it requires massive GPU computation.
4. **Tokens are generated one at a time** - The model outputs one token, feeds it back in, and generates the next. A 500-word response is roughly 650 tokens, each requiring a pass through the network.

**What a "forward pass" costs**: A single forward pass means running one set of inputs through the entire model once. At GPT-4 scale, this involves multiplying matrices with hundreds of billions of numbers across specialized GPU hardware. The industry benchmark for a standard query (input + output) is roughly **$0.01-0.03** depending on context length and model size.

**Why this matters for attribution**: Every attribution method that goes beyond simple heuristics requires running the model *additional times* to measure each source's contribution. If you want to know "what would the response look like without Source A?", you have to run inference again without Source A. If you have 15 sources, you might need to run inference thousands of times per query just to compute fair attribution. That's the Shapley problem.

## 8.1 The Game Theory Behind Shapley Values

The Shapley value comes from cooperative game theory, not AI. Understanding its origins explains both why it's the "right" answer for attribution and why it's impractical.

**The original problem (1953)**: Economist Lloyd Shapley asked a deceptively simple question: if a group of players cooperate in a coalition and earn a joint profit, how should they divide the payout fairly? Imagine three companies jointly bid on a contract worth $1M. Company A's expertise was essential, Company B's was helpful, Company C's was marginal. How much does each deserve?

**The key insight**: A player's fair share should equal their *average marginal contribution* across all possible orderings of the coalition. In other words:

- Imagine every possible order the players could have joined the coalition
- For each ordering, calculate how much value increased when each player joined
- Each player's Shapley value is their average marginal contribution across all orderings

**Why this works for simple models**: In a linear regression (where the output is just a weighted sum of inputs), attribution is trivial - each feature's contribution is its weight times its value. You can read attribution directly from the model's coefficients. No iteration needed.

**Why it breaks for complex models**: Neural networks aren't linear. Features interact in non-linear, deeply nested ways. You can't just read off coefficients. Two alternative approaches emerged:

- **LIME** (2016): Approximate the complex model with a simple local linear model around each prediction, then read off that model's coefficients. Fast but approximate and unstable.
- **Shapley values**: Compute the exact fair attribution by evaluating every possible coalition of features. Provably fair but computationally explosive.

**The four fairness axioms** that make Shapley values unique - no other method satisfies all four simultaneously:

1. **Efficiency** - All attribution sums to the total value. No value is unaccounted for, none is double-counted. If a response is worth $1, the sources' shares sum to exactly $1.
2. **Symmetry** - If two sources contribute equally in every possible coalition, they get equal credit. No arbitrary favoritism.
3. **Dummy player** - A source that contributes nothing to any coalition gets zero. You don't pay for content that wasn't used.
4. **Additivity** - If you combine two independent games (e.g., two separate queries), the attribution for each player is the sum of their attributions in each game. No weird interaction effects from aggregation.

**The Nobel Prize (2012)**: Shapley shared the Nobel in Economics with Alvin Roth for the theory of stable allocations and the practice of market design. The Shapley value had become foundational in economics, political science (voting power analysis), cost allocation, and eventually machine learning interpretability.

**Applied to AI content attribution**: Replace "players" with "retrieved documents" and "coalition profit" with "response quality/usefulness." The Shapley value tells you exactly how much each source document contributed to the final response. It's the mathematically provable fair answer to "how much should we pay The Guardian for this query?"

The problem is computing it.

## 8.2 Why It's Intractable

Computing exact Shapley values is #P-hard. For n sources, it requires evaluating 2^n subsets (every possible coalition):


| Sources per query | Coalitions to evaluate | Forward passes needed |
| ----------------- | ---------------------- | --------------------- |
| 5                 | 32                     | 32                    |
| 10                | 1,024                  | 1,024                 |
| 15                | 32,768                 | 32,768                |
| 20                | ~1 million             | ~1 million            |


A typical RAG response draws on 10-20 retrieved passages. At 15 sources, that's 32,768 forward passes per query for exact Shapley. Each forward pass means running the entire model (hundreds of billions of parameters) once. Multiply the cost of one query by 32,768.

**At production scale**: A normal query costs roughly $0.01 in inference. Exact Shapley at 15 sources: 32,768 x $0.01 = roughly **$320/query**. A major AI chatbot handles roughly 100M queries/day. That's **roughly $32 billion/day** just for attribution - more than any AI company's annual revenue.

Even Monte Carlo approximation (randomly sampling roughly 45 orderings instead of all 32,768) costs roughly $0.45/query, or roughly $16B/year. Embedding similarity (what's actually feasible) adds negligible cost but provides no fairness guarantees.

## 8.3 The State of Research

**TokenShapley** (ACL 2025): Token-level attribution using KNN-Shapley approximation. 11-23% accuracy improvement over baselines. But token-level attribution doesn't directly translate to "how much should we pay The Guardian."

**In-Run Data Shapley** (ICLR 2025): First method to compute training data Shapley during a single training run. Found 16% of training corpora had negative Shapley values. But only demonstrated at GPT-2 scale.

**Cluster Shapley** (2025): Groups similar documents, computes Shapley over clusters. Reduces complexity but still requires orders-of-magnitude more compute than inference.

## 8.4 What This Means

No production system uses formal Shapley values for content revenue allocation. ProRata uses proprietary "algorithmic attribution" that may be Shapley-inspired but is unauditable. The practical path: heuristic attribution (embedding similarity + claim decomposition) dressed in Shapley-inspired language, with fairness properties that are "approximately" correct but not provably so.

**Sources**:

- [TokenShapley (ACL 2025)](https://aclanthology.org/2025.findings-acl.200/)
- [Data Shapley in One Training Run (ICLR 2025)](https://arxiv.org/abs/2406.11011)
- [Shapley Value - Interpretable ML Book](https://christophm.github.io/interpretable-ml-book/shapley.html)
- [Fair Document Valuation via Shapley Values](https://arxiv.org/abs/2505.23842)

---

# 9. Beyond Shapley: Emerging Attribution Approaches

Chapter 8 showed that exact Shapley values are computationally intractable at LLM scale. But the attribution problem hasn't stopped attracting researchers. Several independent threads are converging on alternative approaches - from embedding-based uniqueness to trainable citation models to counterfactual removal experiments. This chapter maps those threads, the companies commercializing them, and the specific gap where they haven't been connected.

## 9.1 The Citation Rank Hypothesis

**Core idea**: In academia, citation count is a revealed-preference signal for human-judged importance. If thousands of researchers independently decide to cite a paper, they're collectively saying "this contributed unique value." Can that signal be detected - and predicted - in embedding space?

### The Foundational Work

**Uzzi et al. (2013)**: Brian Uzzi, Satyam Mukherjee, Michael Stringer, and Ben Jones at Northwestern analyzed 17.9 million scientific papers across all fields and found a striking pattern: the highest-impact science is primarily grounded in *exceptionally conventional* combinations of prior work yet simultaneously features an intrusion of *unusual* combinations. Papers with this "conventional + atypical" profile were **2x as likely to be highly cited**. They measured this by computing z-scores of co-citation pair frequencies. Published in *Science* (vol. 342, 2013), this became foundational to the study of scientific novelty.

**Critical nuance**: Pure novelty *hurts* short-term citations. The highest-impact papers aren't the most distant outliers - they occupy a specific sweet spot of mostly conventional with selective atypical injections. Over the long term, however, high-atypicality papers are more likely to become "sleeping beauties" that accumulate outsized impact.

### The Embedding Evidence

The question is whether these patterns, discovered through co-citation analysis, also show up in vector/embedding space. Multiple research groups now confirm they do:


| Study                                                   | Year | Method                                                                                         | Key Finding                                                                                                                                                                   |
| ------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SPECTER** (Allen AI, ACL 2020)                        | 2020 | Citation-informed transformer embeddings                                                       | 94.8 nDCG on co-citation prediction; can embed new uncited papers                                                                                                             |
| **SPECTER2** (Allen AI)                                 | 2023 | Multi-task extension, 23 fields, 9 tasks                                                       | Task-adaptive embeddings improve further                                                                                                                                      |
| **Shibayama, Yin & Matsumoto** (PLOS ONE)               | 2021 | Word embeddings (scispaCy) measure semantic distance between cited references                  | **Novelty is a significant predictor of 10-year citation impact**. Open code available.                                                                                       |
| **Matsumoto, Shibayama et al.** (PLOS ONE)              | 2023 | "Element novelty" - paper's distance from universe in embedding space                          | Positive correlation with citation, consistent across fields                                                                                                                  |
| **Kojaku, Kim & Ahn** (*Science Advances*)              | 2026 | **Embedding Disruptiveness Measure (EDM)** - directional graph embeddings on citation networks | 10% increase in EDM percentile = **1.23x odds of milestone paper, 1.34x odds of Nobel Prize paper**. Outperforms traditional CD disruption index. Open-source Python package. |
| **Vital et al.** (arXiv / *Physica A*)                  | 2024 | GPT embeddings + Random Forest on 40,567 papers                                                | ~80% accuracy predicting top-20% cited papers from **text content alone**                                                                                                     |
| **AI-CITE**                                             | 2025 | SPECTER2 embeddings for citation forecasting, 100K papers                                      | SPECTER2 yields most informative representations for citation prediction                                                                                                      |
| **SemNovel** (Peng et al., *J. Biomedical Informatics*) | 2025 | LLM embeddings (Llama2-7B backbone) project all of PubMed into semantic space                  | **SemNovel score positively correlates with future citations**, independent of journal IF and author count                                                                    |
| **FastText + LOF** (*J. Informetrics*)                  | 2023 | Local Outlier Factor on FastText vectors                                                       | Successfully identifies faculty-recommended novel papers                                                                                                                      |
| **Wang** (*Information Processing & Mgmt*)              | 2026 | Neural embeddings of collaboration networks                                                    | Directly extends Uzzi framework into embedding space                                                                                                                          |


### The Key Nuance

**Shibayama et al.** found an important asymmetry: novelty measured as distance *between a paper's cited references* (inter-reference novelty) predicted citations well. But novelty measured from the *paper's own text* relative to the corpus showed insignificant or negative correlations. This suggests the signal is in the *combination* of ideas, not the surface-level text novelty.

### Open-Source Tools


| Tool                       | What It Does                                | Access                                                     |
| -------------------------- | ------------------------------------------- | ---------------------------------------------------------- |
| `embedding-disruptiveness` | Computes EDM from citation networks         | [PyPI](https://pypi.org/project/embedding-disruptiveness/) |
| Semantic Scholar API       | SPECTER2 embeddings for any paper           | [Free API](https://www.semanticscholar.org/product/api)    |
| Shibayama et al. code      | Word embedding novelty from reference lists | PLOS ONE supplementary                                     |
| SemNovel                   | LLM-based novelty scoring (biomedical)      | Academic code                                              |


**Sources**:

- [Uzzi et al., Science (2013)](https://www.science.org/doi/10.1126/science.1240474)
- [Kojaku et al., Science Advances (2026) - EDM](https://www.science.org/doi/10.1126/sciadv.adx3420)
- [Shibayama et al., PLOS ONE (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8253414/)
- [SPECTER - ACL 2020](https://aclanthology.org/2020.acl-main.207/)
- [Vital et al. (2024) - GPT Embeddings for Citation Prediction](https://arxiv.org/abs/2407.19942)
- [SemNovel - Peng et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/41242670/)

## 9.2 Data Influence Functions: Tracing Content Through Models

A parallel research thread asks: can you *measure* how much a specific piece of training data influenced a model's output?

**Influence functions** (Koh & Liang, 2017) estimate the effect of individual training points on test predictions without retraining. The core idea: if removing a single data point changes the model's prediction, that data point was influential. Elegant in theory; computationally brutal in practice (requires inverting high-dimensional Hessian matrices).

**TRAK** (Park et al., ICML 2023): "Tracing with Randomly-projected After Kernel." 2-3 orders of magnitude cheaper than comparable methods. Using only a handful of trained models, TRAK can match attribution methods requiring thousands of retrainings. Open source: [github.com/MadryLab/trak](https://github.com/MadryLab/trak).

### Recent LLM-Specific Advances


| Method                                         | Year | Key Innovation                                                                            | Scale Achieved             |
| ---------------------------------------------- | ---- | ----------------------------------------------------------------------------------------- | -------------------------- |
| **DDA** (Wu et al., EMNLP 2024)                | 2024 | Debias/denoise strategies for LLM attribution; 91.64% AUC                                 | LLaMA2, QWEN2, Mistral     |
| **TrackStar** (Chang et al., Google/ICLR 2025) | 2025 | **80,000x memory reduction**; retrieves influential examples from full pretraining corpus | **8B params, 160B tokens** |
| **Multi-Stage IF** (IJCAI 2025)                | 2025 | Traces influence from fine-tuned predictions back to pre-training data                    | Billions of parameters     |
| **SOURCE** (NeurIPS 2024)                      | 2024 | Supports multi-stage training (pre-train then fine-tune)                                  | Foundation model scale     |
| **Proxy Models** (Khaddaj et al., 2025)        | 2025 | 175-370x smaller proxy models approximate attribution of large models                     | Practical for production   |
| **Fast TDA via ICL** (ICML 2024)               | 2024 | In-context learning as alternative to TRAK (needs ~600GB GPU memory)                      | Large LLMs                 |


**TrackStar is the current frontier.** Key finding: there is a **misalignment between factual attribution and causal influence**. BM25 (keyword search) is better at finding passages that explicitly contain facts. But TrackStar identifies examples that cause larger probability increases for target facts - the training data that actually *shaped* the model's behavior. As models scale up, these two measures converge. Open source: [github.com/PAIR-code/pretraining-tda](https://github.com/PAIR-code/pretraining-tda).

**The gap**: These methods tell you which training data influenced a specific output. They don't yet operate at the speed or cost needed for real-time per-query attribution in any production system. The proxy model approach (Khaddaj 2025) is the most promising path to practical deployment.

**Sources**:

- [TRAK - ICML 2023](https://arxiv.org/abs/2303.14186) | [GitHub](https://github.com/MadryLab/trak)
- [TrackStar - ICLR 2025](https://arxiv.org/abs/2410.17413) | [GitHub](https://github.com/PAIR-code/pretraining-tda)
- [DDA - EMNLP 2024](https://aclanthology.org/2024.emnlp-main.782/)
- [Multi-Stage IF - IJCAI 2025](https://www.ijcai.org/proceedings/2025/0892.pdf)

## 9.3 Training Models to Cite: From RLHF to Objective Functions

Rather than computing attribution after the fact, what if you train the model to cite its sources correctly? And can you define a *trainable objective function* for "good attribution"?

### The Pioneering Systems

**WebGPT** (OpenAI, 2022): Fine-tuned GPT-3 to answer questions by browsing the web and citing sources. Trained on human demonstrations, then improved via RLHF.

**GopherCite** (DeepMind, 2022): 280B parameter model trained via RLHF to generate answers with exact supporting quotes. Key result: 80% of fact-seeking answers rated correct with satisfactory evidence. Pioneered the "cite or abstain" pattern - the model says "I don't know" when it can't ground an answer.

### Defining an Objective Function for Attribution Quality

**Huang et al. (ACL 2024)** made the most concrete progress. They defined three explicit, trainable reward signals:

- **R1**: Answer correctness
- **R2**: Citation recall (does the model cite all sources that support its claims?)
- **R3**: Citation precision (are cited sources actually relevant?)

Using rejection sampling + RL with these decomposed rewards, they trained LLaMA-2-7B to **outperform GPT-3.5-turbo** on citation benchmarks (ASQA, QAMPARI, ELI5). This is the closest thing to a trainable objective for attribution quality that exists today.

**SourceCheckup (Nature Communications, 2025)**: Provides the empirical baseline showing why this matters. Across seven LLMs and 58,000 statement-source pairs, **50-90% of responses are not fully supported by cited sources**. Even GPT-4o with web search leaves ~30% unsupported.

### The Latest Approaches


| System                         | Year       | Key Innovation                                                                                            |
| ------------------------------ | ---------- | --------------------------------------------------------------------------------------------------------- |
| **AGREE** (Google, NAACL 2024) | 2024       | Self-grounding framework; NLI model judges claim support; auto-constructs training data; 30%+ improvement |
| **SelfCite**                   | 2025       | Self-supervised citation alignment via context ablation - no human feedback needed                        |
| **LongCite**                   | 2024       | Fine-grained citation in long-context QA; surpasses GPT-4o on citation quality                            |
| **Perplexity's pipeline**      | Production | Strict RAG constraint + hybrid retrieval (BM25 + dense) + authority scoring; ~92% citation accuracy       |


**The limitation**: Optimizing for "answers supported by documents" is not the same as "correctly attributing content value." Citation accuracy (what these systems optimize) is a different problem than fair revenue allocation (what content marketplaces need). A model can select misleading evidence from authoritative sources.

**Sources**:

- [Fine-Grained Rewards - ACL 2024](https://arxiv.org/abs/2402.04315)
- [SourceCheckup - Nature Communications 2025](https://www.nature.com/articles/s41467-025-58551-6)
- [GopherCite - DeepMind](https://deepmind.google/discover/blog/gophercite-teaching-language-models-to-support-answers-with-verified-quotes/)
- [AGREE - NAACL 2024](https://arxiv.org/html/2311.09533v3)

## 9.4 Document-Level Shapley: The Cluster Shortcut

Even as exact Shapley remains intractable, researchers are finding clever approximations for specific LLM use cases.

**Cluster Shapley** (Ye & Yoganarasimhan, U. Washington, 2025): LLMs increasingly retrieve and summarize content from multiple sources, obscuring individual contributions. This paper proposes a Shapley framework for fair document valuation in LLM summaries. The key innovation: group semantically similar documents into clusters, then compute Shapley over clusters rather than individual documents. Off-the-shelf approximations (Monte Carlo, Kernel SHAP) perform poorly in LLM settings; Cluster Shapley substantially improves the efficiency-accuracy frontier. **This is the closest published work to the replaceability concept** - semantically similar (more replaceable) documents get clustered, reducing their individual attribution share.

**DPO-Shapley** (Tamine et al., Dec 2025): For LLMs fine-tuned with Direct Preference Optimization, the mathematical structure enables dramatically faster Shapley computation without retraining for every coalition.

**Fast-DataShapley** (2026): Estimates Shapley values in a single forward pass using a learned explainer model. Approaching real-time data valuation.

**In-Run Data Shapley** (2025): Computes during a single training run. Found **16% of the Pile corpus had negative Shapley values** - training data that actively hurts model performance. Also found that "training data contributes to generative AI even if the output does not closely resemble the input" - implying non-verbatim semantic contribution matters. This undermines naive text-matching approaches to attribution.

**Unlearning Shapley** (Ma et al., 2025): Instead of retraining, use machine *unlearning* to estimate Shapley values. Remove data from a pretrained model and measure performance shifts. A clever inversion - measure replaceability by actually removing the content and observing the gap.

**Sources**:

- [Cluster Shapley - Ye & Yoganarasimhan (2025)](https://arxiv.org/abs/2505.23842)
- [DPO-Shapley (2025)](https://arxiv.org/abs/2512.15765)
- [Fast-DataShapley (2026)](https://arxiv.org/html/2506.05281)
- [In-Run Data Shapley](https://jiachen-t-wang.github.io/data-shapley.github.io/)
- [Unlearning Shapley (2025)](https://arxiv.org/abs/2505.16147)

## 9.5 Counterfactual Attribution in RAG

A particularly promising approach for production systems: instead of tracing training data (expensive), measure what happens when you remove each retrieved document from the context window.

**RAGonite** (Fraunhofer IIS, ACM WSDM 2025): Computes counterfactual attribution by removing each evidence document from the RAG context and measuring how the answer changes. Similarity between the original response and the response generated *without* that evidence = that evidence's causal contribution. **Key finding**: Counterfactual explanations outperform standard similarity-based attribution. Open source: [github.com/Fraunhofer-IIS/RAGonite](https://github.com/Fraunhofer-IIS/RAGonite).

**CF-RAG** (ICLR 2026): Addresses the "Correlation Trap" - standard RAG can't distinguish causally decisive evidence from correlated-but-misleading information. Uses counterfactual queries to identify causally relevant distinctions. This matters for attribution because correlated content can appear unique but actually be redundant.

**Why this matters for content marketplaces**: Unlike training-time influence functions (which require model retraining), counterfactual RAG attribution can be computed at inference time with modest overhead (one additional forward pass per retrieved document). This is the most practical path to per-query attribution in any production RAG system.

**Sources**:

- [RAGonite - WSDM 2025](https://arxiv.org/abs/2412.10571) | [GitHub](https://github.com/Fraunhofer-IIS/RAGonite)
- [CF-RAG - ICLR 2026](https://openreview.net/forum?id=9U51rOnGko)

## 9.6 The Commercial Landscape

### ProRata.ai - Output Decomposition

Founded by Bill Gross (inventor of pay-per-click at GoTo.com, 1998). Their **Gist Attribution** system:

1. **Decompose** AI-generated answers into constituent claims
2. **Match** claims against source documents
3. **Weight** contributions via proprietary algorithm
4. **Allocate** 50% to publishers, 50% to ProRata via "Answer Ads"

700+ publisher agreements (FT, Axel Springer, The Atlantic, Fortune, UMG). $70.9M raised. But: algorithm is a black box with pending patents, no independent audit, no disclosed publisher revenue figures.

### Bria AI - The Closest Commercial Analog

**Bria AI** ($24M Series A) is the only company actively commercializing **embedding-based content attribution** - but for images, not text. Their patented system:

1. Vectorizes all training images
2. Decomposes into concept-level embeddings (composition, style, objects, texture)
3. At generation time, computes similarity between output and training data
4. Distributes royalties proportionally - **unique content earns more** because fewer sources share the revenue

This is the closest commercial implementation of the "replaceability in embedding space = attribution credit" concept. No text-domain equivalent exists.

### Other Players


| Company                     | Approach                                                          | Status                               |
| --------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| **TollBit**                 | JWT-authenticated API access, metered usage, automated settlement | 5,000+ publishers                    |
| **Geodesix** (impact.com)   | 75% to creators, MCP integration                                  | Active                               |
| **Perplexity (Comet Plus)** | 80/20 split from subscription pool                                | Production                           |
| **Encypher AI**             | C2PA text watermarking (provenance, not attribution)              | Open-source, working with NYT/BBC/AP |
| **Spawning AI**             | Consent infrastructure (opt-out tools, anti-scraping)             | $3M raised                           |


**Sources**:

- [ProRata.ai](https://prorata.ai/)
- [Bria Attribution Technology](https://bria.ai/attribution-technology)
- [Encypher AI](https://encypherai.com/solutions)
- [Spawning AI (TechCrunch)](https://techcrunch.com/2024/06/11/spawning-wants-to-build-more-ethical-ai-training-data-sets/)

## 9.7 What Microsoft and OpenAI Are Building Internally

### Microsoft Research: Training-Time Provenance

Microsoft Research has an active project to estimate influence of specific training examples on model outputs. Led by / involving **Jaron Lanier** (his "data dignity" concept, Chapter 9.8). The goal: demonstrate that models can be trained so that the impact of specific data "can be efficiently and usefully estimated." Status: research-stage, no published papers or tools yet. Directly motivated by the NYT lawsuit and GitHub Copilot litigation.

Lanier's "Art of Research" organization, embedded in the Microsoft CTO office (under Kevin Scott), has been developing the Data Dignity project. Principal PM Manager Christian Liensberger leads the technical work.

**The legal implication**: If Microsoft has (or is developing) a working attribution system, it could become a "bad fact" in the NYT litigation - evidence that attribution is technically feasible and was not implemented in Copilot's production pipeline.

### OpenAI: Media Manager (Vaporware)

OpenAI announced **Media Manager** in May 2024 - a tool to let creators specify how their works are used in training, using "cutting-edge ML research" to identify copyrighted content. **It was never launched.** A former employee stated: "I don't think it was a priority." OpenAI pivoted to direct licensing deals instead. This suggests the industry has largely opted for business agreements over technical solutions.

**Sources**:

- [TechCrunch: Microsoft exploring training data attribution (March 2025)](https://techcrunch.com/2025/03/21/microsoft-is-exploring-a-way-to-credit-contributors-to-ai-training-data/)
- [TechCrunch: OpenAI failed to deliver opt-out tool (Jan 2025)](https://techcrunch.com/2025/01/01/openai-failed-to-deliver-the-opt-out-tool-it-promised-by-2025/)

## 9.8 Data Dignity: The Philosophical Frame

Jaron Lanier and E. Glen Weyl proposed "data dignity" (2018) - the theory that people should be compensated for data they create, treating data as labor rather than a free resource.

**The technical vision**: Large-model AI can be reconceived as a social collaboration between the people who contributed data. Explanations of model results would center around the relative influence of specific inputs through a **provenance calculation mechanism**. This "figure/ground inversion" - seeing AI as collaboration rather than autonomous intelligence - suggests different strategies for economics, safety, fairness, and alignment.

**Implementation concept - MIDs**: "Mediators of Individual Data" would act as collective bargaining agents for data contributors. Target: 70% of value returned to creators (matching historical labor share of national income).

**Current state**: Influential but implementation remains nascent. No large-scale MID exists. The provenance mechanism aligns with TrackStar (9.2) and RAGonite (9.5) technically, but operates at a philosophical and policy level.

**Sources**:

- [Lanier & Weyl, HBR: A Blueprint for a Better Digital Society (2018)](https://eliassi.org/lanier_and_weyl_hbr2018.pdf)
- [UC Berkeley: Data Dignity and the Inversion of AI](https://cdss.berkeley.edu/events/data-dignity-and-inversion-ai)

## 9.9 Information-Theoretic Approaches

Use information theory to measure content's unique contribution to a corpus.

**Information gain scoring / SoftDeDup** (Yin et al., IEEE TKDE Survey): Maintain an "information redundancy state" across the corpus. Each new document is scored on how much new information it adds. Originally designed for training data curation (removing waste). **This is the most direct precursor to replaceability scoring** - SoftDeDup does exactly "content replaceability," just framed as deduplication rather than attribution. The leap is: instead of using replaceability to *filter* training data, use it to *compensate* content creators.

**Jensen-Shannon Divergence** for measuring model disagreement (MUSE, arXiv 2507.07236): Content that affects model outputs in regions where models *disagree* is content where the training data matters most.

**Entropy as a value signal**: Content that increases unpredictability (higher conditional entropy) is providing information the model couldn't predict from other sources - by definition, less replaceable.

**Sources**:

- [IEEE TKDE Survey: Data Optimization for LLMs](https://www.techrxiv.org/users/922498/articles/1294436/master/file/data/DPSurvey4LLM/DPSurvey4LLM.pdf)
- [MUSE - arXiv 2507.07236](https://arxiv.org/abs/2507.07236)

## 9.10 The Convergence: What These Threads Add Up To

### The Comparison Table


| Approach                        | What It Measures                           | Scalable?            | Used for Attribution?            | Production?  |
| ------------------------------- | ------------------------------------------ | -------------------- | -------------------------------- | ------------ |
| **Embedding uniqueness** (9.1)  | How replaceable content is in vector space | Yes                  | Theory only                      | No           |
| **TRAK / TrackStar** (9.2)      | Causal effect of training data on output   | Improving (8B scale) | Research                         | No           |
| **Trained citation** (9.3)      | Model's self-reported sources              | Yes                  | Yes (Perplexity ships it)        | Yes          |
| **Cluster Shapley** (9.4)       | Fair value for document groups             | Moderate             | Yes (LLM summaries)              | No           |
| **Counterfactual RAG** (9.5)    | What changes when you remove a document    | Yes (per-query)      | Yes (RAGonite)                   | No           |
| **Output decomposition** (9.6)  | Post-hoc matching of claims to sources     | Yes                  | Yes (ProRata ships it)           | Yes          |
| **Embedding attribution** (9.6) | Visual concept contribution                | Yes                  | Yes (Bria ships it, images only) | Yes (images) |
| **SoftDeDup / Info gain** (9.9) | Information redundancy in corpus           | Yes                  | No (used for filtering)          | No           |


### The Prior Art Assessment

**Has anyone connected these threads into a unified framework?** No.

The prior art search across academic databases, patent filings, and commercial products confirms: the individual research threads exist separately. The specific bridge - **using citation-validated uniqueness as a proxy for content attribution in AI systems** - has not been published. Specifically:

1. **Citation prediction from embeddings**: Well-established (SPECTER, SemNovel, Vital et al.)
2. **Embedding uniqueness correlates with citation impact**: Confirmed (Shibayama, Kojaku EDM, multiple groups)
3. **Data valuation via Shapley/influence functions**: Active research (Ghorbani/Zou, TRAK, TrackStar)
4. **Commercial content attribution**: Exists (ProRata, Bria) but uses different methods
5. **The bridge from #2 to #3/#4**: **Not made.** No one has used citation-validated uniqueness as a training signal for a content value estimator, then deployed it to non-academic content.

The patent space appears unoccupied. No patents found on "embedding-based content uniqueness scoring for valuation" from Microsoft, Google, or OpenAI. Bria's image-domain patents (the closest analog) may have claims worth checking.

### Risk Factors

- **Shibayama's warning**: Within-document text novelty showed insignificant/negative correlation with citations. The positive signal was in *inter-reference* novelty (combinations of cited works). Surface-level text uniqueness may not predict value.
- **Vital et al.**: Text-only prediction power was "limited" - metadata and network effects still dominate citation outcomes.
- **The asymmetry**: Novel content isn't always cited; cited content isn't always novel. The relationship is non-linear.
- **Domain transfer**: What works for scientific papers may not transfer to publisher content. Academic citation is a specific social practice with its own biases.

### What This Means

Attribution is not a solved problem, but it's not a hopeless one. The most likely path to production-quality attribution combines multiple signals:

1. **Counterfactual RAG attribution** (RAGonite-style) for per-query grounding credit - practical now
2. **Embedding-based uniqueness** for corpus-level content valuation - fast and scalable but unvalidated
3. **Output decomposition** (ProRata-style) for claim-level matching - shipping today, accuracy unknown
4. **Influence function sampling** (TrackStar-style) for training-time attribution - years away at production scale

Anyone claiming attribution is "solved" - including any AI company's marketing - is ahead of the science. The most honest position: "We're building the best available system while the research catches up."

## 9.11 Open-Source Tools and Infrastructure

A substantial ecosystem of open-source tools already exists across these research threads. Anyone wanting to prototype or test attribution approaches can build on existing infrastructure rather than starting from scratch.

### Training Data Attribution & Influence Functions


| Tool               | Maintainer                     | What It Does                                                                                                                                                                                                         | License    | GitHub                                                                    |
| ------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------- |
| **TRAK**           | MadryLab / MIT                 | Training data attribution via randomly-projected after kernel. 2-3 OOM faster than alternatives. Works on BERT, mT5, image models.                                                                                   | MIT        | [MadryLab/trak](https://github.com/MadryLab/trak)                         |
| **TrackStar**      | Google DeepMind / PAIR         | Scales influence tracing to 8B params / 160B tokens. No subsampling needed. Key finding: causal influence != factual retrieval.                                                                                      | Apache 2.0 | [PAIR-code/pretraining-tda](https://github.com/PAIR-code/pretraining-tda) |
| **Kronfluence**    | Sang Keun Choe et al.          | Influence functions via Kronecker-factored approximate curvature (KFAC/EKFAC). Scales to Llama-3-8B. Integrates with HuggingFace, DDP, FSDP, DeepSpeed. Currently the most scalable open-source IF library for LLMs. | Open       | [pomonam/kronfluence](https://github.com/pomonam/kronfluence)             |
| **LogIX / LoGra**  | CMU / Toronto                  | Converts existing training code into TDA code with minimal effort. 6,500x compute improvement, 11x logging speedup on Llama3-8B. Paper: "What is Your Data Worth to GPT?"                                            | Open       | [logix-project/logix](https://github.com/logix-project/logix)             |
| **Captum**         | Meta / PyTorch                 | Official PyTorch interpretability library. v0.8.0+ includes influence functions (NaiveIF) and TracIn variants (TracInCP, TracInCPFast). Most mainstream/supported implementation.                                    | BSD        | [pytorch/captum](https://github.com/pytorch/captum)                       |
| **DataInf**        | Yongchan Kwon et al.           | Efficient closed-form influence estimation for LoRA-tuned LLMs and diffusion models. Tested on RoBERTa, Llama-2-13B, Stable Diffusion. ICLR 2024.                                                                    | Open       | [ykwon0407/DataInf](https://github.com/ykwon0407/DataInf)                 |
| **LLM Attributor** | PoloClub / Georgia Tech        | Interactive visual attribution for LLM text generation. Select phrases, see responsible training data. AAAI 2025.                                                                                                    | MIT        | [poloclub/LLM-Attributor](https://github.com/poloclub/LLM-Attributor)     |
| **Influenciae**    | DEEL-AI (French ANITI project) | TensorFlow toolbox for influence functions. Includes TracIn, Arnoldi IF, first/second-order methods.                                                                                                                 | MIT        | [deel-ai/influenciae](https://github.com/deel-ai/influenciae)             |
| **LESS**           | Princeton NLP                  | Selects influential training data for targeted instruction tuning. Shows which data drives which capabilities. ICML 2024.                                                                                            | Open       | [princeton-nlp/LESS](https://github.com/princeton-nlp/LESS)               |


### Data Valuation & Shapley


| Tool             | Maintainer                | What It Does                                                                                                                                                                                  | License | GitHub                                                                        |
| ---------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------- |
| **pyDVL**        | appliedAI Institute       | **Most complete open-source data valuation toolkit.** Implements Shapley values, Banzhaf index, Least Core, semi-values, AND influence functions. Production-grade, updated through Jan 2026. | LGPL    | [aai-institute/pyDVL](https://github.com/aai-institute/pyDVL)                 |
| **OpenDataVal**  | NeurIPS 2023              | Unified benchmark for comparing 11 data valuation algorithms across image, NLP, tabular data. Leaderboards.                                                                                   | Open    | [opendataval/opendataval](https://github.com/opendataval/opendataval)         |
| **Data Shapley** | Ghorbani & Zou / Stanford | Reference implementation of the foundational Data Shapley paper (ICML 2019). Monte Carlo + gradient-based estimators.                                                                         | Open    | [amiratag/DataShapley](https://github.com/amiratag/DataShapley)               |
| **Data Banzhaf** | Wang et al.               | Alternative to Shapley using Banzhaf index - more robust data valuation framework. AISTATS 2023 (Oral).                                                                                       | Open    | [Jiachen-T-Wang/data-banzhaf](https://github.com/Jiachen-T-Wang/data-banzhaf) |
| **FreeShap**     | NUS                       | Fine-tuning-free Shapley attribution for LLMs using eNTK. No retraining needed. ICML 2024.                                                                                                    | Open    | [JTWang2000/FreeShap](https://github.com/JTWang2000/FreeShap)                 |
| **LossVal**      | Wibiral et al.            | Efficient data valuation during neural network training via self-weighting loss functions. No retraining. Dec 2024.                                                                           | Open    | [twibiral/LossVal](https://github.com/twibiral/LossVal)                       |


### RAG Attribution & Citation


| Tool             | Maintainer     | What It Does                                                                                                                                                                                                          | License    | GitHub                                                                        |
| ---------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------- |
| **RAGonite**     | Fraunhofer IIS | Counterfactual attribution in RAG - removes each evidence doc, measures answer change. WSDM 2025.                                                                                                                     | Open       | [Fraunhofer-IIS/RAGonite](https://github.com/Fraunhofer-IIS/RAGonite)         |
| **PaperQA2**     | Future House   | State-of-the-art agentic RAG for scientific papers. Grounded answers with in-text citations, metadata-aware embeddings, LLM re-ranking. **Achieves superhuman performance** on scientific QA (beats PhD researchers). | Apache 2.0 | [Future-House/paper-qa](https://github.com/Future-House/paper-qa)             |
| **RAGFlow**      | InfiniFlow     | Leading open-source RAG engine with traceable citations, deep document understanding, unlimited token context.                                                                                                        | Open       | [infiniflow/ragflow](https://github.com/infiniflow/ragflow)                   |
| **Kotaemon**     | Cinnamon       | RAG with detailed inline citations, PDF viewer highlights, relevance scoring, multi-hop question decomposition. Supports GraphRAG.                                                                                    | Open       | [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon)                     |
| **RAG Citation** | Rahul Anand    | Lightweight library for auto-generating citations in RAG. Two modes: non-LLM (SpaCy + SentenceTransformers) and LLM-based.                                                                                            | Open       | [rahulanand1103/rag-citation](https://github.com/rahulanand1103/rag-citation) |


### Embedding & Novelty Scoring


| Tool                           | Maintainer                | What It Does                                                                                                                                                                                                                                | License    | GitHub                                                                                      |
| ------------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------- |
| **SPECTER / SPECTER2**         | Allen AI                  | Citation-informed document embeddings for scientific papers. Can embed uncited papers. Free API.                                                                                                                                            | Apache 2.0 | [allenai/specter](https://github.com/allenai/specter)                                       |
| **science-novelty**            | Arts, Melluso, Veugelers  | Computes text-based novelty metrics from publications using SPECTER embeddings. Identifies new words, phrases, combinations. *Review of Economics and Statistics* (2025). **Most directly relevant to the citation-uniqueness hypothesis.** | Open       | [nicolamelluso/science-novelty](https://github.com/nicolamelluso/science-novelty)           |
| **Novelty (WIPO)**             | Shibayama, Yin, Matsumoto | Measures novelty of scientific articles by computing semantic distance between cited references using word embeddings. The actual code from the Shibayama 2021 paper.                                                                       | Open       | [DeyunYinWIPO/Novelty](https://github.com/DeyunYinWIPO/Novelty)                             |
| **embedding-disruptiveness**   | Kojaku et al.             | Computes EDM (Embedding Disruptiveness Measure) from citation networks. Predicts milestone/Nobel papers. 55M papers.                                                                                                                        | Open       | [PyPI](https://pypi.org/project/embedding-disruptiveness/)                                  |
| **Semantic Scholar API**       | Allen AI                  | Free API providing SPECTER2 embeddings for any paper. Rate-limited.                                                                                                                                                                         | Free       | [semanticscholar.org/product/api](https://www.semanticscholar.org/product/api)              |
| **Aspect Document Embeddings** | Malte Ostendorff          | SciBERT-based models for aspect-specific paper similarity (task, method, dataset aspects separately). JCDL 2022.                                                                                                                            | Open       | [malteos/aspect-document-embeddings](https://github.com/malteos/aspect-document-embeddings) |
| **DAAM**                       | Castorini Lab             | Diffusion Attentive Attribution Maps - pixel-level attribution for text-to-image models. Shows which words generated which pixels. ACL 2023.                                                                                                | MIT        | [castorini/daam](https://github.com/castorini/daam)                                         |


### Content Provenance & Watermarking


| Tool             | Maintainer                                  | What It Does                                                                                                                                                                | License          | GitHub                                                                          |
| ---------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| **C2PA SDKs**    | Content Authenticity Initiative (Adobe-led) | Reference implementations of the C2PA standard. Rust, Python, JavaScript, iOS, Java. Creates, signs, validates Content Credentials. Fast-tracked as ISO standard.           | Apache 2.0 + MIT | [contentauth](https://github.com/contentauth)                                   |
| **SynthID Text** | Google DeepMind                             | LLM text watermarking. Modifies sampling logits to embed imperceptible watermarks. Bayesian detector. Production in HuggingFace Transformers v4.46+. Published in *Nature*. | Open             | [google-deepmind/synthid-text](https://github.com/google-deepmind/synthid-text) |
| **Meta Seal**    | Meta / FAIR                                 | Comprehensive watermarking suite - image (PixelSeal), video (VideoSeal), audio (AudioSeal), text. **Dataset watermarking tracks training data provenance.**                 | MIT              | [facebookresearch/meta-seal](https://github.com/facebookresearch/meta-seal)     |
| **Encypher AI**  | Encypher                                    | C2PA-compliant text watermarking via Unicode variation selectors. Survives copy-paste. Co-authored the C2PA text standard.                                                  | AGPL-3.0         | [encypherai/encypher-ai](https://github.com/encypherai/encypher-ai)             |


### Publisher Attribution Standards


| Tool                              | Maintainer             | What It Does                                                                                                                                                                                                                                  | License       | GitHub / URL                                                                                           |
| --------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------ |
| **OpenAttribution**               | OpenAttribution.org    | Open standard with two specs: **AIMS** (agent identity + training provenance + licensed sources) and **Telemetry** (tracks which content contributed to AI responses). Python SDKs. **Directly addresses the publisher attribution problem.** | Apache 2.0    | [openattribution.org](https://openattribution.org/)                                                    |
| **RSL (Really Simple Licensing)** | RSL Standard           | XML-based open standard for machine-readable content licensing. Supports pay-per-crawl, pay-per-inference. Integrates with robots.txt, HTTP headers, RSS. **1,500+ orgs** including Reddit, Yahoo, Cloudflare, AP, Stack Overflow.            | Open standard | [rslstandard/rsl](https://github.com/rslstandard/rsl)                                                  |
| **Data Provenance Initiative**    | Multi-institution team | Audited **1,800+ text datasets** for licensing and provenance. Found 70%+ license omission rates, 50%+ error rates on HuggingFace. Published in *Nature Machine Intelligence* (Aug 2024).                                                     | Apache 2.0    | [Data-Provenance-Initiative](https://github.com/Data-Provenance-Initiative/Data-Provenance-Collection) |


### Autonomous Research Agents


| Tool                 | Maintainer      | What It Does                                                                                                                                                                                                                                                              | License | GitHub                                                                                |
| -------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------- |
| **AutoResearch**     | Andrej Karpathy | 630-line Python tool for autonomous ML experiments. Agent modifies code, trains for 5 min, keeps improvements, repeats. 66.7K stars. Ran 700 experiments in 2 days, found 20 optimizations (11% training improvement). Shopify CEO replicated: 19% improvement overnight. | Open    | [karpathy/autoresearch](https://github.com/karpathy/autoresearch)                     |
| **AutoResearch-MLX** | Community fork  | Apple Silicon port - runs on Mac without PyTorch.                                                                                                                                                                                                                         | Open    | [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) |


### Curated Lists & Meta-Resources


| List                           | What It Covers                                                      | GitHub                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Awesome LLM Attributions**   | Comprehensive survey of LLM attribution methods (2024-2025)         | [HITsz-TMG/awesome-llm-attributions](https://github.com/HITsz-TMG/awesome-llm-attributions)               |
| **Awesome Data Valuation**     | Data valuation research, tools, marketplace designs                 | [daviddao/awesome-data-valuation](https://github.com/daviddao/awesome-data-valuation)                     |
| **Awesome ML Data Quality**    | Data selection, attribution, valuation, influence, Shapley, pruning | [SJTU-DMTai/awesome-ml-data-quality-papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers) |
| **Awesome GenAI Watermarking** | Watermarking schemes for generative AI models                       | [and-mill/Awesome-GenAI-Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking)             |
| **Awesome RAG**                | RAG techniques, tools, and attribution methods                      | [Danielskry/Awesome-RAG](https://github.com/Danielskry/Awesome-RAG)                                       |


### Why AutoResearch Matters Here

Karpathy's AutoResearch demonstrates the "auto-updating agent" paradigm that could be applied to the attribution problem. The pattern: define a clear objective function (val_bpb in Karpathy's case, citation-prediction accuracy or attribution quality score in the attribution case), give the agent a codebase to modify, and let it run experiments autonomously. Someone could set up an AutoResearch-style agent to:

1. Take a corpus of scientific papers with known citation counts
2. Experiment with different embedding approaches, distance metrics, and combination strategies
3. Optimize for correlation between computed "uniqueness score" and actual citation impact
4. Run overnight, evaluate 100+ approaches automatically

This is the practical path to testing the citation-uniqueness hypothesis at scale without manual experimentation.

---

# 10. Content Provenance and C2PA

## 10.1 What C2PA Is

C2PA (Coalition for Content Provenance and Authenticity) is an open standard for cryptographically signing digital files with provenance metadata. Founded 2021 by Adobe, Arm, Intel, Microsoft, and Truepic. Over 6,000 members. A Content Credential is a signed manifest embedded in a file asserting: "captured by device X", "AI was used in creation", "edited in application Z."

C2PA does NOT detect fakes or verify truth. It asserts positive provenance.

## 10.2 Microsoft's Implementations


| Product                     | C2PA Status                                            |
| --------------------------- | ------------------------------------------------------ |
| Copilot Image Generation    | C2PA manifest + invisible watermark - Production       |
| Azure OpenAI (DALL-E)       | C2PA manifest - Production                             |
| **Copilot Text Generation** | **NO C2PA** - Not implemented                          |
| Bing AI Summaries           | URL-based citations, not C2PA - Production             |
| Bing Webmaster Tools        | AI Performance dashboard (citation tracking) - Preview |


**Key finding**: Microsoft's citation system in Copilot/Bing is **URL-based attribution** - proprietary bookkeeping that Microsoft controls. It is NOT C2PA-based cryptographic provenance.

## 10.3 The Gap for Publisher Attribution

C2PA was designed for tracking provenance of finished artifacts (photos, videos). It was NOT designed to track what happens when content is ingested, retrieved, and synthesized by an AI system.

- **Ingestion**: C2PA metadata is typically discarded when content is crawled/scraped
- **Retrieval**: Text chunks in vector stores have no C2PA manifest. Source URL is application-level bookkeeping.
- **Generation**: The text provenance standard (C2PA v2.3, Section A.7) was only published **January 2026**. Near-zero adoption.

**C2PA can bookend the pipeline** (mark sources before ingestion, mark outputs after generation) but **cannot track content through the pipeline**. The middle is a black box.

**Encypher** is the most notable company bridging this gap - sentence-level attribution with cryptographic proof. Working with NYT, BBC, AP, Google, OpenAI, Adobe, Microsoft. But requires AI companies to voluntarily integrate.

## 10.4 Assessment

For AI-generated images: attribution technology is largely ready (C2PA + watermarking in production). For publisher text content licensing: **not yet**. The text provenance standard is 3 months old. No mechanism tracks content through the AI pipeline. Current attribution is proprietary URL-based citation, not open-standard provenance.

**Sources**:

- [C2PA Spec v2.2](https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html)
- [Content Credentials in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-credentials)
- [Microsoft Research: Media Integrity and Authentication](https://mediacopilot.ai/microsoft-media-authentication-ai-content-c2pa-2026/)
- [Encypher for AI Companies](https://encypher.com/solutions/ai-companies)

---

# 11. The Legal Landscape

## 11.1 The Scorecard

Three US judges have ruled on AI fair use. Two for AI companies, one against:

- **Bartz v. Anthropic** (June 2025): Training is "quintessentially transformative" fair use - but only on legally acquired copies. Pirate sourcing is infringement. Led to **$1.5B settlement** (largest copyright recovery in US history, ~$3,000/work across ~500K titles).
- **Kadrey v. Meta** (June 2025): Training is fair use regardless of source legality. Contradicts Bartz.
- **Thomson Reuters v. ROSS** (Feb 2025): No fair use where AI product competed directly with source. Limited to non-generative AI.

**No court has ruled on grounding/RAG specifically.** The legal distinction between training and grounding has not been directly adjudicated.

## 11.2 NYT v. OpenAI/Microsoft

The defining case. See **Chapter 12** for a full deep dive covering the filing, claims, regurgitation evidence, Microsoft's specific exposure, Judge Stein's rulings, the discovery war over 100M+ chat logs, the MDL consolidation, settlement landscape, and implications for PCM.

## 11.3 The Broader Litigation Landscape

70+ copyright lawsuits filed against AI companies. MediaNews Group seeking $10B+ in damages. Authors Guild (George R.R. Martin, Ta-Nehisi Coates) proceeding to discovery - class certification hearings scheduled Q2 2026. International suits from Brazil, Canada, Denmark, India, and major European publishers. See **Section 12.9** for a detailed litigation map.

## 11.4 EU AI Act

Key dates:

- **August 2025** (effective now): GPAI model rules - training data summaries, copyright compliance, opt-out respect
- **August 2, 2026**: Transparency rules for AI-generated content - machine-readable disclosure required

EU TDM exception: Commercial AI training on lawfully accessed content is allowed unless rightsholder has expressly opted out in machine-readable format. Munich court (GEMA v. OpenAI, Nov 2025): TDM covers training, but not if the model memorizes complete works.

## 11.5 PCM's Legal Position

**Strengths**: No court has found licensed grounding with attribution infringing. Revenue sharing addresses "market harm" prong of fair use. EU AI Act compliance is built in. Legal sourcing (the Bartz bright line) is inherent.

**Weaknesses**: No court has explicitly blessed the model either. If responses substitute for visiting sources at scale (Google AI Overviews cause 80% fewer clickthroughs), the traffic diversion argument applies. Robots.txt is not legally binding (Ziff Davis v. OpenAI, 2025).

**Sources**:

- [Crowell & Moring: AI Companies Prevail on Fair Use](https://www.crowell.com/en/insights/client-alerts/ai-companies-prevail-in-path-breaking-decisions-on-fair-use)
- [NPR: Judge allows NYT case to go forward](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward)
- [Digiday: WTF is AI grounding licensing](https://digiday.com/media/wtf-is-ai-grounding-licensing-and-why-do-publishers-say-it-matters-over-training-deals/)
- [Norton Rose Fulbright: AI Copyright Cases 2026](https://www.nortonrosefulbright.com/en/knowledge/publications/ce8eaa5f/ai-in-litigation-series-an-update-on-ai-copyright-cases-in-2026)

---

# 12. The New York Times v. OpenAI/Microsoft: The Defining Case

This is the lawsuit that will set the terms for AI content licensing for the next decade. Everything else in this briefing - content marketplaces, attribution technology, publisher economics - exists in the shadow of this case. Microsoft is a named co-defendant alongside OpenAI, making this chapter inherently Microsoft-specific.

## 12.1 The Filing

On December 27, 2023, The New York Times Company filed suit against OpenAI LP, OpenAI Inc., Microsoft Corporation, and related entities in the U.S. District Court for the Southern District of New York (Case No. 1:23-cv-11195). The Times sought "billions of dollars in statutory and actual damages" plus an extraordinary remedy: the destruction of all ChatGPT models and training data that incorporated Times content.

The complaint alleged that OpenAI scraped millions of Times articles - news reports, investigations, opinion pieces, reviews, how-to guides - to train its large language models without authorization, license, or compensation. It named Microsoft as a co-defendant because Microsoft's multi-billion-dollar investment in OpenAI gave it access to the models powering Bing Chat (now Copilot) and Microsoft 365 Copilot.

The Times spent $10.8 million on AI litigation costs in 2024 alone. This is not a symbolic lawsuit - it's a fully resourced campaign by the most powerful news organization in the world.

## 12.2 What the Times Alleges

**Six causes of action:**

1. **Direct copyright infringement** - OpenAI copied millions of copyrighted articles into training data without license. The models encode actual copyrighted expression, not just abstract patterns.
2. **Contributory copyright infringement** - Microsoft materially contributed to and profited from the infringement through its partnership with OpenAI, deploying the infringing models in Copilot and Bing.
3. **Vicarious copyright infringement** - Both defendants had the right and ability to supervise the infringing activity and a direct financial interest in it.
4. **DMCA Section 1202(b) violations** - Removal or alteration of copyright management information (attribution, authorship metadata) during the scraping and training process.
5. **Unfair competition by misappropriation** - Common law claim that defendants free-rode on the Times' substantial investment in journalism.
6. **Trademark dilution** - AI-generated hallucinations falsely attributed to the Times damage its brand.

**The "regurgitation" evidence** is the centerpiece. The Times' First Amended Complaint includes an exhibit with over 100 examples of ChatGPT and Bing Chat reproducing Times content verbatim or near-verbatim. One example: Bing Chat copied all but two of the first 396 words of the Times' 2023 article "The Secrets Hamas Knew About Israel's Military." The Times argues this proves actual copyrighted expression is encoded in the model's parameters - not just learned patterns.

**The substitution argument** is equally important. The Times alleges that GPT-powered products allow users to bypass its paywall, producing "synthetic search results" that reproduce "significantly more expressive content from an original article than what would traditionally be displayed" by a search engine.

## 12.3 OpenAI's Defense

OpenAI's response rests on three pillars:

1. **Fair use** - Training is transformative. Two other federal judges (in Bartz v. Anthropic and Kadrey v. Meta) found AI training to be fair use. The outputs are new creative works, not copies.
2. **Manipulation** - OpenAI alleged "the Times paid someone to hack OpenAI's products," claiming it "took them tens of thousands of attempts to generate the highly anomalous results" in the regurgitation exhibit. OpenAI calls verbatim reproduction a "rare bug" during training where the model memorizes content, not a feature.
3. **Ubiquity of source material** - OpenAI argued that "the regurgitations The New York Times cites appear to be from years-old articles that have proliferated on multiple third-party websites," implying the content was already freely available across the internet.

**Academic research partially supports OpenAI's position.** A December 2024 arXiv study found ChatGPT typically exhibits less verbatim memorization than the Times suggests, though frequently republished articles are much more likely to be memorized. However, AI critics Gary Marcus and Reid Southen demonstrated in IEEE Spectrum that AI systems regurgitate data even without targeted prompting, undermining OpenAI's "manipulation" defense.

## 12.4 Microsoft's Specific Exposure

Microsoft is not a passive investor in this lawsuit. It faces direct and contributory infringement claims because:

- **Copilot and Bing** are the products at issue alongside ChatGPT. Microsoft deployed OpenAI's models in consumer and enterprise products, making it a direct user of the allegedly infringing technology.
- **Microsoft's partnership** with OpenAI (roughly $13 billion invested) gave it access to the models and a financial stake in their success, creating the nexus for vicarious and contributory liability.
- **Enterprise deployment** - Microsoft 365 Copilot pushes the technology into commercial workflows, potentially multiplying both the use of copyrighted content and the damages exposure.

**Microsoft's Copyright Commitment** (announced September 2023) provides intellectual property indemnity to its commercial Copilot customers - meaning Microsoft absorbs the legal risk for enterprise users. This is both a competitive advantage and a tacit acknowledgment of the liability exposure.

**What this means for the Copilot content team**: PCM exists in part to solve the problem this lawsuit defines. Licensed grounding with attribution is the alternative to the "scrape everything, defend with fair use" approach that landed Microsoft in court. The outcome of this case will directly shape what content is available through PCM, at what price, and under what terms.

## 12.5 Judge Stein's Rulings

The case is assigned to Judge Sidney H. Stein (SDNY), with Magistrate Judge Ona T. Wang handling discovery. On March 26, 2025 (published April 4), Judge Stein ruled on the motion to dismiss:

**Survived (going to trial):**

- All direct copyright infringement claims
- All contributory copyright infringement claims
- All vicarious copyright infringement claims

**Dismissed with prejudice:**

- Common law unfair competition by misappropriation (the Times lost this permanently)

**Dismissed without prejudice (can be refiled):**

- Most DMCA Section 1202(b) claims
- Microsoft's specific DMCA exposure was eliminated at this stage

**Net result**: The core copyright claims - the ones with billions in potential statutory damages ($150,000 per willful infringement, multiplied by millions of articles) - all survived. The case is going to trial on the merits unless it settles first.

## 12.6 The Discovery War

Discovery has been the most consequential battleground since the motion to dismiss ruling.

**May 2025 - The Preservation Order**: Magistrate Judge Wang issued a preservation order requiring OpenAI to retain all ChatGPT conversation logs, affecting over 400 million users worldwide. This turned a copyright case into a global data governance event.

**The 20 Million Log Battle (October 2025 - January 2026)**:

- News plaintiffs initially requested 120 million ChatGPT logs from the tens of billions OpenAI had preserved. OpenAI countered with 20 million (0.5% of its total logs), and the plaintiffs agreed.
- Then OpenAI reversed course in October 2025, proposing instead to run keyword searches and produce only conversations that referenced plaintiffs' specific works - a self-serving cherry-pick.
- Magistrate Judge Wang rejected that approach in November 2025.
- On January 5, 2026, Judge Stein affirmed in full, ordering OpenAI to produce the entire 20 million-log sample.

**Why the full sample matters**: Judge Wang found that even logs without verbatim reproductions of plaintiffs' works are discoverable because they bear on OpenAI's fair use defense. Logs showing what ChatGPT produces across a broad range of queries could reveal patterns relevant to whether outputs compete with or substitute for copyrighted works. This is the substitution analysis at scale.

**Privacy arguments failed**: OpenAI argued user privacy should block production. The court acknowledged "sincere" privacy interests but found them adequately protected by three safeguards: reduced sample size, de-identification, and the existing protective order. The ruling established that user-privacy arguments will not automatically shield AI companies from discovery.

**March 2026 - Additional Log Orders**: The court ordered production of an additional 78 million and 10 million logs, expanding the evidentiary base substantially. The total discovery corpus now exceeds 100 million conversation logs.

## 12.7 The MDL Consolidation

On April 3, 2025, the NYT case was consolidated into *In re: OpenAI, Inc. Copyright Infringement Litigation* (MDL, SDNY), combining 16+ copyright lawsuits. The consolidated plaintiffs include:

- **The New York Times** (the lead case)
- **MediaNews Group** (LA Daily News, San Diego Union-Tribune, Boston Herald, Hartford Courant, and others) - seeking $10+ billion in damages
- **Tribune Publishing** (New York Daily News, Chicago Tribune, Orlando Sentinel)
- **The Intercept** and **Center for Investigative Reporting**
- **Ziff Davis** (tech publisher)
- **Raw Story** and **AlterNet**
- **Individual authors** from multiple separate filings

The consolidation means a single judge controls discovery, scheduling, and potentially settlement for the entire newspaper/publisher cohort. This creates massive pressure for a global settlement - no publisher wants to be the last one holding out while others cut deals.

## 12.8 The Settlement Landscape

No settlement has been announced in the NYT case as of April 2026, but the conditions are aligning:

**Indicators pointing toward settlement:**

- OpenAI has signed licensing deals with roughly 20 media groups, establishing a pattern of negotiated outcomes over litigation
- The Anthropic $1.5 billion settlement (largest copyright recovery in US history) set a price anchor
- The NYT-Amazon settlement (May 2025, reported at $20-25 million/year) showed the Times will make deals
- Discovery is producing material that both sides likely prefer to keep confidential
- OpenAI's valuation (roughly $300 billion by early 2026) makes a multi-billion-dollar settlement financially feasible

**Key licensing deals already signed** (establishing market rates):

- News Corp + OpenAI: $250M+/5 years (roughly $50M/year)
- FT + OpenAI: $5-10M/year
- Axel Springer + OpenAI: "tens of millions of euros" over 3 years
- Washington Post + OpenAI: terms undisclosed
- The Guardian + OpenAI: terms undisclosed
- Dotdash Meredith + OpenAI: at least $16M
- AP + OpenAI: undisclosed (the first deal, July 2023)

**What a settlement might look like**: Given the Times' market position, legal leverage, and the Anthropic benchmark, experts estimate a settlement in the range of $100-500 million, likely structured as a multi-year licensing deal with attribution requirements and ongoing per-use fees. The destruction of training data (the Times' most dramatic ask) is unlikely - but restrictions on how Times content appears in outputs, combined with substantial upfront payments, are plausible.

## 12.9 The Broader Litigation Map

The NYT case exists within a wave of 70+ copyright lawsuits against AI companies:

**News publishers:**

- **MediaNews Group v. OpenAI/Microsoft** (Nov 2025) - 9 papers, seeking $10B+
- **Tribune Publishing v. OpenAI/Microsoft** - NY Daily News, Chicago Tribune
- **Ziff Davis v. OpenAI** - Robots.txt not legally binding (2025 ruling)
- **Encyclopedia Britannica and Merriam-Webster v. OpenAI** (2025)

**Authors:**

- **Authors Guild v. OpenAI** (Sep 2023) - Grisham, Martin, Picoult et al. Survived motion to dismiss. Class certification hearings scheduled Q2 2026, potentially representing thousands of authors.
- **Bartz v. Anthropic** (June 2025) - $1.5B settlement. Training on pirated copies is infringement; training on legally acquired copies is fair use.

**Visual media:**

- **Getty Images v. Stability AI** (US) - Stalled over discovery disputes since late 2024
- **Getty Images v. Stability AI** (UK) - Stability AI won at High Court (Nov 2025), but Getty can appeal

**Music:**

- **Concord/UMG v. Anthropic** (Oct 2023) - Music lyrics copyright. Active discovery, no ruling.
- **UMG v. Udio** - Settled. UMG will license music to Udio with guardrails. New service planned for 2026.

**Code:**

- **Doe v. GitHub/Microsoft/OpenAI** - GitHub Copilot. Class action over code reproduction. Ongoing.

**The fair use scorecard** (as of April 2026): 3 judges have ruled - 2 for AI companies, 1 against. No further summary judgment decisions expected until summer 2026. The law is genuinely unsettled.

## 12.10 Implications for PCM and Content Attribution

This lawsuit is the single strongest argument for PCM's existence:

1. **Licensed grounding eliminates training liability.** PCM sources content through paid licenses, not web scraping. This avoids the core infringement theory in every lawsuit - unauthorized copying into training data.
2. **Attribution addresses the DMCA claims.** The NYT's DMCA argument hinges on removal of copyright management information. PCM's attribution model preserves provenance by design.
3. **Revenue sharing defuses the substitution argument.** If publishers earn money every time their content is used, the "market harm" prong of fair use cuts in their favor, not against them.
4. **The discovery findings will shape pricing.** Whatever the 100+ million chat logs reveal about how frequently copyrighted content appears in AI outputs will directly inform what publishers demand for grounding licenses.
5. **Settlement terms become the template.** If the NYT settles for a specific structure (upfront payment + per-use fees + attribution requirements), that structure will propagate across the industry. PCM needs to be compatible with whatever template emerges.
6. **Destruction remedies validate provenance technology.** The Times asked for the destruction of training data built on its content. Even if that remedy isn't granted, the fact that it was requested creates demand for systems that can prove content sourcing is clean - exactly what C2PA and content credentials enable.

**The bottom line**: The NYT lawsuit proves that "scrape and defend" is not a sustainable content strategy. PCM is Microsoft's bet that "license and attribute" will be. How this case resolves will determine whether that bet pays off - and how much it costs.

## 12.11 The Strategic Paradox: What Happens If NYT Wins vs. Loses

Microsoft is in a uniquely awkward position - simultaneously a defendant in this lawsuit and the operator of the product (PCM) designed to solve the problem the lawsuit defines. The outcome cuts both ways regardless of who wins.

### If the NYT Wins (or Settles on Strong Terms)

**Pros for Microsoft:**

- **Validates PCM's entire reason to exist.** A ruling that unlicensed training/grounding is infringement makes licensed content marketplaces not optional but legally required. PCM goes from "nice to have" to "the only safe way to use publisher content in AI."
- **Creates a moat against smaller competitors.** If AI companies must license content, only players with deep pockets (Microsoft, Google, Apple) can afford it. Startups like Perplexity and open-source models face existential cost pressure. Microsoft's existing publisher relationships become a strategic asset.
- **Establishes settlement templates PCM can adopt.** If the NYT deal includes per-use fees + attribution + revenue share, that structure maps directly onto how PCM already works. Microsoft can say: "We built the infrastructure the courts are now requiring."
- **Publisher urgency increases.** A win gives publishers leverage to demand licensing from every AI company, driving more of them toward marketplaces like PCM rather than bilateral deals.

**Cons for Microsoft:**

- **Microsoft pays damages too.** As a named co-defendant, Microsoft is on the hook for potentially billions in statutory damages. The Copyright Commitment to enterprise customers means Microsoft may also absorb downstream liability.
- **Precedent applies to Microsoft's own models.** Whatever the court rules about unauthorized training applies retroactively to every Microsoft product built on OpenAI's models - Copilot, Bing, M365 Copilot. Microsoft may need to retrain or restrict models.
- **Content costs go up across the board.** A strong NYT win gives every publisher more leverage to demand higher licensing fees. PCM's economics get squeezed - Microsoft pays more for content, making the marketplace harder to operate profitably.
- **Destruction remedy risk (unlikely but existential).** If the court orders destruction of training data incorporating NYT content, it could force a rebuild of the foundational models Microsoft's entire AI strategy depends on.

### If the NYT Loses (Fair Use Prevails)

**Pros for Microsoft:**

- **No damages.** Microsoft avoids a multi-billion-dollar payout and eliminates the legal cloud over its AI products.
- **Freedom to operate.** A fair use ruling for training and/or grounding gives Microsoft (and everyone else) broad latitude to use web content in AI products without licensing.
- **Competitive parity.** If content is effectively free to use, Microsoft's scale advantage in compute and distribution matters more than content relationships.

**Cons for Microsoft:**

- **PCM's value proposition collapses.** This is the big one. If AI companies can legally scrape and use publisher content without licensing, why would anyone pay for it through PCM? Publishers lose their leverage, and the marketplace becomes a voluntary charity rather than a business necessity.
- **Publishers abandon the table.** Publishers who were negotiating PCM terms in the shadow of litigation will walk away if they have no legal stick. The "content economy" Microsoft is pitching becomes a story nobody believes.
- **Race to the bottom on content quality.** Without licensing requirements, there's no financial incentive for AI companies to use high-quality sourced content over whatever's freely crawlable. The premium content layer PCM is designed to surface becomes indistinguishable from the open web.
- **Google wins by default.** Google already has the largest crawl index and the deepest search relationships. In a "free content" world, Google's existing infrastructure advantage over Microsoft in content access grows, not shrinks.

### The Most Likely Outcome: Settlement (and Why It's Optimal for Microsoft)

A negotiated settlement is actually Microsoft's best-case scenario because:

1. **It establishes licensing norms without creating binding precedent.** A settlement sets market expectations ("this is what NYT content costs") without a court ruling that locks in legal doctrine one way or the other.
2. **It keeps PCM relevant.** Settlement terms that include per-use fees and attribution give PCM a clear role as the infrastructure that implements those terms at scale.
3. **It limits damages.** A settlement is negotiated, not imposed - Microsoft controls the number.
4. **It signals to other publishers.** "Even the NYT made a deal" becomes the strongest argument for other publishers to join PCM rather than sue.

**The irony**: Microsoft's ideal world is one where content licensing is legally ambiguous enough that publishers feel they *need* a marketplace like PCM for protection, but not so clearly required that Microsoft's own past practices create massive liability. A settlement threads that needle.

**Sources**:

- [CourtListener: NYT v. Microsoft Corporation Docket](https://www.courtlistener.com/docket/68117049/the-new-york-times-company-v-microsoft-corporation/)
- [Judge Stein's MTD Opinion (April 2025)](https://www.nysd.uscourts.gov/sites/default/files/2025-04/yf%2023cv11195%20OpenAI%20MTD%20opinion%20april%204%202025.pdf)
- [National Law Review: OpenAI Loses Privacy Gambit](https://natlawreview.com/article/openai-loses-privacy-gambit-20-million-chatgpt-logs-likely-headed-copyright)
- [Bloomberg Law: OpenAI Must Turn Over 20M Logs](https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms)
- [NPR: Judge Allows NYT Case to Go Forward](https://www.npr.org/2025/03/26/nx-s1-5288157/new-york-times-openai-copyright-case-goes-forward)
- [Harvard Law Review: NYT v. OpenAI Analysis](https://harvardlawreview.org/blog/2024/04/nyt-v-openai-the-timess-about-face/)
- [Columbia Undergraduate Law Review: NYT v. OpenAI](https://www.culawreview.org/ddc-x-culr-1/nyt-v-openai-and-microsoft)
- [Hollywood Reporter: NYT Spent $10.8M on AI Litigation](https://www.hollywoodreporter.com/business/business-news/new-york-times-legal-battle-openai-1236127637/)
- [Digiday: Publisher AI Deal Timeline 2024-2025](https://digiday.com/media/2024-in-review-a-timeline-of-the-major-deals-between-publishers-and-ai-companies/)
- [AI Business: AI Lawsuits in 2026](https://aibusiness.com/generative-ai/ai-lawsuits-in-2026-settlements-licensing-deals-litigation)
- [Press Gazette: News Publisher AI Deals and Lawsuits](https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/)
- [Copyright Alliance: AI Lawsuits 2025 Year in Review](https://copyrightalliance.org/ai-copyright-lawsuit-developments-2025/)
- [McKool Smith: AI Infringement Case Tracker](https://www.mckoolsmith.com/newsroom-ailitigation-1)

---

# 13. The Economics Under Stress

## 13.1 What Publishers Actually Earn

Lump-sum deals dominate: News Corp + OpenAI ($250M+/5 years), FT + OpenAI ($5-10M/year), Informa + Microsoft ($10M+ year 1). Total tracked commitments: ~$2.92B. Average deal: ~$24M over ~3.5 years.

Per-use models are nascent: Microsoft PCM (no disclosed rates), Perplexity Comet Plus (80/20 split from $42.5M pool), ProRata (50/50 ad revenue share, no disclosed actual payments).

## 13.2 The Net Negative

AI licensing pays publishers ~$816M/year. AI simultaneously destroys an estimated $2B+/year in advertising revenue through zero-click searches and traffic cannibalization. Publishers reporting 50-90% AdSense revenue losses in 2026. CNN down 30%, Business Insider down 40%.

**Nieman Lab (December 2025)**: "Publishers will see no meaningful AI licensing revenue." As long as Google's search crawler and AI training crawler function as a single system, the market price for data is effectively zero.

## 13.3 The Historical Comparison


| Revenue Source                      | Peak        | Current            | Change |
| ----------------------------------- | ----------- | ------------------ | ------ |
| US newspaper advertising            | $49B (2000) | ~$6B (2023)        | -88%   |
| Google's own ad revenue             | -           | $300B+ (2025)      | -      |
| Total AI licensing to publishers    | -           | ~$817M/year (2024) | -      |
| Estimated fair value (Google alone) | -           | $10-12B/year       | -      |


## 13.4 The Dilution Risk

As more publishers join per-use marketplaces, each additional publisher dilutes everyone else's share. Power law applies: top 10-20 publishers capture disproportionate citations. The music streaming precedent: Spotify pays ~$0.003-0.005 per stream, and only the top 1-2% of artists earn meaningful income. Per-use AI attribution likely follows the same pattern.

**Sources**:

- [Nieman Lab: Publishers will see no meaningful AI licensing revenue](https://www.niemanlab.org/2025/12/publishers-will-see-no-meaningful-ai-licensing-revenue/)
- [A Media Operator: The Economics Don't Work](https://www.amediaoperator.com/analysis/the-economics-of-an-ai-future-doesnt-work-for-publishers/)
- [Search Engine Land: AI disrupting publisher revenue](https://searchengineland.com/ai-answers-disrupting-publisher-revenue-advertising-465185)

---

# 14. The Blockchain Question

References to "distributed ledger" and "smart contracts" in connection with PCM have circulated in secondary coverage of the product. This raised an obvious question: is Microsoft actually building blockchain infrastructure for content licensing? The answer turns out to be more interesting than expected - because Microsoft never made the claim in the first place.

## The Source Trail: Third-Party Speculation, Not Microsoft

**Microsoft's own official PCM announcement** - the February 2026 blog post on about.ads.microsoft.com - contains **zero mentions** of blockchain, distributed ledger, or smart contracts. The blog focuses on usage-based reporting, publisher-defined licensing terms, "delivered value" compensation, and a scalable marketplace model.

The blockchain claims originate from a **single third-party blog post** on ai2.work, which uses hedging language throughout: "potentially blockchain-based," "potentially built on Azure Blockchain Service," and "could." This is analyst speculation dressed as technical architecture. The ai2.work article then got picked up and recycled by other secondary sources, creating a **circular citation pattern** where it looks like multiple sources confirm the claim - but they all trace back to one speculative post.

The ai2.work article's reference to "Azure Blockchain Service" is particularly revealing - that service has been dead since 2021 (see below). This suggests the author was filling in technical details speculatively, not reporting actual Microsoft disclosures.

## Azure Blockchain Service: Dead Since 2021

Azure Blockchain Service was **retired on September 10, 2021**. Microsoft announced the deprecation in May 2021, citing low adoption and a strategic shift away from managed blockchain infrastructure.

**What replaced it**: Microsoft pointed customers to three alternatives:

- **Azure Confidential Ledger (ACL)** - a tamper-proof, append-only ledger backed by Intel SGX enclaves (hardware-based trust, not consensus-based). GA since May 2022.
- **ConsenSys Quorum Blockchain Service** - a third-party managed version of what Azure previously hosted.
- **Azure SQL Database ledger tables** - append-only database tables with cryptographic verification. "Blockchain properties without the blockchain."

Microsoft also published a white paper suggesting Azure Cosmos DB could replace blockchain for many enterprise scenarios.

**Sources**: [IT Pro](https://www.itpro.com/technology/blockchain/359526/microsoft-to-sunset-azure-blockchain-service), [Azure Deprecation Dashboard](https://github.com/azure-deprecation/dashboard/issues/158)

## What PCM Almost Certainly Uses

Based on what Microsoft actually said, what they have available, and standard Azure marketplace patterns, the probable PCM stack is:

- **Azure SQL Database** (possibly with the Ledger feature for tamper-evident audit trails) for transaction records
- **Azure Monitor / Application Insights** for usage tracking and telemetry
- **Azure API Management** for publisher Content Access APIs
- **Azure Payments / standard billing** for monthly invoicing (PCM documentation mentions "detailed statements: Total Tokens Generated, Revenue Share, Royalty Amount, Net Payable")
- **Copilot integration** for grounding queries in licensed content
- **Dublin Core metadata schema** recommended for publisher onboarding

This is conventional cloud marketplace infrastructure - architecturally identical to how Azure Marketplace already handles ISV transactions.

## Has Blockchain for Content Licensing Worked Anywhere?


| Platform               | Uses Blockchain?         | Status                                                                                                                                                 |
| ---------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ProRata.ai**         | No                       | Patent-pending attribution algorithm, 50% revenue share, 700+ publishers. Standard infrastructure.                                                     |
| **TollBit**            | No                       | JWT-authenticated API access, metered usage, automated settlement. 5,000+ publishers.                                                                  |
| **Story Protocol**     | Yes (it IS a blockchain) | Dedicated L1 chain for IP tokenization. $140M raised, $2.25B valuation. But real adoption questioned - 10% layoffs March 2026, token unlock postponed. |
| **Fox Verify**         | Yes                      | Blockchain-based content verification for Fox Corp journalism. Used by TIME for IP ledger. Niche.                                                      |
| **Audius** (music)     | Yes                      | Most successful case - 5M+ monthly users at peak, smart contracts for royalties. But growth stalled, only $16.1M total raised.                         |
| **Po.et**              | Yes                      | Content attribution on Bitcoin blockchain. Shut down 2019.                                                                                             |
| **Spotify/Mediachain** | Acquired 2017            | Absorbed blockchain tech into conventional infrastructure. No public ledger ships.                                                                     |


**The pattern is clear:** The platforms actually gaining publisher traction (ProRata, TollBit) don't use blockchain. The blockchain-native platforms (Story Protocol, Po.et) have struggled for commercial adoption or shut down entirely. Blockchain for content licensing has been tried repeatedly and has never reached production scale.

## Why Blockchain Doesn't Solve the Actual Problem

The theoretical argument for distributed ledger in content licensing:


| Feature            | Regular Database                               | Distributed Ledger                      |
| ------------------ | ---------------------------------------------- | --------------------------------------- |
| Tamper evidence    | Possible with audit logs, but admin can modify | Cryptographically guaranteed            |
| Multi-party trust  | Publisher trusts platform's reporting          | Both parties independently verify       |
| Transparency       | Platform controls reporting                    | Shared view of all transactions         |
| Dispute resolution | Platform is judge and jury                     | Immutable record both parties agreed to |


**But here's the catch**: For PCM as currently designed - where Microsoft is the sole marketplace operator - a distributed ledger adds minimal practical value. The trust problem it solves ("can publishers verify Microsoft's usage reporting?") could be solved much more simply with signed audit logs, third-party auditors, or the Azure SQL Ledger feature.

A full distributed ledger would only make sense if PCM became a **multi-operator system** where no single party controls the infrastructure. That's not in any roadmap.

## What This Means

**The blockchain story around content marketplaces is a telephone game, not a platform claim.** Key takeaways:

1. **Don't repeat the blockchain framing.** No major content marketplace operator has claimed it, and repeating it creates expectations the products don't meet.
2. **Describe what's real.** Content marketplaces like PCM, ProRata, and TollBit provide usage-based reporting with detailed statements publishers can audit. That's genuinely valuable - and doesn't need blockchain credibility to sell.
3. **Know the competitive landscape.** None of the major content marketplace operators use blockchain. This is not a differentiator anyone is shipping.
4. **Watch for the question in publisher conversations.** Technically sophisticated publishers may have seen the secondary coverage and ask about it directly. The honest answer varies by platform, but generally: "We use auditable ledger infrastructure for tamper-evident payment records. We don't use blockchain."

**Sources**: [Microsoft PCM announcement](https://about.ads.microsoft.com/en/blog/post/february-2026/building-toward-a-sustainable-content-economy-for-the-agentic-web), [ProRata](https://prorata.ai/), [TollBit](https://tollbit.com/), [Story Protocol](https://www.story.foundation/)

---

# 15. What This All Means

**The honest assessment of where the industry stands**:

1. **The agentic web narrative is ahead of the technology.** The industry is selling a vision where AI agents reliably access, cite, and pay for premium content. The protocols exist (MCP, NLWeb). Content marketplaces exist (Microsoft PCM, ProRata, TollBit). The attribution technology to make it fair and accurate does not yet exist at production quality. This is a multi-year gap.
2. **Content marketplaces are the most publisher-friendly initiative in the industry** - but "best available" is not the same as "good enough." The most publisher-friendly marketplace (PCM, per Digiday) still can't solve the core attribution problem.
3. **The economics are structurally negative for publishers.** AI licensing is a rounding error compared to the traffic destruction. No single marketplace can fix this alone. The only structural solutions may be legislative.
4. **Attribution is a policy decision dressed as a technology.** Until Shapley-class computation becomes feasible (years away, if ever at production scale), "attribution" means business rules about how to split payments - not a mathematical measurement of influence.
5. **99.6% of AI content usage is invisible.** AI products use publisher content far more than they cite. Usage dashboards are a step, but they're sampling, not comprehensive tracking.
6. **Every platform transition has followed the same pattern.** Content marketplaces claim to be different. The history traced in this document should make anyone skeptical enough to ask whether that claim holds.
7. **Honesty is the opportunity.** Every AI company claims reliable citations. The CJR says they're all wrong 60%+ of the time. The first company to acknowledge reality rather than paper over it could build genuine trust with publishers and audiences.

---

# 16. Where This Is Going

Chapter 1 traced 5,000 years of the same pattern: a new distribution technology excites content creators, the platform consolidates power, creators get commoditized. Chapter 15 assessed where we are today. This chapter projects forward - not predictions, but trajectories that are already in motion and the branching points where outcomes diverge.

## 16.1 The Historical Pattern Applied Forward

Every previous platform transition followed a roughly 15-year arc:

1. **Excitement** (years 1-3): Creators rush onto the new platform. Early adopters get outsized returns.
2. **Dependency** (years 4-7): Creators optimize for the platform. Revenue shifts. Going back becomes impossible.
3. **Consolidation** (years 8-12): The platform extracts more value. Creator economics deteriorate. The platform is "too big to leave."
4. **Commoditization** (years 12-15): Creator content becomes interchangeable. The platform captures nearly all economic value. A new technology emerges and the cycle restarts.

**Where AI is on this arc (April 2026)**: We're in late Stage 1, entering Stage 2. Publishers are signing licensing deals (excitement), but the terms are already shifting in the platform's favor (the lump-sum deals of 2024 are being replaced by per-use models that transfer risk to publishers). The dependency phase is beginning - publishers who've signed exclusive grounding deals with one AI company are already locked in.

If the pattern holds, the consolidation phase (2028-2032) will see AI platforms renegotiating deals downward, citing commoditized content supply. By 2033-2035, the content layer may be fully commoditized - just as it was for music by 2015, news by 2020, and video by 2023.

**The open question**: Is there anything structurally different about AI that could break this pattern? Two candidates:

- **Legal precedent**: If courts establish that AI companies must license content (the NYT case outcome), it creates a floor under creator compensation that didn't exist for previous platform transitions. Copyright law didn't help newspapers against Google because aggregation and linking aren't infringement. AI training and grounding might be.
- **Attribution technology**: If provenance and attribution become technically reliable and legally required (EU AI Act, August 2026), content stops being interchangeable because each source is individually identifiable and compensable. This would be genuinely unprecedented - no previous platform transition had machine-readable attribution infrastructure.

Neither is guaranteed. Both are active right now.

## 16.2 Three Scenarios for the Content Economy (2026-2030)

### Scenario A: The Licensed Web (Best Case for Publishers)

**What happens**: The NYT lawsuit settles on terms that establish licensing as the norm. The EU AI Act's transparency rules (August 2026) create enforceable requirements for content sourcing disclosure. C2PA-style provenance becomes standard. Multiple competing content marketplaces emerge (PCM, ProRata, TollBit, Google's equivalent).

**Publisher economics**: Per-use licensing revenue grows from roughly $800M/year (2024) to $5-10B/year by 2030, partially offsetting traffic losses. Premium publishers with differentiated content earn meaningful per-query fees. A "middle class" of publishers survives through marketplace participation.

**Content marketplaces**: Multiple competing platforms (Microsoft PCM, ProRata, TollBit, Google's equivalent). Interoperability standards emerge. Publishers multi-home across platforms.

**Probability**: 20-25%. Requires both legal and technical stars to align.

### Scenario B: The Spotify Model (Most Likely)

**What happens**: Settlements establish licensing norms, but per-use rates trend toward fractions of a cent. The top 20-30 publishers capture 80%+ of attribution revenue. Long-tail publishers earn effectively nothing. Content marketplaces consolidate to 2-3 major players. Lump-sum deals fade; per-use models dominate.

**Publisher economics**: Total licensing revenue grows to $2-4B/year, but concentrated among top brands. Small and mid-size publishers continue to decline. Local news essentially disappears as an independent force. The music streaming parallel completes: technically, everyone gets paid; practically, only superstars earn a living.

**Content marketplaces**: Survive as infrastructure, but with thin margins. AI companies subsidize them as strategic defensive plays (keeping publishers from suing, maintaining content quality). Cost centers that prevent worse outcomes, not profit centers.

**Probability**: 45-50%. This is where the trends are naturally heading.

### Scenario C: Fair Use Wins (Worst Case for Publishers)

**What happens**: Courts broadly rule that AI training and grounding are fair use. The EU AI Act's content provisions are weakly enforced or challenged by trade agreements. AI companies continue scraping freely. Licensing deals dry up as publishers lose leverage.

**Publisher economics**: Licensing revenue plateaus and then declines. Traffic erosion continues at 30-50%/year. Subscription models hold for 5-10 elite brands (NYT, WSJ, FT). Everything else consolidates into a few conglomerates or shuts down. The advertising-supported web effectively ends.

**Content marketplaces**: Wither. Without legal pressure to license, demand-side incentive disappears. AI companies may maintain small versions for quality/brand-safety reasons, but they're not strategic assets.

**Probability**: 25-30%. Requires multiple courts to rule in AI companies' favor.

## 16.3 The Technology Trajectory

**Attribution (2026-2028)**: Current state is heuristic (embedding similarity, keyword matching). The convergence of citation-rank research, data influence functions, and counterfactual methods (Chapter 9) suggests that Shapley-approximation methods will become 10-100x cheaper within 2-3 years. Not exact Shapley, but "good enough" attribution that can withstand audit. The key development to watch: whether any research group publishes a unified framework connecting citation-validated uniqueness in embedding space to AI output attribution (the gap identified in Section 9.10).

**Provenance (2026-2027)**: C2PA is already in production for images. Text provenance is the hard problem. SynthID (Google's watermarking) is in HuggingFace. But watermarking only works for AI-generated content - it doesn't help attribute human-created source content used by AI. The missing piece: a standard for embedding source provenance metadata into AI outputs, not just flagging outputs as AI-generated.

**Agentic infrastructure (2027-2029)**: MCP (Model Context Protocol) and NLWeb are weeks old. If they gain adoption, they create a structured layer where AI agents negotiate content access programmatically. This is the "agentic web" Microsoft is betting on. The forward question: do agents negotiate per-query licensing in real time, or do they operate on pre-negotiated bulk deals? The former requires attribution infrastructure that doesn't exist yet. The latter looks like the current licensing market with better plumbing.

**Inference costs (2026-2030)**: GPU inference costs have been falling roughly 50-70% per year. If this continues, the Shapley computation problem becomes less absurd - not solvable, but less absurd. At 100x cost reduction, Monte Carlo Shapley drops from roughly $0.45/query to roughly $0.005/query. That's expensive but potentially viable for high-value commercial queries. The question is whether cost reduction arrives before the market has locked in simpler (and less fair) heuristic methods.

## 16.4 The Regulatory Timeline

What's already locked in:

- **August 2, 2026**: EU AI Act transparency rules - machine-readable disclosure of AI-generated content. First enforceable content-related AI regulation.
- **2026-2027**: EU GPAI Code of Practice finalized. Training data summaries required. Copyright opt-out compliance enforced.
- **2026**: NYT v. OpenAI likely settles or reaches summary judgment. Either outcome sets the tone for the next 50+ cases in the MDL.
- **Q2 2026**: Authors Guild v. OpenAI class certification hearing. If certified, represents thousands of authors and dramatically increases pressure.

What's emerging:

- **US federal AI legislation**: Still fragmented. No comprehensive federal copyright framework for AI as of April 2026. Congress has held hearings but passed nothing. State-level efforts (California, Illinois) are further along but create a patchwork.
- **International divergence**: EU regulating aggressively, US leaving it to courts, UK favoring industry codes, China requiring watermarking since 2023. AI companies face a compliance mosaic that favors large platforms (who can afford multi-jurisdictional compliance) over small ones.
- **The "right to be forgotten" for training data**: Not yet enacted anywhere, but the NYT's request for model destruction points toward it. If any jurisdiction requires that specific content be removable from trained models, it would fundamentally reshape AI infrastructure.

## 16.5 What This Means for Anyone Working in This Space Now

If you're working in AI, content, or publishing in 2026, you're arriving at a specific moment on the historical arc:

**The next 6 months (April - October 2026):**

- EU AI Act transparency rules go live. Every AI company will need to explain compliance to publishers and enterprise customers.
- The NYT case will either settle or produce major discovery revelations from the 100M+ chat logs. Either way, the industry will need to respond.
- Content marketplaces are still in early access. The first real publisher feedback and usage data will arrive. The gap between the pitch and reality will become measurable.

**The next 12-18 months (2026-2027):**

- Attribution technology will improve but not be solved.
- Content marketplaces will launch, expand, or consolidate. Differentiation will matter.
- Agentic protocols (MCP, NLWeb) will either gain adoption or stall. If they gain adoption, the "agentic web" narrative becomes tangible. If they stall, the narrative needs to evolve.

**The 3-5 year horizon:**

- The legal landscape will settle. Whatever template emerges from the NYT case and EU enforcement will define the rules for a generation.
- Content will either become a licensed commodity (Scenario B) or an unlicensed free-for-all (Scenario C).
- The question anyone building in this space should be asking: **What would we build differently if we knew which scenario was coming?** The answer reveals what's robust across scenarios (attribution infrastructure, publisher relationships, honest communication) vs. what's a bet on a specific outcome (per-use pricing models, marketplace dominance).

**The 5,000-year view**: Every technology that expanded access to knowledge - writing, the alphabet, printing, the internet - eventually concentrated power in the hands of whoever controlled distribution, not creation. The scribes lost to the monasteries. The monasteries lost to the printers. The printers lost to the platforms. The question for AI is whether "license and attribute" breaks this cycle, or whether it's the content equivalent of paying Spotify royalties - technically fair, practically meaningless for everyone except the top 1%.

---

# 17. Content Business Models in the AI Era

This chapter is the business model map. Chapters 1-16 established the history, the technology, the legal landscape, and the forward trajectory. This chapter answers the practical question: **how does anyone actually make money creating content in 2026?** The answer depends entirely on who you are - a major publisher, a mid-tier outlet, an independent creator, or a newsletter writer each face radically different economics.

This is also the chapter most relevant to the Bell AI Fellowship workshop, because it moves from "what happened" to "what are the options."

## 17.1 The Six Business Models

Every content business in 2026 runs on some combination of these six revenue models. None is sufficient alone. The viable strategies combine 2-4 of them.

### Model 1: AI Licensing (Lump-Sum)

**How it works**: AI companies pay publishers a flat fee for the right to use their content for training and/or grounding. Multi-year contracts, typically renegotiated at renewal.

**Who it works for**: Major publishers with large archives and brand recognition. News Corp ($250M+/5yr from OpenAI), Axel Springer ("tens of millions of euros"/3yr), Financial Times ($5-10M/yr).

**Who it doesn't work for**: Anyone below the top 50-100 publishers. AI companies have no incentive to negotiate individual deals with thousands of small publishers when they can license a handful of large ones and cover most queries. Only 20% of publishers anticipate AI licensing becoming a major revenue source.

**The math**: Total AI licensing market across all companies: roughly $817M/year (2024). Roughly $2.92B in total commitments. Average deal: roughly $24M over 3.5 years. This sounds meaningful until you compare it to the $2B+/year in advertising revenue AI simultaneously destroys through zero-click searches. Net negative.

**Trend**: Lump-sum deals dominated 2023-2024. Shifting toward per-use models (Model 2) as both sides gain more data on actual usage patterns.

### Model 2: AI Licensing (Per-Use / Attribution)

**How it works**: Publishers earn a fee each time their content is retrieved and used in an AI response. Requires attribution infrastructure to track usage. Revenue scales with actual consumption.

**Who it works for**: In theory, anyone with content good enough to be cited. In practice, power law dynamics apply - the top 10-20 publishers will capture 80%+ of citations, just as top artists capture most Spotify streams.

**Key platforms**:

- **Microsoft PCM**: Pay-per-use marketplace. Publisher-defined licensing terms. Still in early access. No disclosed rates.
- **ProRata.ai**: 50/50 revenue share with publishers. Proprietary "algorithmic attribution." 700+ publishers signed. $70.9M raised. But no disclosed actual payments to publishers.
- **TollBit**: JWT-authenticated API access. 5,000+ publishers. Metered usage with automated settlement.
- **Perplexity Comet Plus**: 80/20 split from a $42.5M annual pool shared across all publishers.

**The Spotify parallel**: Spotify pays $0.003-0.005 per stream. Only the top 1-2% of artists earn a living. Per-use AI attribution will likely follow the same distribution. A Guardian article cited 50 times a day earns fractional cents; a local newspaper cited twice a month earns effectively nothing.

**The dilution risk**: As more publishers join per-use marketplaces, each additional publisher dilutes everyone else's share. The marketplace incentive is to sign everyone; the individual publisher incentive is for competitors to stay out.

**Trend**: Growing. This is where Microsoft, ProRata, and others are investing. But the unit economics remain unproven at scale.

### Model 3: Subscriptions / Memberships

**How it works**: Readers pay directly for content access. Paywalls, membership tiers, premium newsletters.

**Who it works for**: Elite brands with loyal audiences and differentiated content. The NYT (12.21M digital subscribers) is the proof case. The FT, WSJ, The Athletic, The Information - all subscription-driven.

**Who it doesn't work for**: Most publishers. Across 20 wealthy countries, only roughly 18% of users pay for news. When readers hit a paywall, 57% leave entirely. Most households have 1-2 news subscriptions, so dominant brands capture nearly all demand.

**The newsletter revolution**: Substack (8.4M paid subscribers, $510M+ annualized creator revenue in Q1 2026), Beehiiv (75,000+ newsletters, 350M monthly readers), and Ghost (open-source, zero revenue share) have enabled independent creators to build subscription businesses at scale. Top examples: Zeteo (Mehdi Hasan, 31K paying subscribers, $3M/year), Newcomer (Eric Newcomer, $1.6M/year). The median Beehiiv newsletter earns its first dollar in 66 days.

**The bundling experiment**: Independent journalists are experimenting with bundles (3 newsletters for the price of 1.5) to address subscription fatigue. This mirrors the magazine bundle logic from the print era - same economic problem, same structural solution.

**Trend**: Stable for elite brands. Growing for independent creators. Plateaued for mid-tier publishers stuck between "not famous enough for subscriptions, not cheap enough for casual readers."

### Model 4: Advertising (Display, Programmatic, Sponsored)

**How it works**: The original web business model. Sell eyeballs to advertisers via display ads, programmatic exchanges, or sponsored content.

**Who it works for**: Increasingly, nobody in traditional form. Google and Meta capture 60%+ of digital ad dollars. The "ad tech tax" means publishers keep only 30-40 cents of every dollar. AI Overviews and zero-click search are eroding the traffic that display ads depend on. Publishers reporting 50-90% AdSense revenue losses in 2026.

**The creator version works better**: YouTube paid creators $60B+ in 2025. TikTok's Creator Fund and brand deal ecosystem. Instagram Reels monetization. Creator-led advertising bypasses the traditional publisher entirely - the creator IS the content AND the ad unit.

**Brand spending on creators**: $11.6B on direct partnerships (up 21% from 2025), $11.1B on paid amplification of creator content (up 56%), $7.9B on ad adjacencies (up 33%). Meta paid creators $3B in 2025 alone. Total creator economy: roughly $253B (2025), projected $1T+ by 2034.

**Trend**: Declining for publishers. Exploding for creators. The ad dollar is migrating from institutional content to personality-led content.

### Model 5: Collective Licensing

**How it works**: A collecting body negotiates blanket licenses on behalf of many publishers, distributes fees proportionally. Like ASCAP/BMI for music, but for text/journalism content used by AI.

**Key initiatives**:

- **RSL Collective** (Really Simple Licensing): Machine-readable licensing terms embedded in robots.txt. 50+ publishers including Reddit, Yahoo, Quora, Medium, Ziff Davis. Four pricing models: pay-per-crawl, pay-per-inference, subscription access, free with attribution.
- **UK CLA/PLS**: Generative AI Training Licence launched Q3 2025. Collective license + online content store. Designed to complement (not replace) direct deals.
- **US CCC** (Copyright Clearance Center): AI content re-use rights launched March 2026 for academic content.
- **Australia Copyright Agency**: AI-covered business license.
- **Germany VG WORT**: AI license for German-language content.

**Why it matters**: Only the largest publishers can negotiate directly with AI companies. Collective licensing is the only path for small and mid-size publishers to earn anything from AI usage. It's the radio royalty model applied to AI - pool the money, distribute proportionally.

**The structural argument**: A statutory or collective licensing regime could standardize access, ensure all AI developers can train under transparent terms, and prevent the current dynamic where 3-4 AI companies cut exclusive deals with 20-30 major publishers while everyone else gets nothing.

**Trend**: Early but accelerating. The infrastructure is being built now. Whether it scales depends on whether enough publishers opt in and whether AI companies participate voluntarily or are compelled by regulation.

### Model 6: Direct Audience Monetization (Beyond Subscriptions)

**How it works**: Creators monetize their audience relationship directly through merchandise, events, courses, consulting, community access, tips/donations, and affiliate revenue. Content is the top of the funnel, not the product itself.

**Who it works for**: Creators with engaged communities. The content attracts the audience; the revenue comes from everything around the content. Estimated that direct-to-audience monetization now represents 60%+ of creator earnings.

**Examples**: YouTube creator earns ad revenue on videos (Model 4) but makes more from course sales and consulting. Newsletter writer charges for the newsletter (Model 3) but earns more from paid communities and events. Journalist builds a following on TikTok (free) and monetizes through speaking fees and brand partnerships.

**Trend**: This is where the creator economy is heading. "Creators are building their own tables - launching brands, owning their IP, and cashing in on what they built from scratch: attention, trust, and community."

## 17.2 The AI Content Flood: Why Quality Becomes the Differentiator

The business model question can't be answered without understanding what's happening to the content supply side.

**The numbers are staggering**:

- **74.2% of newly published web pages** contain AI-generated content (Ahrefs, April 2025 analysis of 900K pages)
- **52% of newly published articles** are AI-generated (Graphite study of 65K URLs)
- Bot traffic crossed the **50% threshold** for the first time in 2024 (Imperva) - humans are now the minority online
- **2,089 AI-fabricated news websites** active as of October 2025 (NewsGuard), nearly double the count from a year earlier
- On X, roughly 64% of accounts are likely bots. LinkedIn long-form posts are 54% AI-generated.
- **21% of YouTube recommendations** to new accounts are AI slop, from 278 channels generating 63 billion views and an estimated $117M/year
- On music platforms, **34% of new tracks** on Deezer are AI-generated (50,000+ daily), and 97% of listeners can't tell the difference
- Merriam-Webster named **"slop"** its 2025 Word of the Year

**The Dead Internet becomes real**: Sam Altman acknowledged on X: "I never took the dead internet theory that seriously but it seems like there are really a lot of LLM-run twitter accounts now." Nieman Lab's 2026 prediction: "AI will outwrite humans."

**Model collapse**: A July 2024 *Nature* paper documented what happens when AI models train on AI-generated data - output diversity collapses across generations, eventually producing nonsense. High-quality human text suitable for training may be exhausted between 2026 and 2032. Models trained on the "old internet" (pre-2023) may have a permanent advantage.

**Why this matters for business models**: The flood makes human-created, verified, authoritative content more valuable, not less. "Human-made" is becoming a marketing differentiator:

- Bandcamp banned AI-generated music entirely (January 2026)
- Clothing brand Aerie pledged "No AI-generated bodies or people" - it became their most-liked Instagram content of the year
- 56% of Gen Z are more likely to trust brands committed to human-created content
- 72% of Gen Z hold negative or cautious views toward AI-generated content

The paradox: AI makes content production nearly free, which floods the market with low-quality output, which makes high-quality human content more scarce and therefore more valuable. The business model that survives is the one built on trust, authenticity, and verified provenance - not volume.

## 17.3 The Creator-Publisher Split

The briefing up to this point has mostly treated "content" as "journalism and publishing." But the creator economy is now larger than traditional publishing by most measures, and the economics are fundamentally different.


|                           | Traditional Publisher                                         | Independent Creator                                                 |
| ------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Revenue model**         | Advertising + subscriptions + licensing                       | Direct audience monetization + brand deals + platform revenue share |
| **Content cost**          | High (newsrooms, editors, legal, fact-checking)               | Low (individual + AI tools)                                         |
| **Distribution**          | SEO, owned websites, syndication                              | Algorithm-driven (TikTok, YouTube, Instagram)                       |
| **Audience relationship** | Institutional brand trust                                     | Personal brand trust                                                |
| **AI licensing access**   | Yes (if large enough)                                         | No (too small to negotiate individually)                            |
| **AI threat level**       | Existential (zero-click destroys traffic)                     | Moderate (personality can't be replicated by AI)                    |
| **Content moat**          | Investigative journalism, archives, institutional credibility | Authenticity, personality, community, niche expertise               |


**The key insight**: AI threatens publishers more than creators because publishers produce commodity information (news, facts, analysis) that AI can synthesize from multiple sources. Creators produce personality-driven content that is inherently non-fungible - you can't AI-generate a specific person's perspective, humor, or community relationship.

This is why:

- YouTube paid creators $60B+ in combined ad and subscription revenue in 2025
- The creator economy ($253B) is growing at 23% CAGR while traditional publishing revenue declines
- 76% of young adults get news from social media (creator-distributed) vs. 60% from news websites
- User-generated content eclipsed professional media ad revenue for the first time in 2025 (WPP analysis)

**For the fellowship discussion**: The question isn't "how do publishers survive AI?" - it's "who are the publishers in an AI world?" The answer increasingly looks like: individuals with audiences, not institutions with newsrooms. The business models that work (Models 3, 4, 6) are all creator-native. The business models that are struggling (Models 1, 4-traditional) are publisher-native.

## 17.4 What Works: A Decision Framework

For the workshop, here's how to think about which business model fits which situation:

**If you're a top-20 publisher** (NYT, WSJ, FT, Washington Post, Guardian):

- Primary: Subscriptions (Model 3) + Lump-sum AI licensing (Model 1)
- Secondary: Per-use attribution (Model 2) as it matures
- Strategy: Your brand IS the moat. Invest in investigative journalism and exclusive content that AI can't replicate from other sources. Negotiate aggressively with AI companies while you have legal leverage.

**If you're a mid-tier publisher** (regional paper, trade publication, niche outlet):

- Primary: Collective licensing (Model 5) + Subscriptions (Model 3) for your core audience
- Secondary: Per-use attribution (Model 2) if the platform economics work
- Strategy: You can't negotiate individually with AI companies. Join collective licensing bodies (RSL, CLA/PLS, CCC). Build a loyal niche audience that pays directly. Your survival depends on community, not scale.

**If you're an independent creator** (newsletter writer, YouTuber, podcaster, TikTok educator):

- Primary: Direct audience monetization (Model 6) + Platform ad revenue (Model 4-creator) + Subscriptions (Model 3)
- Secondary: Brand partnerships
- Strategy: Own your audience (email list, community). Diversify across platforms. Your personality is your moat - AI can't replicate you. Use AI tools to produce more, not to replace your voice.

**If you're building an AI product** (the platform perspective):

- Primary: Per-use licensing (Model 2) as the infrastructure play
- Secondary: Lump-sum deals (Model 1) for launch, transitioning to per-use
- Strategy: Sign publishers now while legal uncertainty gives them motivation. Build attribution infrastructure that's auditable and fair. The platform that publishers trust will win the long game.

## 17.5 The Unanswered Question

Every business model above assumes that content has economic value in an AI world. But there's a scenario where it doesn't.

If AI models become good enough that their training data gives them sufficient knowledge to answer most queries without retrieving external content, then grounding becomes optional, attribution becomes unnecessary, and the entire licensing/marketplace infrastructure becomes irrelevant. In that world, the only content with value is content that's genuinely new - breaking news, original investigation, novel analysis - not the vast middle of "competent information" that most publishers produce.

We're not there yet. Current LLMs still hallucinate, still need grounding for accuracy, still produce better answers with retrieved context. But the trajectory of model improvement points toward a future where less grounding is needed, not more.

The honest assessment: the window for building sustainable content business models in the AI era may be 5-10 years, not permanent. The business models that will last are the ones built on what AI genuinely can't do - original reporting, authentic personality, community trust, and creative work that's valued for who made it, not just what it says.

**Sources**:

- [Pew Research: Social Media and News Fact Sheet](https://www.pewresearch.org/journalism/fact-sheet/social-media-and-news-fact-sheet/)
- [Digiday: Publisher-AI Deal Timelines 2024 and 2025](https://digiday.com/media/a-timeline-of-the-major-deals-between-publishers-and-ai-tech-companies-in-2025/)
- [Pugpig: How Publishers Are Navigating AI, Creators, and Fragmented Audiences in 2026](https://www.pugpig.com/2026/01/22/ai-creators-fragmented-audiences-2/)
- [A Media Operator: Collective Licensing for AI](https://www.amediaoperator.com/analysis/collective-licensing-ai-pls-cla-copyright/)
- [Encypher: Publisher's Guide to AI Content Licensing 2026](https://encypherai.com/blog/the_publishers_guide_to_ai_content_licensing_in_2026)
- [ProMarket: Content Licensing Will Concentrate Markets](https://www.promarket.org/2025/11/20/content-licensing-agreements-will-concentrate-markets-without-standardized-access/)
- [Beehiiv: The State of Newsletters 2026](https://www.beehiiv.com/blog/the-state-of-newsletters-2026)
- [Sacra: Substack Revenue and Valuation](https://sacra.com/c/substack/)
- [Nieman Lab: In 2026, AI Will Outwrite Humans](https://www.niemanlab.org/2025/12/in-2026-ai-will-outwrite-humans/)
- [Nieman Lab: Independent Journalists Experiment with Bundles](https://www.niemanlab.org/2026/04/three-newsletters-for-the-price-of-1-5-independent-journalists-experiment-with-a-bundle/)
- [Digiday: Creator Economy in 2026](https://digiday.com/marketing/in-graphic-detail-heres-what-the-creator-economy-is-expected-to-look-like-in-2026/)
- [CreatorIQ: What the Creator Economy Did in 2025](https://www.creatoriq.com/blog/influencer-marketing-2025-trends)
- [Oliver Wyman: How to Benefit from Generative AI in Digital Publishing](https://www.oliverwyman.com/our-expertise/insights/2025/nov/how-to-benefit-from-generative-ai-in-digital-publishing.html)
- [HBR: How Gen Z Uses Gen AI](https://hbr.org/2026/01/how-gen-z-uses-gen-ai-and-why-it-worries-them)
- [Kapwing AI Slop Report 2025](https://www.kapwing.com/resources/ai-slop-report/)

