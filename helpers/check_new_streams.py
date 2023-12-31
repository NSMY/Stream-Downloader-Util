# first logic for renew jsons.

import json
import os
import threading

from helpers import util_functions as util
from my_utils import get_single_vod_ as gsv
from my_utils import spinner as spn

from . import gql_main_call
from . import swap_old_data as sod

# import pretty_errors


# def test_data_for_checkStreams(json_file_path, streamer_user_name, vod_index=6):
#     gql_fake_data = {'data': {'user': {'videos': {'totalCount': 334, 'edges': [{'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1973622401', 'title': 'Henry, Master Thief - KCD Hardcore Day 5 - Half Sword Later - !Glasses', 'publishedAt': '2023-11-10T14:44:52Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 18123, 'viewCount': 15944, 'game': {'id': '458912', 'name': 'Kingdom Come: Deliverance'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1973536243', 'title': 'Henry, Master Thief - KCD Hardcore Day 5 - Half Sword Later - !Glasses', 'publishedAt': '2023-11-10T12:02:03Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 9589, 'viewCount': 8708, 'game': {'id': '458912', 'name': 'Kingdom Come: Deliverance'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1972672377', 'title': 'Half Sword - Chasing that Highscore (4410) - !Glasses', 'publishedAt': '2023-11-09T12:09:24Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 27786, 'viewCount': 24941, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1972663957', 'title': 'Half Sword - Chasing that Highscore (4410) - !Glasses', 'publishedAt': '2023-11-09T11:52:13Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 810, 'viewCount': 1057, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1971836501', 'title': 'Morning Half Sword - 4410 High Score - KCD Later! - !Glasses', 'publishedAt': '2023-11-08T12:10:01Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 28625, 'viewCount': 26015, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1970976562', 'title': 'Half Sword - 4410 High Score - Kingdom Come: Deliverance Later - !Glasses', 'publishedAt': '2023-11-07T11:39:44Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 30290, 'viewCount': 28046, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1970170845', 'title': 'Early Morning Coffee & Half Sword - Kingdom Come Deliverance TODAY - !Glasses', 'publishedAt': '2023-11-06T11:48:10Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 28424, 'viewCount': 30573, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1967417346', 'title': "We're Beating Half Sword - !Glasses", 'publishedAt': '2023-11-03T12:07:53Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 24358, 'viewCount': 24951, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1967275983', 'title': 'New Tech Test Stream - !Glasses', 'publishedAt': '2023-11-03T05:08:48Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 2840, 'viewCount': 1951, 'game': {'id': '509658', 'name': 'Just Chatting'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1966532291', 'title': 'Half Sword - Becoming the Ultimate Gladiator - !Glasses', 'publishedAt': '2023-11-02T11:33:14Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 27050, 'viewCount': 29925, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1965704937', 'title': 'Road to 200,000 Citizens - Los Pepegos - Day 7 - !Glasses', 'publishedAt': '2023-11-01T11:28:09Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 23748, 'viewCount': 25335, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1964873487', 'title': 'Road to 200,000 Citizens - Los Pepegos - Day 6 - !Glasses', 'publishedAt': '2023-10-31T11:38:16Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 19898, 'viewCount': 20968, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1964080409', 'title': 'Road to 100,000 Citizens - Los Pepegos - Day 5 - !Glasses', 'publishedAt': '2023-10-30T12:28:33Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 23733, 'viewCount': 28526, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1964070619', 'title': 'Road to 100,000 Citizens - Los Pepegos - Day 5 - !Glasses', 'publishedAt': '2023-10-30T12:05:08Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 1327, 'viewCount': 2266, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1961505777', 'title': 'Road to 100,000 Citizens - Los Pepegos - Day 4 - !Glasses', 'publishedAt': '2023-10-27T11:11:50Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 28993, 'viewCount': 30199, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1960693424', 'title': 'Cities Skylines "Master" Building Los Pepegos - Day 3 - !Glasses', 'publishedAt': '2023-10-26T11:23:40Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 27455, 'viewCount': 26549, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1960188971', 'title': 'Cities Skylines "Master" Building Los Pepegos - !Glasses', 'publishedAt': '2023-10-25T19:36:27Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 58, 'viewCount': 958, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1959862412', 'title': 'Cities Skylines "Master" Building Los Pepegos - !Glasses', 'publishedAt': '2023-10-25T10:34:10Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 30236, 'viewCount': 30137, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1959081227', 'title': 'Tuesday Raids & Coffee - CITIES 2 TODAY - !Glasses', 'publishedAt': '2023-10-24T12:02:47Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 33394, 'viewCount': 40587, 'game': {'id': '491931', 'name': 'Escape from Tarkov'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}]}}}, 'extensions': {'durationMilliseconds': 73, 'requestID': '01HEYEJXN3VC4QH7RRNZJ6V3WT'}}  # fake test data to stop calls and fasten dev.
#     with open(json_file_path, 'r+') as f:
#         data = json.load(f)
#         new_data = data[vod_index:]
#         f.seek(0)
#         json.dump(new_data, f, indent=4)
#         f.truncate()
#     return gql_fake_data


