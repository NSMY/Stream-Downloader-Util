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
def get_reso_():
    loops = 0
    while loops < 5:
        loops += 1
        try:
            cmdd = r"C:/Program Files/Streamlink/ffmpeg/"
            process = subprocess.Popen(r'streamlink "https://www.twitch.tv/videos/2002087915"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=cmdd)
            # process = subprocess.Popen(r'streamlink "https://www.twitch.tv/videos/1957556164"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=cmdd)
            # process = subprocess.Popen(r'streamlink "https://www.youtube.com/watch?v=6PuXPxhf-Js"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=cmdd)
            # process = subprocess.Popen(r'streamlink "https://youtu.be/cvq7Jy-TFAU?list=PLbAqlIAMdRgtQkPnpqCoqZv1hi9xWnsgZ"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=cmdd)
    # stdout, stderr = process.communicate()





    # try:
    #     line = ''
    #     while True:
    #         char = process.stdout.read(1)
    #         if char in ['\n', '\r']:
    #             print(line)
    #             if 'error' in line:
    #                 print('Mine', line)
    #             line = ''
    #         else:
    #             line += char
    #         if '[cli][info] Stream ended' in line:
    #             print("Stream has Ended")
    #         if process.poll() is not None:
    #             break
    #     gg,gf = process.communicate()
    #     print(process,gg,gf)
    #     process.wait()
    # except Exception as e:
    #     err = str(e)
    #     raise PluginError(err) from None
    # stderr = ''
    # try:  
            process.wait()
            for line in iter(process.stdout.readline, ''):
                print(line.rstrip())
                if 'error: No play' in line.rstrip():
                    print('Error downloading file', line)
                    raise ValueError
                elif 'error: This plugin' in line.rstrip():
                    print('DMCA', line)
                    raise SyntaxError
                    # main_script()
                elif "Available streams:" in line:
                    result = re.sub(r"[^\w\s]", "", line).split()[2:]
                    print("🐍 File: zextra_Funcs_/tessettt.py | Line: 90 | undefined ~ result",result)
                    return result
                    # return queue.put(results)
                # elif '[download]' in line.rstrip():
                #     print('Downloading file')
            process.communicate()
            print("\nLikely Sub Only Vods Enabled")
            # print(process.stderr.read())
            raise OSError
        except SyntaxError:
            # print('OSError')
            return
        except OSError:
            print("put sub only code rhere")
        except ValueError:
            pass
            # print("ValueError")
    # except TypeError:
    #     print('Error downloading')
get_reso_()

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

'''



