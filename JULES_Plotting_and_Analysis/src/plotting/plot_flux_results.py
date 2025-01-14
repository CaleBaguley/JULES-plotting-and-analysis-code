"""
Plot the flux data from a set of jules outputs.
"""

import xarray
import matplotlib.pyplot as plt
from JULES_Plotting_and_Analysis.src.plotting.plot_daily import plot_daily_total, plot_daily_mean
from JULES_Plotting_and_Analysis.src.plotting.plot_col_at_daily_time import plot_col_at_daily_time
from JULES_Plotting_and_Analysis.src.load_jules_output_file import open_dataset


def plot_flux_data(data_xarrays,
                   observation_xarray,
                   labels,
                   data_colours,
                   observation_colours,
                   stress_indicator,
                   title = None,
                   fig_size = (10, 8),
                   smoothing = None,
                   smoothing_type = 'mean',
                   percentiles = None,
                   x_range = None,
                   gpp_key = "gpp_gb",
                   latent_heat_key = "latent_heat",
                   psi_root_key = "psi_root_zone_pft",
                   psi_leaf_key = "psi_leaf_pft",
                   beta_key = "fsmc_gb",
                   observation_gpp_key = "GPP",
                   observation_latent_heat_key = "Qle",
                   additional_sub_plots = 0,
                   legend = True):

    """
    Plot the flux data from a set of jules outputs.
    :param data_xarrays: The input xarray datasets. Xarray.Dataset or list of Xarray.Dataset
    :param observation_xarray: The observational data. Xarray.Dataset
    :param labels: The labels to plot the data with. String or list of strings.
    :param data_colours: The colours to plot the data in. String or list of strings.
    :param observation_colours: The colours to plot the observational data in. String.
    :param stress_indicator: The stress indicator to plot. 'wp' water potential or 'beta' JULES fsmc value.
                             List of String.
    :param title: The title of the plot. String.
    :param fig_size: The size of the figure. Tuple of integers.
    :param smoothing: The number of days to smooth the data by. Integer.
    :param smoothing_type: The type of smoothing to apply to the data. 'mean' or 'median'. String.
    :param percentiles: The percentiles to plot the data with. List of floats.
    :param x_range: The range of dates to plot, in the form [date]. List of datetime objects.
    :param gpp_key: The key for the GPP variable. String.
    :param latent_heat_key: The key for the latent heat variable. String.
    :param psi_root_key: The key for the root zone water potential variable. String.
    :param psi_leaf_key: The key for the leaf water potential variable. String.
    :param beta_key: The key for the fsmc value variable. String.
    :param observation_gpp_key: The key for the observational GPP variable. String.
    :param observation_latent_heat_key: The key for the observational latent heat variable. String.
    :param additional_sub_plots: The number of additional plots to add to the bottom of the figure. Integer.
    :return: fig, axs
    """

