# import tkinter as tk
# from tkinter import filedialog
# import os
# import sys
# import time

# def saveFile():
#     """Opens: Save File Explorer

#     Returns:
#     Save Path
#     """
#     print("Save File To:... \n")
#     root = tk.Tk()
#     root.withdraw()
#     filep = filedialog.asksaveasfilename(defaultextension='.mp4',
#                                          filetypes=[
#                                              ("MP4 files", ".mp4"),
#                                              ("MOV files", ".mov"),
#                                              ("MKV files", ".mkv"),
#                                              ("MP4 files", ".mp3"),
#                                              ("All files", ".*"),
#                                          ])
#     root.destroy()
#     file = os.path.normpath(filep)

#     return file

# print(saveFile())


import funcs, os

def setLink_Path(find_ffmpeg = False):
    """Check if Streamlink or FFmpeg is installed on the user's system.

    Args:
        find_ffmpeg (bool): If True, check for FFmpeg instead of Streamlink.

    Returns:
        str: The path to the Streamlink or FFmpeg installation, or False if 
        not found.
    """
    if (funcs.loadSettings("streamlinkPath") or funcs.isMoreThan30days(funcs.loadSettings('LastSave'))):
        pass
    else: return os.path.dirname(funcs.loadSettings("streamlinkPath"))
    print("passeed")
print(setLink_Path())