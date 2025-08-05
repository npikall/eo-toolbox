"""Module for operations related to masking in Earth Observation scl."""

from enum import IntEnum

import xarray as xr  # type: ignore


class SCLValues(IntEnum):
    """Enum for Sentinel-2 Scene Classification Layer (SCL) values."""

    # https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/scene-classification/
    NO_DATA = 0  # Not Wanted
    DEFECTIVE = 1  # Not Wanted
    DARK_SHADOWS = 2  # Not Wanted
    CLOUD_SHADOWS = 3  # Not Wanted
    VEGETATED = 4  # Wanted
    NOT_VEGETATED = 5  # Wanted
    WATER = 6  # Wanted
    CLOUDS_LOW_PROB = 7  # ???
    CLOUDS_MEDIUM_PROB = 8  # Not Wanted
    CLOUDS_HIGH_PROB = 9  # Not Wanted
    THIN_CIRRUS = 10  # ???
    SNOW_OR_ICE = 11  # Wanted


def is_valid_pixel(
    scl: xr.DataArray,
    *,
    include_little_clouds: bool = False,
) -> xr.DataArray:
    """Check if a pixel is valid based on the SCL (Scene Classification Layer).

    A pixel is considered valid if its not a cloud or shadow pixel.
    """
    # include only vegetated, not_vegitated, water, and snow
    # https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/scene-classification/
    if include_little_clouds:
        # include thin cirrus and clouds with low probability
        return (
            (scl >= SCLValues.VEGETATED)
            & (scl <= SCLValues.CLOUDS_MEDIUM_PROB)
        ) | (scl >= SCLValues.THIN_CIRRUS)

    return (
        (scl >= SCLValues.VEGETATED) & (scl <= SCLValues.CLOUDS_LOW_PROB)
    ) | (scl == SCLValues.SNOW_OR_ICE)
