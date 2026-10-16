# GIS Model for Assessing the Flood Susceptibility of Kazakhstan’s Cities: Terrain, Drainage and Land Use

*ГИС-модель оценки подверженности городов Казахстана наводнениям: рельеф, дренаж и землепользование*

Diploma project · School of Software Engineering · Astana IT University · 2026–2027

The project builds an interpretable model that maps how susceptible districts of Kazakhstan's cities are to flooding, explains which factors drive the risk (SHAP), and lets users compare cities through a web map.

## Team

| Member | Group | Role | Main responsibilities |
|---|---|---|---|
| Rakhymbay Yerkebulan | SE-2417 | QA engineer & developer | Data preparation, factor calculation (Python), testing, model validation, CI |
| Tenglesbayev Zhandos | SE-2414 | Developer | Model implementation, susceptibility maps, API and web map |
| Tutkabay Assem | SE-2413 | Analyst & project manager | Literature review, factor weighting, comparative analysis, schedule |

**Supervisor:** Tulebayev Yersultan Bakhytovich, Senior Lecturer

## Repository structure

```
src/        source code: data pipeline, model, API, web client
data/       small sample data and data source descriptions (no large rasters)
docs/       presentations, reports, requirements, survey results
diagrams/   system context, use case and component diagrams
tests/      automated tests (pytest, API and UI tests)
```

## Stack

Python (GDAL, rasterio, geopandas, scikit-learn, SHAP) · QGIS · PostgreSQL + PostGIS · FastAPI · React + Leaflet · pytest, Playwright

## How we work

- Tasks live in YouTrack, project key **DIP**. Every branch and commit starts with the task ID.
- Branch name: `DIP-23-database-schema`. Commit message: `DIP-23 Add districts table`.
- No direct pushes to `main`: work in a branch, open a Pull Request, get one review from a teammate, then merge.
- Commit small and often. Each member commits from their own GitHub account.
- Never commit passwords, API keys, tokens or personal data. Large rasters stay out of Git (see `data/README.md`).
- Milestones are tagged: `pre-defense-1`, `pre-defense-2`, `final`.

## Status

Current stage: requirements, analysis and design (pre-defense 1, 24 October 2026).
