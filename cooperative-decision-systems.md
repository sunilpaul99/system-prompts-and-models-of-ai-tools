# Cooperative Decision Systems: DAOs, Collaborative Platforms, and the Jeffersonian Ward Question

*Research memo, July 2026*

**The question:** What has been attempted in building cooperative decision systems — DAOs, collaboratively governed platforms like Reddit — and why has none succeeded at scale? Could Jeffersonian "ward" involvement be implemented, and has it been?

**The short answer:** The ward layer has been implemented, repeatedly and successfully — town meetings, participatory budgeting, citizens' assemblies, subreddits, Mastodon instances, subDAOs. What has never been built is the layer Jefferson actually cared about: the **pyramid of graduated authorities** that federates ward-level deliberation upward into binding higher-level decisions. Every attempt at that aggregation layer has been captured by oligarchy, plutocracy, or the platform sovereign.

---

## 1. The DAO experiment (2016–present)

The founding premise: governance can be made trustless — encode the rules in smart contracts, distribute voting tokens, let the organization run itself. A decade in, the record is mostly a catalog of failure modes.

### What broke

**Plutocracy by design.** Token-weighted voting was supposed to align incentives; in practice it recreated shareholder voting with extra steps. Analyses in 2025–26 find the top 10% of token holders controlling roughly 76% of voting power across major DAOs. Decades of pre-crypto governance research — Michels' iron law of oligarchy (1911), principal-agent theory — predicted this recentralization precisely.

**Rational apathy.** Turnout routinely sits below 10% of token holders, often below 1%. Delegation systems (Uniswap, ENS, Arbitrum) were built to fix this and mostly produced a small professional delegate class — a de facto legislature nobody quite elected.

**Governance as attack surface.** When votes are property, they get bought:

- *Beanstalk (2022):* $182M lost to a flash loan that borrowed a voting majority for a single block.
- *Compound "GoldenBoyz" (2024):* a coordinated bloc used three progressive proposals to move $25M of COMP at 4–5% turnout.
- *Curve/Convex:* open vote-bribery markets (Votium) turned governance into a yield product.
- *Build Finance (2022):* an outright hostile takeover — an attacker acquired a voting majority and drained the treasury, legally, by the DAO's own rules.

**Decentralization theater.** MakerDAO — the most serious long-run experiment — spent years building delegate and Core Unit structures, then its founder pushed through "Endgame," effectively re-founding the organization around his own roadmap. Arbitrum's first governance proposal (AIP-1, 2023) was rejected by voters *after the foundation had already spent the funds*, revealing the vote as ceremonial. The pattern generalizes: foundations, core teams, and founders retain the root password.

### The mechanism-design catalog

The creativity has been genuinely impressive, and each mechanism teaches something:

| Mechanism | Where tried | What it solved / where it failed |
|---|---|---|
| Quadratic voting/funding | Gitcoin, RadicalxChange | Dampens whale power; collapses without Sybil-resistant identity |
| Conviction voting | 1Hive, Commons Stack | Time-weighted preference beats snapshot votes; niche adoption |
| Futarchy (vote values, bet beliefs) | DXdao, MetaDAO (live on Solana) | Elegant in theory; thin markets, few real deployments |
| Ragequit (codified exit) | MolochDAO | Minority protection via guaranteed exit; only fits shared-treasury orgs |
| Optimistic governance + veto council | Many L2 DAOs | Efficiency; quietly reintroduces an unelected upper house |
| Delegation / liquid democracy | Uniswap, ENS, Arbitrum | Fights apathy; produces professional delegate oligarchy |
| Bicameral + non-transferable citizenship | Optimism | See §3 — the most Jeffersonian design in crypto |

Three primitives remained unsolved beneath all of them: **identity** (Sybil resistance — quadratic anything collapses if one person can be many wallets), **attention** (deliberation is a cost nobody wants to pay), and **incentive alignment** (token holders optimize token price, not the commons).

---

## 2. Collaborative social media

### Reddit: digital feudalism

Reddit is best understood as feudalism, not democracy: volunteer moderators hold near-absolute power over their fiefs; the company holds absolute power over the moderators; ordinary users vote on *content* but never on *rules*. At the subreddit level it works surprisingly well — which matters for the ward question. The 2023 API-pricing blackout showed the limit precisely: thousands of communities "voted" by going dark, and the admins simply removed defiant moderator teams. Sovereignty was never actually shared; "community governance" was revealed as consultation.

### The rest of the record

