import json
import os
import subprocess
import sys
import time
import tkinter as tk
import winsound
import zipfile
from datetime import datetime, timedelta
from tkinter import filedialog
from urllib.parse import urlparse

import inquirer
import psutil
import requests
from pyperclip import copy, paste
from send2trash import send2trash
from tqdm import tqdm

import Main
from default_path_factory import DefaultPathFactory

video_file_types = [".mp4", ".mov", ".mkv", ".ts",]

def make_new_dir_from_input(input_file_path:str , new_dir_name_arg: str)-> str:
    '''Makes a directory from the input file path
    inline with input_file_path'''
    file_path_2 = os.path.dirname(input_file_path)
    new_folder_combine_path = os.path.join(file_path_2, new_dir_name_arg)
    
    if not os.path.exists(new_folder_combine_path):
        os.makedirs(new_folder_combine_path)
    return os.path.join(new_folder_combine_path)


def video_file_exe_return(filename: str) -> str:
    '''Returns the .extension if in video_file_types
    otherwise returns empty string'''
    for file_type in video_file_types:
        if filename.endswith(file_type):
            print(file_type)
            return file_type
    return ""


# def ffmpeg_path_set(): # FIX make abstract.

#     # Check if ffmpeg is installed in the default location
#     default_ffPath = "C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe"
#     if os.path.isfile(default_ffPath):
#         saveSettings("ffmpegpath", default_ffPath)
#         return default_ffPath

#     # Search for the ffmpeg executable
#     ffmpegpath = file_search("ffmpeg.exe")
#     if ffmpegpath:
#         saveSettings("ffmpegpath", ffmpegpath)
#         return ffmpegpath

#     # Download and unzip the ffmpeg executable
#     ffmpegpath = execute_or_setting(DL_unZip_ffmpeg, key="ffmpegpath")
#     os.system("cls")
#     from cpyVid_scritp_____1 import mux
#     mux()
    
#     if ffmpegpath:
#         saveSettings("ffmpegpath", ffmpegpath)
#         return ffmpegpath


# def setLink_Path(find_ffmpeg = False):
#     """Check if Streamlink or FFmpeg is installed on the user"s system.

#     Args:
#         find_ffmpeg (bool): If True, check for FFmpeg instead of Streamlink.

#     Returns:
#         str: The path to the Streamlink or FFmpeg installation, or False if 
#         not found.
#     """
#     if (loadSettings("streamlinkPath")
#         is None or isMoreThan30days(loadSettings("LastSave"))):
#         print("pass")
#     else: return os.path.dirname(loadSettings("streamlinkPath"))
    
#     # Define the paths to check for Streamlink
#     streamlink_paths = [
#         "C:\\Program Files\\Streamlink\\bin\\streamlink.exe",
#         "C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"
#     ]

#     # Check if Streamlink is installed at one of the defined paths
#     for path in streamlink_paths:
#         if os.path.isfile(path) and find_ffmpeg == False:
#             saveSettings("streamlinkPath", path)
#             return os.path.dirname(path)
#         elif not path:
#             streamlink_path = file_search("streamlink.exe")
#             if streamlink_path and find_ffmpeg == False:
#                 saveSettings("streamlinkPath", streamlink_path)
#                 return os.path.dirname(streamlink_path)
    
    # # If find_ffmpeg is True, check for FFmpeg
    # if find_ffmpeg:
    #     slinkFFMPEG = os.path.isfile(streamlink_paths[0].replace(
    #                 "\\bin\\streamlink.exe", "\\ffmpeg\\ffmpeg.exe"))
    #     if slinkFFMPEG:
    #         ffmpg = os.path.dirname(streamlink_paths[0].replace(
    #                 "\\bin\\streamlink.exe", "\\ffmpeg\\ffmpeg.exe"))
    #         saveSettings("ffmpegpath", ffmpg)
    #         return ffmpg
    #     if not slinkFFMPEG:
    #         ffmpeg_path = os.path.dirname(file_search("ffmpeg.exe")) # type: ignore fixed in OpenFile
    #         saveSettings("ffmpegpath", ffmpeg_path)
    #         return ffmpeg_path
    #     else:
    #         ffmpeg_path = DL_unZip_ffmpeg()
    #         saveSettings("ffmpegpath", ffmpeg_path)
    #         return ffmpeg_path
            
    # return False


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

