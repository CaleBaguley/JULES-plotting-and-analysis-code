"""
Plot timeseries data for different daily atributes:
- Total
- Mean
- Median
- Maximum
- Minimum
- Standard deviation
"""

from JULES_Plotting_and_Analysis.src.plotting.plot_time_series import plot_time_series


def plot_daily_total(data_xarray, col_key,
                     smoothing = None, smoothing_type = 'mean', percentiles = None, x_range = None, c ='blue',
                     label = None, axs = None, title = None, linestyle = '-', linewidth = 1.):
    """
    Plot the daily total for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.
    linesyle (str): The linestyle of the plot.
    linewidth (float): The width of the line.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").sum()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axs, title = title, linestyle = linestyle,
                     linewidth = linewidth)

    return None


def plot_daily_mean(data_xarray, col_key,
                    smoothing = None, smoothing_type = 'mean', percentiles = None, x_range = None, c ='blue', label = None,
                    axs = None, title = None, linestyle = '-', linewidth = 1.):
    """
    Plot the daily mean for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.
    linesyle (str): The linestyle of the plot.
    linewidth (float): The width of the line.

    Returns:
    None
    """

    # Calculate the daily mean
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").mean()

    # Plot the daily mean
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axs, title = title, linestyle = linestyle,
                     linewidth = linewidth)

    return None


def plot_daily_median(data_xarray, col_key,
                      smoothing = None, smoothing_type = 'mean', percentiles = None, x_range = None, c ='blue', label = None,
                      axs = None, title = None, linestyle = '-'):
    """
    Plot the daily median for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").median()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axs, title = title, linestyle = linestyle)

    return None


def plot_daily_max(data_xarray, col_key,
                   smoothing = None, smoothing_type = 'mean', percentiles = None, x_range = None, c ='blue', label = None,
                   axs = None, title = None, linestyle = '-'):
    """
    Plot the daily maximum for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").max()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axs, title = title, linestyle = linestyle)

    return None


def plot_daily_min(data_xarray, col_key,
                   smoothing = None, smoothing_type = 'mean', percentiles = None, x_range = None, c ='blue', label = None,
                   axs = None, title = None, linestyle = '-'):
    """
    Plot the daily minimum for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").min()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axs, title = title, linestyle = linestyle)

    return None


def plot_daily_std(data_xarray, col_key,
                   smoothing = None, smoothing_type = 'mean', percentiles = None, x_range = None, c ='blue', label = None,
                   axs = None, title = None, linestyle = '-'):
    """
    Plot the daily standard deviation for a given variable.

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_key (str): The key for the GPP variable.
    smoothing (int): The number of days to smooth the data by.
    smoothing_type (str): The type of smoothing to apply to the data. 'mean' or 'median'.
    x_range (list): The range of dates to plot, in the form [date].
    c (str): The color to plot the data.
    label (str): The label for the date in the plot's legend.
    axis (plt.axis): The axis to plot the data on.
    title (str): The title of the plot.

    Returns:
    None
    """

    # Calculate the daily total GPP
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").std()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                     x_range = x_range, c = c, label = label, axs = axs, title = title, linestyle = linestyle)

    return None
