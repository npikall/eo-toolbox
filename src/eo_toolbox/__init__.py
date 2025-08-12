# ruff: noqa: D104
from eo_toolbox import calc, index, mask, stac

__all__ = [
    "calc",
    "index",
    "mask",
    "stac",
]


def hello() -> str:
    """Return the greeting message."""
    return "Hello from eo-toolbox!"
