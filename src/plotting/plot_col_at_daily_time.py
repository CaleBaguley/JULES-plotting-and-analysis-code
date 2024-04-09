"""
The function to plot the value of some input column at a given time of each day.
"""

from src.data_conversions.to_daily_value import get_daily_values_at_time
import matplotlib.pyplot as plt
from datetime import datetime

def plot_col_at_daily_time(data_xarray,
                           variable_key,
                           time,
                           smoothing = None,
                           x_range = None,
                           c ='blue',
                           label = None,
                           axis = None,
                           title = None):

    """
    Plot the value of some input column at a given time of each day.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    variable_key (str): The key for the variable to plot.
    time (str): The time to plot the column at, in the form "HH:MM:SS".
    smoothing (int): The number of days to smooth the data by.
                     If None then no smoothing is applied.
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

    # If a smoothing range is given then smooth the data
    if(smoothing != None):
        # Calculate median and 95% confidence intervals from the daily total GPP
        data_xarray_daily['median'] = (data_xarray_daily[variable_key].rolling(time=smoothing, center=True)
                                     .construct('tmp').quantile(.50, dim='tmp'))
        data_xarray_daily['lower'] = (data_xarray_daily[variable_key].rolling(time=smoothing, center=True)
                                    .construct('tmp').quantile(.96, dim='tmp'))
        data_xarray_daily['upper'] = (data_xarray_daily[variable_key].rolling(time=smoothing, center=True)
                                    .construct('tmp').quantile(.04, dim='tmp'))

    # Create a new figure and set axs if there is no input axis
    if(axis == None):
        fig = plt.figure(figsize=(5, 5))
        axis = plt.gca()

    # Plot the daily values
    # If smoothing is given plot the smoothed data
    if(smoothing != None):
        data_xarray_daily['median'].plot(color=c, label=label, ax=axis)

        # Fill the area between the input confidence intervals
        axis.fill_between(data_xarray_daily['time'].values,
                          data_xarray_daily['lower'].values[:, 0, 0],
                          data_xarray_daily['upper'].values[:, 0, 0],
                          alpha=0.5, color=c)
    # If no smoothing is given plot the raw data
    else:
        data_xarray_daily[variable_key].plot(color = c, label=label, ax = axis)


    # Set the x-axis range
    if(x_range != None):
        min_x = datetime.combine(x_range[0], datetime.min.time())
        max_x = datetime.combine(x_range[1], datetime.min.time())
        plt.xlim(min_x, max_x)

    axis.set_xlabel('Date')
    axis.set_ylabel(variable_key)

    if(title != None):
        axis.set_title(title)

    return None
