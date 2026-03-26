"""Calculate common Earth Observation Indices."""

from typing import TypedDict, Unpack

import xarray as xr

from eo_toolbox._protocol import SupportsMathOps
from eo_toolbox.calc import normalized_difference


def nd_vegetation_index[T: SupportsMathOps](red: T, nir: T) -> T:
    """Compute the NDVI from the Red and the Near-Infrared Bands.

    NDVI = Normalized Difference Vegetation Index

    Formula: ndvi = (nir - red) / (nir + red)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return normalized_difference(band1=nir, band2=red)


def green_nd_vegetation_index[T: SupportsMathOps](green: T, nir: T) -> T:
    """Compute the GNDVI from the Green and the Near-Infrared Bands.

    GNDVI = Green Normalized Difference Vegetation Index

    Formula: gndvi = (nir - green) / (nir + green)
    (Not to be confused with NDWI)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return normalized_difference(band1=nir, band2=green)


def nd_moisture_index[T: SupportsMathOps](nir: T, swir: T) -> T:
    """Compute the NDMI from the Near-Infrared and the Shortwave-IR Bands.

    NDMI = Normalized Difference Moisture Index

    Formula: ndvi = (nir - swir) / (nir + swir)

    Interpretation:
    - (-1 - -0.8) Bare soil,
    - (-0.8 - -0.6) Almost absent canopy cover,
    - (-0.6 - -0.4) Very low canopy cover,
    - (-0.4 - -0.2) Low canopy cover, dry or very low canopy cover, wet,
    - (-0.2 - 0) Mid-low canopy cover, high water stress or low canopy cover, low water stress,
    - (0 - 0.2) Average canopy cover, high water stress or mid-low canopy cover, low water stress,
    - (0.2 - 0.4) Mid-high canopy cover, high water stress or average canopy cover, low water stress,
    - (0.4 - 0.6) High canopy cover, no water stress,
    - (0.6 - 0.8) Very high canopy cover, no water stress,
    - (0.8 - 1) Total canopy cover, no water stress/waterlogging

    Resources:
    ---------
    https://eos.com/make-an-analysis/ndmi/
    """  # noqa: E501
    return normalized_difference(band1=nir, band2=swir)


def nd_water_index[T: SupportsMathOps](green: T, nir: T) -> T:
    """Compute the NDWI from the Green and NIR Bands.

    NDWI = Normalized Difference Water Index

    Formula: ndwi = (green - nir) / (green + nir)
    (Not to be confused with GNDVI)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return normalized_difference(band1=green, band2=nir)


def soil_adjusted_vegetation_index[T: SupportsMathOps](
    nir: T,
    red: T,
    adjustment_factor: float = 0.5,
) -> T:
    """Compute the SAVI from NIR and Red bands.

    SAVI = Soil Adjusted Vegetation Index

    Formula: savi = ((nir - red) / (nir + red + l)) * (1 + l)
        * l = adjustment_factor

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return ((nir - red) / (nir + red + adjustment_factor)) * (adjustment_factor + 1)


def optimized_soil_adjusted_vegetation_index[T: SupportsMathOps](
    nir: T,
    red: T,
) -> T:
    """Compute the OSAVI from the Red and NIR Bands.

    OSAVI = Optimized Soil Adjusted Vegetation Index

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return (nir - red) / (nir + red + 0.16)


def atmospherically_resistant_vegetation_index[T: SupportsMathOps](
    nir: T,
    red: T,
    blue: T,
) -> T:
    """Compute the ARVI from the Red, Blue and NIR Bands.

    ARVI = Atmospherically Resistant Vegetation Index

    Formula: arvi = (nir - (2 * red) + blue) / (nir + (2 * red) + blue)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return (nir - (red * 2) + blue) / (nir + (red * 2) + blue)


class EVIParams(TypedDict):
    """Optional Kwargs for the EVI function."""

    c1: float
    c2: float
    l_factor: float


def enhanced_vegetation_index[T: SupportsMathOps](
    nir: T,
    red: T,
    blue: T,
    **kwargs: Unpack[EVIParams],
) -> T:
    """Compute the EVI from Red, NIR and Blue Bands.

    EVI = Enhanced Vegetation Index

    Formula: evi = 2.5 * ((nir - red) / (nir + (c1 * red) - (c2 * blue) + l))

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    c1 = kwargs.get("c1", 6)
    c2 = kwargs.get("c2", 7.5)
    l_factor = kwargs.get("l_factor", 1)
    return ((nir - red) / (nir + (red * c1) - (blue * c2) + l_factor)) * 2.5


def visible_atmospherically_resistant_index[T: SupportsMathOps](
    green: T,
    red: T,
    blue: T,
) -> T:
    """Compute the VARI from the Green, Red and Blue Bands.

    VARI = Visible Atmospherically Resistant Index

    Formula: vari = (green - red) / (green + red - blue)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return (green - red) / (green + red - blue)


def normalized_burn_ratio[T: SupportsMathOps](nir: T, swir: T) -> T:
    """Compute the NBR from the Near-Infrared and Shortwave-IR Bands.

    NBR = Normalized Burn Ratio

    Formula: nbr = (nir - swir) / (nir + swir)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return normalized_difference(band1=nir, band2=swir)


def structure_insensitive_pigment_index[T: SupportsMathOps](
    nir: T, red: T, blue: T
) -> T:
    """Compute the SIPI from the NIR, Red and Blue Bands.

    SIPI = Structure Insensitive Pigment (Vegetation) Index

    Formula: sipi = (nir - blue) / (nir - red)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return (nir - blue) / (nir - red)


def green_chlorophyll_index[T: SupportsMathOps](green: T, nir: T) -> T:
    """Compute the GCI from the Green and NIR Bands.

    GCI = Green Chlorophyll Index

    Formula: gci = (nir / green) - 1

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return (nir / green) - 1


def nd_snow_index[T: SupportsMathOps](green: T, swir: T) -> T:
    """Compute the NDSI from the Green and Shortwave-IR Bands.

    NDSI = Normalized Difference Snow Index

    Formula: ndsi = (green - swir) / (green + swir)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return normalized_difference(band1=green, band2=swir)


def istack(
    ndvi: xr.DataArray,
    ndwi: xr.DataArray,
    ndsi: xr.DataArray,
) -> xr.DataArray:
    """Compute the IStack from NDVI, NDWI and NDSI.

    IStack = Index Stack

    Formula: istack = (ndvi + ndwi + ndsi) / 3

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return xr.concat([ndvi, ndwi, ndsi], dim="band")


def red_edge_chlorophyll_index[T: SupportsMathOps](red: T, nir: T) -> T:
    """Compute the RECL from the Red and NIR Bands.

    RECL = Red Edge Chlorophyll Index

    Formula: recl = (nir / red) - 1

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return (nir / red) - 1


def nd_red_edge_index[T: SupportsMathOps](nir: T, red_edge: T) -> T:
    """Compute the NDRE from the NIR and Red Edge Bands.

    NDRE = Normalized Difference Red Edge Index

    Formula: ndre = (nir - red_edge) / (nir + red_edge)

    Resources:
    ---------
    https://eos.com/blog/vegetation-indices/
    """
    return normalized_difference(band1=nir, band2=red_edge)


def moisture_stress_index[T: SupportsMathOps](swir: T, nir: T) -> T:
    """Compute the MSI from the Shortwave-IR and NIR Bands.

    MSI = Moisture Stress Index

    Formula: msi = swir / nir
    """
    return swir / nir
