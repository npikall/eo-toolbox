"""Test if pydantic validations work correctly."""
# ruff: noqa: PT011

import pytest
from pydantic import validate_call

from eo_toolbox.valid_types import BoundingBox, TimeRangeStr


def test_validate_timerangestr_returns_correct():
    # Mock function that should be validated
    @validate_call
    def do_nothing_but_validate(bar: TimeRangeStr) -> TimeRangeStr:
        return bar

    # Correct Strings
    want = [
        "2020-01-01",
        "2020-01-01/2020-02-05",
    ]
    for case in want:
        assert do_nothing_but_validate(case) == case

    # Wrong Strings
    not_want = [
        "2050-01-01",  # Too far in the future
        "1950-01-01",  # Too early
        "1969-01-01/2020-02-05",  # Lower is out of Bounds
        "2020-01-01/2050-02-05",  # Upper is out of Bounds
        "Hello",  # No timestamp at all
        "10.03.2002",  # Wrong datetime format
    ]
    for case in not_want:
        with pytest.raises(ValueError):
            do_nothing_but_validate(case)


def test_validate_bbox_returns_correct():
    # Mock function that should be validated
    @validate_call
    def do_nothing_but_validate(bar: BoundingBox) -> BoundingBox:
        return bar

    want = [
        (-180.0, -90.0, 180.0, 90.0),
        (-10.0, -10.0, 10.0, 10.0),
    ]
    for case in want:
        assert do_nothing_but_validate(case) == case

    not_want = [
        (10.0, -10.0, -10.0, 10.0),  # min_lon > max_lon
        (-10.0, 10.0, 10.0, -10.0),  # min_lat > max_lat
        (10.0, 20.0, -10.0, -20.0),  # min_lon > max_lon and min_lat > max_lat
        (10.0, -20.0, 10.0, 20.0),  # minlon == max_lon
    ]
    for case in not_want:
        with pytest.raises(ValueError):
            do_nothing_but_validate(case)