- **Wikipedia** — the closest thing to a scaled success: consensus editing, RfCs, an elected Arbitration Committee, and it actually produced the encyclopedia. But it is governed by a shrinking oligarchy of power editors (the 90-9-1 participation law in extreme form), and its own research shows newcomers repelled by accreted bureaucracy.
- **Slashdot meta-moderation (1999)** — the earliest formal experiment: moderators moderated by randomly selected meta-moderators. Worked, at Slashdot's scale, for Slashdot's narrow purpose.
- **Stack Overflow** — elected moderators, community-drafted policy; repeated moderator strikes (2019, 2023) showed the Reddit pattern again — the community governs content, the company governs the community.
- **The Fediverse (Mastodon)** — genuinely polycentric: each instance sets its own rules; defederation is the inter-community sanction. Chronically limited by admin burnout and the absence of a funding model. Instances do not govern Mastodon gGmbH.
- **Bluesky** — "stackable moderation": anyone can run a labeler, users compose their own moderation regime. Governance as marketplace rather than democracy; too early to judge.
- **X Community Notes** — the one narrow, genuine scaled success. Bridging-based ranking (a note publishes only if raters who normally *disagree* both endorse it) is a real algorithmic innovation in consensus-finding. But it governs one function — context on posts — not the platform.
- **vTaiwan / Polis (Taiwan, g0v, Audrey Tang)** — the same bridging idea used to crowdsource actual legislation (Uber regulation, digital signatures). The most successful state-adjacent digital deliberation to date; still plateaued at tens of thousands of participants and depended on a sympathetic ministry to act on its outputs.

---

## 3. The Jeffersonian ward question

### What Jefferson actually proposed

In the 1816 letters to Joseph Cabell and Samuel Kercheval, Jefferson proposed dividing counties into wards of roughly 100 citizens — "little republics" — each with *real jurisdiction* over local functions: schools, roads, police, poor relief, militia, justice of the peace. The point was participatory, not administrative: every citizen would be "a participator in the government of affairs, not merely at an election one day in the year."

Crucially, the wards were the base of a **pyramid of graduated authorities** — wards → counties → state → federal — each layer constituted by and answerable to the one below. Hannah Arendt, in *On Revolution*, called the ward system the "lost treasure" of the American founding: proposed only after Jefferson's presidency, and never implemented.

### Has it been implemented? The ward layer, yes. The pyramid, never.

Working ward-scale instances:

1. **New England town meetings** — Jefferson's explicit model ("the wisest invention ever devised by the wit of man for the perfect exercise of self-government"). Functioning for ~380 years; still only at populations of a few thousand.
2. **Participatory budgeting** — Porto Alegre 1989, now in 7,000+ cities including NYC council districts and Paris. Real money, real neighborhood assemblies; the most literal modern ward implementation. But it governs a *slice of a budget delegated downward* by a city that retains sovereignty — not authority constituted from below.
3. **Citizens' assemblies by sortition** — Ireland's assemblies (which produced the abortion and marriage-equality referendums), France's Convention Citoyenne pour le Climat, Ostbelgien's *permanent* citizens' council. The OECD's "deliberative wave" now counts 700+ processes, ~78% at the local level, with EU-funded transnational assemblies running through 2025–26 and MIT/DemocracyNext piloting AI-assisted assemblies. Sortition solves Jefferson's participation problem differently: instead of everyone participating a little, a random sample participates deeply. But nearly all remain *advisory* — France's climate convention watched most of its 149 proposals get diluted or dropped.
4. **Digital wards** — subreddits, Mastodon instances, Discord servers, and DAO subDAOs are all ward-shaped: small groups with real rule-setting power over a local domain.
5. **Optimism's Citizens' House** — the most deliberate crypto attempt at Jeffersonian design: a bicameral system where a plutocratic Token House is checked by a Citizens' House of non-transferable, one-person-one-vote citizenships allocating retroactive public-goods funding. Explicitly an attempt to bootstrap non-plutocratic digital citizenship. Still small, curated, and dependent on the foundation that convenes it.

### Ostrom's validation

Elinor Ostrom's Nobel-winning fieldwork on commons governance distilled eight design principles for institutions that endure. The eighth is **nested enterprises**: governance in multiple layers, local units federated upward. That is Jefferson's ward pyramid, validated empirically across centuries of irrigation systems, fisheries, and forests. Her principles double as the best diagnostic for why specific DAOs and platforms fail:

- No boundary definition → Sybil attacks
- No graduated sanctions → ban-or-nothing moderation
- No cheap conflict resolution → forks and flame wars
- No monitoring by members → invisible capture
- No nesting → either 100-person communes or million-person plutocracies, nothing in between

---

## 4. Why the pyramid never scales