#NOTE is needed?
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
    root.withdraw()
    filep = filedialog.askopenfilename(defaultextension=".*",
                                    filetypes=[
                                        ("All files", ".*"),
                                        ("MP4 files", ".mp4"),
                                        ("MOV files", ".mov"),
                                        ("EXE files", ".exe"),
                                    ])
    root.destroy()
    file = os.path.normpath(filep)
    if not filep: #closes Program if No Save path is Entered
        check = multi_choice_dialog("Canceled Open File: Try again?", 
                                    ["yes", "no", "exit"])
        if check == "yes":
            os.system("cls" if os.name == "nt" else "clear")
            openFile()
        elif check == "no":
            os.system("cls" if os.name == "nt" else "clear")
            Main.main_script()
        sys.exit()
    return file


def saveFile():
    """Opens: Save File Explorer
    
    Returns:
        Save Path
    """
    print("Save File To:... \n")
    root = tk.Tk()
    root.withdraw()
    filep = filedialog.asksaveasfilename(defaultextension=".mp4",
                                        filetypes=[
                                            ("MP4 files",".mp4"),    
                                            ("MOV files",".mov"),    
                                            ("MKV files",".mkv"),    
                                            ("MP4 files",".mp3"),    
                                            ("All files",".*"),
                                        ])
    root.destroy()
    file = os.path.normpath(filep)
    if not filep: #closes Program if No Save path is Entered
        check = multi_choice_dialog("Canceled Save Path: Try again?",
                                    ["yes", "no", "exit"])
        if check == "yes":
            os.system("cls" if os.name == "nt" else "clear")
            saveFile()
        elif check == "no":
            os.system("cls" if os.name == "nt" else "clear")
            Main.main_script()
        sys.exit ()
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
        with open(dloadFilePath, "wb") as f:
            for data in tqdm(response.iter_content(block_size), 
                                total=total_size//block_size, unit="KB"):
                
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


def unzip_file_from_path(zip_file_path,
                        outputDir,
                        specific_filename_to_extract: str = "",
                        mssg = ""
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
            with zipfile.ZipFile(zip_file, "r") as zf:
                if specific_filename_to_extract:
                    zf.extract(specific_filename_to_extract, output_dir)
                zf.extractall(output_dir)
                print(f"\nSuccessful Extraction To {output_dir}")
        except Exception:
            print(f"\n\nERROR: Could not extract {zip_file_path} \n")
            fldr = zip_file_path.replace(specific_filename_to_extract,"")
            return os.startfile(fldr)
        if (os.path.isfile(zip_file_path)
            and os.path.isfile(f"{outputDir}\\{specific_filename_to_extract}")
            ):
            send_to_trash(zip_file_path)
            return True
    return True


def send_to_trash(filename):
            send2trash(filename)
            if not os.path.isfile(filename):
                print(f"sent {filename} to recycler")
                winsound.PlaySound("C:\\Windows\\Media\\Recycle.wav",
                                    winsound.SND_FILENAME)
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
    directories = (["C:\\ffmpeg\\", "C:\\Program Files", "C:\\Program Files (x86)"] 
                    + [os.path.expanduser(f"~\\AppData\\{subDir}") 
                        for subDir in appDataSubDirs]
                    )
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



"""
def channelsSplit(fprobeDir, filename):
    
    pathDir = os.path.dirname(fprobeDir)
    
    if pathDir:
        command = (f"ffprobe -v error -show_entries stream=index"
                    fr" -select_streams a -of csv=p=0 "{filename}"")
        opusCmd = (f"ffprobe -v error -select_streams a:0 -show_entries "
                "stream=codec_name -of "
                fr"default=noprint_wrappers=1:nokey=1 "{filename}"")

        output = (subprocess.check_output(command, shell=True, cwd=pathDir)
                    .decode("utf-8").strip())
        opus = (subprocess.check_output(opusCmd, shell=True, cwd=pathDir)
                    .decode("utf-8").strip())
        
        audChannels = output.split() 
        return audChannels, opus
        
    else:
        print(f"\nCould Not Find "{fprobeDir}" on your Computer\n")
        while True:
            try:
                audChannels = int(input(f"Couldn"t Auto retrieve Maximum"
                                        "number of Audio Channels, How Many "
                                        "Channels does {filename} have?:"))
                break
            except ValueError:
                print("Please enter a numerical value(int) EG: 3.")

        channels_list = []
        for i in range(1, audChannels+1):
            channels_list.append(i)
        return channels_list"""

def channelsSplit(fprobeDir, filename):
    
    if pathDir := os.path.dirname(fprobeDir):
        return _extracted_from_channelsSplit_(filename, pathDir)
    print(f"\nCould Not Find '{fprobeDir}' on your Computer\n")
    while True:
        try:
            audChannels = int(
                input(
                    f"Couldn't Auto retrieve Max Num of A/Channels, "
                        f"How Many Channels does {filename} have?:"))
            break
        except ValueError:
            print("Please enter a numerical value(int) EG: 3.")

    return list(range(1, audChannels+1))


# TODO Rename this here and in `channelsSplit`
def _extracted_from_channelsSplit_(filename, pathDir):
    command = (f"ffprobe -v error -show_entries stream=index"
                fr" -select_streams a -of csv=p=0 '{filename}'")
    opusCmd = (f"ffprobe -v error -select_streams a:0 -show_entries "
            "stream=codec_name -of "
            fr"default=noprint_wrappers=1:nokey=1 '{filename}'")

    output = (subprocess.check_output(command, shell=True, cwd=pathDir)
                .decode("utf-8").strip())
    opus = (subprocess.check_output(opusCmd, shell=True, cwd=pathDir)
                .decode("utf-8").strip())

    audChannels = output.split()
    return audChannels, opus



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


def initSettings():
    # Get the path to the local AppData folder
    appdata_path = os.getenv("LOCALAPPDATA")

    # Define the path to the settings file
    settings_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "SDUsettings.json")

    # Check if the settings file already exists
    if not os.path.exists(settings_file):
        # Create the directory if it doesn"t exist
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)
        
        LastSave = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Define the initial settings as a dictionary
        settings = {
            "ExamplePath": "/path/to/file",
            "Example_feature": True,
            "Initialize": True,
            "LastSave": LastSave,
        }
        # Save the initial settings to the file
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)


