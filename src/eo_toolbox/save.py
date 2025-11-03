"""Save arrays as files locally.

Saving xarray objects can often be cumbersome, as many libraries offer various
methods to write these objects to disk. This module aims to simplify this
process by providing a unified and convenient interface for saving xarray
objects, without having to think about the exact implementation details.
"""

from enum import Enum, auto
from pathlib import Path

import rioxarray as rio  # noqa: F401

from eo_toolbox.valid_types import XarrayObject


class SaveMethod(Enum):
    """Different Methods to use to save an xarray object."""

    RIO = auto()
    ZARR = auto()

    @classmethod
    def list(cls) -> list[str]:
        """List all available Saving Methods."""
        return [member.name for member in cls]


def save_xarray(
    array: XarrayObject,
    *,
    savepath: Path,
    auto_suffix: bool = True,
    method: SaveMethod = SaveMethod.RIO,
) -> None:
    """Save an xarray object to disk.

    The file suffix will automatically be changed accordingly.

    Methods:
    - RIO: saves to tiff with rioxarray
    - ZARR: save as a zarr file

    """
    savepath.parent.mkdir(parents=True, exist_ok=True)
    if auto_suffix:
        match method:
            case SaveMethod.RIO:
                savepath = savepath.with_suffix(".tiff")
            case SaveMethod.ZARR:
                savepath = savepath.with_suffix(".zarr")
    if savepath.is_file():
        savepath.unlink()
    match method:
        case SaveMethod.RIO:
            array.rio.to_raster(
                savepath,
                driver="GTiff",
                compress="lzw",
            )
        case SaveMethod.ZARR:
            array.to_zarr(
                savepath,
                zarr_format=2,
                consolidated=False,
                mode="w",
            )
        case _:
            err: str = f"Method '{method.__name__}' is not known."
            raise ValueError(err)
