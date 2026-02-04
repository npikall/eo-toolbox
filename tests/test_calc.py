import numpy as np
import xarray as xr

import eo_toolbox as etb


def test_normalized_difference_returns_correct():
    step = 25  # DO NOT CHANGE or the test will fail
    mock_data = np.arange(0, 255, step)
    length = len(mock_data)

    arr1 = xr.DataArray(
        mock_data,
        dims="x",
        coords={"x": np.arange(0, length)},
    )
    arr2 = xr.DataArray(
        mock_data[::-1],  # Reverse data
        dims="x",
        coords={"x": np.arange(0, length)},
    )

    result = etb.calc.normalized_difference(arr1, arr2)
    expected = xr.DataArray(
        [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1],
        dims="x",
        coords={"x": np.arange(0, length)},
    )
    assert type(result) is xr.DataArray
    xr.testing.assert_equal(result, expected)
