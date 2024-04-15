"""
The function to plot the value of some input column at a given time of each day.
"""

from src.data_conversions.to_daily_value import get_daily_values_at_time
from src.plotting.plot_time_series import plot_time_series
import matplotlib.pyplot as plt
from datetime import datetime

def plot_col_at_daily_time(data_xarray,
                           variable_key,
                           time,
                           smoothing = None,
                           smoothing_type = 'mean',
                           percentiles = None,
                           x_range = None,
                           c ='blue',
                           label = None,
                           axis = None,
                           title = None,
                           linestyle = '-'):

    """
    Plot the value of some input column at a given time of each day.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    variable_key (str): The key for the variable to plot.
    time (str): The time to plot the column at, in the form "HH:MM:SS".
    smoothing (int): The number of days to smooth the data by.
                     If None then no smoothing is applied.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [datetime.date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.

    Returns:
    None
    """

    # Get the values at the specified time
    data_xarray_daily = get_daily_values_at_time(data_xarray, time)

    # Plot the daily values
    plot_time_series(data_xarray_daily, variable_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axis, title = title, linestyle = linestyle)

    return None
