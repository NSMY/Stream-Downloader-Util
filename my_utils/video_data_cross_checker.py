# ########################## Mass File Checking to compare if has been downloaded with Jsons data #########################
import json
import os
import re
import subprocess
import threading
from queue import Queue
from tkinter import filedialog

import helpers.funcs as funcs
import init_dir.init_files as init_files
import my_utils.spinner as spinner
from helpers.util_functions import get_appdata_dir

# to make the file work as a stand alone
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# import funcs

def find_files(directory):
    ok_extentions = ["mp4", "mvk", "mov", "flv"]
    files = []
    for dirpath, dirnames, filenames in os.walk(directory, followlinks=True):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if filename.rsplit('.')[-1] in ok_extentions:
                files.append(full_path)
    return files


def get_video_data(vid_list: list, ffprobe_path):
    """Returns a list(tuple) (video_path, vid_length, vid_fps, vid_height, vid_size)"""
    '''
        import subprocess
    import concurrent.futures

    # List of commands to run
    commands = ['ls', 'pwd', 'date']

    def run_command(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            return f'Error executing command: {command}\nError message: {stderr.decode()}'
        else:
            return stdout.decode()

    # Use a ThreadPoolExecutor to run the commands in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        outputs = list(executor.map(run_command, commands))

    # Now outputs contains the output of each command
    for i, output in enumerate(outputs):
        print(f'Output of command {commands[i]}: {output}')
    '''

    video_info = []
    for video in vid_list:
        q1 = Queue()
        q2 = Queue()
        q3 = Queue()
        vid_size = os.path.getsize(video)
        vid_length = threading.Thread(target=get_video_file_length, args=(video, q1, ffprobe_path))
        vid_fps = threading.Thread(target=get_video_framerate, args=(video, q2, ffprobe_path))
        vid_height = threading.Thread(target=get_video_height, args=(video, q3, ffprobe_path))
        vid_height.start()
        vid_length.start()
        vid_fps.start()
        vid_height.join()
        vid_length.join()
        vid_fps.join()
        vid_height = q3.get()
        vid_length = q1.get()
        vid_fps = q2.get()

        video_info.append((video, vid_length, vid_fps, vid_height, vid_size))
    return video_info


def get_video_file_length(file_path, queue, ffprobe_path):
    get_len_of_vod_file = subprocess.Popen(
        rf'ffprobe -i "{file_path}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd=ffprobe_path
    )
    stdout, stderr = get_len_of_vod_file.communicate()
    get_len_of_vod_file.wait()
    queue.put(int(stdout.split('.')[0]))


def get_video_framerate(filepath, queue, ffprobe_path):
    stdout = ''
    try:
        process = subprocess.Popen(
            f'ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "{filepath}"',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd=ffprobe_path
        )
        stdout, stderr = process.communicate()
        process.wait()
        numerator, denominator = map(int, stdout.split('/'))
        result = numerator / denominator
        queue.put(str(round(result)))
    except ValueError as e:
        print(
            f"\n{e}: {os.path.basename(filepath)}"
            "\nLikely an Non Mux'ed video Included or Sys is accessing the File\n"
        )
        queue.put(stdout.split('/')[0])


def get_video_height(filepath, queue, ffprobe_path):
    process = subprocess.Popen(
        f'ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=s=x:p=0 "{filepath}"',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd=ffprobe_path
    )
    stdout, stderr = process.communicate()
    process.wait()
    queue.put(stdout.split('\n')[0])
    # return str(stdout)


def vod_titles_parse(vods_info):
    """returns a dicts{dicts} of vods. Key(filepath): keys{
        length,
        size,
        username,
        date,
        game,
        title,
        gamename,
        filetype
        }
"""
    vods_details = {}
    for info in vods_info:
        try:
            path = os.path.basename(info[0])
            if match := re.match(
                r'(?P<username>.*?) - (?P<date>\d{4}-\d{2}-\d{2}) (?P<title>.*?)_(?P<gamename>.*?)\.(?P<filetype>\w+)$',
                path,
            ):
                vods_details[f'{info[0]}'] = {
                    "length": info[1],
                    "size": info[-1],
                    "height_fps": f'{info[3].strip()}p{info[2]}',
                    "username": match.group('username'),
                    "date": match.group('date'),
                    "title": match.group('title'),
                    "gamename": match.group('gamename'),
                    "filetype": match.group('filetype')
                }
            else:
                filetype = path.rsplit('.', 1)[-1]
                basename = path.rsplit('.', 1)
                username = basename[0].split('-', 1)[0].strip().lower()
                date = basename[0].split(' ', 3)[-2]
                title0 = basename[0].rsplit('_', 1)[0]
                titlename = title0.split(' ', 3)[-1].strip()
                gamename = basename[0].rsplit('_', 1)[-1].strip()
                vods_details[f'{info[0]}'] = {
                    "length": info[1],
                    "size": info[-1],
                    "height_fps": f'{info[3].strip()}p{info[2].strip()}',
                    "username": username,
                    "date": date,
                    "titlename": titlename,
                    "gamename": gamename,
                    "filetype": filetype
                }
        except IndexError:
            continue
    return vods_details


