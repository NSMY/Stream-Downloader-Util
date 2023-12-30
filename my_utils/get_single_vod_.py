# Gets specific index data from saved Json dict[list].

import json
import os
import pprint

from helpers import util_functions as util

# import util_functions as util  # Only to test code inside this module
from helpers.tk_get_file_list import call_tk_file


def get_file_list_from_dir(vods_dir) -> list:
    '''Returns a list of file names in the given directory & strips .json Suffix'''
    files_list = []
    for files in os.listdir(vods_dir):
        if not os.path.isdir(f'{vods_dir}//{files}'):
            files_list.append(files.removesuffix('.json'))
    return files_list


def select_json(list_of_streamer_jsons):
    string_list_of_streamer_jsons = ', '.join(list_of_streamer_jsons) + '**Cancel**'
    list_of_streamer_jsons.append('**Cancel**')
    choice = util.multi_choice_dialog(
        'List of saved Jsons',
        choice_s=list_of_streamer_jsons,
        return_options="dict",
        keys_name='streamer'
    )
    if choice.get("streamer") == '**Cancel**':
        import startup
        os.system("cls")
        startup.main_start()
    return choice


def creator_load_json_data(selected_json):
    # with open(f'jsons\\{selected_json['streamer']}.json', 'r') as f:
    with open(rf'{util.get_appdata_dir()}\jsons\{selected_json['streamer']}.json', 'r') as f:
        return json.load(f)


def select_video(data, selected_json):
    stream = call_tk_file(rf'{util.get_appdata_dir()}\jsons\{selected_json['streamer']}.json')
    if stream == []:
        get_desired_vod_from_lst()
    else:
        return stream # type: ignore will not be None


def get_desired_vod_from_lst(**kwargs) -> dict:
    vods_file_dir = rf'{util.get_appdata_dir()}\jsons'
    if 'selected_json' not in kwargs:
        list_of_streamers_jsons = get_file_list_from_dir(vods_file_dir)
        selected_json = select_json(list_of_streamers_jsons)
    data = creator_load_json_data(selected_json)
    video = select_video(data, selected_json)
    if video:
        return selected_json, {
            'file': f"{selected_json['streamer']}.json",  # type: ignore will not be None
            'index': video[0],
            'vod_info': video[1]
        }
    else:
        os.system('cls')
        print('No Selection Made!\n')
        import startup
        startup.main_start()
    # return selected_json, {
    #     'file': f"{selected_json['streamer']}.json",  # type: ignore will not be None
    #     'index': video[0],
    #     'vod_info': video[1]
    # }
    # webbrowser.open(video[1]['url'])


def Run_get_vod(streamer_name):
    return get_desired_vod_from_lst(streamer=streamer_name)


if __name__ == '__main__':
    Run_get_vod('')