def saveSettings(key = None, value = None):
    """To save new Settings Must Pass via Args
    Args:
    key (str, optional=No Change):
    
    value (all, optional=No Change):
    """
    initSettings()

    appdata_path = os.getenv("LOCALAPPDATA")

    settings_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "SDUsettings.json")
    
    with open(settings_file, "r") as f:
        settings = json.load(f)
        
    if key is not None and value is not None:
        settings[key] = value
        LastSave = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        settings["LastSave"] = LastSave
        
    with open(settings_file, "w") as f:
        json.dump(settings, f, indent=4)


def loadSettings(key = None):
    """iF Known pass in via Args the Key 
    you want to know the Value of to call
    Keys must be in a "string"
    
    LastSave = last save date
    """
    # Initialize the settings file with initial values if it doesn"t exist
    initSettings()

    # Get the path to the local AppData folder.
    appdata_path = os.getenv("LOCALAPPDATA")

    # Define the path to the settings file
    settings_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "SDUsettings.json")

    # Load settings from the file
    with open(settings_file, "r") as f:
        settings = json.load(f)

    # Return the value associated with the key if a key is provided
    return settings.get(key, None) if key is not None else settings


def isMoreThan30days(datetime1st):
    """Must pass 1 (Past) Date Time in as STR
    %d/%m/%Y %H:%M:%S
    
    True=>30d
    False<30d"""
    datetimeNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    datetime1 = datetime.strptime(datetimeNow, "%d/%m/%Y %H:%M:%S")
    datetime2 = datetime.strptime(datetime1st, "%d/%m/%Y %H:%M:%S")

    # Calculate the difference between the two dates
    difference = abs(datetime2 - datetime1)

    # Check if the difference is greater than 30 days
    return difference > timedelta(days=30)


