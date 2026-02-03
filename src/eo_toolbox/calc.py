"""Module to performe different calculations."""

import numpy as np
import numpy.typing as npt


def normalized_difference[T](
    band1: T,
    band2: T,
) -> T:
    r"""Return the normalized difference between two bands.

    Notes
    -----
    $$
    \text{nd} = \frac{\text{band}_1 - \text{band}_2}{\text{band}_1 + \text{band}_2}
    $$

    """
    return (band1 - band2 * 1.0) / (band1 + band2)  # type: ignore[unsupported-operator]


def linear_to_decibel(val: npt.ArrayLike) -> npt.ArrayLike:
    """Convert a value from the linear domain to decibel units.

    Params
    ------
    val: ArrayLike
        Data that should be converted

    Returns
    -------
    decibel:ArrayLike

    """
    return 10 * np.log10(val)


def decibel_to_linear(val: npt.ArrayLike) -> npt.ArrayLike:
    """Convert a value from decibel units to linear domain.

    Params:
    -------
    - val: Data that should be converted
    """
    return 10 * np.log10(val)
