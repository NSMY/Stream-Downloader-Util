
import json
import os
import subprocess
import sys
import tkinter as tk
import winsound
import zipfile
from datetime import datetime, timedelta
from tkinter import filedialog
from urllib.parse import urlparse, urlunparse

import inquirer
import psutil
import requests
from pyperclip import copy, paste
from send2trash import send2trash
from tqdm import tqdm

from default_path_factory import DefaultPathFactory
from Main import main_script

video_file_types = [".mp4", ".mov", ".mkv", ".ts"]


def make_new_dir_from_input(input_file_path: str, new_dir_name_arg: str) -> str:
    '''Makes a directory from the input file path
    inline with input_file_path'''
    file_path_2 = os.path.dirname(input_file_path)
    new_folder_combine_path = os.path.join(file_path_2, new_dir_name_arg)

    if not os.path.exists(new_folder_combine_path):
        os.makedirs(new_folder_combine_path)
    return os.path.join(new_folder_combine_path)


def video_file_exetension_return(filename: str) -> str:
    '''Returns the .extension if in video_file_types
    otherwise returns empty string'''
    for file_type in video_file_types:
        if filename.endswith(file_type):
            print(file_type)
            return file_type
    return ""


def shorten_path_name(file_path: str):
    """shortens Filepaths for viewing/printing

    Args:
        file_path (str):
    Returns:

        str: _shorter_filepath_
    """
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    dir_parts = dir_name.split(os.sep)
    if len(dir_parts) > 2:
        short_dir = f"{dir_parts[0]}{os.sep}...{os.sep}{dir_parts[-1]}"
    else:
        short_dir = dir_name
    return os.path.join(short_dir, base_name)


def is_url(variable):
    """Checks if str is URL"""
    try:
        result = urlparse(variable)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def has_ffmpeg_dir(stream_lnk_Path):
    store_path = os.path.join(os.path.dirname(stream_lnk_Path), "ffmpeg")
    return os.path.isdir(store_path)


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


def open_directory_Force_front(full_dir_path: str):
    root = tk.Tk()
    root.withdraw()
    path = os.path.dirname(full_dir_path)
    os.startfile(os.path.realpath(path))
    root.destroy()


def openFile():
    """Opens File dialog box
    Returns:
        str:

    loops if canceled
    """
    # print("Open File From:... \n")
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filep = filedialog.askopenfilename(
        parent=root,
        defaultextension=".*",
        filetypes=[
            ("MP4 files", ".mp4"),
            ("MOV files", ".mov"),
            ("MKV files", ".mkv"),
            ("MP3 files", ".mp3"),
            ("All files", ".*"),
        ])
    root.destroy()
    file = os.path.normpath(filep)
    if not filep:  # closes Program if No Save path is Entered
        check = multi_choice_dialog("Canceled Open File: Try again?",
                                    ["yes", "no", "exit"])
        if check == "yes":
            os.system("cls" if os.name == "nt" else "clear")
            openFile()
        elif check == "no":
            os.system("cls" if os.name == "nt" else "clear")
            main_script()
        sys.exit()
    return file


def saveFile(kwargs=''):
    """Opens: Save File Explorer
    Returns:
        Save Path
    """
    print("Save File To:... \n")
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    filep = filedialog.asksaveasfilename(
        parent=root,
        initialfile=kwargs,
        defaultextension=".mp4",
        filetypes=[
            ("MP4 files", ".mp4"),
            ("MOV files", ".mov"),
            ("MKV files", ".mkv"),
            ("MP3 files", ".mp3"),
            ("All files", ".*"),
        ],
        title='kwargs')
    root.destroy()
    file = os.path.normpath(filep)
    if not filep:  # Closes Program if No Save path is Entered
        check = multi_choice_dialog("Canceled Save Path: Try again?",
                                    ["yes", "no", "exit"])
        if check == "yes":
            os.system("cls" if os.name == "nt" else "clear")
            saveFile()
        elif check == "no":
            os.system("cls" if os.name == "nt" else "clear")
            main_script()
        sys.exit()
    return (file)


def program_Path_Details(program_name):
    """Gets Program file path, but only if its in "the Path".
    """
    try:
        where = subprocess.check_output(["where", program_name])
        version = subprocess.check_output([program_name, "--version"])
        return where.decode("utf-8").split(), version.decode("utf-8").strip()
    except FileNotFoundError:
        return None


