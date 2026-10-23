from pathlib import Path

import pytest
import yaml

CONFIG = Path(__file__).resolve().parents[2] / "src/pipeline/config.example.yaml"
CITIES = ("astana", "petropavlovsk", "atyrau", "uralsk")


@pytest.fixture(scope="module")
def city_settings():
    with CONFIG.open(encoding="utf-8") as file:
        return yaml.safe_load(file)["cities"]


def test_all_cities_are_configured(city_settings):
    assert set(city_settings) == set(CITIES)


@pytest.mark.parametrize("city", CITIES)
def test_city_bbox(city_settings, city):
    bbox = city_settings[city]["bbox"]
    assert isinstance(bbox, list) and len(bbox) == 4
    assert all(type(value) in (int, float) for value in bbox)

    west, south, east, north = bbox
    assert -180 <= west < east <= 180
    assert -90 <= south < north <= 90
