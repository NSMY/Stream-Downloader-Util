import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path
from queue import Queue
from tkinter import filedialog

# import funcs



 # to make the file work as a stand alone
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import funcs
from utility_dir.util_functions import get_appdata_dir

# ########################## Mass File Checking to compare if has been downloaded with Jsons #########################

# ############get vods check length, has been downloaded??#######################


def find_files(directory):
    ok_extentions = ["mp4", "mvk", "mov", "flv"]
    files = []
    for dirpath, dirnames, filenames in os.walk(directory, followlinks=True):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename) # WATCH may need fstring / instead of .join??.
            if filename.rsplit('.')[-1] in ok_extentions:
                files.append(full_path)
    return files


def get_video_data(vid_list: list):
    """Returns a list(tuple) (video_path, vid_length, vid_fps, vid_height, vid_size)"""
    import timeit

    start_time = timeit.default_timer()

    # timing to see if should send out to concurrent threads or this is ok Hidden Next Line
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
        vid_length = threading.Thread(target=get_video_file_length, args=(video, q1))
        vid_fps = threading.Thread(target=get_video_framerate, args=(video, q2))
        vid_height = threading.Thread(target=get_video_height, args=(video, q3))
        vid_length.start()
        vid_fps.start()
        vid_height.start()
        vid_length.join()
        vid_fps.join()
        vid_height.join()
        vid_length = q1.get()
        vid_fps = q2.get()
        vid_height = q3.get()

        
        video_info.append((video, vid_length, vid_fps, vid_height, vid_size))

    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print('The script took ', execution_time, ' seconds to run.')
    return video_info


def get_video_file_length(file_path, queue):
    get_len_of_vod_file = subprocess.Popen(
        rf'ffprobe -i "{file_path}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd='c:/ffmpeg/'  # FIX replace me.
    )
    stdout, stderr = get_len_of_vod_file.communicate()
    get_len_of_vod_file.wait()
    queue.put(int(stdout.split('.')[0]))
    return int(stdout.split('.')[0])

def get_video_framerate(filepath, queue):
    try:
        process = subprocess.Popen(
            f'ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "{filepath}"',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd='c:/ffmpeg/'  # FIX replace me.
        )
        stdout, stderr = process.communicate()
        process.wait()
        numerator, denominator = map(int, stdout.split('/'))
        result = numerator / denominator
        queue.put(str(round(result)))
        return str(round(result))
    except ValueError as e:
        print(f"\n{e}: Likely an Non Mux'ed video Included")
        queue.put("NA")

def get_video_height(filepath, queue):
    process = subprocess.Popen(
        f'ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=s=x:p=0 "{filepath}"',
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd='c:/ffmpeg/'  # FIX replace me.
    )
    stdout, stderr = process.communicate()
    process.wait()
    queue.put(stdout)
    return str(stdout)



import os

# have multi if checks set to a list/tup or a += count up and if 2-3 of x num of checks > say 3 then whe have enough to say its the file and call downloaded
# one of th checks is length.

# gather info for cross check.. how to error check if/trys if id- date- game- len- error /not available.

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
        path = os.path.basename(info[0])
        if match := re.match(
            r'(?P<username>.*?) - (?P<date>\d{2}-\d{2}-\d{4}) (?P<title>.*?)_(?P<gamename>.*?)\.(?P<filetype>\w+)$',
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
                "height_fps": f'{info[3].strip()}p{info[2]}',
                "username": username,
                "date": date,
                "titlename": titlename,
                "gamename": gamename,
                "filetype": filetype
            }
    return vods_details


# walk_tree = ('E:/DeleteStreams/FFMPEG__re-Muxed')
walk_tree = filedialog.askdirectory()

vods_info = get_video_data((find_files(walk_tree)))
# print("🐍 File: zextra_Funcs_/check_old_files_downloaded.py | Line: 177 | undefined ~ vods_info",vods_info)
compare_data = (vod_titles_parse(vods_info))

print(json.dumps(vod_titles_parse(vods_info), indent=2))


def compare_with_tolerance(a, b, tolerance=10):
    return abs(a - b) <= tolerance

# TODO make the next part == sets video if Found in the jsons to downloaded = height_fps.


# BELOW is misunderstanding that for the download check not file already exists check
########## the huge if (next) block to cross check x out of y pass == true downloaded ############################


appdir = f'{get_appdata_dir()}/jsons'

total_names_from_dld_dir = []

for key in compare_data:
    if compare_data[key]['username'] not in total_names_from_dld_dir:
        total_names_from_dld_dir.append(compare_data[key]['username'])

# TODO got ^ individual names now need to cross compare// also what if the name dnt exist in jsons still check for title?/date/gamename???.


# # Get the directory name
# dirname = os.path.dirname(file)
# print(f"Directory: {dirname}")



# for index, v in enumerate(filedata):
#     # if string in i['title']:
#         # print('partial match')
#     if v['title'] in string:
#         print('partial match', index)