# GIS Model for Assessing the Flood Susceptibility of Kazakhstan’s Cities: Terrain, Drainage and Land Use

*ГИС-модель оценки подверженности городов Казахстана наводнениям: рельеф, дренаж и землепользование*

Diploma project · School of Software Engineering · Astana IT University · 2026–2027

The project builds an interpretable model that maps how susceptible districts of Kazakhstan's cities are to flooding, explains which factors drive the risk (SHAP), and lets users compare cities through a web map.

### Links

- **Task board (Taiga):** https://tree.taiga.io/project/yerkosh-flood-susceptibility-kz-diploma/backlog
- **Pre-defense 1 presentation:** [`docs/presentations/pre-defense-1.pdf`](docs/presentations/pre-defense-1.pdf)
- **Documentation:** [`docs/`](docs/)  **Diagrams:** [`diagrams/`](diagrams/)  **Prototype:** [`prototype/`](prototype/)

### Problem, users and expected outcomes

**Problem.** Spring snowmelt floods hit Kazakhstan's cities almost every year; in April 2024 nearly 100,000 people were evacuated across six regions. Residents and planners have no open, city-level map that shows which districts are susceptible and why. Global flood maps are coarse and black-box; local studies stay in papers.

**Target users.** Akimat urban planning departments, emergency services (MES) planners, residents choosing or insuring housing, researchers and students.

**Expected outcomes.** Susceptibility maps (5 classes) for 3–4 cities; per-factor explanation for any location; a city-to-city comparison report; a web prototype with an interactive map; a validated model (AUC and error analysis).

**Scope.** In: susceptibility, 8–10 factors (terrain, drainage, land use), 3–4 cities (candidates: Astana, Petropavl, Atyrau, Oral), open data, web map. Out: real-time forecasting and warnings, hydrodynamic simulation, damage in money. Details: [`docs/project-proposal.md`](docs/project-proposal.md).

### Team

| Member | Group | Role | Main responsibilities |
|---|---|---|---|
| Rakhymbay Yerkebulan | SE-2417 | QA engineer & developer | Data preparation, factor calculation (Python), testing, model validation, CI |
| Tenglesbayev Zhandos | SE-2414 | Developer | Model implementation, susceptibility maps, API and web map |
| Tutkabay Assem | SE-2413 | Analyst & project manager | Literature review, factor weighting, comparative analysis, schedule |

**Supervisor:** Tulebayev Yersultan Bakhytovich, Senior Lecturer

### Repository structure

```
src/        source code: data pipeline, model, API, web client
data/       small sample data and data source descriptions (no large rasters)
docs/       proposal, relevance evidence, literature, comparisons, requirements, plans
diagrams/   system context, use case and component diagrams (editable sources + PNG)
prototype/  UX mockups of key scenarios and draft API
tests/      automated tests (pytest, API and UI tests)
```

### Documentation

| Document | Content |
|---|---|
| [Project proposal](docs/project-proposal.md) | Problem, users, aim, objectives, expected results, scope |
| [Evidence of relevance](docs/relevance-evidence.md) | Survey (n = 22), hypotheses, impact on requirements; [interview guide](docs/interviews/) |
| [Literature review](docs/literature-review.md) | 12 peer-reviewed publications, analysis table, gap |
| [Existing systems](docs/existing-systems.md) | 4 systems × 8 criteria |
| [Technology comparison](docs/technology-comparison.md) | 4 key decisions × 3 alternatives |
| [Requirements](docs/requirements.md) | FR / NFR with MoSCoW priorities and acceptance criteria |
| [Architecture diagrams](diagrams/) | System context, use case, component (draft) |
| [Prototype](prototype/) | Mockups of key scenarios, draft API |
| [Evaluation plan](docs/evaluation-plan.md) | Model metrics, baselines, software testing |
| [Project management](docs/project-management.md) | Roles, milestones, dependencies, risks |
| [Supervisor feedback](docs/supervisor-feedback.md) | Comments and decisions |

### Stack

Python (GDAL, rasterio, geopandas, scikit-learn, SHAP) · QGIS · PostgreSQL + PostGIS · FastAPI · React + Leaflet · pytest, Playwright

### How we work

- Tasks live in [Taiga](https://tree.taiga.io/project/yerkosh-flood-susceptibility-kz-diploma/backlog) (Scrum, 2-week sprints). Every task has an owner, priority, acceptance criteria and a due date.
- Every branch and commit starts with the Taiga task reference `TG-<number>`.
- Branch name: `TG-24-database-schema`. Commit message: `TG-24 Add districts table`.
- The Pull Request description links the Taiga task; the Taiga task gets a comment with the PR link when it moves to «Ожидает проверки».
- No direct pushes to `main`: work in a branch, open a Pull Request, get one review from a teammate, then merge.
- Commit small and often. Each member commits from their own GitHub account.
- Never commit passwords, API keys, tokens or personal data. Large rasters stay out of Git (see `data/README.md`).
- Milestones are tagged: `prob-period-1` (pre-defense 1, as required by the submission form), `pre-defense-2`, `final-pre-defense`. Tags are never moved.

### Use of AI tools

Parts of this stage were prepared with the help of an AI assistant (Claude, Anthropic).

### Status

Current stage: requirements, analysis and design (pre-defense 1, 24 October 2026).

| Done for pre-defense 1 | Next |
|---|---|
| Proposal, survey (n = 22), literature review, existing systems, technology comparison, requirements, diagrams, mockups, evaluation plan | Interviews with 3–5 users (TG-7), clickable Figma prototype (TG-13), AHP weights and city list (TG-16), data collection (TG-18) |

**Known limitations:** the survey sample is mostly Astana students; interviews are not done yet; no runnable code yet (planned from November 2026).

### Setup and testing

No runnable code yet. Setup, run and test instructions will be added here together with the data pipeline (TG-18, TG-19) and CI (TG-17).
