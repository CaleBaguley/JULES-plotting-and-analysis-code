"""
Plot daily value.
"""

import matplotlib.pyplot as plt
from datetime import datetime

def plot_daily(data_xarray, col_key, smoothing = 1, x_range = None, c ='blue', label = None):
    """
    Plot the daily GPP for a site.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray.resample(time="1D").sum()

    # Calculate median and 95% confidence intervals from the daily total GPP
    data_xarray_daily_total['median'] = data_xarray_daily_total[col_key].rolling(time=smoothing, center = True).construct('tmp').quantile(.50, dim='tmp')
    data_xarray_daily_total['lower'] = data_xarray_daily_total[col_key].rolling(time=smoothing, center = True).construct('tmp').quantile(.96, dim='tmp')
    data_xarray_daily_total['upper'] = data_xarray_daily_total[col_key].rolling(time=smoothing, center = True).construct('tmp').quantile(.04, dim='tmp')

    # Plot the daily GPP for all sites
    data_xarray_daily_total['median'].plot(color = c, label=label)
    plt.fill_between(data_xarray_daily_total['time'].values,
                     data_xarray_daily_total['lower'].values[:, 0, 0],
                     data_xarray_daily_total['upper'].values[:, 0, 0],
                     alpha = 0.5,
                     color = c)

    # Set the x-axis range
    if(x_range != None):
        min_x = datetime.combine(x_range[0], datetime.min.time())
        max_x = datetime.combine(x_range[1], datetime.min.time())
        plt.xlim(min_x, max_x)

    plt.xlabel('Date')
    plt.ylabel(col_key)

    return None
