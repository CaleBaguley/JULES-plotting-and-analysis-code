"""
Plot timeseries data for different daily atributes:
- Total
- Mean
- Median
- Maximum
- Minimum
- Standard deviation
"""

from src.plotting.plot_time_series import plot_time_series

def plot_daily_total(data_xarray, col_key,
                     smoothing = None, percentile = [16.,84.], x_range = None, c ='blue', label = None,
                     axs = None, title = None):
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
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").sum()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, percentile = percentile, x_range = x_range, c = c, label = label,
                     axs = axs, title = title)

    return None


def plot_daily_mean(data_xarray, col_key,
                    smoothing = None, percentile = [16.,84.], x_range = None, c ='blue', label = None,
                    axs = None, title = None):
    """
    Plot the daily mean for a given variable.

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
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").mean()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, percentile = percentile, x_range = x_range, c = c, label = label,
                     axs = axs, title = title)

    return None


def plot_daily_median(data_xarray, col_key,
                      smoothing = None, percentile = [16.,84.], x_range = None, c ='blue', label = None,
                      axs = None, title = None):
    """
    Plot the daily median for a given variable.

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
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").median()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, percentile = percentile, x_range = x_range, c = c, label = label,
                     axs = axs, title = title)

    return None


def plot_daily_max(data_xarray, col_key,
                   smoothing = None, percentile = [16.,84.], x_range = None, c ='blue', label = None,
                   axs = None, title = None):
    """
    Plot the daily maximum for a given variable.

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
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").max()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, percentile = percentile, x_range = x_range, c = c, label = label,
                     axs = axs, title = title)

    return None


def plot_daily_min(data_xarray, col_key,
                   smoothing = None, percentile = [16.,84.], x_range = None, c ='blue', label = None,
                   axs = None, title = None):
    """
    Plot the daily minimum for a given variable.

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
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").min()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, percentile = percentile, x_range = x_range, c = c, label = label,
                     axs = axs, title = title)

    return None


def plot_daily_std(data_xarray, col_key,
                   smoothing = None, percentile = [16.,84.], x_range = None, c ='blue', label = None,
                   axs = None, title = None):
    """
    Plot the daily standard deviation for a given variable.

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
    data_xarray_daily_total = data_xarray[[col_key]].resample(time="1D").std()

    # Plot the daily total GPP
    plot_time_series(data_xarray_daily_total, col_key,
                     smoothing = smoothing, percentile = percentile, x_range = x_range, c = c, label = label,
                     axs = axs, title = title)

    return None