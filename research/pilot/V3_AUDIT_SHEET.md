# V3 Diarization Audit — Labelling Sheet

**What this is:** 20 two-minute clips. For each, mark roughly how much of the
talking is done by the HOST (Russ Roberts for EconTalk, Lex Fridman for Lex).
You are checking the pipeline's speaker attribution, so please label BEFORE
looking at `answer_key.json` — it holds the pipeline's answers and scoring
happens after.

**Target (PILOT_PLAN WS3):** host-attribution accuracy >=90%.

**How to label:** listen to `audit/clips/<ID>.wav`. For each clip give:
- `host_pct`: your estimate of host share of speech (0-100)
- `who_dominates`: HOST / GUEST / EVEN
- `notes`: anything odd (music, third voice, crosstalk, ad read)

Clips are in the session scratchpad; ask and I will send them to you directly.

| ID | show | era | episode | window (s) |
|---|---|---|---|---|
| A01 | Lex | 2019-21 | 2020-10-30__134_Eric_Weinstein_On_the_Nature_o | 6036–6156 |
| A02 | Lex | 2023-25 | 2025-08-24__478_Scott_Horton_The_Case_Against_ | 22175–22295 |
| A03 | Lex | 2019-21 | 2021-11-30__245_Tom_Brands_Iowa_Wrestling | 3201–3321 |
| A04 | Lex | 2019-21 | 2020-11-16__139_Andrew_Huberman_Neuroscience_o | 9076–9196 |
| A05 | Lex | 2019-21 | 2021-11-28__244_Robert_Crews_Afghanistan_Talib | 9185–9305 |
| A06 | Lex | 2019-21 | 2021-02-23__163_Eric_Weinstein_Difficult_Conve | 9205–9325 |
| A07 | Lex | 2019-21 | 2020-03-21__82_Simon_Sinek_Leadership_Hard_Wor | 1480–1600 |
| A08 | Lex | 2019-21 | 2021-09-30__227_Sean_Kelly_Existentialism_Nihi | 1258–1378 |
| A09 | Lex | 2023-25 | 2025-10-01__482_Pavel_Durov_Telegram_Freedom_C | 7180–7300 |
| A10 | Lex | 2023-25 | 2025-08-13__477_Keyu_Jin_China_s_Economy_Tarif | 3696–3816 |
| A11 | Lex | 2023-25 | 2023-09-10__395_Walter_Isaacson_Elon_Musk_Stev | 7234–7354 |
| A12 | Lex | 2023-25 | 2024-04-17__426_Edward_Gibson_Human_Language_P | 8113–8233 |
| A13 | Lex | 2023-25 | 2024-03-25__421_Dana_White_UFC_Fighting_Khabib | 3538–3658 |
| A14 | Lex | 2023-25 | 2023-06-02__381_Chris_Lattner_Future_of_Progra | 1053–1173 |
| A15 | EconTalk | 2019-21 | 2020-09-28_Agnes_Callard_on_Aspiration | 4552–4672 |
| A16 | EconTalk | 2019-21 | 2019-05-20_Mary_Hirschfeld_on_Economics_Cultur | 4397–4517 |
| A17 | EconTalk | 2019-21 | 2019-06-10_Bjorn_Lomborg_on_the_Costs_and_Bene | 1828–1948 |
| A18 | EconTalk | 2023-25 | 2024-11-25_Tyler_Cowen_on_Life_and_Fate | 2134–2254 |
| A19 | EconTalk | 2023-25 | 2025-09-08_How_Teams_Succeed_with_Colin_Fisher | 2440–2560 |
| A20 | EconTalk | 2023-25 | 2025-06-30_The_Deceptive_Power_of_Maps_with_Pa | 748–868 |

## Your labels (fill in)

| ID | host_pct | who_dominates | notes |
|---|---|---|---|
| A01 |  |  |  |
| A02 |  |  |  |
| A03 |  |  |  |
| A04 |  |  |  |
| A05 |  |  |  |
| A06 |  |  |  |
| A07 |  |  |  |
| A08 |  |  |  |
| A09 |  |  |  |
| A10 |  |  |  |
| A11 |  |  |  |
| A12 |  |  |  |
| A13 |  |  |  |
| A14 |  |  |  |
| A15 |  |  |  |
| A16 |  |  |  |
| A17 |  |  |  |
| A18 |  |  |  |
| A19 |  |  |  |
| A20 |  |  |  |

---

**Note on two clips:** the sample deliberately includes the two episodes the
QA rule flagged as implausible (pipeline claims ~99.9% host). They are not
marked here — labelling them blind alongside the rest is the point. Your
labels settle whether those episodes should be excluded from analysis.