def download_url(url: str, dloadFilePath: str, dlmssg: str = ""):
    # sourcery skip: extract-method
    """Downloads the url to dloadFilepath using Requests

    Args:
        url (str): URLdownload link
        dloadFilePath (str): Download Path

        dlmssg (str, optional): Transparency mssg whats
        happening. Defaults to "".
    """
    if os.path.exists(dloadFilePath):
        return dloadFilePath
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024

        print(dlmssg)
        with open(file=dloadFilePath, mode="wb") as f:
            for data in tqdm(
                response.iter_content(chunk_size=block_size),
                total=total_size//block_size, unit="KB"
            ):

                f.write(data)
        return True
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return False
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return False
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return False
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong. Error: {err}")
        return False


def unzip_file_from_path(
    zip_file_path,
    outputDir,
    specific_filename_to_extract: str = "",
    mssg=""
):
    """Unzips files or specific File into outputDir,

    moves Old .zip to Bin if both exist.

    Args:
        dloadFilePath (str): C:\\example\\file.type

        outputDir (str): C:\\OutPutFolder\\

        specificFile (str, optional): fileType.exe Defaults to " ".

        mssg (str, optional): Trash mssg Defaults to "".
    """
    if not os.path.isfile(f"{outputDir}\\{specific_filename_to_extract}"):
        try:
            zip_file = zip_file_path
            print(zip_file)
            output_dir = outputDir
            with zipfile.ZipFile(file=zip_file, mode="r") as zf:
                if specific_filename_to_extract:
                    zf.extract(specific_filename_to_extract, output_dir)
                zf.extractall(output_dir)
                print(f"\nSuccessful Extraction To {output_dir}")
        except Exception:
            print(f"\n\nERROR: Could not extract {zip_file_path} \n")
            fldr = zip_file_path.replace(specific_filename_to_extract, "")
            return os.startfile(fldr)
        if os.path.isfile(zip_file_path) and os.path.isfile(
            f"{outputDir}\\{specific_filename_to_extract}"
        ):
            send_to_trash(zip_file_path)
            return True
    return True


def send_to_trash(filename):
    send2trash(filename)
    if not os.path.isfile(filename):
        print(f"sent {filename} to recycler")
        winsound.PlaySound(
            sound="C:\\Windows\\Media\\Recycle.wav",
            flags=winsound.SND_FILENAME
        )
        return True
    return False


def file_search(extensionNam: str):
    """

    Args:
        exeName ('Example.exe'):

    Returns:
        _type_: str
    """
    appDataSubDirs = ["Local", "LocalLow", "Roaming"]
    directories = ["C:\\ffmpeg\\", "C:\\Program Files", "C:\\Program Files (x86)"] + [
        os.path.expanduser(f"~\\AppData\\{subDir}") for subDir in appDataSubDirs
    ]
    found = False
    exePth = ""
    for directory in directories:
        if found:
            return str(exePth)

        for root, dirs, files in os.walk(directory):
            if extensionNam in files:
                exePth = (os.path.join(root, extensionNam))
                found = True
                break
    return None


def audio_channel_get_info(fprobeDir, filename):
    '''-> Codec type at pos[0], channels at pos[1]'''
    if not fprobeDir:
        print(f'\nCould Not Find "{fprobeDir}" on your Computer\n')
        while True:
            try:
                audChannels = int(input('Couldn"t Auto retrieve Maximum'
                                        'number of Audio Channels, How Many '
                                        f'Channels does {filename} have?:'))
                channels_list = []
                for i in range(1, audChannels + 1):
                    channels_list.append(i)
                return channels_list
            except ValueError:
                print("Please enter a numerical value(int) EG: 3.")
    else:
        command = (
            f"ffprobe -v error -show_entries stream=index"
            rf' -select_streams a -of csv=p=0 "{filename}"'
        )
        opusCmd = (
            f"ffprobe -v error -select_streams a:0 -show_entries "
            "stream=codec_name -of "
            rf'default=noprint_wrappers=1:nokey=1 "{filename}"'
        )
        output = (
            subprocess.check_output(f"{opusCmd} && {command}", shell=True, cwd=fprobeDir)
            .decode("utf-8")
            .strip()
        )
        codec_type = output.split()
        codec = (codec_type[0])
        channels = (codec_type[1:])
        return codec, channels


