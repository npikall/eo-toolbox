# ruff: noqa: D104
from eo_toolbox import calc
from eo_toolbox import index
from eo_toolbox import mask

__all__ = [
    "calc",
    "index",
    "mask",
]


def hello() -> str:
    """Return the greeting message."""
    return "Hello from eo-toolbox!"