# --- Check input arrays. ---
    # Check the input data_xarrays is a list of xarray.Dataset
    if(type(data_xarrays) == xarray.Dataset):
        data_xarrays = [data_xarrays]
    elif(type(data_xarrays) != list):
        raise ValueError("The input data_xarrays must be either a list of xarray.Dataset or a single xarray.Dataset.")

    if(type(labels) == str):
        labels = [labels]
    elif(type(labels) != list):
        raise ValueError("The input labels must be a list of strings.")

    if(type(data_colours) == str):
        data_colours = [data_colours]
    elif(type(data_colours) != list):
        raise ValueError("The input data_colours must be a string or list of strings.")

    # --- Data processing. ---

    # First we need to convert the units of the GPP data from both the JULES output files and the observation file.

    # Convert GPP data units from kgC m-2 s-1 to gC m-2 timestep-1
    # kgC -> gC: * 1000
    # s-1 -> timestep-1: * timestep
    for i in range(len(data_xarrays)):
        timestep = data_xarrays[i]["time"].values[1] - data_xarrays[i]["time"].values[0]
        timestep = timestep.astype("timedelta64[s]").astype(int)
        data_xarrays[i][gpp_key] = data_xarrays[i][gpp_key] * 1000 * timestep

    # Convert GPP data units from umol m-2 s-1 to gC m-2 timestep-1
    # umol -> mol: * 1e-6
    # molCO2 -> molC: * 44/12.01
    # molC -> gC: * 12.01
    # s-1 -> timestep-1: * timestep
    if(observation_gpp_key != None):
        timestep = observation_xarray["time"].values[1] - observation_xarray["time"].values[0]
        timestep = timestep.astype("timedelta64[s]").astype(int)
        observation_xarray[observation_gpp_key] = observation_xarray[observation_gpp_key] * 1e-6 * 12.01 * timestep

    # --- Figure setup ---
    # Create figure with multiple subplots.
    fig, axs = plt.subplots(3 + additional_sub_plots, 1, figsize=fig_size, sharex=True)

    # Change padding around figure
    plt.margins(0.05)

    # Set the title of the plot
    if(title != None):
        fig.suptitle(title, y = 0.93, fontsize = "xx-large", fontweight = "bold")

    # Remove vertical spacing between subplots
    plt.subplots_adjust(hspace=0.)

    # Label the x-axis
    axs[2].set_xlabel('Date')

    # ---- Plot the GPP data ----
    for i in range(len(data_xarrays)):
        plot_daily_total(data_xarrays[i], gpp_key, c = data_colours[i], label = labels[i], axs = axs[0],
                         title = "", smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                         x_range = x_range)

    # Plot the observational data
    if(observation_gpp_key != None):
        plot_daily_total(observation_xarray, observation_gpp_key, c=observation_colours, label="Observation",
                         axs=axs[0], title="", smoothing=smoothing, smoothing_type = smoothing_type,
                         percentiles = percentiles, x_range=x_range)

    # set the y-axis label
    axs[0].set_ylabel("GPP (gC m-2 day-1)")

    # ---- Plot the latent heat data ----
    for i in range(len(data_xarrays)):
        plot_daily_mean(data_xarrays[i], latent_heat_key, c = data_colours[i], label = labels[i], axs = axs[1],
                        title = "", smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                        x_range = x_range)

    plot_daily_mean(observation_xarray, observation_latent_heat_key, c=observation_colours, label="Observation",
                    axs=axs[1], title="", smoothing=smoothing, smoothing_type = smoothing_type,
                    percentiles = percentiles, x_range=x_range)

    # set the y-axis label
    axs[1].set_ylabel("Latent Heat (W m-2)")

    # ---- Plot the stress indicator ----
    for i in range(len(data_xarrays)):
        if(stress_indicator[i] == "wp"):
            # Calculate the mean leaf and root zone water potential over plant functional types
            data_xarrays[i]["psi_root_zone_mean"] = data_xarrays[i][psi_root_key].mean(dim= "pft")
            data_xarrays[i]["psi_leaf_mean"] = data_xarrays[i][psi_leaf_key].mean(dim= "pft")

            plot_col_at_daily_time(data_xarrays[i], "psi_leaf_mean", "06:00:00",
                                   c=data_colours[i], label=labels[i], title="", axis=axs[2], smoothing=smoothing,
                                   smoothing_type = smoothing_type, percentiles = percentiles, linestyle = ":")
            plot_col_at_daily_time(data_xarrays[i], "psi_leaf_mean", "12:00:00",
                                   c = data_colours[i], label = labels[i], title = "", axis = axs[2],
                                   smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                                   linestyle = "-")

        elif(stress_indicator[i] == "beta"):
            # Calculate the mean leaf and root zone fsmc value (beta) over plant functional types
            plot_col_at_daily_time(data_xarrays[i], beta_key, "12:00:00",
                                   c=data_colours[i], label=labels[i], title="", axis=axs[2], smoothing=smoothing,
                                   smoothing_type=smoothing_type, percentiles=percentiles, linestyle="--")
        elif(stress_indicator[i] == "beta&wp"):
            # Calculate the mean leaf and root zone fsmc value (beta) over plant functional types
            plot_col_at_daily_time(data_xarrays[i], beta_key, "12:00:00",
                                   c=data_colours[i], label=labels[i], title="", axis=axs[2], smoothing=smoothing,
                                   smoothing_type=smoothing_type, percentiles=percentiles, linestyle="--")

            # Calculate the mean leaf and root zone water potential over plant functional types
            data_xarrays[i]["psi_root_zone_mean"] = data_xarrays[i][psi_root_key].mean(dim= "pft")
            data_xarrays[i]["psi_leaf_mean"] = data_xarrays[i][psi_leaf_key].mean(dim= "pft")

            plot_col_at_daily_time(data_xarrays[i], "psi_root_zone_mean", "06:00:00",
                                   c=data_colours[i], label=labels[i], title="", axis=axs[2], smoothing=smoothing,
                                   smoothing_type = smoothing_type, percentiles = percentiles, linestyle = ":")
            plot_col_at_daily_time(data_xarrays[i], "psi_leaf_mean", "12:00:00",
                                   c = data_colours[i], label = labels[i], title = "", axis = axs[2],
                                   smoothing = smoothing, smoothing_type = smoothing_type, percentiles = percentiles,
                                   linestyle = "-")
        else:
            raise ValueError("The input stress_indicator must be either 'wp', 'beta' or 'beta&wp'.")

    # set the y-axis label
    axs[2].set_ylabel("Leaf Water Potential (MPa)")

    if(legend):
        axs[1].legend()

    return fig, axs


if __name__ == "__main__":

    from datetime import datetime

    # Load the JULES output files
    data_file_paths = ["../../../data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_PMax_run/AT_Neu-JULES_vn7.4-presc0.Stom_opt.nc",
                       "../../../data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_SOX_run/AT_Neu-JULES_vn7.4-presc0.Stom_opt.nc"]

    data_files = []
    for path in data_file_paths:
        data_files.append(open_dataset(path))

    # Load the observational data
    observation_file_path = "~/Desktop/Flux_data/Plumber2_catalogue_data/Flux/AT-Neu_2002-2012_FLUXNET2015_FLUX.nc"

    observation_file = open_dataset(observation_file_path)

    # Plot the flux data
    plot_flux_data(data_files,
                   observation_file,
                   labels = ["Profit Max","SOX"],
                   data_colours = ["blue","red"],
                   observation_colours = "orange",
                   stress_indicator = ["wp", "wp"],
                   title = "AT-Neu",
                   smoothing = 5,
                   smoothing_type = 'mean',
                   x_range = [datetime(2007,1,1), datetime(2013,1,1)])
    plt.show()