def execute_or_setting(command, args = (), key = ""):
    """Executes a command if the "LastSave" setting is more than 30 days old
or if the path loaded from the settings using the key is None. Otherwise, 
returns the value loaded from the settings using the key.
    
    Args:
        command (function): The command to be executed without ().
        
        args for the func (tuple, optional): If need (True,) or ("string",)
        EG (funcs.setLink_Path, (True,), "ffmpegpath")
        
        key (str, optional): Key used to load the path from the settings.
        
    Returns:
        The result of executing the command or the value loaded from
        the settings using the
    """
    ls = loadSettings("LastSave")
    longer = isMoreThan30days(ls)
    path = loadSettings(key)

    if longer == True or path is None:
        return command(*args)
    elif longer == False:
        return loadSettings(key)
    


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
    
    
    
    
    
    
####################################################
def ffprobepath_download_an_unzip():
    """calls dldURL() and Unzip() with all info inside"""
    
    dloadFilePath = os.path.join(os.path.expanduser("~\\Desktop"),
                                "ffprobe-4.4.1-win-64.zip")

    url = ("https://github.com/ffbinaries/ffbinaries-prebuilt/releases/"
            "download/v4.4.1/ffprobe-4.4.1-win-64.zip")

    dlmssg = ("\n---------------Downloading ffprobe from OFFICIAL FFMPEG "
                "link (45mb - 110mb Extracted) "
                " LINK >>> https://ffbinaries.com/downloads <<<"
                f"---------------\n ----------------to {dloadFilePath} "
                "and will auto extract to C:\\ffmpeg\\ ------------------\n")

    save_Dir = "C:\\ffmpeg\\"
    spefFile = "ffprobe.exe"
    zipmssg = "\nSent .zip to Recycle Bin (no longer required)\n"
    
    dld = download_url(url, dloadFilePath, dlmssg)
    zp = unzip_file_from_path(dloadFilePath, "C:\\ffmpeg\\", spefFile, zipmssg)
    if dld and zp ==True:
        Fprobe_Path = ("C:\\ffmpeg\\ffprobe.exe")
        saveSettings("ffprobepath", Fprobe_Path)
        return Fprobe_Path
    
    return f"{save_Dir}ffmpeg.exe"


def ffmpegpath_download_an_unzip():
    """calls dldURL() and Unzip() with all info inside"""
    
    urlmpg = ("https://github.com/ffbinaries/ffbinaries-prebuilt/"
                "releases/download/v4.4.1/ffmpeg-4.4.1-win-64.zip")

    dloadFilePath = os.path.join(os.path.expanduser("~\\Desktop"),
                                    "ffmpeg-4.4.1-win-64.zip")

    dlmssg = ("\n---------------Downloading ffmpeg from OFFICIAL FFMPEG "
                "link (45mb - 110mb Extracted) LINK >>> "
                "https://ffbinaries.com/downloads <<<---------------\n "
                f"----------------to {dloadFilePath} "
                "and will auto extract to C:\\ffmpeg\\ ------------------\n")
    save_Dir = "C:\\ffmpeg\\"
    spefFile = "ffmpeg.exe"
    zipmssg = "\nSent .zip to Recycle Bin (no longer required)\n"
    
    dld = download_url(urlmpg, dloadFilePath, dlmssg)
    zp = unzip_file_from_path(dloadFilePath, save_Dir, spefFile, zipmssg)
    if dld and zp ==True:
        ffm_Path = ("C:\\ffmpeg\\ffmpeg.exe") #only needs the dir to cmd into
        saveSettings("ffmpegpath", ffm_Path)
        return ffm_Path

    return f"{save_Dir}ffmpeg.exe"




##############################################################################################
def ffmpeg_factory_init(callback_info: list[str]):
    '''callback_info is module then the parent function from calling
    ["Main", "main_script"]'''
    
    default_ffPath = ("C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe")
    saveTo1 = "ffmpegpath"
    exename = "ffmpeg.exe"

    init_factory = DefaultPathFactory(default_ffPath, saveTo1, exename, callback_info)
    return init_factory.set_default_path()


def ffprobe_factory_init(callback_info: list[str]):
    '''callback_info is module then the parent function from calling
    ["Main", "main_script"]'''

    default_ffprobePath = ("C:\\ffmpeg\\ffprbe.exe")
    saveTo = "ffprobepath"
    exename = "ffprobe.exe"

    init_factory = DefaultPathFactory(default_ffprobePath, saveTo, exename, callback_info)
    return init_factory.set_default_path()


def streamlink_factory_init(callback_info: list[str]):
    '''callback_info is module then the parent function from calling
    ["Main", "main_script"]'''

    default_slinkPath = ("C:\\Program Files\\Streamlink\\bin\\streamlink.exe")
    saveTo = "streamlinkPath"
    exename = "streamlink.exe"

    init_factory = DefaultPathFactory(default_slinkPath, saveTo, exename, callback_info)
    return init_factory.set_default_path()

