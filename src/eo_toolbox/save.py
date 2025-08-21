"""Save arrays as files locally.

Saving xarray objects can often be cumbersome, as many libraries offer various
methods to write these objects to disk. This module aims to simplify this
process by providing a unified and convenient interface for saving xarray
objects, without having to think about the exact implementation details.
"""

from enum import Enum, auto
from pathlib import Path

import rioxarray as rio  # noqa: F401
from pydantic import validate_call

from eo_toolbox.valid_types import XarrayObject


class SaveMethod(Enum):
    """Different Methods to use to save a xarray object."""

    RIO = auto()

    @classmethod
    def list(cls) -> list[str]:
        """List all available Saving Methods."""
        return [member.name for member in cls]


@validate_call
def save_xr(
    array: XarrayObject,
    *,
    savepath: Path,
    method: SaveMethod = SaveMethod.RIO,
) -> None:
    """Save a xarray object to disk."""
    savepath.parent.mkdir(parents=True, exist_ok=True)
    if savepath.exists():
        savepath.unlink()
    match method:
        case SaveMethod.RIO:
            array.rio.to_raster(savepath, driver="GTiff")
        case _:
            err: str = f"Method '{method.__name__}' is not known."
            raise ValueError(err)
