import ctypes
import json
import os
import pprint
import re
import subprocess
import sys
import timeit
import tkinter as tk
from pathlib import Path
from re import L, split
from subprocess import PIPE, Popen
from turtle import title
from urllib.parse import urlparse

from numpy import append, size

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

# # for loop to get all sizes of vids in dir.
# choseendir = 'E:/DeleteStreams/FFMPEG__re-Muxed/'
# for files in os.listdir(choseendir):
#     # print(files)
#     fp = os.path.join(choseendir, files)
#     # print("🐍 File: new_mass_gql/tessettt.py | Line: 368 | undefined ~ fp",fp)

#     dldVid_sizs = subprocess.Popen(
#         rf'ffprobe -i "{fp}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
#         shell=False,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         universal_newlines=True,
#         cwd='c:/ffmpeg/'
#     )
#     stdout, stderr = dldVid_sizs.communicate()
#     out_pt, _ = dldVid_sizs.communicate()
#     dldVid_sizs.wait()
#     files = files.split('-')
#     print(f'{out_pt.split('.')[0]}  {files}')

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
'''
# stdout, stderr = process.communicate()
for line in iter(process.stdout.readline, ''):
    print(line.rstrip())
    if '[download]' in line.rstrip():
        print('Downloading file')
'''

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

# # tk gui
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# from new_mass_gql.tk_get_file_list import call_tk_vod_view

# print(call_tk_vod_view('C:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/shenryyr.json'))
'''





playn

# # listbox = A listing of selectable text items within it's own container


# def submit():
#     food = []

#     for index in listbox.curselection():
#         food.insert(index, listbox.get(index))

#     print("You have ordered: ")

#     for index in food:
#         print(index)


# def add():
#     listbox.insert(listbox.size(), entryBox.get())

#     listbox.config(height=listbox.size())


# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)

#     listbox.config(height=listbox.size())

# # import tkinter
# from tkinter import *

# window = Tk()


# listbox = Listbox(
#     window, bg="#f7ffde", font=("Constantia", 35), width=12, selectmode=MULTIPLE
# )

# listbox.pack()


# listbox.insert(1, "pizza")

# listbox.insert(2, "pasta")

# listbox.insert(3, "garlic bread")

# listbox.insert(4, "soup")

# listbox.insert(5, "salad")


# listbox.config(height=listbox.size())


# entryBox = Entry(window)

# entryBox.pack()


# frame = Frame(window)

# frame.pack()


# submitButton = Button(frame, text="submit", command=submit)

# submitButton.pack(side=LEFT)


# addButton = Button(frame, text="add", command=add)

# addButton.pack(side=LEFT)


# deleteButton = Button(frame, text="delete", command=delete)

# deleteButton.pack(side=LEFT)


# window.mainloop()
while True:
    import tkinter
    from tkinter import Frame, ttk

    window = tkinter.Tk()
    window.geometry("480x480")

    frame = tkinter.Frame(window, bg='grey')
    frame.pack()

    # list = tkinter.Listbox(frame, selectmode="")

    tree = ttk.Treeview(frame)
    tree.pack()


    window.mainloop()