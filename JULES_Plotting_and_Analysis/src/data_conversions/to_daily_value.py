"""
Functions to convert xarray data sets to daily values.
"""

from datetime import time

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

def to_daily_mean(data_xarray):
    """
    Convert the input xarray dataset into daily mean values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily mean values.
    """
    # Convert the input xarray dataset into daily mean values
    data_xarray_out = data_xarray.resample(time="1D").mean()

    return data_xarray_out

def to_daily_median(data_xarray):
    """
    Convert the input xarray dataset into daily median values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily median values.
    """
    # Convert the input xarray dataset into daily median values
    data_xarray_out = data_xarray.resample(time="1D").median()

    return data_xarray_out

def to_daily_max(data_xarray):
    """
    Convert the input xarray dataset into daily maximum values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily maximum values.
    """
    # Convert the input xarray dataset into daily maximum values
    data_xarray_out = data_xarray.resample(time="1D").max()

    return data_xarray_out

def to_daily_min(data_xarray):
    """
    Convert the input xarray dataset into daily minimum values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily minimum values.
    """
    # Convert the input xarray dataset into daily minimum values
    data_xarray_out = data_xarray.resample(time="1D").min()

    return data_xarray_out

def to_daily_std(data_xarray):
    """
    Convert the input xarray dataset into daily standard deviation values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily standard deviation values.
    """
    # Convert the input xarray dataset into daily standard deviation values
    data_xarray_out = data_xarray.resample(time="1D").std()

    return data_xarray_out

def to_daily_quantile(data_xarray, quantile = 0.5):
    """
    Convert the input xarray dataset into daily quantile values.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    quantile (float): The quantile to calculate.

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values converted to daily quantile values.
    """
    # Convert the input xarray dataset into daily quantile values
    data_xarray_out = data_xarray.resample(time="1D").quantile(quantile)

    return data_xarray_out

def get_daily_values_at_time(data_xarray, time_selected = "12:00:00"):
    """
    Get the daily values at a specific time.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    time (str): The time to get the daily values at. The time should be in the format "HH:MM:SS".

    Returns:
    data_xarray (xarray.Dataset): The input xarray dataset with the values at the specified time.
    """

    # Split the time into hours, minutes and seconds
    h, m, s = time_selected.split(':')

    # Convert the hours, minutes and seconds to integers
    h = int(h)
    m = int(m)
    s = int(s)

    # Create a time object
    time_selected = time(h, m, s)

    # Get the daily values at the specified time
    data_xarray_out = data_xarray.sel(time = time_selected)

    return data_xarray_out
