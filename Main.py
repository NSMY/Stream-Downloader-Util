import os
import sys
import time
from pyperclip import copy, paste
import webbrowser
from tkinter import *
from tkinter import filedialog

#Retrieves Last item in Clipboard(ctrl v)
#clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
clp_brd = paste()  # text will have the content of clipboard
url_ = clp_brd.replace("?filter=archives&sort=time","")

#Runs Check if streamlink is installed and gives link/opens if Not
acptLst = ["yes", "y"]
check_in = 0
isthere = False
isthere_86 = False
while True:
    isthere = os.path.isfile(r"C:\Program Files\Streamlink\bin\streamlink.exe")
    isthere_86 = os.path.exists(r"C:\Program Files (x86)\Streamlink\bin\streamlink.exe")
    if check_in == 0 and isthere is False:
        if isthere_86 is False:
            print(f"\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe----\n")
            ipt_asw = input("Auto Launch Website?\ny/n?: ").lower()
            if ipt_asw in acptLst:
                webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
                check_in = +1
            else:            
                check_in = +1
                continue
        else:
            break
    elif check_in >= 0 and isthere is False:
        if isthere_86 is False:
            print("\nWaiting for Installation...")
            time.sleep(7)
            got_it = input("\nHas Streamlink been installed yet?\ny/n?:").lower()
            if got_it in acptLst and isthere is False or isthere_86 is False:
                lie_chk = input("\nHaven't Found Stream Link In File Path\nC.Program.Files.Streamlink.bin      Are you sure? y/n?:").lower()
            elif lie_chk not in acptLst:
                print("\nWaiting!......")
                time.sleep(20)
        else:
            break
    else:
        break

# choses directory of streamlink ----
if isthere is True:
    sLink_pth = r'C:\\Program Files\\Streamlink\\bin\\'
elif isthere_86 is True:
    sLink_pth = r'C:\\Program Files (x86)\\Streamlink\\bin\\'



#opens Windows Save Folder and stores chosen path
def saveFile():
    file = filedialog.asksaveasfilename(defaultextension='.mp4',
                                        filetypes=[
                                            ("MP4 files",".mp4"),    
                                            ("MOV files",".mov"),    
                                            ("All files",".*"),
                                        ])
    return (file)
file_path = saveFile()

if len(file_path) ==0: #closes Program if No Save path is Entered
    sys.exit ()

sizes = ["worst", "160p", "360p", "480p", "720p", "720p60", "1080p", "1080p60","160p30", "360p30", "480p30", "720p30", "720p30", "1080p30", "source", "best"]

#old Code
# name_of_File = input("Enter File Name:\n")
# file_path = fr'"E:\DeleteStreams\New folder\{name_of_File}.mp4"'

def check_size(Vid_size):
    # print(Vid_size in sizes) Checks if True/False
    if Vid_size in sizes:
        return fr'cd {sLink_pth} && streamlink "{url_}" {Vid_size} --hls-segment-threads 5 -o {file_path}'
    else:
        return ("Enter a Valid Size")     
Fake_ = ""
while True:
    if Fake_ == "":  
        Size_string = input("Please enter Resolution you want to download:\nworst, 160p, 360p, 480p, 720p, 720p60, 1080p60, source, best:\n").lower()  #stores Input into size_string Variable
        cmd_Str = check_size(Size_string)       #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
        Fake_ = "1"
    
    elif cmd_Str == "Enter a Valid Size":
        Size_string = input("Enter a Valid Size: worst, 160p, 360p, 480p, 720p, 720p60, 1080p60, source, best:\n")  #stores Input into size_string Variable
        cmd_Str = check_size(Size_string)       #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
    else:
        os.system(fr'cmd /k "{cmd_Str}"')
        break
