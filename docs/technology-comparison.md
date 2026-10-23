### Technology comparison

Taiga: #10 «Сравнение технологий».

Four key technical decisions, each with three alternatives. ✓ marks the choice.

### 1. Susceptibility method

| Option | Pros | Cons |
|---|---|---|
| AHP (expert weights) | Simple, transparent, no flood inventory needed | Subjective weights, no accuracy check |
| Frequency Ratio | Statistical, easy to explain per class | Ignores factor interactions |
| ✓ Random Forest + SHAP | Potentially high predictive accuracy (to be confirmed by validation); SHAP explains every prediction | Needs a flood inventory, more complex; SHAP explains the model, not whether it is correct |

**Choice:** Random Forest + SHAP as the main model; AHP and Frequency Ratio kept as interpretable baselines.
**Requirement link:** NFR Accuracy (AUC ≥ 0.80), NFR Interpretability, FR2.

### 2. GIS processing stack

| Option | Pros | Cons |
|---|---|---|
| ✓ QGIS + Python (GDAL, rasterio, geopandas) | Free, scriptable, reproducible | Manual setup, local compute |
| ArcGIS Pro | Rich toolset, industry standard | Paid licence, Windows only |
| Google Earth Engine | Petabyte catalogue, fast | Vendor lock-in, quotas |

**Choice:** QGIS + Python for the pipeline; Earth Engine only to download Sentinel-1 flood extents.
**Requirement link:** NFR Reproducibility (pipeline re-runs from raw data with one command).

### 3. Spatial data storage

| Option | Pros | Cons |
|---|---|---|
| ✓ PostgreSQL + PostGIS | Spatial queries, multi-user, standard | Needs a server and admin |
| GeoPackage + COG files | Zero setup, portable | No concurrent queries |
| Cloud object storage | Scales, cheap for rasters | Cost, internet dependency |

**Choice:** PostGIS for districts, results and SHAP values; Cloud-Optimized GeoTIFF files for factor rasters.
**Requirement link:** FR2, FR3, NFR Performance (API p95 ≤ 500 ms).

### 4. Component communication and web map

| Option | Pros | Cons |
|---|---|---|
| ✓ FastAPI REST + Leaflet | Python end to end, automatic OpenAPI docs | Async learning curve |
| Flask + OpenLayers | Mature, many examples | More boilerplate, heavier client |
| Static map tiles only | Cheapest hosting | No queries or explanations |

**Choice:** FastAPI REST API (JSON + XYZ tiles) with a React + Leaflet front end; testable with Playwright and REST tests.
**Requirement link:** FR1-FR6, NFR Performance (tiles ≤ 1 s), NFR Maintainability.
