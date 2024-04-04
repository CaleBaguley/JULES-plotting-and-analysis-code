"""
Plot daily value.
"""

import matplotlib.pyplot as plt
from datetime import datetime

def plot_daily(data_xarray, col_key, smoothing = 1, x_range = None, c ='blue', label = None, axs = None, title = None):
    """
    Plot the daily total for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray.resample(time="1D").sum()

    # Calculate median and 95% confidence intervals from the daily total GPP
    data_xarray_daily_total['median'] = (data_xarray_daily_total[col_key].rolling(time=smoothing, center = True)
                                         .construct('tmp').quantile(.50, dim='tmp'))
    data_xarray_daily_total['lower'] = (data_xarray_daily_total[col_key].rolling(time=smoothing, center = True)
                                        .construct('tmp').quantile(.96, dim='tmp'))
    data_xarray_daily_total['upper'] = (data_xarray_daily_total[col_key].rolling(time=smoothing, center = True)
                                        .construct('tmp').quantile(.04, dim='tmp'))

    # Create a new figure and set axs if there is no input axis
    if(axs == None):
        fig = plt.figure(figsize=(5, 5))
        axs = plt.gca()

    # Plot the daily GPP for all sites
    data_xarray_daily_total['median'].plot(color = c, label=label, ax = axs)

    # Fill the area between the input confidence intervals
    axs.fill_between(data_xarray_daily_total['time'].values,
                 data_xarray_daily_total['lower'].values[:, 0, 0],
                 data_xarray_daily_total['upper'].values[:, 0, 0],
                 alpha = 0.5, color = c)


    # Set the x-axis range
    if(x_range != None):
        min_x = datetime.combine(x_range[0], datetime.min.time())
        max_x = datetime.combine(x_range[1], datetime.min.time())
        plt.xlim(min_x, max_x)

    axs.set_xlabel('Date')
    axs.set_ylabel(col_key)

    if(title != None):
        axs.set_title(title)

    return None
