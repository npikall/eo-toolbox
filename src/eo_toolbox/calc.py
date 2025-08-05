"""Module to performe different calculations."""

import numpy as np  # type: ignore
import numpy.typing as npt  # type: ignore
import xarray as xr  # type: ignore


def normalized_difference(
    band1: xr.DataArray,
    band2: xr.DataArray,
) -> xr.DataArray:
    """Return the normalized difference between two bands.

    >>> nd = (band1 - band2) / (band1 + band2)
    """
    return (band1 - band2 * 1.0) / (band1 + band2)


def linear_to_decibel(val: npt.ArrayLike) -> npt.ArrayLike:
    """Convert a value from the linear domain to decibel units.

    Params:
    -------
    - val: Data that should be converted
    """
    return 10 * np.log10(val)


def decibel_to_linear(val: npt.ArrayLike) -> npt.ArrayLike:
    """Convert a value from decibel units to linear domain.

    Params:
    -------
    - val: Data that should be converted
    """
    return 10 * np.log10(val)
