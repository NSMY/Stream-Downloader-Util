import os
from urllib.parse import urlparse
# import re
# import subprocess
import sys
import time
# import webbrowser
from tkinter import filedialog
import inquirer
# from pyperclip import copy, paste
import cpyVid_scritp_____1 as cpvs


    # checks path ----
# def setLink_Path():
#     stlink = []
#     stlink.append(os.path.isfile("C:\\Program Files\Streamlink\\bin\\streamlink.exe"))
#     stlink.append(os.path.isfile("C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"))
#     if (stlink[0]) == True:
#         lnk_pth = "C:\\Program Files\\Streamlink\\bin\\"
#         return lnk_pth
#     elif (stlink[1]) == True:
#         lnk_pth = "C:\\Program Files (x86)\\Streamlink\\bin\\"
#         return lnk_pth            
#     else:
#         print("Streamlink path not Found...\n")    
#         return



def setLink_Path():
    paths = ["C:\\Program Files\\Streamlink\\bin\\streamlink.exe",
                "C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"]
    for path in paths:
        if os.path.isfile(path):
            return os.path.dirname(path)
    print("Streamlink path not Found...\nPlease Find streamlink.exe...."
            "EG path (Streamlink\\bin\\streamlink.exe)")
    fpath = openFile().replace("/streamlink.exe", "")
    return fr'{fpath}'

def is_url(variable):
    try:
        result = urlparse(variable)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def has_ffmpeg_dir(stream_lnk_Path):
    store_path = os.path.join(os.path.dirname(stream_lnk_Path), "ffmpeg")
    return os.path.isdir(store_path)

def openFile():
    # print("Open File From:... \n")
    file = filedialog.askopenfilename(defaultextension=".*",
                                    filetypes=[
                                        ("All files", ".*"),
                                        ("MP4 files", ".mp4"),
                                        ("MOV files", ".mov"),
                                        ("EXE files", ".exe"),
                                    ])
    if len(file) == 0: #closes Program if No Save path is Entered
        check = mChoiseQeustion("Canceled File Finder: Try again?", ["yes", "no"])
        if check == "yes":
            openFile()
        else:
            print("Exiting...")
            time.sleep(3)
            sys.exit ()
    return file

def mChoiseQeustion(mssg, chois):
    questions = [
        inquirer.List(
            "Key",
            message=mssg,
            choices=chois,
        ),
    ]
    answer = inquirer.prompt(questions)
    qstnStrRtn = ''.join([str(value) for value in answer.values()])
    return qstnStrRtn

def saveFile():
    print("\nSave File To:... \n")
    file = filedialog.asksaveasfilename(defaultextension='.mp4',
                                        filetypes=[
                                            ("MP4 files",".mp4"),    
                                            ("MOV files",".mov"),    
                                            ("All files",".*"),
                                        ])
    if len(file) == 0: #closes Program if No Save path is Entered
        check = mChoiseQeustion("Canceled Save: Try again?", ["yes", "no"])
        if check == "yes":
            saveFile()
        else:
            print("Exiting...")
            time.sleep(3)
            sys.exit ()
    return (file)