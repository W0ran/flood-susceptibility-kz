# Project proposal

**Title:** GIS Model for Assessing the Flood Susceptibility of Kazakhstan's Cities: Terrain, Drainage and Land Use
*(ГИС-модель оценки подверженности городов Казахстана наводнениям: рельеф, дренаж и землепользование)*

**Programme:** Software Engineering, School of Software Engineering, Astana IT University
**Period:** September 2026 – May 2027
**Supervisor:** Tulebayev Yersultan Bakhytovich, Senior Lecturer

## Team

| Member | Group | Role | Responsibilities |
|---|---|---|---|
| Rakhymbay Yerkebulan | SE-2417 | QA engineer & developer | Data preparation, factor calculation in Python, model testing and validation against satellite flood extents, CI |
| Tenglesbayev Zhandos | SE-2414 | Developer | Model implementation, susceptibility maps, API and web map prototype |
| Tutkabay Assem | SE-2413 | Analyst & project manager | Literature review, factor justification and weighting, comparative analysis, schedule, supervisor contact |

## Problem statement

Spring snowmelt floods hit Kazakhstan's cities almost every year. In April 2024 nearly 100,000 people (99,869, including 36,591 children) were evacuated across six regions, and 66 settlements were cut off from roads (Ministry of Emergency Situations, via The Astana Times, 12 April 2024).

Residents and planners have no open, city-level map that shows which districts are susceptible to flooding and, crucially, **why**. Global flood maps are coarse and work as black boxes; Kazakh studies (Yertis basin, Ust-Kamenogorsk) confirm the hazard but stay in papers as static maps that non-experts cannot query.

## Target users

- Akimat urban planning departments
- Emergency services (MES) planners
- Residents choosing or insuring housing
- Researchers and students

## Aim

Build an interpretable GIS model that maps the flood susceptibility of districts in several flood-prone cities of Kazakhstan, explains each factor's contribution and lets users compare cities.

## Objectives

1. Review existing methods, data sources and systems for flood susceptibility mapping (see [literature review](literature-review.md), [existing systems](existing-systems.md)).
2. Confirm the need and requirements with potential users (see [relevance evidence](relevance-evidence.md)).
3. Collect open data for 3–4 cities and build 8–10 factor rasters grouped into terrain, drainage and land use.
4. Build an inventory of flooded / non-flooded points from Sentinel-1 imagery (April 2024).
5. Train the main model (Random Forest + SHAP) and two interpretable baselines (AHP, Frequency Ratio).
6. Validate the models and compare cities (see [evaluation plan](evaluation-plan.md)).
7. Deliver a web prototype: map, explanations, city comparison, export.

## Expected results

- Susceptibility maps (5 classes) for 3–4 cities
- Per-factor explanation for any location
- City-to-city comparison report
- Web prototype with an interactive map
- Validated model: AUC and error analysis

## Scope

**In scope:** flood *susceptibility* (where floods are structurally likely); 8–10 factors; 3–4 cities (candidates: Astana, Petropavl, Atyrau, Oral); open data only; web map.

**Out of scope:** real-time forecasting and flood warnings (requested in the survey, listed as future work); hydrodynamic simulation; damage in money.

## Engineering complexity

- Geospatial data pipeline over heterogeneous rasters and vectors (DEM, SAR, land cover, OSM), reproducible from raw data with one command.
- Machine learning with spatially blocked validation and per-cell SHAP explanations.
- Backend (FastAPI, PostGIS, tile server) and web client (React + Leaflet).
- Automated testing on three levels (pipeline, API, UI) in CI, plus usability testing.

## Related documents

[Requirements](requirements.md) · [Technology comparison](technology-comparison.md) · [Architecture diagrams](../diagrams/) · [Prototype](../prototype/) · [Project management](project-management.md) · [Supervisor feedback](supervisor-feedback.md)
