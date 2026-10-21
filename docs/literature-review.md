# Literature review

Taiga: #8 «Обзор литературы».

12 peer-reviewed publications are used, including foundational works (AHP, SHAP) and recent studies (2021–2026), two of them on Kazakhstan. Bibliographic data checked against publisher pages on 21 October 2026.

## Analysis table

| # | Authors, year | Title | Source | Method / data | Key finding / limitation | What we use |
|---|---|---|---|---|---|---|
| 1 | Saaty, 1990 | How to make a decision: The analytic hierarchy process | European Journal of Operational Research, 48(1), 9–26. doi:10.1016/0377-2217(90)90057-I | AHP theory | Structured pairwise comparison of criteria; weights remain subjective | Expert factor weights for the AHP baseline |
| 2 | Rahmati, Pourghasemi & Zeinivand, 2016 | Flood susceptibility mapping using frequency ratio and weights-of-evidence models in the Golastan Province, Iran | Geocarto International, 31(1), 42–70. doi:10.1080/10106049.2015.1041559 | Frequency Ratio, Weights-of-Evidence; Iran | Simple bivariate models give good accuracy; ignore factor interactions | Statistical (FR) baseline model |
| 3 | Tehrany, Pradhan & Jebur, 2014 | Flood susceptibility mapping using a novel ensemble weights-of-evidence and support vector machine models in GIS | Journal of Hydrology, 512, 332–343. doi:10.1016/j.jhydrol.2014.03.008 | WoE + SVM ensemble; Malaysia | Ensemble outperforms single models; factor ranking | Ensemble idea, factor ranking |
| 4 | Khosravi et al., 2018 | A comparative assessment of decision trees algorithms for flash flood susceptibility modeling at Haraz watershed, northern Iran | Science of the Total Environment, 627, 744–755. doi:10.1016/j.scitotenv.2018.01.266 | Tree-based ML; Iran | Tree ensembles achieve high AUC on flood inventories | Tree models for the main model |
| 5 | Pham et al., 2021 | Flood risk assessment using hybrid artificial intelligence models integrated with multi-criteria decision analysis in Quang Nam Province, Vietnam | Journal of Hydrology, 592, 125815. doi:10.1016/j.jhydrol.2020.125815 | Hybrid AI + MCDA; Vietnam | Combining ML susceptibility with MCDA improves risk maps | Combining MCDA baselines with ML |
| 6 | Lundberg & Lee, 2017 | A unified approach to interpreting model predictions | Advances in Neural Information Processing Systems 30 (NeurIPS 2017), 4765–4774 | SHAP values | Consistent, additive per-feature attributions for any model | Per-factor explanations for every cell |
| 7 | Bentivoglio et al., 2022 | Deep learning methods for flood mapping: a review of existing applications and future research directions | Hydrology and Earth System Sciences, 26, 4345–4378. doi:10.5194/hess-26-4345-2022 | Review | Deep models rarely explain results; interpretability is an open gap | Justifies the interpretability focus |
| 8 | Twele et al., 2016 | Sentinel-1-based flood mapping: a fully automated processing chain | International Journal of Remote Sensing, 37(13), 2990–3004. doi:10.1080/01431161.2016.1192304 | Sentinel-1 SAR | Automated thresholding of SAR images gives reliable flood extents | Flood extents for training and validation |
| 9 | Tellman et al., 2021 | Satellite imaging reveals increased proportion of population exposed to floods | Nature, 596, 80–86. doi:10.1038/s41586-021-03695-w | MODIS, 2000–2018 | Population exposed to floods grew 20–24% | Motivation: rising exposure |
| 10 | Ward et al., 2015 | Usefulness and limitations of global flood risk models | Nature Climate Change, 5, 712–715. doi:10.1038/nclimate2742 | Global models | Global models are useful for screening but too coarse for local decisions | Why a local model is needed |
| 11 | Apshikur et al., 2023 | The method of multi-criteria analysis for determining the flood-hazardous area and the development of protective structures | ISPRS Archives (Int. Arch. Photogramm. Remote Sens. Spatial Inf. Sci.) | GIS multi-criteria analysis; Ust-Kamenogorsk | MCA identifies flood-hazardous zones of a Kazakh city | Kazakhstan context, factor choice |
| 12 | Makhmudova et al., 2026 | Modeling flood-prone areas using statistical and GIS approaches: Insights from the Yertis River basin, Kazakhstan | Environments (MDPI) | DEM-based scenarios; Yertis basin | Flood-prone zones of Kazakh cities along the Yertis | Flood zones of KZ cities, validation context |

## Other sources

- The Astana Times, 12 April 2024 — official figures on the spring 2024 floods.
- Copernicus GloFAS; WRI Aqueduct Floods; ThinkHazard!; Kazhydromet bulletins — see [existing systems](existing-systems.md).

## Synthesis

**What approaches exist.** Expert MCDA (AHP), bivariate statistics (FR, WoE) and machine learning (SVM, tree ensembles, hybrids). ML gives the highest accuracy but needs a flood inventory; MCDA and FR are transparent but subjective or ignore interactions.

**What is known.** Terrain (elevation, slope, TWI), drainage (distance to rivers, drainage density) and land use (land cover, soil, imperviousness) are the most frequently used and most important factors. Sentinel-1 SAR provides reliable flood extents for training and validation.

**Limitations the project takes into account.**
- Black-box ML → per-cell SHAP explanations.
- Subjective AHP weights → AHP used only as a baseline; sensitivity test ±20%.
- Spatial autocorrelation inflates accuracy → spatially blocked validation.
- Global models are too coarse → district-level maps for Kazakh cities.

**Gap.** There is no open, interpretable, district-level flood susceptibility tool for Kazakhstan's cities that non-experts can query and compare.
