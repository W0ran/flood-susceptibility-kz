### Verification and evaluation plan

Taiga: #14 «План верификации и оценки».

### 1. Model evaluation

| Aspect | Metric | Target | Measurement conditions |
|---|---|---|---|
| Discrimination | AUC-ROC | ≥ 0.80 | 70/30 spatially blocked split of flood / non-flood points |
| Classification | Accuracy, F1, Cohen's Kappa | F1 ≥ 0.75 | Threshold 0.5; balanced sample |
| Agreement with reality | Share of the 2024 flooded area in High / Very high classes | ≥ 70% | Sentinel-1 flood extents, April 2024 |
| Explanation stability | Rank correlation of SHAP importances | ≥ 0.8 | 10 bootstrap retrains |
| Sensitivity | Change of the class map when AHP weights change ±20% | ≤ 15% of cells | One-at-a-time weight perturbation |

### Baselines

1. AHP-only model (expert weights)
2. Frequency Ratio model
3. Global flood hazard maps (JRC / Aqueduct) resampled to districts

The main model (Random Forest + SHAP) must beat all three on AUC and on agreement with the 2024 flood extents.

### 2. Software testing

| Level | What is tested | Tool | Target |
|---|---|---|---|
| Data pipeline | Factor rasters: CRS, resolution, no-data, value ranges | pytest | Coverage ≥ 70% |
| REST API | Contract tests on every endpoint, OpenAPI schema check | pytest / RestAssured | All endpoints green in CI |
| Web UI | End-to-end tests of the 3 key scenarios in 3 browsers | Playwright | p95 tile load ≤ 1 s |
| Usability | 5+ users from the survey do 3 tasks, then fill in SUS | Moderated test | SUS ≥ 70, task ≤ 60 s |

Tests run in GitHub Actions on every pull request. Bugs are tracked in Taiga with the task ID (for example `TG-23`).

### 3. Requirement coverage

| Requirement | Verified by |
|---|---|
| FR1 Map | Playwright scenario 1, load time check |
| FR2 Explanation | API contract test: normalized absolute SHAP shares sum to 100% (±0.1), signs match raw SHAP values |
| FR3 Comparison | Unit test comparing chart values with raster statistics |
| FR4 Search | 10 test addresses, top-1 hit rate |
| NFR Accuracy | AUC on the spatially blocked test set |
| NFR Interpretability | API test on a random sample of cells |
| NFR Reproducibility | CI job re-running the pipeline on sample data, checksum compare |
| NFR Usability | SUS questionnaire and task timing |
