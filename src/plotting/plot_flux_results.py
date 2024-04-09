"""
Plot the flux data from a set of jules outputs.
"""

import xarray
import matplotlib.pyplot as plt
from src.plotting.plot_daily import plot_daily_total, plot_daily_mean
from src.plotting.plot_col_at_daily_time import plot_col_at_daily_time
from src.load_jules_output_file import open_dataset

def plot_flux_data(data_xarrays, observation_xarrays, labels, data_colours, observation_colours,
                   title = None, timestep_s = 3600.0, smoothing = None, x_range = None):

    """
    Plot the flux data from a set of jules outputs.
    :param data_xarrays: The input xarray datasets. Xarray.Dataset or list of Xarray.Dataset
    :param observation_xarrays: The observational data. Xarray.Dataset
    :param labels: The labels to plot the data with. String or list of strings.
    :param data_colours: The colours to plot the data in. String or list of strings.
    :param observation_colours: The colours to plot the observational data in. String.
    :param title: The title of the plot. String.
    :param timestep_s: The time step of the input data in seconds. Float.
    :return: None
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
    # Convert GPP data units from kgC m-2 s-1 to gC m-2 timestep-1
    for i in range(len(data_xarrays)):
        data_xarrays[i]["gpp_gb"] = data_xarrays[i]["gpp_gb"] * timestep_s * 1000

# --- Plot the data. ---
    # Create figure with multiple subplots.
    fig, axs = plt.subplots(3, 1, figsize=(8, 5), sharex=True)

    # Set the title of the plot
    if(title != None):
        fig.suptitle(title)

    # Remove vertical spacing between subplots
    plt.subplots_adjust(hspace=0.)

    # Label the x-axis
    axs[2].set_xlabel('Date')

    # ---- Plot the GPP data ----
    for i in range(len(data_xarrays)):
        plot_daily_total(data_xarrays[i], "gpp_gb", c = data_colours[i], label = labels[i], axs = axs[0],
                         title = "", smoothing = smoothing, x_range = x_range)

    # set the y-axis label
    axs[0].set_ylabel("GPP (gC m-2 day-1)")

    # ---- Plot the latent heat data ----
    for i in range(len(data_xarrays)):
        plot_daily_mean(data_xarrays[i], "latent_heat", c = data_colours[i], label = labels[i], axs = axs[1],
                        title = "", smoothing = smoothing, x_range = x_range)

    # set the y-axis label
    axs[1].set_ylabel("Latent Heat (W m-2)")


    #TODO: Rerun profit max and SOX code with psi_leaf_pft variable as output.
    # ---- Plot the leaf water potential data ----
    for i in range(len(data_xarrays)):
        data_xarrays[i]["psi_leaf_mean"] = data_xarrays[i]["psi_leaf_pft"].mean(dim= "pft")
        print(data_xarrays[i]["psi_leaf_pft"])
        plot_col_at_daily_time(data_xarrays[i], "psi_leaf_mean", "12:00:00",
                               c = data_colours[i], label = labels[i], title = "", axis = axs[2], smoothing = smoothing)


    # set the y-axis label
    axs[2].set_ylabel("Leaf Water Potential (MPa)")




if __name__ == "__main__":
    # Load the JULES output files
    data_file_paths = ["../../../data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_PMax_run/AT_Neu-JULES_vn7.4-presc0.Stom_opt.nc"]

    data_files = []
    for path in data_file_paths:
        data_files.append(open_dataset(path))

    # Load the observational data
    observation_file_path = "../../../data/PLUMBER2/met/AT-Neu_2002-2012_FLUXNET2015_Met.nc"

    observation_file = open_dataset(observation_file_path)

    # Plot the flux data
    plot_flux_data(data_files[0], observation_file, "JULES Output", "blue", "orange", "JULES Output", smoothing = 30)
    plt.show()
