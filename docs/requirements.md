# Requirements specification

Taiga: #11 «Функциональные и нефункциональные требования».

Prioritised with MoSCoW. ↑ = priority raised after the user survey (n = 22), see [relevance evidence](relevance-evidence.md).

## Functional requirements

| ID | Requirement | Priority | Acceptance criterion | Use case |
|---|---|---|---|---|
| FR1 | Show a susceptibility map (5 classes) for a selected city | Must | The map loads in ≤ 3 s for each of the 3–4 cities | View susceptibility map |
| FR2 | Explain factor contributions for any clicked location | Must | The panel lists all factors with SHAP shares summing to 100% | See factor explanation |
| FR3 | Compare cities by share of area in each class | Must | Chart values match values computed from the rasters (±1%) | Compare cities |
| FR4 | Search by address or coordinates | Must ↑ | Top-1 geocoding hit for 9 of 10 test addresses | Search address |
| FR5 | Toggle layers: factors, 2024 flood extent | Should | Each layer toggles without page reload | View susceptibility map |
| FR6 | Export a city report (PDF) and data (GeoTIFF) | Could | Files open in a PDF reader and in QGIS | Export report / data |
| FR7 | Interface in Kazakh, Russian and English | Should ↑ | All UI strings translated; the language switch persists | all |
| FR8 | Re-run the model with new data (admin) | Won't (now) | Deferred until after the diploma | Update data & retrain |

## Non-functional requirements

| Category | Requirement | Priority | Acceptance criterion / measurement |
|---|---|---|---|
| Accuracy | Model discriminates flooded and non-flooded locations | Must | AUC ≥ 0.80 on held-out flood points (spatially blocked split) |
| Interpretability | Every result has a factor explanation | Must | 100% of map cells return SHAP values via the API |
| Reproducibility | Pipeline re-runs from raw data with one command | Must | Clean run on a new machine produces identical rasters (checksum) |
| Security | No personal data stored; HTTPS only; secrets out of Git | Must | Secret scan in CI passes; no personal fields in the DB schema |
| Performance | Fast map and API | Should | Map tiles ≤ 1 s; API p95 ≤ 500 ms under 20 concurrent users |
| Usability | First-time users understand the map | Should | SUS ≥ 70 with 5+ test users; "is my district at risk and why" answered in ≤ 60 s |
| Compatibility | Works in common browsers and on phones | Should | Chrome, Firefox, Safari; mobile width 375 px |
| Maintainability | Code is tested | Should | Test coverage ≥ 70% for API and pipeline |

## Traceability

Each Must requirement is verified by a test or metric in the [evaluation plan](evaluation-plan.md). Use cases are shown in the [use case diagram](../diagrams/).
