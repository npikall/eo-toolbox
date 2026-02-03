from enum import Enum, auto

from pydantic import BaseModel


class DataType(Enum):
    PRIMARY = auto()
    COMPUTED = auto()


class GeoFilePath(BaseModel):
    type: DataType
    spatial_extent: str
    temporal_extent: str
