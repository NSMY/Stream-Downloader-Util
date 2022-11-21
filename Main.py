import os
import sys
import time
from pyperclip import copy, paste
import webbrowser
from tkinter import filedialog

#Retrieves Last item in Clipboard(ctrl v)
#clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
clp_brd = paste()  # text will have the content of clipboard
url_ = clp_brd.replace("?filter=archives&sort=time","")

#Runs Check if streamlink is installed and gives link/opens if Not
accp_lst = {"yes": ["y", "yes"], "no": ["n", "no"]}

def chk_if_Install():
    stlink = []
    stlink.append(os.path.isfile("C:\\Program Files\Streamlink\\bin\\streamlink.exe"))
    stlink.append(os.path.isfile("C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"))
    return stlink


def setLink_Path():
    if (chk_if_Install()[0]) == True:
        lnk_pth = "C:\\Program Files\\Streamlink\\bin\\"
        return lnk_pth
    elif (chk_if_Install()[1]) == True:
        lnk_pth = "C:\\Program Files (x86)\\Streamlink\\bin\\"
        return lnk_pth            
    else:
        return ("404 Not Here")

stream_lnk_Path = ""
swtch = 1

while stream_lnk_Path != "c":
    stream_lnk_Path = setLink_Path()
    if stream_lnk_Path == "404 Not Here" and swtch == 1:
        swtch = +2
        ipt_asw = input(f"\nYou do not seem to have streamLink installed.\n\nPlease "
                "Visit: https://github.com/streamlink/windows-builds/releases/latest\nTo download "
                "Streamlink and install it.\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe----\nOR"
                "\nAuto Launch Website? y/n?: ").lower()
        if ipt_asw in accp_lst["yes"]:
            webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
            print("\nWaiting for Installation...")
            time.sleep(15)
        else:
            print("\nWaiting for Installation...")
            time.sleep(7)               # TEMPORARY CODE ----15
    elif swtch >= 0 and stream_lnk_Path == "404 Not Here":
            swtch = +2
            got_it = input("\nHas Streamlink been installed?\ny/n?:").lower()
            stream_lnk_Path = setLink_Path()
            time.sleep(5)
            if got_it in accp_lst["yes"] and stream_lnk_Path == "404 Not Here":
                stream_lnk_Path = setLink_Path()
                lie_chk = input("\nHaven't Found Streamlink In File Path C\\Program (or {x86}) \\Files\\Streamlink\\bin\\"
                                "   Are you sure it is there?\nDo you need the website again? y/n?:").lower()
                time.sleep(5)
                if lie_chk in accp_lst["yes"]:
                    webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
                    print("\nWaiting!......")
                    time.sleep(7)
                elif stream_lnk_Path == "404 Not Here":
                    time.sleep(8)# 21 ----
                    print("\nPlease Check: C\\Program (or {x86}) \\Files\\Streamlink\\bin\\ Path")
            else:
                time.sleep(12)
                
    else:
        break



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
        return fr'cd {stream_lnk_Path} && streamlink "{url_}" {Vid_size} --hls-segment-threads 5 -o "{file_path}"'
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
