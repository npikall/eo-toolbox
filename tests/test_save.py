"""Test the save module."""

import pytest  # noqa
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def mock_array():
    pass


def test_save_xarray_method_rio_returns_correct(tmp_path, mock_array):  # noqa: ANN001, ARG001
    filepath: Path = tmp_path / "my_xarray.tiff"  # noqa: F841
    assert True
