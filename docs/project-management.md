# Project management, milestones and risks

Taiga: #17 «Настройка репозитория, правил работы и CI».

## Tools

| Tool | Link | Purpose |
|---|---|---|
| GitHub | https://github.com/W0ran/flood-susceptibility-kz | Code, documentation, diagrams, reviews |
| Taiga (Scrum) | https://tree.taiga.io/project/yerkosh-flood-susceptibility-kz-diploma/backlog | 34 user stories in 5 epics: University bureaucracy, Analytics, Backend, Frontend, ML |

We moved from YouTrack to Taiga in October 2026 after discussing it with the supervisor; the supervisor and all team members are members of the Taiga project.

## Responsibilities

| Member | Role | Main responsibilities |
|---|---|---|
| Rakhymbay Yerkebulan | QA engineer & developer | Data preparation, factor calculation (Python), testing, model validation, CI |
| Tenglesbayev Zhandos | Developer | Model implementation, susceptibility maps, API and web map |
| Tutkabay Assem | Analyst & PM | Literature, factor weighting, comparative analysis, interviews, schedule, supervisor contact |

## Milestones

| Period | Milestone | Deliverable |
|---|---|---|
| Sep 2026 | Topic, team, approval | Application and justifications submitted |
| Oct 2026 | Requirements & analysis | **Pre-defense 1 (24 Oct 2026)** — tag `prob-period-1` |
| Oct – Nov 2026 | Data & factor rasters | Factor rasters for 3–4 cities, flood inventory |
| Nov – Dec 2026 | Model + SHAP | Trained and validated models |
| Dec 2026 – Feb 2027 | API & web map | Working prototype — pre-defense 2 (`pre-defense-2`) |
| Feb – Mar 2027 | Testing & evaluation | Test reports, usability test |
| Mar – May 2027 | Thesis & final defense | Thesis text — `final-pre-defense` |

Work runs in 2-week sprints with a weekly team sync and a meeting with the supervisor at least every two weeks.

## Dependencies

- Factor rasters depend on open data availability (Copernicus DEM, Sentinel-1, ESA WorldCover, SoilGrids, OSM).
- The main model depends on the flood inventory from Sentinel-1 (April 2024).
- API and web map depend on model outputs stored in PostGIS / COG.
- Usability testing depends on a working prototype and on survey volunteers.

## Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Too few flood points for training | Medium | High | Sentinel-1 2024 extents; AHP / FR baselines that need no inventory |
| Coarse data for Kazakh cities | Medium | High | Global open data at 10–30 m; fix the city list early |
| Overfitting (spatial autocorrelation) | Medium | Medium | Spatially blocked validation |
| Schedule slips (studies + work) | Medium | High | 2-week sprints, weekly sync, tasks with deadlines in Taiga |
| Scope creep (real-time warnings) | High | Medium | MoSCoW; warnings listed as future work |
| Uneven contribution in the team | Medium | High | Each task has an owner in Taiga; every member commits from their own account through PRs |

## Workflow

See [README](../README.md#how-we-work): task ID in branch and commit (`TG-23-...`), PR with review, tags for each pre-defense.
