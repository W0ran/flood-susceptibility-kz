import argparse
import math
from contextlib import ExitStack
from pathlib import Path

import rasterio
import requests
import yaml
from rasterio.merge import merge

SOURCE = "https://copernicus-dem-30m.s3.eu-central-1.amazonaws.com"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = Path(__file__).with_name("config.example.yaml")
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def check_bbox(bbox):
    if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
        raise ValueError("bbox must have 4 numbers: west, south, east, north")
    if any(type(number) not in (int, float) for number in bbox):
        raise ValueError("bbox values must be numbers")

    west, south, east, north = bbox
    if not all(math.isfinite(number) for number in bbox):
        raise ValueError("bbox must contain finite numbers")
    if not (-180 <= west < east <= 180 and -90 <= south < north <= 90):
        raise ValueError("bbox coordinates are out of range or reversed")
    return tuple(bbox)


def get_city_bbox(city, config_path=CONFIG_PATH):
    with open(config_path, encoding="utf-8") as file:
        cities = yaml.safe_load(file)["cities"]

    name = city.strip().lower()
    if name not in cities:
        raise ValueError(f"Unknown city: {city}. Available: {', '.join(cities)}")
    return check_bbox(cities[name]["bbox"])


def tile_names(bbox):
    west, south, east, north = check_bbox(bbox)
    names = []
    for lat in range(math.floor(south), math.ceil(north)):
        for lon in range(math.floor(west), math.ceil(east)):
            ns = f"N{lat:02d}" if lat >= 0 else f"S{abs(lat):02d}"
            ew = f"E{lon:03d}" if lon >= 0 else f"W{abs(lon):03d}"
            names.append(f"Copernicus_DSM_COG_10_{ns}_00_{ew}_00_DEM")
    return names


def download_tile(name, folder):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.tif"
    if path.exists() and path.stat().st_size > 0:
        return path

    url = f"{SOURCE}/{name}/{name}.tif"
    partial = path.with_suffix(".part")
    try:
        with requests.get(url, stream=True, timeout=(15, 120)) as response:
            response.raise_for_status()
            with partial.open("wb") as file:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        file.write(chunk)
        partial.replace(path)
    finally:
        partial.unlink(missing_ok=True)
    return path


def download_dem(city, bbox, output_dir=RAW_DIR):
    bbox = check_bbox(bbox)
    names = tile_names(bbox)
    if len(names) > 16:
        raise ValueError("bbox is too large; choose a smaller area")

    output_dir.mkdir(parents=True, exist_ok=True)
    paths = [download_tile(name, output_dir / "tiles") for name in names]

    with ExitStack() as stack:
        rasters = [stack.enter_context(rasterio.open(path)) for path in paths]
        data, transform = merge(rasters, bounds=bbox)
        profile = rasters[0].profile.copy()

    profile.update(
        driver="GTiff",
        count=1,
        height=data.shape[1],
        width=data.shape[2],
        transform=transform,
        compress="deflate",
    )
    output_path = output_dir / f"{city.strip().lower()}_dem.tif"
    with rasterio.open(output_path, "w", **profile) as result:
        result.write(data)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Download Copernicus DEM for a city")
    parser.add_argument("--city", required=True, help="astana, petropavlovsk, atyrau, uralsk")
    parser.add_argument("--bbox", nargs=4, type=float, metavar=("W", "S", "E", "N"))
    args = parser.parse_args()

    bbox = check_bbox(args.bbox) if args.bbox else get_city_bbox(args.city)
    result = download_dem(args.city, bbox)
    print(f"DEM saved to {result}")


if __name__ == "__main__":
    main()
