"""
Plotting script to plot the results of the flux analysis for multiple sites.
"""

from src.plotting.plot_flux_results import plot_flux_data

from os import listdir

def plot_multi_site_flux_data(observation_folder, JULES_run_folders, JULES_labels):

    """
    Plot the flux data from a set of JULES outputs for multiple sites.
    :param observation_folder: Folder containing the observational data files. String.
    :param JULES_run_folders: Folders containing the JULES output files. List of strings.
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



if __name__ == "__main__":
    # Define the input folders
    observation_folder = "../../../../../Desktop/Flux_data/Plumber2_catalogue_data/Flux/"
    JULES_run_folders = ["../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_PMax_run/",
                         "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_SOX_run/"]
    JULES_labels = ["Profit max", "SOX"]

    # Plot the flux data
    plot_multi_site_flux_data(observation_folder, JULES_run_folders, JULES_labels)