# Comparison with existing systems

Taiga: #9 «Сравнение существующих систем».

Four relevant systems are compared with the proposed solution on 8 criteria. Ratings are our assessment from public documentation and will be re-checked during the review.

| Criterion | Copernicus GloFAS | WRI Aqueduct Floods | ThinkHazard! (GFDRR) | Kazhydromet bulletins | Our system |
|---|---|---|---|---|---|
| Purpose | Forecast | Risk maps | Hazard level | Bulletins | Susceptibility |
| District-level detail in cities | No | No | No | No | Yes |
| Explains contributing factors | No | No | Partly | No | Yes |
| Compares cities | No | Partly | No | No | Yes |
| Interactive web map | Yes | Yes | Yes | Partly | Yes |
| Free and open | Yes | Yes | Yes | Yes | Yes |
| Kazakh / Russian interface | No | No | No | Yes | Planned |
| Focus on Kazakhstan | No | No | No | Yes | Yes |

## Why a new solution is needed

1. **Too coarse.** Global products work at river-basin or province scale, so a district inside Astana or Petropavl gets one value.
2. **Black box.** Users see a risk class but not the reason: terrain, river proximity, soil or land cover.
3. **Forecast ≠ susceptibility.** GloFAS and bulletins warn about a specific event; they do not show where floods are structurally likely.
4. **No local tool.** Kazakh research results stay in papers; nothing lets a planner query and compare cities.

**Our answer:** an open, district-level susceptibility map for Kazakhstan's cities that explains every result.

## How the systems are used in the project

- GloFAS and Aqueduct / JRC global hazard maps serve as **baseline 3** in the [evaluation plan](evaluation-plan.md): our model must beat them on agreement with the 2024 flood extents.
- Kazhydromet bulletins are a source of flood event dates for building the inventory.
