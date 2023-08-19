import json
import os
import shutil
from datetime import datetime, timedelta

import funcs

version_number = 3.2

def initSettings():
    appdata_path = os.getenv("LOCALAPPDATA")

    settings_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "SDUsettings.json")

    # Check if the settings file already exists
    if not os.path.exists(settings_file):
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)
        
        LastSave = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        settings = {
            "Twitch_snippet_for_auth": 'document.cookie.split("; ").find(item=>item.startsWith("auth-token="))?.split("=")[1]',
            "SDLI_Version": version_number,
            "Initialize": True,
            "LastSave": LastSave,
        }
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)


def init_links_file():
    appdata_path = os.getenv("LOCALAPPDATA")
    links_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "download_links.txt")

    # Check if the settings file already exists
    if not os.path.exists(links_file):
        os.makedirs(os.path.dirname(links_file), exist_ok=True)
        
        Links = {
        "_comment": "If this File is Updated in Github you can update it without needing to download a new version of the App.",
        "_comment2": "Just replace this file with the updated one in Github. File Location C_Users_USERNAME_AppData_Local_Stream_Downloader-Util_download_Links.txt",
        "_comment3": "https://github.com/NSMY/Stream-Downloader-Util",
        "_Version": "1.0",
        "FFMPEG_Link": "https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v4.4.1/ffmpeg-4.4.1-win-64.zip",
        "FFPROBE_Link": "https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v4.4.1/ffprobe-4.4.1-win-64.zip",
        "STREAMLINK_Link": "https://github.com/streamlink/windows-builds/releases/latest"
        }
        with open(links_file, "w") as f:
            json.dump(Links, f, indent=4)


def version_check():
    appdata_path = os.getenv("LOCALAPPDATA")
    settings_dir = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util")

    try:
        funcs.loadSettings(["SDLI_Version"])
    except FileNotFoundError as e:
        initSettings()
        init_links_file()

    try:
        if funcs.loadSettings(["SDLI_Version"]) != [version_number]:
            print('Settings Files Deleted, Outdated Version')
            shutil.rmtree(settings_dir)
            # funcs.send_to_trash(settings_dir)
            funcs.main_start()
    except PermissionError as f:
        # print("Permission error")
        funcs.main_start()