def compare_with_tolerance(size1, size2, tolerance=10) -> bool:
    """
    This function compares two file sizes with a certain tolerance.
    """
    return abs(size1 - size2) <= tolerance


appdir = f'{get_appdata_dir()}/jsons'


def list_files_in_directory(appdir):
    appdir_files = []
    for fjsons in os.listdir(appdir):
        appdir_files.append(fjsons)
    return appdir_files


def vod_user_names(appdir_files, compare_data):
    total_names_from_dld_dir = []
    for key in compare_data:
        if (f'{compare_data[key]['username'].lower()}.json') in appdir_files and compare_data[key]['username'].lower() not in total_names_from_dld_dir:
            total_names_from_dld_dir.append(compare_data[key]['username'])
    return total_names_from_dld_dir


def change_download_status(total_names_from_dld_dir, appdir, compare_data):
    edited = []
    for i in total_names_from_dld_dir:
        with open(f'{appdir}/{i}.json', 'r') as jf:
            innerdata = json.load(jf)
        for index, jdata in enumerate(innerdata):
            for vodfile in compare_data:
                if compare_data[vodfile]['username'].lower() == i.lower():
                    # Compare 'username' with 'id'
                    if (
                        compare_data[vodfile]['username'] == jdata['displayName']
                        and compare_with_tolerance(compare_data[vodfile]['length'], jdata['lengthSeconds'], 20)
                        and compare_data[vodfile].get('title') == jdata['title']
                        and jdata['downloaded'] is False
                    ):
                        edited.append((
                            innerdata[index]['displayName'],
                            innerdata[index]['url'],
                            compare_data[vodfile]['height_fps'])
                        )
                        innerdata[index]['downloaded'] = compare_data[vodfile]['height_fps']
        with open(f'{appdir}/{i}.json', 'w') as wf:
            json.dump(innerdata, wf, indent=4)
    return edited


def main():
    from startup import main_start
    try:
        check_settings = funcs.loadSettings(
            keys=["LastSave", "ffprobepath"]
        )
    except FileNotFoundError as e:
        init_files.initSettings()
        os.system("cls")
        print(e)
        main_start()

    is_a_fresh_save = [funcs.is_less_than_30days(check_settings[0])]  # type: ignore possible unbound

    is_a_fresh_save.extend(check_settings[1:2])  # type: ignore possible unbound

    if not all(is_a_fresh_save):
        funcs.ffprobe_factory_init(["main", "video_data_cross_checker"])
        os.system("cls")
        main()

    ffprobe_dir = os.path.dirname(check_settings[1])

    os.system('cls')

    lfid = list_files_in_directory(appdir)

    spinner1 = spinner.Spinner(message='Choose Parent directory to search through..')
    spinner1.start()

    walk_tree = filedialog.askdirectory()
    if walk_tree == '':
        spinner1.stop()
        return (main() if funcs.multi_choice_dialog('Quit or Choose again?', ['Redo', 'Quit']) == 'Redo' else main_start())
    spinner1.stop()
    os.system("cls")

    spinner2 = spinner.Spinner(message='Processing Video Information...')
    spinner2.start()
    vods_info = get_video_data((find_files(walk_tree)), ffprobe_dir)
    compare_data = (vod_titles_parse(vods_info))

    vun = vod_user_names(lfid, compare_data)

    if edited_list := change_download_status(vun, appdir, compare_data):
        spinner2.stop()
        os.system('cls')
        for i in edited_list:
            print(i)
        print('\nItems Changed.\n')
    else:
        spinner2.stop()
        print("\nNo Changes\n")



if __name__ == '__main__':
    main()
    main()
    main()