def check_for_new_vods(
    json_file_path,
    streamer_user_name,
    amount_of_vods: int = 100,
    sort_by: str = "TIME"
):
    """_summary_

    Args:
        json_file_path (_type_): _description_
        streamer_user_name (_type_): _description_
        amount_of_vods (int, optional): _description_. Defaults to 100.
        sort_by (str, optional): _description_. Defaults to "TIME".

    Returns:
        tuple: [0]json_file_path [1]file_data [2]GQLresp [3]vod_index
    """
    if not os.path.exists(json_file_path):
        gql_main_call.First_making_cmds(streamer_user_name)
        # [ ] call 1st set up of vods making....
        return None

    # Blocked OUT USING Fake DATA to stop calls and fasten dev
    query = gql_main_call.query_channel_vods(streamer_user_name, amount_of_vods, sort_by)
    spinner1 = spn.Spinner()
    spinner1.start()
    query_resp = gql_main_call.gql_query(query=query)
    resp = query_resp.json()
    spinner1.stop()
    if query_resp.status_code != 200:
        print("Error retrieving Data from GraphQL Twitch API")
        import startup
        startup.main_start()

    # resp = test_data_for_checkStreams(json_file_path, streamer_user_name, vod_index=6)  # Testing Code Fake data.

    with open(json_file_path, "r") as f:
        file_data = json.load(f)

    # one can be threaded.
    vod_index = util.compare_latest_vod_index(file_data, resp)

    return json_file_path, file_data, resp, vod_index


def add_new_entries_json(
    json_file_path: str,
    file_data: list[dict],
    GQLquery, vod_index: int
) -> list[dict]:

    vods_dict = gql_main_call.Vod.create_vods_from_edges(
        GQLquery["data"]["user"]["videos"]["edges"]
    )

    print_new_vods_from_dictClass(vod_index, vods_dict)

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
    return loaded_list_dicts[:vod_index]


def print_new_vods_from_dictClass(vod_index, vods_dict):
    if vod_index != 0:
        from helpers import tk_get_file_list
        tk_get_file_list.call_tk_data(vods_dict[:vod_index], '')

    print(f'\n\n{(vod_index)}: New Vods\n')
    return
    # FIX if streamers dont keep vods will
    # return 0 vods new but will update file if a vods temporarily still available
    # unti`l hidden.


# def start_new_vods(json_file_path, streamer_user_name):


def update_json_data(cnv_rtrn):
    spinner1 = spn.Spinner()
    spinner1.start()
    start_point_index = int(util.get_index_last_vod(cnv_rtrn[1], cnv_rtrn[2]))
    conflict_data = sod.get_conflicting_indexes(cnv_rtrn[1], cnv_rtrn[2], start_point_index, ['downloaded'])
    newData = sod.new_data_to_json_exclude(cnv_rtrn[1], conflict_data[-1], conflict_data[0], 'downloaded')
    with open(cnv_rtrn[0], 'w') as f:
        json.dump(newData, f, indent=4)

    if cnv_rtrn[3] is not None:
        newData = add_new_entries_json(cnv_rtrn[0], cnv_rtrn[1], cnv_rtrn[2], cnv_rtrn[3])
    spinner1.stop()
    return newData
    # print(gsv.Run_get_vod(streamer_name))


def start_new_vods():
    # [] input the best way??
    # print(type(gsv.get_file_list_from_dir(rf"{util.get_appdata_dir()}\jsons")))
    # streamer_name = input('Streamer Name or "saved" to get a list of previous:').lower()
    # if streamer_name == "saved":
    streamer_name = util.multi_choice_dialog(
        "Who?",
        gsv.get_file_list_from_dir(rf"{util.get_appdata_dir()}\jsons")
        + ['--New Streamer to Add--']
        + ['**CANCEL**']
    )

    if streamer_name == '**CANCEL**':
        os.system('cls')
        import startup
        startup.main_start()
    elif not streamer_name == "--New Streamer to Add--":
        cnv_rtrn = check_for_new_vods(
            rf"{util.get_appdata_dir()}\jsons\{streamer_name}.json",
            streamer_user_name=streamer_name
        )
        if cnv_rtrn[-1] == 0:
            update_info = threading.Thread(target=update_json_data, args=(cnv_rtrn, ))
            update_info.start()
            # print('in the if')
            return
        else:
            # print("else\n\n")
            return update_json_data(cnv_rtrn)
    else:
        gql_main_call.First_making_cmds(input('User Name:').lower())


if __name__ == "__main__":
    start_new_vods()


# streamer = 'lanaee_lux'
# amount = 100
# # if os.path.exists(streamer
# check_for_new_vods(f"jsons\\{streamer}.json", f'{streamer}', amount)
# # 'https://www.twitch.tv/videos/1957663657', '22-10-2023 The Cumback Colony 500 BrutalCassandra  mods RimWorld Kotton'
# # print(f"jsons\\{input('Streamer Name:').lower()}.json")
# # print(f"jsons\\{input('Streamer Name:').lower()}.json")
