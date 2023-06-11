# import json
# import os
# import subprocess
# import sys
# import time
# import tkinter as tk
# import winsound
# import zipfile
# from datetime import datetime, timedelta
# from tkinter import filedialog
# from urllib.parse import urlparse

# import inquirer
# import psutil
# import requests
# from pyperclip import copy, paste
# from send2trash import send2trash
# from tqdm import tqdm

# import funcs
# from funcs import download_url, file_search, saveSettings, unzip_file_from_path


# def DL_unZip_ffmpeg():
#     """calls dldURL() and Unzip() with all info inside"""
    
#     urlmsg = ("https://github.com/ffbinaries/ffbinaries-prebuilt/"
#                 "releases/download/v4.4.1/ffmpeg-4.4.1-win-64.zip"
#             )
#     dloadFilePath = os.path.join(os.path.expanduser("~\\Desktop"),
#                                     "ffmpeg-4.4.1-win-64.zip"
#                                 )
#     dlmssg = ("\n---------------Downloading ffmpeg from OFFICIAL FFMPEG "
#                 "link (45mb - 110mb Extracted) LINK >>> "
#                 "https://ffbinaries.com/downloads <<<---------------\n "
#                 f"----------------to {dloadFilePath} "
#                 "and will auto extract to C:\\ffmpeg\\ ------------------\n"
#             )
#     dld = download_url(urlmsg, dloadFilePath, dlmssg)
#     zp = unzip_file_from_path(dloadFilePath, "C:\\ffmpeg\\", "ffmpeg.exe")
#     fpath = os.path.dirname(file_search("ffmpeg.exe")) 
    
#     if dld and zp ==True:
#         ffm_Path = ("C:\\ffmpeg\\") #only needs the dir to cmd into
#         saveSettings("ffmpegpath", ffm_Path)
#         return ffm_Path
    
#     return fpath


# import funcs
# from funcs import (ffmpegpath_download_an_unzip, program_Path_Details,
#                    shorten_path_name)

# settings_Key = "ffmpegpath"
# dld = "_download_an_unzip"
# func_name = self.settings_Key + dld
# func = getattr(funcs, func_name)
# func()


import os
# # print(getattr(settings_Key, dld))
import tkinter as tk

new_file_path = "E:\\DeleteStreams\\New folder\\FFMPEG__re-Muxed"

def open_directory_Force_front(full_path: str):
    # root = tk.Tk()
    # root.withdraw()
    path = os.path.dirname(full_path)
    os.startfile(os.path.realpath(path))
    # root.destroy()
open_directory_Force_front(new_file_path)