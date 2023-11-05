import json
import os
import pprint

from . import util_functions as util

# import util_functions as util  # Only to test code inside this module




def get_file_list_from_dir(vods_dir) -> list:
    '''Returns a list of file names in the given directory & strips .json Suffix'''
    return [files.removesuffix('.json') for files in os.listdir(vods_dir)]


def select_json(list_of_streamer_jsons):
    string_list_of_streamer_jsons = ', '.join(list_of_streamer_jsons)
    return util.multi_choice_dialog(string_list_of_streamer_jsons, choice_s=list_of_streamer_jsons, return_options="dict", keys_name='streamer')


def creator_load_json_data(selected_json):
    # with open(f'jsons\\{selected_json['streamer']}.json', 'r') as f:
    with open(rf'{util.get_appdata_dir()}\jsons\{selected_json['streamer']}.json', 'r') as f:
        return json.load(f)


def select_video(data, selected_json):
    quick_desc_ = [(i, util.simple_convert_timestamp(d['publishedAt']), util.convert_seconds(d['lengthSeconds']), d['gameName'], d['title'], d['not_downloaded']) for i, d in enumerate(data)]
    stream = util.multi_choice_dialog(f'What Vod do you want form {selected_json['streamer']}----------', choice_s=quick_desc_)
    index = int(stream.strip('(').split(',')[0])  # type: ignore will not be None
    return (index, data[index])


def get_desired_vod_from_lst(**kwargs) -> dict:
    vods_file_dir = rf'{util.get_appdata_dir()}\jsons'
    if 'selected_json' not in kwargs:
        list_of_streamers_jsons = get_file_list_from_dir(vods_file_dir)
        selected_json = select_json(list_of_streamers_jsons)
    data = creator_load_json_data(selected_json)
    video = select_video(data, selected_json)
    return {
        'file': f"{selected_json['streamer']}.json",  # type: ignore will not be None
        'index': video[0],
        'vod_info': video[1]
    }
    # webbrowser.open(video[1]['url'])


def Run_get_vod(streamer_name):
    r = get_desired_vod_from_lst(streamer=streamer_name)
    return (
        r['vod_info']["url"],
        f"{r['vod_info']['displayName']} "
        f"{util.simple_convert_timestamp(r['vod_info']['publishedAt'])} "
        f"{r['vod_info']['title']} "
        f"{r['vod_info']['gameName']}"
    )


if __name__ == '__main__':
    Run_get_vod('')

# print(Run_get_vod(''))
'''
if __name__ == '__main__':
    r = get_desired_vod_from_lst()
    download_tup = (
        r['vod_info']["url"],
        f"{util.simple_convert_timestamp(r['vod_info']['publishedAt'])} "
        f"{r['vod_info']['title']} "
        f"{r['vod_info']['gameName']} "
        f"{r['vod_info']['displayName']}"
    )
    print("🐍 File: utility_dir/get_single_vod_.py | Line: 44 | undefined ~ downlaod_tup",download_tup)
'''
