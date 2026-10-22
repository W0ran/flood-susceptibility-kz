# Architecture diagrams

Editable sources are the `.mmd` files in this folder (Mermaid). GitHub renders them below; PNG exports used in the pre-defense presentation (slides 14–16) are in `exports/`.

Taiga task: #12 «Диаграммы архитектуры». Owner: Tenglesbayev Zhandos.

## System context diagram

Who uses the system and which open data sources feed it.

Source: [`system-context.mmd`](system-context.mmd) · Export: [`exports/system-context.png`](exports/system-context.png)

```mermaid
%% System context diagram — Flood Susceptibility System
%% Source of truth for slide 14. Edit here, then re-export PNG to diagrams/exports/.
flowchart LR
    subgraph Users
        R[Resident]
        UP["Urban planner (akimat)"]
        MES[MES planner]
        RS["Researcher / student"]
    end

    SYS(["Flood Susceptibility System"])

    subgraph External data sources
        DEM[("Copernicus DEM / SRTM")]
        S1[("Sentinel-1 via Earth Engine")]
        WC[("ESA WorldCover & SoilGrids")]
        OSM[("OpenStreetMap (rivers, geocoding)")]
    end

    R -- views map --> SYS
    UP -- compares cities --> SYS
    MES -- gets explanations --> SYS
    RS -- exports data --> SYS

    DEM -- elevation --> SYS
    S1 -- flood extents --> SYS
    WC -- land cover, soil --> SYS
    OSM -- rivers, addresses --> SYS
```

## Use case diagram

What each actor can do. The Researcher inherits all Planner use cases.

Source: [`use-case.mmd`](use-case.mmd) · Export: [`exports/use-case.png`](exports/use-case.png)

```mermaid
%% Use case diagram — Flood Susceptibility System
%% Source of truth for slide 15. Mermaid has no native UML use case type,
%% so actors are drawn as nodes and use cases as stadium shapes.
%% Researcher inherits all Planner use cases.
flowchart LR
    Resident(("👤 Resident"))
    Planner(("👤 Planner<br/>(akimat / MES)"))
    Researcher(("👤 Researcher"))
    Admin(("👤 Data admin<br/>(team)"))

    subgraph SYS["Flood Susceptibility System"]
        UC1([View susceptibility map])
        UC2([Search address])
        UC3([See factor explanation])
        UC4([Compare cities])
        UC5([Export report / data])
        UC6([Update data & retrain])
    end

    Resident --- UC1
    Resident --- UC2
    Resident --- UC3

    Planner --- UC1
    Planner --- UC3
    Planner --- UC4
    Planner --- UC5

    Researcher -. inherits .-> Planner

    Admin --- UC6
```

## Component diagram (first draft)

How the system is split into layers. Processing runs offline as a Python pipeline and writes to the data layer; the API only reads.

Source: [`component.mmd`](component.mmd) · Export: [`exports/component.png`](exports/component.png)

```mermaid
%% Component diagram (first draft) — Flood Susceptibility System
%% Source of truth for slide 16.
%% Processing runs offline as a Python pipeline and writes results to the data layer; the API only reads.
flowchart TB
    subgraph Presentation
        WEB["Web client<br/>(React + Leaflet)"]
    end

    subgraph API
        REST["REST API (FastAPI)<br/>map · explain · compare · export"]
        TILES["Tile server<br/>(XYZ from COG)"]
    end

    subgraph Processing["Processing (offline Python pipeline)"]
        ING["Data ingestion<br/>(DEM, Sentinel-1, OSM)"]
        FAC["Factor builder<br/>(slope, TWI, distances)"]
        MOD["Model + SHAP<br/>(RF, AHP, FR)"]
    end

    subgraph Data
        PG[("PostGIS: districts, results, SHAP")]
        COG[("COG rasters: factors, maps")]
    end

    WEB -- JSON / HTTPS --> REST
    WEB -- tiles --> TILES
    ING --> FAC --> MOD
    MOD -- writes --> PG
    MOD -- writes --> COG
    FAC -- writes --> COG
    REST -- reads --> PG
    TILES -- reads --> COG
```

## How to update

1. Edit the `.mmd` file (preview at https://mermaid.live).
2. Export PNG to `exports/` with the same name.
3. Update the slide in the presentation if the diagram changed.
