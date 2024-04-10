"""
Plotting script to plot the results of the flux analysis for multiple sites.
"""

from src.plotting.plot_flux_results import plot_flux_data
from src.load_jules_output_file import open_dataset
from matplotlib import pyplot as plt

from os import listdir, makedirs
from os.path import exists

def plot_multi_site_flux_data(observation_folder, JULES_run_folders, JULES_labels, output_folder,
                              smoothing = 30, data_colours = None, observation_colour = None, percentiles = [16., 84.]):

    """
    Plot the flux data from a set of JULES outputs for multiple sites.
    :param observation_folder: Folder containing the observational data files. String.
    :param JULES_run_folders: Folders containing the JULES output files. List of strings.
    :param JULES_labels: Labels for the JULES output files. List of strings.
    :param data_colours: Colours to plot the JULES output files in. List of strings.
    :param observation_colour: Colour to plot the observational data in. String.
    :return:
    """

    # -- Identify which site files are available --
    # get a list of all available site files
    observation_files = listdir(observation_folder)
    JULES_run_files = []
    for folder in JULES_run_folders:
        JULES_run_files.append(listdir(folder))

    # remove non-nc files
    observation_files = [file for file in observation_files if file.endswith(".nc")]
    for file_list in JULES_run_files:
        file_list = [file for file in file_list if file.endswith(".nc")]

    # get a list available sites in each folder
    # Note the site names are the first part of the file name but the observation files
    # have a different naming convention.
    observation_sites = [file.split("_")[0] for file in observation_files]
    JULES_run_sites = []
    for file_list in JULES_run_files:
        JULES_run_sites.append([file.split("-")[0] for file in file_list])

    # change the - to a _ in the observation sites to match the JULES sites
    observation_sites = [site.replace("-", "_") for site in observation_sites]

    # collate the sites that are available in all the folders and their associated file addresses
    collated_sites_files = []
    for i in range(len(observation_sites)):
        tmp_site_files = []

        # Add the name of the site and the observation file address
        tmp_site_files.append(observation_sites[i])
        tmp_site_files.append(observation_folder + observation_files[i])

        # Add the JULES file addresses
        for j in range(len(JULES_run_sites)):
            if observation_sites[i] in JULES_run_sites[j]:
                # Add the JULES file address
                tmp_site_files.append(JULES_run_folders[j]
                                      + JULES_run_files[j][JULES_run_sites[j].index(observation_sites[i])])

        # Add the site to the collated list if it is available in all the folders
        if len(tmp_site_files) == len(JULES_run_folders) + 2:
            collated_sites_files.append(tmp_site_files)

    # -- Plot the flux data --
    # Loop through the sites and plot the flux data
    for site_files in collated_sites_files:
        # Load the data
        observation_data = open_dataset(site_files[1])
        JULES_data = []
        for i in range(2, len(site_files)):
            JULES_data.append(open_dataset(site_files[i]))

        # Plot the flux data
        plot_flux_data(JULES_data, observation_data, JULES_labels, title=site_files[0],
                       smoothing=smoothing, data_colours=data_colours, observation_colours=observation_colour)

        # -- Save the plot --
        # Check the output folder for this site exists
        if(not exists(output_folder + site_files[0] + "/")):
            makedirs(output_folder + site_files[0] + "/")

        plt.savefig(output_folder + site_files[0] + "/" + site_files[0] + "_flux_data.png")
        plt.close()

if __name__ == "__main__":
    # Define the input folders
    observation_folder = "../../../../../Desktop/Flux_data/Plumber2_catalogue_data/Flux/"
    JULES_run_folders = ["../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_PMax_run/",
                         "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_SOX_run/",
                         "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_fsmc_run/"]
    JULES_labels = ["Profit max", "SOX", "JULES"]

    output_folder = "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/figures/"

    # Plot the flux data
    plot_multi_site_flux_data(observation_folder, JULES_run_folders, JULES_labels, output_folder,
                              smoothing = 30, data_colours = ["blue", "red", "green"], observation_colour = "orange")
