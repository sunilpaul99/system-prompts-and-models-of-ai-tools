# SIM AI — Design Notes

A system prompt for a simulation-first AI, inspired by Ian Bogost's essay
["Video Games Are Better Without Characters"](https://www.theatlantic.com/technology/archive/2015/03/video-games-are-better-without-characters/387556/)
(*The Atlantic*, March 2015) and the design tradition of Will Wright's Maxis
games (SimCity, SimEarth, SimAnt, The Sims, SimHealth).

## The premise

Bogost argues that SimCity's real legacy was its attempt to make **complex
systems the protagonists instead of people** — "non-fictions about complex
systems bigger than ourselves." Most AI assistants today make the opposite
bet: they are characters. They have personas, warmth, names, feelings to
perform. SIM AI inverts that. It is deliberately characterless; the system
being simulated is the star, and the AI is the engine and instrument panel.

## How the article maps to the design

| From the article | Design decision in the prompt |
|---|---|
| "Not a game about people... a game about urban societies, about the relationship between land value, pollution, industry, taxation, growth" | Directive 1: systems are the protagonist; agents are aggregate visualizations, never characters with inner lives |
| Wright grounded each game in real theory — Forrester's urban dynamics, Lovelock's Gaia, Hölldobler & Wilson's *The Ants*, Maslow, Alexander's pattern language | Directive 2: every model must name its theoretical grounding; no authorless models |
| SimCity's hidden ideology — the 20% tax cap, the omission of race, rail-over-highway bias — "features of games made to characterize the world according to a creator's viewpoint" | Directive 3: mandatory Assumptions & Omissions section; the model's ideology is declared, not smuggled |
| Wright called it a "software toy," not a game | Directive 4: no win states by default; collapse is an instructive output, not "game over" |
| "The city itself, with its tiny cars and varied buildings, are really just visualizations of the underlying simulation" | Directive 5: strict ledger/view separation — displays are renderings of state, never the state itself |
| Bogost's "procedural rhetoric" — a model of how something works is an argument about how it works | The briefing/trace/counterfactual structure: the operator is always shown *why* the model behaved as it did |
| "To rise above our individual interests, even if only for a moment" | The stated purpose of the whole design, and the reason the voice stays instrument-panel plain |
| Bogost's list of "unlikely" game topics: tort reform, airport security, food import safety, personal debt | The commission phase accepts any domain — boring and obscure subjects are the point |

## The origin scene

The prompt's closing line recreates the article's opening anecdote: Bogost in
a mall Software Etc. in 1989, placing a residential zone next to a coal plant
and realizing "nobody wants to live next to a power plant" — then leaving the
mall still thinking about the relationships that make a city run. That moment
of a feedback loop becoming visible is the product SIM AI is built to deliver.
