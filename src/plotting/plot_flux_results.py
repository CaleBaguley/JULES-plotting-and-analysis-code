"""
Plot the flux data from a set of jules outputs.
"""

import xarray
import matplotlib.pyplot as plt
from src.plotting.plot_daily import plot_daily
from src.plotting.plot_col_at_daily_time import plot_col_at_daily_time
from src.load_jules_output_file import open_dataset

def plot_flux_data(data_xarrays, labels, colours, title = None, timestep_s = 3600.0):

    """
    Plot the flux data from a set of jules outputs.
    :param data_xarrays: The input xarray datasets. Xarray.Dataset or list of Xarray.Dataset
    :param labels: The labels to plot the data with. String or list of strings.
    :param colours: The colours to plot the data in. String or list of strings.
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

    if(type(colours) == str):
        colours = [colours]
    elif(type(colours) != list):
        raise ValueError("The input colours must be a list of strings.")

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
        plot_daily(data_xarrays[i], "gpp_gb", c = colours[i], label = labels[i], axs = axs[0], title = "")

    # set the y-axis label
    axs[0].set_ylabel("GPP (gC m-2 day-1)")

    # ---- Plot the latent heat data ----
    for i in range(len(data_xarrays)):
        plot_daily(data_xarrays[i], "latent_heat", c = colours[i], label = labels[i], axs = axs[1], title = "")

    # set the y-axis label
    axs[1].set_ylabel("Latent Heat (W m-2)")

    # ---- Plot the leaf water potential data ----
    for i in range(len(data_xarrays)):
        data_xarrays[i]["psi_leaf_mean"] = data_xarrays[i]["psi_leaf_pft"].mean(dim= "pft")
        print(data_xarrays[i]["psi_leaf_pft"])
        plot_col_at_daily_time(data_xarrays[i], "psi_leaf_mean", "12:00:00",
                               c = colours[i], label = labels[i], title = "", axis = axs[2])

    # set the y-axis label
    axs[2].set_ylabel("Leaf Water Potential (MPa)")




if __name__ == "__main__":
    # Load the JULES output files
    file_path = "../../../data/data_runs/stomatal_optimisation_runs/testing/FI_Lom-fsmc_comp.h.nc"
    file = open_dataset(file_path)

    # Plot the flux data
    plot_flux_data(file, "JULES Output", "blue", "JULES Output")
    plt.show()
