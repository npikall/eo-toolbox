"""eo-toolbox: A Package to..."""

from importlib.metadata import version

from eo_toolbox import calc, index, mask, stac

__version__ = version(__name__)

name = "eo_toolbox"

__all__ = [
    "calc",
    "index",
    "mask",
    "stac",
]
