"""
This file contains functions to load a JULES output file and convert it into a pandas dataframe.
"""

from xarray import open_dataset


def load_jules_output_file_pandas(file_path):
    """
    Load a JULES output file and convert it into a pandas dataframe.

    Args:
    file_path (str): The file path to the JULES output file.

    Returns:
    df (pd.DataFrame): The JULES output file as a pandas dataframe.
    """
    # Load the JULES output file
    file = open_dataset(file_path)

    return file.to_dataframe()


def load_jules_output_file_xarray(file_path):
    """
    Load a JULES output file and convert it into an xarray dataset.

    Args:
    file_path (str): The file path to the JULES output file.

    Returns:
    file (xarray.Dataset): The JULES output file as an xarray dataset.
    """
    # Load the JULES output file
    file = open_dataset(file_path)

    return file

if __name__ == "__main__":
    # Load the JULES output file
    file_path = "~/Desktop/Flux_data/Plumber2_cat/Met/AR-SLu_2010-2010_FLUXNET2015_Met.nc"
    file = load_jules_output_file_xarray(file_path)

    # Print the file
    print(file)