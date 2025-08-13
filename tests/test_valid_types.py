"""Test if pydantic validations work correctly."""

import pytest  # noqa: F401
from pydantic import validate_call
from eo_toolbox.valid_types import TimeRangeStr, BoundingBox


def test_validate_timerangestr_returns_correct():
    # Mock function that should be validated
    @validate_call
    def foo(bar: TimeRangeStr):
        return bar

    # Correct Strings
    assert foo("2020-01-01") == "2020-01-01"
    assert foo("2020-01-01/2020-02-05") == "2020-01-01/2020-02-05"

    # Wrong Strings
    with pytest.raises(ValueError):
        # Too far in the future
        foo("2050-01-01")

    with pytest.raises(ValueError):
        # Too early
        foo("1950-01-01")

    with pytest.raises(ValueError):
        # Lower is out of Bounds
        foo("1969-01-01/2020-02-05")

    with pytest.raises(ValueError):
        # Upper is out of Bounds
        foo("2020-01-01/2050-02-05")

    with pytest.raises(ValueError):
        # No timestamp at all
        foo("Hello")

    with pytest.raises(ValueError):
        # Wrong datetime format
        foo("10.03.2002")

def test_validate_bbox_returns_correct():
    # Mock function that should be validated
    @validate_call
    def foo(bar: BoundingBox):
        return bar

    # Correct Bounding Boxes
    assert foo((-180.0, -90.0, 180.0, 90.0)) == (-180.0, -90.0, 180.0, 90.0)
    assert foo((-10.0, -10.0, 10.0, 10.0)) == (-10.0, -10.0, 10.0, 10.0)

    # Wrong Bounding Boxes
    with pytest.raises(ValueError):
        # min_lon > max_lon
        foo((10.0, -10.0, -10.0, 10.0))

    with pytest.raises(ValueError):
        # min_lat > max_lat
        foo((-10.0, 10.0, 10.0, -10.0))

    with pytest.raises(ValueError):
        # min_lon > max_lon and min_lat > max_lat
        foo((10.0, 20.0, -10.0, -20.0))

    with pytest.raises(ValueError):
        # minlon == max_lon
        foo((10.0, -20.0, 10.0, 20.0))