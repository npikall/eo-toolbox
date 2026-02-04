"""Module to programticially get the filename of EO Data."""

from enum import Enum, auto

from pydantic import BaseModel


class DataType(Enum):
    """Enum for different Datatypes accepted by GeoFilePath."""

    PRIMARY = auto()
    COMPUTED = auto()


class GeoFilePath(BaseModel):
    """Basemodel to handle the Filename creation."""

    type: DataType
    spatial_extent: str
    temporal_extent: str
