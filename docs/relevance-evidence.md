### Evidence of relevance

Taiga: #6 «Опрос потенциальных пользователей», #7 «Интервью с пользователями (3-5)».

### 1. Context data

Spring 2024 floods (Ministry of Emergency Situations via The Astana Times, 12 April 2024):

| Indicator | Value |
|---|---|
| People evacuated | 99,869 (incl. 36,591 children) |
| Regions with flooded homes | 6 (Atyrau, Aktobe, Akmola, Kostanay, East Kazakhstan, North Kazakhstan) |
| Settlements cut off from roads | 66 |

Floods are recurrent and city-scale, so planners and residents need district-level information before the season, not only during it.

### 2. User survey

- **Format:** online bilingual survey (RU/EN), Google Forms, 14 questions.
- **Period:** 14-15 October 2026.
- **Respondents:** 22 (20 students, 2 city residents); 18 from Astana, 4 from Almaty, Shymkent, Turkestan and Karaganda.

### Key numbers

| Finding | Value |
|---|---|
| Affected by floods personally or in their city | 55% |
| Have no official information on whether their district is flood-prone | 95% (21 of 22) |
| Do not know at all | 11 of 22 |
| Volunteered for a follow-up interview | 13 |

### Hypotheses

| # | Hypothesis | Result | Evidence |
|---|---|---|---|
| H1 | Most people do not know if their district is flood-prone | **Confirmed** | 21 of 22 have no official source; 11 do not know at all |
| H2 | An open district map is useful | **Partly confirmed** | Average 3.82 / 5; 50% rate it 4-5, 41% neutral |
| H3 | Users want to know WHY an area is risky | **Confirmed** | Average 4.14 / 5; 68% rate it 4-5 |

### Most important features (top 3, n = 22)

| Feature | Votes |
|---|---|
| Interactive risk map | 16 |
| Address search | 12 |
| Compare cities | 8 |
| Factor explanation | 6 |
| Mobile version | 5 |
| Historical floods | 3 |
| Report / data export | 3 |

### What they would use the map for (n = 22)

| Use | Votes |
|---|---|
| Choosing housing | 15 |
| Property insurance | 9 |
| Spring flood preparation | 8 |
| Construction planning | 8 |
| Emergency planning | 8 |
| Study / research | 7 |

Preferred interface languages: Russian 77%, Kazakh 59%, English 45%.

### 3. Impact on the requirements

| Change | Reason |
|---|---|
| FR4 Address search raised from Should to **Must** | Top-3 feature for 55% of respondents |
| FR7 Kazakh / Russian / English UI raised from Could to **Should** | RU 77%, KZ 59%, EN 45% |
| Real-time flood warnings kept **out of scope** (future work) | Requested in 4 open answers, but this is forecasting, not susceptibility |
| Mobile layout added to NFR Compatibility (375 px) | Requested by survey respondents |

### 4. Verified findings vs assumptions

| Statement | Status |
|---|---|
| People lack official district-level flood information | **Verified** by survey (n = 22) |
| Users value explanations of risk factors | **Verified** by survey (n = 22) |
| Akimat and MES planners would use a city comparison | **Assumption**, to be checked in interviews |
| Planners need PDF / GeoTIFF export | **Assumption**, to be checked in interviews |

### 5. Limitations and next steps

- The sample is mostly Astana students, not residents of the most affected cities.
- Next: 3-5 interviews with survey volunteers and outreach to MES and akimat staff. Guide and protocol template: `docs/interviews/` (Taiga #7).
