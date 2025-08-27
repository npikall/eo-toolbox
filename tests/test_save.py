"""Test the save module."""

import pytest  # noqa
import xarray as xr
import numpy as np
import pandas as pd
from pathlib import Path
from eo_toolbox.save import save_xarray, SaveMethod


@pytest.fixture
def mock_array():
    # TODO: write a mock for an xarray object
    pass


def test_save_xarray_method_rio_returns_correct(tmp_path, mock_array):
    filepath: Path = tmp_path / "my_xarray.tiff"
    # TODO: write the test, assert saved file exists.
    assert True
