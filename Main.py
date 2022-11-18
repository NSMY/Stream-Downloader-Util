import os
import sys
import time
from pyperclip import copy, paste
import webbrowser

#clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
clp_brd = paste()  # text will have the content of clipboard
url_ = clp_brd.replace("?filter=archives&sort=time","")

# def chk_sLink():
#     isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlink.exe")
#     if isthere is False:
#         print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nto download Streamlink and install it\n")

# chk_sLink()


acptLst = ["yes", "y"]
check_in = 0
isthere = False
while True:
    isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
    if isthere is False and check_in == 0:
        print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n")
        ipt_asw = input("Auto Launch Website?\ny/n?: ").lower()
        if ipt_asw in acptLst:
            webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
            check_in = +1
        else:
            check_in = +1
            continue
    elif check_in >= 0 and isthere == False:
        print("\nWaiting for Installation...")
        time.sleep(7)
        got_it = input("\nHas Streamlink been installed yet?\ny/n?:").lower()
        if got_it in acptLst and isthere is False:
            got_it = input("\nHaven't Found Stream Link In File Path\nC.Program.Files.Streamlink.bin      Are you sure? y/n?:").lower()
        elif got_it not in acptLst:
            print("\nWaiting!......")
            time.sleep(20)
    else:
        break

sizes = ["worst", "160p", "360p", "480p", "720p", "720p60", "1080p", "1080p60","160p30", "360p30", "480p30", "720p30", "720p30", "1080p30", "source", "best"]
name_of_File = input("Enter File Name:\n")


file_path = fr'"E:\DeleteStreams\New folder\{name_of_File}.mp4"'




def check_size(Vid_size):
    # print(Vid_size in sizes) Checks if True/False
    if Vid_size in sizes:
        return fr'cd C:\Program Files\Streamlink\bin && streamlink "{url_}" {Vid_size} --hls-segment-threads 5 -o {file_path}'
    else:
        return ("Enter a Valid Size")     
Fake_ = ""
while True:
    # if Fake_ == "":
    #     os.system(fr'cmd /k "cd C:\Program Files\Streamlink\bin && streamlink "https://youtu.be/d9iR5CYa2io"')
    #     time.sleep(3)
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
