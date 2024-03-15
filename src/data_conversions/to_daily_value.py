"""
Functions to convert to daily values.
"""

def to_daily_total(data_xarray):
    """
    Convert the input xarray dataset into daily total values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily total values.
    """
    # Convert the input xarray dataset into daily total values
    data_xarray_out = data_xarray.resample(time="1D").sum()

    return data_xarray_out