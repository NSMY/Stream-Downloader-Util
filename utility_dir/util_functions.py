import json
import os
import pprint
import webbrowser
from datetime import datetime, timezone

import inquirer


def update_downloaded_to_resolution(target_id, new_value):
    jsonss_dir = f'{get_appdata_dir()}/jsons/'

    for filename in os.listdir(jsonss_dir):
        if filename.endswith('.json'):  # Assuming the dicts are stored in .json files
            file = os.path.join(jsonss_dir, filename)
            with open(file, 'r') as f:
                data = json.load(f)
                for i, d in enumerate(data):
                    if d.get('id') == target_id:
                        # target_file_obj = {filename: i}
                        data[i]['downloaded'] = new_value
                        break  # If you want to stop searching after finding the first match
            with open(file, 'w') as f:
                json.dump(data, f, indent=4)


def get_appdata_dir():
    """Returns the STU appdata_path directory"""
    appdata_path = os.getenv("LOCALAPPDATA")
    return os.path.join(str(appdata_path), "Stream-Downloader-Util")


def decode_seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes}:{seconds}"

def encode_hms_to_seconds(time_str, split_on=':'):
    """input must be hh:mm:ss format separated by :"""
    hours, minutes, seconds = map(int, time_str.split(split_on))
    return hours * 3600 + minutes * 60 + seconds


def dump_json_ind4(*, file_path, content_dump) -> None:
    """Dumps Content to FilePath as Json with indent=4"""
    with open(file_path, "w") as json_file:
        json.dump(content_dump, json_file, indent=4)


def convert_timestamp(timestamp):
    """
    Returns:
        Readable Time from twitch gql query.
    """
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return dt.strftime("%A, %d %B %Y %I-%M-%S")


def simple_convert_timestamp(timestamp):
    """
    Returns:
        Readable Time from twitch gql query.
    """
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return dt.strftime("%Y-%m-%d")


def days_ago(timestamp):
    """
    Returns:
        int of days ago
    """
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    difference = now - dt
    return difference.days


def compare_latest_vod_index(content: list[dict], gql_resp):
    """
    Compares the latest video id from GraphQL response with
    the first id in a .JSON data.

    Args:
        content (str): Data from a JSON file list[dict].
        gql_resp (dict): GraphQL.json() response.

    Returns:
        None if ids match, else calls get_index_last_vod function returns
        with matching index:int.
    """
    # [] need to error handle incase response is empty/ not the same structure.
    latest = gql_resp["data"]["user"]["videos"]["edges"][0]["node"].get("id")
    if latest == content[0]["id"]:
        return 0
    else:
        return get_index_last_vod(content, gql_resp)


def get_index_last_vod(content, gql_resp):
    """
    Creates a list[dict] of video ids from gql map, gets the [0]['id'] from
    the content and passes to get_index_of_target_id to find in gql.

    Args:
        content (key=id{value=stream-id-number}): Content loaded from a JSON file.
        gql_resp (dict): GraphQL response.

    Returns:

    """
    id_list = []
    if isinstance(gql_resp, list):
        for i in gql_resp:
            id_value = i.get("id")
            id_dict = {"id": id_value}
            id_list.append(id_dict)
    else:
        for edge in gql_resp["data"]["user"]["videos"]["edges"]:
            id_value = edge["node"].get("id")
            id_dict = {"id": id_value}
            id_list.append(id_dict)
    targid = content[0]["id"]
    # [] add return to after the base call not here makes this dependant on Get_index
    # make return just be the raw data return id_list, targid.
    return get_index_of_target_id(input_content=id_list, target_id=targid)


def get_index_of_target_id(*, input_content, target_id: str):
    """
    Finds the list index of a target ID in a JSON [lst{dict}] object.

    Parameters:
    input_content (str or list): The content to be searched.
    It could be a filename (str) or a list of dictionaries.
    target_id (str): The ID to be searched for.

    Returns:
    int or bool: The index of the target ID in the content.
    If the target ID is not found, it returns False.
    """
    if isinstance(input_content, list):
        first_id = input_content[0].get("id")
        if first_id == target_id:
            # print("🐍 File: utility_dir/util_functions.py | Line: 105 | get_index_of_target_id ~ first_id",first_id)
            return 0
        else:
            content = input_content
    else:
        with open(input_content, "r") as f:
            content = json.load(f)
    return next(
        (
            objects
            for objects, dictkey in enumerate(content)
            if dictkey.get("id") == target_id
        ),
        False,
    )


def multi_choice_dialog(mssg: str, choice_s: list,
                        return_options="str", keys_name="Key"
                        ):
    """
    Args:
        mssg (str): questions mssg
        choice_s (list): choices
        return_options (str, optional): if u want a string returned or dict.
        keys_name (str, optional): name of "Key" in dict.

    Returns:
        Str or Dict
    """
    questions = [
        inquirer.List(
            keys_name,
            message=mssg,
            choices=choice_s,
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer is not None:
        if return_options == "str":
            return "".join([str(value) for value in answer.values()])
        return answer

# vods_dir = r'jsons\\'
# vods_list = []
# for files in os.listdir(vods_dir):
#     vods_list.append(files.removesuffix('.json'))
# import pretty_errors

# def retreve_video_desired():
#     vods_dir = r'jsons\\'
#     list_of_streamer_jsons = [files.removesuffix('.json')for files in os.listdir(vods_dir)]
#     string_list_of_streamer_jsons = ', '.join(list_of_streamer_jsons)

#     selected_json = multi_choice_dialog(
#         string_list_of_streamer_jsons, 
#         choice_s=list_of_streamer_jsons, 
#         return_options="dict", keys_name='streamer' )

#     with open(f'jsons\\{selected_json['streamer']}.json', 'r') as f: # type: ignore will not be None
#         data = json.load(f)

#     quick_desc_ = [(i, d['publishedAt'], d['title']) for i, d in enumerate(data)]

#     stream = multi_choice_dialog(
#         f'What Vod do you want form {selected_json['streamer']}----------',# type: ignore will not be None
#         choice_s=quick_desc_
#         )

#     index = int(stream.strip('(').split(',')[0])# type: ignore will not be None
#     print({f"{selected_json}.json":data[index]})

#     # webbrowser.open(data[index]['url'])






# import pretty_errors

# print("hello")
# # testing errors.
# with open("jsons/kotton.json") as f:
#     data = json.load(f)
# latest = data[100].get("id")
# print(latest)
# # Your list
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,]

# # Pop the item at index 14
# popped_item = data.pop(8)
# print(f"Popped item: {popped_item}")
# print(f"List after popping: {data}")

# # The new item you want to insert
# new_item = 'new_item'

# # Insert the new item at index 14
# data.insert(8, 255)
# print(f"List after inserting: {data}")
