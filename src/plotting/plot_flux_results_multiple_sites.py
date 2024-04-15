"""
Plotting script to plot the results of the flux analysis for multiple sites.
"""

from src.plotting.plot_flux_results import plot_flux_data
from src.load_jules_output_file import open_dataset

from matplotlib import pyplot as plt
from os import listdir, makedirs
from os.path import exists
from datetime import date

def plot_multi_site_flux_data(observation_folder, JULES_run_folders, JULES_labels, output_folder, stress_indicator,
                              smoothing = 30, smoothing_type = 'mean', data_colours = None,
                              observation_colour = None, percentiles = None):

    """
    Plot the flux data from a set of JULES outputs for multiple sites.
    :param observation_folder: Folder containing the observational data files. String.
    :param JULES_run_folders: Folders containing the JULES output files. List of strings.
    :param JULES_labels: Labels for the JULES output files. List of strings.
    :param output_folder: Folder to save the output plots in. String.
    :param stress_indicator: Type of stress indicator to plot for each JULES run.
                             'wp' water potential or 'beta' JULES beta. List of strings.
    :param smoothing: Number of days to smooth the data by. Integer.
    :param smoothing_type: Type of smoothing to apply to the data. 'mean' or 'median'. String.
    :param data_colours: Colours to plot the JULES output files in. List of strings.
    :param observation_colour: Colour to plot the observational data in. String.
    :param percentiles: Percentiles to plot the data with. List of floats.
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
    itter = 1
    for site_files in collated_sites_files:

        print("Plotting flux data for site: " + site_files[0] + " (" + str(itter) + "/" + str(len(collated_sites_files)) + ")")

        # Load the data
        observation_data = open_dataset(site_files[1])
        JULES_data = []
        for i in range(2, len(site_files)):
            JULES_data.append(open_dataset(site_files[i]))

        # -- identify overlapping time periods --
        # Find the start and end dates for the data
        start_dates = [data.time.values[0] for data in JULES_data]
        start_dates.append(observation_data.time.values[0])

        end_dates = [data.time.values[-1] for data in JULES_data]
        end_dates.append(observation_data.time.values[-1])

        # Find the latest start date and the earliest end date
        start_date = max(start_dates)
        end_date = min(end_dates)

        # Convert the start and end dates to datetime objects
        start_date = date.fromisoformat(str(start_date)[:10])
        end_date = date.fromisoformat(str(end_date)[:10])

        # Round the start_date down to the nearest year and the end_date up to the nearest year
        start_date = date(start_date.year, 1, 1)
        end_date = date(end_date.year + 1, 1, 1)

        # Calculate the number of years between the start and end dates
        num_years = end_date.year - start_date.year

        # Plot the flux data
        plot_flux_data(JULES_data, observation_data, JULES_labels, title=site_files[0],
                       smoothing = smoothing, smoothing_type = smoothing_type, data_colours = data_colours,
                       observation_colours = observation_colour, stress_indicator = stress_indicator,
                       x_range = [start_date, end_date], percentiles = percentiles)

        # -- Save the plot --
        # Check the output folder for this site exists. If not create it.
        if(not exists(output_folder + site_files[0] + "/")):
            makedirs(output_folder + site_files[0] + "/")

        # Save the entire time series plot
        plt.savefig(output_folder + site_files[0] + "/" + site_files[0] + "_flux_data.png")

        # If there are more than 3 years of data plot each set of 3 years separately
        if(num_years > 3):
            for i in range(0, num_years-2):
                # Calculate the start and end dates for this plot
                start_date_plot = date(start_date.year + i, 1, 1)
                end_date_plot = date(start_date.year + i + 3, 1, 1)

                # change the x_range to the new start and end dates
                plt.xlim(start_date_plot, end_date_plot)

                # Save the plot
                file_name = site_files[0] + "_flux_data_" + str(start_date_plot.year) + "_" + str(end_date_plot.year) + ".png"
                plt.savefig(output_folder + site_files[0] + "/" + file_name)

        plt.close()

        itter += 1

if __name__ == "__main__":
    # Define the input folders
    observation_folder = "../../../../../Desktop/Flux_data/Plumber2_catalogue_data/Flux/"
    JULES_run_folders = ["../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_PMax_run/",
                         "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_SOX_run/",
                         "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/JULES_fsmc_run/"]
    JULES_labels = ["Profit max", "SOX", "JULES"]
    stress_indicator = ["wp", "wp", "beta"]

    output_folder = "../../../../../Desktop/JULES/data/data_runs/stomatal_optimisation_runs/plumber2_runs/figures/"

    # Plot the flux data
    plot_multi_site_flux_data(observation_folder, JULES_run_folders, JULES_labels, output_folder, stress_indicator,
                              smoothing = 5, smoothing_type='median', data_colours = ["blue", "red", "green"],
                              observation_colour = "orange")
