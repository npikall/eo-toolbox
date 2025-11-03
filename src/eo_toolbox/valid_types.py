"""Type definitions that pydantic can validate."""

from datetime import UTC, datetime
from typing import Annotated

import xarray as xr
from annotated_types import Interval, Len
from pydantic import BeforeValidator


def validate_iso_date_is_before_today(date_string: str) -> None:
    """Raise ValidationError if date_string is not before today."""
    today = datetime.now(tz=UTC).date()
    earliest_allowed_date = datetime(1970, 1, 1, tzinfo=UTC).date()

    try:
        day = datetime.fromisoformat(date_string).date()
    except ValueError as e:
        err: str = f"Date must be in ISO format (YYYY-MM-DD): {date_string}"
        raise ValueError(err) from e

    if not (earliest_allowed_date <= day <= today):
        err: str = (
            f"Date must be before {today} and after {earliest_allowed_date}"
        )
        raise ValueError(err)


def validate_time_range_str(value: str) -> str:
    """Validate that one or two dates are specified and separated via Slash."""
    parts = value.split("/")
    max_timestamps = 2
    if not (1 <= len(parts) <= max_timestamps):
        err: str = "Must be either one or two ISO timestamps separated via '/'"
        raise ValueError(err)

    for part in parts:
        validate_iso_date_is_before_today(part)

    return value


def validate_bounding_box(
    value: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    """Validate the order of the values in the bounding box."""
    if not (value[0] < value[2] and value[1] < value[3]):
        err = "Invalid bounding box: (min_lon, min_lat, max_lon, max_lat)"
        raise ValueError(err)
    return value


type XarrayObject = xr.DataArray | xr.Dataset
# fmt: off
type BoundingBox = Annotated[
    tuple[
        Annotated[float, Interval(ge=-180, le=180)],  # min x or lonmin
        Annotated[float, Interval(ge=-90, le=90)],    # min y or latmin
        Annotated[float, Interval(ge=-180, le=180)],  # max x or lonmax
        Annotated[float, Interval(ge=-90, le=90)],    # max y or latmax
    ], Len(4), BeforeValidator(validate_bounding_box),
]
type TimeRangeStr = Annotated[str, BeforeValidator(validate_time_range_str)]
# fmt: on
