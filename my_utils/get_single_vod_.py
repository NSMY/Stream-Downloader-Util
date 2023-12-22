# Gets specific index data from saved Json dict[list].

import json
import os
import pprint

from helpers import util_functions as util
# import util_functions as util  # Only to test code inside this module
from helpers.tk_get_file_list import call_tk_file


def get_file_list_from_dir(vods_dir) -> list:
    '''Returns a list of file names in the given directory & strips .json Suffix'''
    return [files.removesuffix('.json') for files in os.listdir(vods_dir)]


def select_json(list_of_streamer_jsons):
    string_list_of_streamer_jsons = ', '.join(list_of_streamer_jsons) + '**Cancel**'
    list_of_streamer_jsons.append('**Cancel**')
    choice = util.multi_choice_dialog(
        'List of saved Jsons',
        choice_s=list_of_streamer_jsons,
        return_options="dict",
        keys_name='streamer'
    )
    if choice.get("streamer") == '**Cancel**': # WATCH Implemented only for multichoise, if tkinter maybe take OUT.
        import startup
        os.system("cls")
        startup.main_start()
    return choice


def creator_load_json_data(selected_json):
    # with open(f'jsons\\{selected_json['streamer']}.json', 'r') as f:
    with open(rf'{util.get_appdata_dir()}\jsons\{selected_json['streamer']}.json', 'r') as f:
        return json.load(f)


def select_video(data, selected_json):
    # quick_desc_ = [(i, util.simple_convert_timestamp(d['publishedAt']), util.decode_seconds_to_hms(d['lengthSeconds']), d['gameName'], d['title'], d['downloaded']) for i, d in enumerate(data)]
    # quick_desc_.append("Cancel")
    # stream = util.multi_choice_dialog(f'What Vod do you want form {selected_json['streamer']}----------', choice_s=quick_desc_)
    # if stream == "Cancel":
    #     get_desired_vod_from_lst()  # WATCH Implemented only for multichoise, if tkinter maybe take OUT.

    stream = call_tk_file(rf'{util.get_appdata_dir()}\jsons\{selected_json['streamer']}.json')
    # print("🐍 File: utility_dir/get_single_vod_.py | Line: 49 | select_video ~ stream",stream)
    
    if stream == []:
        get_desired_vod_from_lst()  # WATCH Implemented only for multichoise, if tkinter maybe take OUT.
    else:
        return stream # type: ignore will not be None
    # else:
    #     index = int(stream.strip('(').split(',')[0])  # type: ignore will not be None
    # return (index, data[index])
    # return (index, data[index])


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
