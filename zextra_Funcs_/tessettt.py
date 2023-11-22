
# def create_popup(content):
#     popup = tk.Tk()
#     popup.title("Popup Window")
#     listbox = tk.Listbox(popup)
#     for key, value in content.items():
#         listbox.insert(tk.END, f"{key}: {value}")
#     listbox.pack()
#     button = tk.Button(popup, text="Close", command=popup.destroy)
#     button.pack()
#     # Update the window to calculate the size of the content
#     popup.update_idletasks()
#     # Get the width and height of the content
#     width = popup.winfo_width()
#     height = popup.winfo_height()
#     # Add some padding
#     width += 80
#     height += 80
#     # Set the window size
#     popup.geometry(f"{width}x{height}")
#     popup.mainloop()

# ffmpeg -i "C:\Users\970EVO-Gamer\Desktop\Jason Parris X My Buddy Mike ft. Neon Hitch - No Warning.mp3" -c copy "C:\Users\970EVO-Gamer\Desktop\Jason Parris X My Buddy Mike ft. Neon Hitch - No Warning.wav"  

import ctypes
import json
import os
import pprint
import re
import subprocess
import timeit
import tkinter as tk
from re import L, split
from subprocess import PIPE, Popen
from turtle import title
from urllib.parse import urlparse

# for loop to get all sizes of vids in dir.
choseendir = 'E:/DeleteStreams/FFMPEG__re-Muxed/'
for files in os.listdir(choseendir):
    # print(files)
    fp = os.path.join(choseendir, files)
    # print("🐍 File: new_mass_gql/tessettt.py | Line: 368 | undefined ~ fp",fp)

    dldVid_sizs = subprocess.Popen(
        rf'ffprobe -i "{fp}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        cwd='c:/ffmpeg/'
    )
    stdout, stderr = dldVid_sizs.communicate()
    out_pt, _ = dldVid_sizs.communicate()
    dldVid_sizs.wait()
    files = files.split('-')
    print(f'{out_pt.split('.')[0]}  {files}')
    
# result = re.sub(r"[^\w\s]", "", out_pt).split()[10:]


# cmdd = r"C:/Program Files/Streamlink/ffmpeg/"
# process = subprocess.Popen(r'streamlink https://www.twitch.tv/videos/1981304674 worst --hls-segment-threads 5 -o "C:\Users\970EVO-Gamer\Desktop\junkme.mp4"', stdout=subprocess.PIPE, universal_newlines=True,  cwd=cmdd)
# # stdout, stderr = process.communicate()
# line = ''
# while True:
#     char = process.stdout.read(1)
#     if char == '\n' or char == '\r':
#         print(line)
#         line = ''
#     else:
#         line += char
#     if '[cli][info] Stream ended' in line:
#         print("success")
#     if process.poll() is not None:
#         break

'''# stdout, stderr = process.communicate()
for line in iter(process.stdout.readline, ''):
    print(line.rstrip())
    if '[download]' in line.rstrip():
        print('Downloading file')
'''


# dd ='[cli][info] Closing currently open stream...'
# if "Closing " in dd:
#     print('True')
# if "Closing " not in dd:
#     print('False')
# url = 'https://www.twitch.tv/videos/1981192341?filter=archives&sort=time'

# if (url := urlparse(url).path.rsplit('/')[-1]).isnumeric():
# # (url := url.split('/', -1))
#     print(url)