The consistent pattern across a century of attempts: **local self-governance works and keeps being reinvented; upward federation of it does not.** Subreddits don't elect Reddit's admins. Instances don't govern Mastodon gGmbH. Participatory budgets don't aggregate into participatory states. SubDAOs answer to treasuries, not vice versa. The failure modes at the aggregation layer are stable:

1. **Participation economics.** Deliberation costs evenings (Oscar Wilde's complaint about socialism). At ward scale, social bonds subsidize the cost; at federation scale they don't. Participation collapses into the 90-9-1 power law, and the vacuum is filled by whoever has professional incentive to show up — whales, delegates, activists, staff. Michels' iron law of oligarchy has held for every DAO since 1911.
2. **Cheap exit atrophies voice** (Hirschman). Online, leaving — unsubscribing, defederating, forking — is nearly free, so the hard work of contested collective decision rarely gets done. Jefferson's wards worked partly because his citizens couldn't leave.
3. **The identity problem.** Every one-person-one-vote scheme online collides with Sybil attacks; every workaround (token-weighting, curated citizenship, proof-of-personhood) reintroduces plutocracy or gatekeeping.
4. **Sovereignty is never transferred.** Platforms, foundations, and founders retain the root password. When community decisions conflict with the sovereign's interests (Reddit blackout, Arbitrum AIP-1, Maker Endgame), the community loses.

### The honest scorecard of partial successes

Short and instructive — every entry succeeds by *narrowing the domain* of collective decision rather than scaling general-purpose democracy:

- **Wikipedia** — one artifact, oligarchic process, real output.
- **Open-source governance** (Debian's constitution and General Resolutions, IETF's "rough consensus and running code," Apache, Python's PEP process) — works because contribution is the franchise and the fork disciplines leadership. Arguably the most successful cooperative decision system in existence.
- **Community Notes** — one function, clever bridging math.
- **Participatory budgeting** — real but bounded delegation.
- **Taiwan's Polis processes** — real legislative input, dependent on state sponsorship.

---

## 5. Where it points

The live frontier is essentially: *can technology lower the cost of the pyramid's middle layers?*

- **AI-mediated deliberation** — Polis at scale; DeepMind's "Habermas Machine" experiments (LLMs drafting consensus statements that participants rate above human mediators'); MIT/DemocracyNext tech-enhanced citizens' assemblies.
- **Bridging algorithms as a general consensus primitive** — the Community Notes math applied beyond fact-checking.
- **Sortition** — replacing mass participation with representative deep participation; the permanent Ostbelgien model as template.
- **Proof-of-personhood** — the identity primitive that would make one-human-one-vote possible online.

**The synthesis:** Jefferson's insight was never really about the wards — it was about *nesting*, and Ostrom proved him right empirically. The unsolved engineering problem of the last thirty years is the articulation joint between layers: how a hundred small deliberating bodies bind a large institution without the aggregation step being captured. Nobody has built that joint. Whoever does — plausibly with sortition plus bridging algorithms as the mechanism — gets the ward republic.

---

## Sources

- [Forbes — DAOs Keep Centralizing: Decades of Governance Research Explain Why (Apr 2026)](https://www.forbes.com/sites/digital-assets/2026/04/04/daos-keep-centralizingdecades-of-governance-research-explain-why/)
- [SoK: Attacks on DAOs (arXiv 2406.15071)](https://arxiv.org/pdf/2406.15071)
- [How DAOs Failed to Deliver on Their Original Promise (Mar 2026)](https://lopetaku.medium.com/dao-governance-failures-whales-low-turnout-attacks-d1375c556384)
- [DemocracyNext — Citizens' Assemblies in Central & Eastern Europe](https://www.demnext.org/projects/cee)
- [DemocracyNext / MIT CCC — Tech-Enhanced Deliberative Assemblies](https://www.demnext.org/projects/tech-enhanced-citizens-assemblies)
- [Citizens Take Over Europe — CitiDem local & transnational assemblies 2025–26](https://citizenstakeover.eu/citidem/)
- [LSE USAPP — Citizens' assemblies can work together with electoral institutions](https://blogs.lse.ac.uk/usappblog/2025/03/14/citizens-assemblies-can-work-together-with-electoral-institutions-to-improve-democracy/)
- [International IDEA — Renewing Democracy 2026](https://www.idea.int/renewing-democracy-2026)
- Jefferson to Joseph C. Cabell (Feb 2, 1816); Jefferson to Samuel Kercheval (Jul 12, 1816)
- Hannah Arendt, *On Revolution* (1963), ch. 6
- Elinor Ostrom, *Governing the Commons* (1990)
- Albert O. Hirschman, *Exit, Voice, and Loyalty* (1970)
- Robert Michels, *Political Parties* (1911)
