"""
    Functions to calculate different averages over plant functional types (PFTs).
"""

import xarray as xr

def mean_pfts(data_xarray, col_ids):
    """
    Calculate the mean value of the input data_xarray over the plant functional types (PFTs).

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_ids (list, str): The column IDs to calculate the mean over.

    Returns:
    data_xarray_out (xarray.Dataset): The input xarray dataset with the mean values calculated over the plant functional types (PFTs).
    """

    # Check that col_ids is a list
    if(type(col_ids) == str):
        col_ids = [col_ids]
    elif(type(col_ids) != list):
        raise ValueError("The input col_ids must be a string or list of column IDs.")

    # Generate the new column IDs for the mean values
    new_col_ids = [col_id + "_mean" for col_id in col_ids]

    for i in range(len(col_ids)):
        # Calculate the mean value of the input data_xarray over the plant functional types (PFTs)
        data_xarray[new_col_ids[i]] = data_xarray[col_ids[i]].mean(dim='pft')

    return data_xarray

def sum_pfts(data_xarray, col_ids):
    """
    Calculate the sum value of the input data_xarray over the plant functional types (PFTs).

    Args:
    data_xarray (xarray.Dataset): The input xarray dataset.
    col_ids (list, str): The column IDs to calculate the mean over.

    Returns:
    data_xarray_out (xarray.Dataset): The input xarray dataset with the summed values calculated over the plant functional types (PFTs).
    """

    # Check that col_ids is a list
    if(type(col_ids) == str):
        col_ids = [col_ids]
    elif(type(col_ids) != list):
        raise ValueError("The input col_ids must be a string or list of column IDs.")

    # Generate the new column IDs for the mean values
    new_col_ids = [col_id + "_sum" for col_id in col_ids]

    for i in range(len(col_ids)):
        # Calculate the sum value of the input data_xarray over the plant functional types (PFTs)
        data_xarray[new_col_ids[i]] = data_xarray[col_ids[i]].sum(dim='pft')

    return data_xarray