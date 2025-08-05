import eo_toolbox as etb
import numpy as np
import xarray as xr

def test_normalized_difference_returns_correct():
    step = 25
    arr1 = xr.DataArray(np.arange(0, 255, step), dims="x", coords={"x": np.arange(0, 255, step)})
    arr2 = xr.DataArray(np.arange(0, 255, -step), dims="x", coords={"x": np.arange(0, 255, step)})

    result = etb.calc.normalized_difference(arr1, arr2)
    expected = xr.DataArray(
        (arr1 - arr2) / (arr1 + arr2), dims="x", coords={"x": np.arange(0, 255, step)}
    )
    xr.testing.assert_equal(result, expected)

