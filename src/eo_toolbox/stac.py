"""Module to load data from a preconfigured STAC Catalog."""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Literal

import odc.stac as odc_stac
import xarray as xr
from odc.geo.geobox import GeoBox
from pydantic import HttpUrl, validate_call
from pystac_client import Client

from eo_toolbox.valid_types import BoundingBox, TimeRangeStr

type XarrayObject = xr.DataArray | xr.Dataset


class NoDataError(Exception):
    """No data was found in the Stac Catalog."""


@dataclass
class CatalogConfig:
    """Attributes every config entry should hold."""

    url: HttpUrl
    collections: list[str]


CONFIG: dict[str, CatalogConfig] = {
    "element84": CatalogConfig(
        url=HttpUrl("https://earth-search.aws.element84.com/v1"),
        collections=["sentinel-2-l2a"],
    ),
    # TODO: Add CDSE and other collections  # noqa: FIX002
}


@validate_call
def sentinel2(  # noqa: PLR0913
    bounds: BoundingBox,
    timerange: TimeRangeStr,
    *,
    config: CatalogConfig = CONFIG["element84"],
    epsg: int = 4326,
    dx: float = 0.0006,
    bands: str | Sequence[str] | None = None,
    chunks: dict[str, int | Literal["auto"]] | None = None,
    odc_kwargs: dict,
) -> XarrayObject:
    """Load Sentinel-2 Data."""
    if chunks is None:
        chunks = {"time": "auto", "x": "auto", "y": "auto"}

    items = (
        Client.open(config.url)  # type: ignore
        .search(
            bbox=bounds,
            collections=config.collections,
            datetime=timerange,
        )
        .item_collection()
    )
    if len(items) == 0:
        msg: str = f"No data found in the STAC Catalog with url: {config.url}"
        raise NoDataError(msg)

    # Load items into xarray
    geobox = GeoBox.from_bbox(bounds, crs=f"epsg:{epsg}", resolution=dx)
    return odc_stac.load(
        items,
        bands=bands,
        chunks=chunks,
        geobox=geobox,
        resampling="bilinear",
        **odc_kwargs,
    )
