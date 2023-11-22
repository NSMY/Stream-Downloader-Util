# Swaps new Data for the old data in the json file while keeping X key/s.

import json

from utility_dir.util_functions import get_index_last_vod


def compare_dicts_excluding(dict1, dict2, exclude_keys):
    '''Compares 2 dicts keys, But Excludes Specific Key/s
    in comparison.

    Args:
        dict1 (dict):
        dict2 (dict):
        exclude_keys (str | lst[str]): Key Name/s

    Returns:
        bool: T (same)/F (different)
    '''
    dict1_copy = {k: v for k, v in dict1.items() if k not in exclude_keys}
    dict2_copy = {k: v for k, v in dict2.items() if k not in exclude_keys}

    return dict1_copy == dict2_copy


def get_conflicting_indexes(file_list1_data: list, list2_data, start_point_index, exclude_Key_s):
    """
    This function compares two lists of dictionaries and identifies the indexes
    of conflicting elements, excluding the keys in 'exclude_Key_s'.
    If 'list2_data' is a dictionary, it will be normalized using
    'main_call.Vod.create_vods_from_edges'.

    Parameters:
    file_list1_data (list): The original list of dictionaries.
    list2_data (list or dict): The data to be compared with 'file_list1_data'. If it's a dict, it will be normalized to a List[dict].
    start_point_index (int): The starting index from where 'list2_data' should be compared with 'file_list1_data'.
    exclude_Key_s (str or list): The key(s) to be excluded from the comparison.

    Returns:
    tuple: A tuple containing a list of tuples with the indexes of the
    conflicting elements in 'file_list1_data' and 'list2_data',
    and the (new Data) 'list2_data'.
    """
    if isinstance(list2_data, dict):
        # Normalize Data.
        from new_mass_gql import gql_main_call as main_call
        list2_data = main_call.Vod.create_vods_from_edges(list2_data["data"]["user"]["videos"]["edges"])
    strt = []
    for index, (list1, list2) in enumerate(zip(file_list1_data, list2_data[start_point_index:])):
        check = (index, compare_dicts_excluding(list1, list2, exclude_Key_s))
        if check[-1] is False:
            # file_list1_data[index] = list2_data[start_point_index + index]
            strt.append((index, start_point_index + index))

    return strt, list2_data


def new_data_to_json_exclude(file_data, new_data, indexes, exclude_key):
    """
    This function updates the 'file_data' dictionary with 'new_data' excluding the 'exclude_key/s'.
    If 'exclude_key' exists in 'file_data', it is preserved.

    Parameters:
    file_data (dict): The original data to be updated.
    new_data (dict): The new data to update 'file_data'.
    indexes (list): A list of tuples. Each tuple contains two indexes.
    The first index is for 'file_data' and the second index is for 'new_data'.
    exclude_key (str): The key to be excluded from 'new_data' when updating 'file_data'.

    Returns:
    list[dict]: The updated 'file_data' to update json.
    """
    for File_index, new_data_index in indexes:
        dict_copy = {k: v for k, v in new_data[new_data_index].items() if k != exclude_key}

        if exclude_key in file_data[File_index]:
            dict_copy[exclude_key] = file_data[File_index][exclude_key]
        file_data[File_index] = dict_copy
    return file_data