def file_path_get(passed_input_path: str = paste()):
    """Defaults to paste() if no Args specified,
    if input is not a file opens finder window and
    converts to norm path

    returns normal path.
    """
    norm_file_path = os.path.normpath(passed_input_path)
    if not os.path.isfile(norm_file_path):
        return os.path.normpath(openFile())
    return norm_file_path


def saveSettings(key=None, value=None):
    """To save new Settings Must Pass via Args
    Args:
    key (str, optional=No Change):

    value (all, optional=No Change):
    """
    appdata_path = os.getenv("LOCALAPPDATA")

    settings_file = os.path.join(str(appdata_path),
                                 "Stream-Downloader-Util", "SDUsettings.json")

    with open(file=settings_file, mode="r") as f:
        settings = json.load(f)
    if key is not None and value is not None:
        settings[key] = value
        LastSave = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        settings["LastSave"] = LastSave
    with open(file=settings_file, mode="w") as f:
        json.dump(settings, f, indent=4)


def loadSettings(keys: list[str]) -> list[str]:
    """iF Known pass in via Args the Key
    you want to know the Value of to call
    Keys must be in a "string"

    '[LastSave]' = last save date
    """
    if keys is None:
        keys = []

    # Get the path to the local AppData folder.
    appdata_path = os.getenv("LOCALAPPDATA")

    # Define the path to the settings file
    settings_file = os.path.join(str(appdata_path),
                                 "Stream-Downloader-Util", "SDUsettings.json")
    answers = []
    for key in keys:
        # Load settings from the file
        with open(settings_file, "r") as f:
            settings = json.load(f)
            # Return the value associated with the key if a key is provided
            answer = settings.get(key, None) if key is not None else settings
            answers.append(answer)

    return answers


def is_less_than_30days(datetime1st):
    """Must pass 1 (Past) Date Time in as STR
    %d/%m/%Y %H:%M:%S

    True=<30d
    False=>30d"""
    datetimeNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    datetime1 = datetime.strptime(datetimeNow, "%d/%m/%Y %H:%M:%S")
    datetime2 = datetime.strptime(datetime1st, "%d/%m/%Y %H:%M:%S")

    # Calculate the difference between the two dates
    difference = abs(datetime2 - datetime1)

    # Check if the difference is greater than 30 days
    return difference < timedelta(days=30)


def kill_process(process):
    try:
        parent = psutil.Process(process.pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()
        print("Subprocess killed")
    except psutil.NoSuchProcess as e:
        print("Subprocess already closed")


def wait_for_subprocess(process):
    process.wait()
    # Run some code after the subprocess has completed


def get_download_links(keys: list[str]):
    appdata_path = os.getenv("LOCALAPPDATA")
    links_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "download_links.txt")
    answers = []
    for key in keys:
        with open(links_file, "r") as f:
            settings = json.load(f)
            answer = settings.get(key, None) if key is not None else settings
            # answers.append(answer)
    return answer


def ffprobepath_download_an_unzip():
    """calls dldURL() and Unzip() with all info inside"""

    url = get_download_links(["FFPROBE_Link"])
    last_segment = url.split('/')[-1]

    dloadFilePath = os.path.join(os.path.expanduser("~\\Desktop"),
                                 f"{last_segment}")

    dlmssg = (
        "\n---------------Downloading ffprobe from OFFICIAL FFMPEG "
        "link (45mb - 110mb Extracted) "
        " LINK >>> https://ffbinaries.com/downloads <<<"
        f"---------------\n ----------------to {dloadFilePath} "
        "and will auto extract to C:\\ffmpeg\\ ------------------\n"
    )
    save_Dir = "C:\\ffmpeg\\"
    spefFile = "ffprobe.exe"
    zipmssg = "\nSent .zip to Recycle Bin (no longer required)\n"

    dld = download_url(url, dloadFilePath, dlmssg)
    zp = unzip_file_from_path(dloadFilePath, "C:\\ffmpeg\\", spefFile, mssg=zipmssg)
    if dld and zp == True:
        Fprobe_Path = ("C:\\ffmpeg\\ffprobe.exe")
        saveSettings("ffprobepath", Fprobe_Path)
        return Fprobe_Path

    return f"{save_Dir}ffmpeg.exe"


