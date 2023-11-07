# first logic for renew jsons.


import json
import os

from new_mass_gql.utility_dir import get_single_vod_ as gsv
from new_mass_gql.utility_dir import util_functions as util

from . import gql_main_call

# import pretty_errors


def check_for_new_vods(
    json_file_path, streamer_user_name, amount_of_vods: int = 100, sort_by: str = "TIME"
):
    if not os.path.exists(json_file_path):
        # [ ] call 1st set up of vods making....
        return None
    query = gql_main_call.query_channel_vods(streamer_user_name, amount_of_vods, sort_by)
    query_resp = gql_main_call.gql_query(query=query)
    resp = query_resp.json()
    if query_resp.status_code != 200:
        print("Error retrieving Data from GraphQL Twitch API")
    with open(json_file_path, "r") as f:
        file_data = json.load(f)
    if (vod_index := util.compare_latest_vod_index(file_data, resp)) is None:
        print('No new streams\n')
        return file_data
    print(f'\n{str(vod_index)}: New Vods\n')
    # [] add a print list of added vods.
    return add_new_entries_json(json_file_path, file_data, resp, vod_index)


def add_new_entries_json(
    json_file_path: str,
    file_data: list[dict],
    GQLquery, vod_index: int
) -> list[dict]:

    newly_vods = gql_main_call.Vod.create_vods_from_edges(
        GQLquery["data"]["user"]["videos"]["edges"]
    )
    # Convert Vod instances to dictionaries
    vods_dict = [vars(vod) for vod in newly_vods]

    # Dynamic max length?????.
    loaded_list_dicts_len: int = len(file_data)
    # The new list of dictionaries can be concatenated with the old one:
    loaded_list_dicts = vods_dict[:vod_index] + file_data
    # If the length of loaded_list_dicts exceeds X (100), we trim it down to 100:
    if len(loaded_list_dicts) > loaded_list_dicts_len:
        loaded_list_dicts = loaded_list_dicts[:loaded_list_dicts_len]

    # Write the final list of dictionaries back to the file as a JSON string:
    util.dump_json_ind4(
        file_path=json_file_path, content_dump=loaded_list_dicts
    )
    return print(loaded_list_dicts[:vod_index])


# def start_new_vods(json_file_path, streamer_user_name):
def start_new_vods():
    # [] input the best way??
    streamer_name = input('Streamer Name or "saved" to get a list of previous:').lower()
    if streamer_name == "saved":
        streamer_name = util.multi_choice_dialog(
            # "Who to Check?:", gsv.get_file_list_from_dir("jsons\\")
            "Who to Check?:", gsv.get_file_list_from_dir(rf"{util.get_appdata_dir()}\jsons")
        )
    check_for_new_vods(
        # f"jsons\\{streamer_name}.json",
        rf"{util.get_appdata_dir()}\jsons\{streamer_name}.json",
        streamer_name,
        int(input("amount of vods to retrieve:")),
    )
    print(gsv.Run_get_vod(streamer_name))


if __name__ == "__main__":
    start_new_vods()


# streamer = 'lanaee_lux'
# amount = 100
# # if os.path.exists(streamer
# check_for_new_vods(f"jsons\\{streamer}.json", f'{streamer}', amount)
# # 'https://www.twitch.tv/videos/1957663657', '22-10-2023 The Cumback Colony 500 BrutalCassandra  mods RimWorld Kotton'
# # print(f"jsons\\{input('Streamer Name:').lower()}.json")
