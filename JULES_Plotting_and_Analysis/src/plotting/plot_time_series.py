"""
Plot timeseries.
"""

import matplotlib.pyplot as plt
from datetime import datetime


def plot_time_series(data_xarray, col_key,
                     smoothing=None,
                     smoothing_type='mean',
                     percentiles = None,
                     x_range=None,
                     c='blue',
                     label=None,
                     axs=None,
                     title=None,
                     linestyle='-',
                     linewidth=1):
    """
    Plot the daily total for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [min datetime, max datetime].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.
    linestyle (str): The linestyle of the plot.
    linewidth (int): The width of the line.

    Returns:
    None
    """

    # Create a copy of the input xarray dataset so that we don't modify the input data
    data_xarray_tmp = data_xarray[[col_key]].copy()

    # Smooth the data if a smoothing range is given
    if (smoothing != None):
        if(smoothing_type == 'mean'):
            # Calculate mean from the daily total GPP
            data_xarray_tmp['mean'] = (data_xarray_tmp[col_key].rolling(time=smoothing, center=True).mean())
        elif(smoothing_type == 'median'):
            # Calculate median and confidence intervals from the daily total GPP
            data_xarray_tmp['median'] = (data_xarray_tmp[col_key].rolling(time=smoothing, center=True)
                                         .construct('tmp').quantile(.50, dim='tmp'))

            if(percentiles != None):
                data_xarray_tmp['lower']  = (data_xarray_tmp[col_key].rolling(time=smoothing, center=True)
                                             .construct('tmp').quantile(1-percentiles[0]/100., dim='tmp'))
                data_xarray_tmp['upper']  = (data_xarray_tmp[col_key].rolling(time=smoothing, center=True)
                                             .construct('tmp').quantile(1-percentiles[1]/100., dim='tmp'))
        else:
            raise ValueError("The input smoothing_type must be either 'mean' or 'median'.")

    # Create a new figure and set axs if there is no input axis
    if (axs == None):
        fig = plt.figure(figsize=(5, 5))
        axs = plt.gca()

    if (smoothing == None):
        # Plot the daily GPP for all sites
        data_xarray_tmp[col_key].plot(color=c, label=label, ax=axs, linestyle=linestyle, linewidth=linewidth)
    else:
        if(smoothing_type == 'mean'):
            # Plot the daily GPP for all sites
            data_xarray_tmp['mean'].plot(color=c, label=label, ax=axs, linestyle=linestyle, linewidth=linewidth)
        elif(smoothing_type == 'median'):
            # Plot the daily GPP for all sites
            data_xarray_tmp['median'].plot(color=c, label=label, ax=axs, linestyle=linestyle, linewidth=linewidth)

            if(percentiles != None):
                # Fill the area between the input confidence intervals
                axs.fill_between(data_xarray_tmp['time'].values,
                                 data_xarray_tmp['lower'].values[:, 0, 0],
                                 data_xarray_tmp['upper'].values[:, 0, 0],
                                 alpha=0.3, color=c, linestyle = linestyle, linewidth=linewidth)

    # Set the x-axis range
    if (x_range != None):
        min_x = datetime.combine(x_range[0], datetime.min.time())
        max_x = datetime.combine(x_range[1], datetime.min.time())
        plt.xlim(min_x, max_x)

    axs.set_xlabel('Date')
    axs.set_ylabel(col_key)

    if (title != None):
        axs.set_title(title)

    return None