def ffmpegpath_download_an_unzip():
    """calls dldURL() and Unzip() with all info inside"""

    urlmpg = get_download_links(["FFMPEG_Link"])
    last_segment = urlmpg.split('/')[-1]

    dloadFilePath = os.path.join(os.path.expanduser("~\\Desktop"),
                                    f"{last_segment}")

    dlmssg = (
        "\n---------------Downloading ffmpeg from OFFICIAL FFMPEG "
        "link (45mb - 110mb Extracted) LINK >>> "
        "https://ffbinaries.com/downloads <<<---------------\n "
        f"----------------to {dloadFilePath} "
        "and will auto extract to C:\\ffmpeg\\ ------------------\n"
    )
    save_Dir = "C:\\ffmpeg\\"
    spefFile = "ffmpeg.exe"
    zipmssg = "\nSent .zip to Recycle Bin (no longer required)\n"

    dld = download_url(urlmpg, dloadFilePath, dlmssg)
    zp = unzip_file_from_path(dloadFilePath, save_Dir, spefFile, zipmssg)
    if dld and zp == True:
        ffm_Path = ("C:\\ffmpeg\\ffmpeg.exe")  # only needs the dir to cmd into
        saveSettings("ffmpegpath", ffm_Path)
        return ffm_Path

    return f"{save_Dir}ffmpeg.exe"


def ffmpeg_factory_init(callback_info: list[str]):
    '''callback_info is module then the parent function from calling
    ["Main", "main_script"]'''

    default_ffPath = ("C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe")
    saveTo1 = "ffmpegpath"
    exename = "ffmpeg.exe"

    init_factory = DefaultPathFactory(
        default_Path=default_ffPath,
        settings_save_Key=saveTo1,
        extension_name_Lookup=exename,
        parent_func_Callback=callback_info
    )
    return init_factory.set_default_path()


def ffprobe_factory_init(callback_info: list[str]):
    '''callback_info is module then the parent function from calling
    ["Main", "main_script"]'''

    default_ffprobePath = ("C:\\ffmpeg\\ffprbe.exe")
    saveTo = "ffprobepath"
    exename = "ffprobe.exe"

    init_factory = DefaultPathFactory(
        default_Path=default_ffprobePath,
        settings_save_Key=saveTo,
        extension_name_Lookup=exename,
        parent_func_Callback=callback_info
    )
    return init_factory.set_default_path()


def streamlink_factory_init(callback_info: list[str]):
    '''callback_info is module then the parent function from calling
    ["Main", "main_script"]'''

    default_slinkPath = ("C:\\Program Files\\Streamlink\\bin\\streamlink.exe")
    saveTo = "streamlinkPath"
    exename = "streamlink.exe"

    init_factory = DefaultPathFactory(
        default_Path=default_slinkPath,
        settings_save_Key=saveTo,
        extension_name_Lookup=exename,
        parent_func_Callback=callback_info
    )
    return init_factory.set_default_path()


def manual_shutdown_timer():
    time = input(
        "\nEnter the time until shutdown in the format '1h &/or 45m'"
        " (EG: 1h, 1h 45m or 45m)\nTo cancel "
        "the shutdown command if necessary\nOpen a "
        "Windows Command Prompt Or Shell\nand type "
        "[shutdown -a] without Brackets [] then enter to Cancel: "
    )

    time = time.split()

    hours = 0
    minutes = 0

    for t in time:
        if 'h' in t:
            hours = int(t.replace('h', ''))
        elif 'm' in t:
            minutes = int(t.replace('m', ''))

    seconds = (hours * 3600) + (minutes * 60)
    os.system(f"shutdown -s -t {seconds}")
    print(f"Shutdown in {seconds} seconds")


def parse_url_twitch(url):
    urlparsed = urlparse(url)
    if not urlparsed.path.split('/')[-1].isnumeric():
        return urlunparse(urlparsed), urlparsed
    if urlparsed.query.startswith(('t=', 'acmb=')):
        return url, urlparsed
    elif urlparsed.query.startswith('filter='):
        new_url_parts = (urlparsed.scheme, urlparsed.netloc, urlparsed.path, '', '', '')
        return urlunparse(new_url_parts), urlparsed
    else:
        return url, urlparsed
