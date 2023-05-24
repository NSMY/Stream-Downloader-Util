import os
import re
import subprocess
import sys
import time
import webbrowser
from tkinter import filedialog
from urllib.parse import urlparse
from datetime import datetime
import inquirer
from pyperclip import copy, paste

import cpyVid_scritp_____1 as cpvs
import funcs


def main_script():


    accp_lst = {"yes": ["y", "yes"], "no": ["n", "no"]}



    # cpvs.mux()
    # setlnk = funcs.setLink_Path()
    # print(setlnk)

    #Retrieves Last item in Clipboard(ctrl v)
    #clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
    clp_brd = paste()  # text will have the content of clipboard
    url_ = clp_brd.replace("?filter=archives&sort=time","")


    stream_lnk_Path = ""
    swtch = 1
    #Runs Check if streamlink is installed and gives link/opens if Not
    while stream_lnk_Path != "c":
        stream_lnk_Path = funcs.setLink_Path()
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
                time.sleep(7)
        elif swtch >= 0 and stream_lnk_Path == "404 Not Here":
                swtch = +2
                got_it = input("\nHas Streamlink been installed?\ny/n?:").lower()
                stream_lnk_Path = funcs.setLink_Path()
                time.sleep(5)
                if got_it in accp_lst["yes"] and stream_lnk_Path == "404 Not Here":
                    stream_lnk_Path = funcs.setLink_Path()
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
    

    if funcs.has_ffmpeg_dir(stream_lnk_Path):
        ffmpeg_path = stream_lnk_Path.replace("bin", "ffmpeg")
    else:
        print(f"\nThe 'ffmpeg', 'pkgs', 'Python' directory does not"
                f" exist in the parent directory of: {stream_lnk_Path}\n"
                    "   Please Re-Install correctly if needed")
        time.sleep(3)
        webbrowser.open("https://streamlink.github.io/install.html#windows-binaries")


    urlchk = funcs.is_url(url_)
    
    while urlchk == False:   
        if urlchk == False:
            print(f"ERROR: Clipboard: ( {url_}) Is NOT a Url.\n")
            rs = [
                inquirer.List(
                "OP",
                message="Clipboard is NOT a URL, Copied URL Again......",
                choices=["Done", "Exit"],
                ),
                ]
            rs1 = inquirer.prompt(rs)
            rs2 = ''.join([str(value) for value in rs1.values()])
            if rs2 == "Done":
                #rs = input('\nClipboard is NOT a URL "y" to Restart...:').lower
                os.system('cls' if os.name == 'nt' else 'clear')
                main_script()
            elif rs2 == "Exit":
                sys.exit ()
        else:
            continue
        
    
    #opens Windows Save Folder browser and stores chosen path
    def saveFile():
        print("Save File To:... \n")
        file = filedialog.asksaveasfilename(defaultextension='.mp4',
                                            filetypes=[
                                                ("MP4 files",".mp4"),    
                                                ("MOV files",".mov"),    
                                                ("All files",".*"),
                                            ])
        if len(file) == 0: #closes Program if No Save path is Entered
            check = funcs.mChoiseQeustion("Canceled Save Path: Try again?", ["yes", "no"])
            if check in accp_lst["yes"]:
                os.system('cls' if os.name == 'nt' else 'clear')
                saveFile()
            else:
                print("Exiting")
                time.sleep(3)
                sys.exit ()
        return (file)
    file_path = saveFile()
    print("Getting Resolutions...")

    # jank ass code to get dynamic resolution
    subprocess.call(f'cd {stream_lnk_Path}', shell=True)
    rw_stream = subprocess.Popen(f"streamlink {url_}", stdout=subprocess.PIPE, universal_newlines=True)
    out_pt = str(rw_stream.communicate())
    res_str_edt = out_pt.replace("\\n'", "")
    res_stripped = re.sub(pattern = "[^\w\s]",
            repl = "",
            string = res_str_edt)
    res_Options = res_stripped.split()[10:-1]
    #  -Old way-
    #res_Options = res_split[10:-1]
    #res_Options = str(res_split[10:-1])
    
    my_choices = list(reversed(res_Options))
    siz_rtn2 = funcs.mChoiseQeustion("What Size to Download?", my_choices)
    print(siz_rtn2)
    
    #old Code
    # name_of_File = input("Enter File Name:\n")
    # file_path = fr'"E:\DeleteStreams\New folder\{name_of_File}.mp4"'

    # print(Vid_size in sizes) Checks if True/False
    def check_size(Vid_size):
        if 1<2: #Vid_size in siz_rtn:
            return fr'cd {stream_lnk_Path} && streamlink "{url_}" {Vid_size} --stream-segment-threads 5 -o "{file_path}"'
        else:
            return ("404") 
        
        
        
    Fake_ = ""
    while True:
        if Fake_ == "":  
            # Size_string = input(f"Please enter Resolution you want to download, No Quote (\'\') marks EG 720p:\n\n{siz_rtn}: ").lower()    #stores Input into size_string Variable
            cmd_Str = check_size(siz_rtn2)   #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
            Fake_ = "1"
        
        elif cmd_Str == "404":
            time.sleep(1)
            # Size_string = input(f"Enter a Valid Size, No Quote (\'\') marks EG 720p:\n{siz_rtn}: ").lower()
            cmd_Str = check_size(siz_rtn2)   #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
        else:
            process = subprocess.Popen(f"{cmd_Str}", shell=True)
            process.wait()
            break

    # Old script run ----
        # else:
        #     os.system(fr'cmd /k "{cmd_Str}"')
        #     break
    # time.sleep(10)

    print("\nCompletion Time:", datetime.now().strftime("%H:%M:%S\n"))

    print("\nBecause of how Video is downloaded (Chunks) sometimes"
                    " Re-Muxing is needed for smooth playback."
                    " \n(Re-Mux)Make a Copy of this file?:\n ")
    convert = funcs.mChoiseQeustion("Convert?", ["yes", "no"])

    if convert in accp_lst["yes"]:
        cpvs.mux(ffmpegpath=ffmpeg_path, file_path_inpt=file_path)
        print("\nDone!!")

    print("\nRe Run Program? if Yes you need to copy the next URL"
                " in the clipboard before answering this:\n")
    exit = funcs.mChoiseQeustion("ReRun or Exit", ["yes", "no"])
    if exit in accp_lst["yes"]:
        main_script()
    else:
        sys.exit ()

rprog = funcs.mChoiseQeustion("Download or Re-Mux", ["Download", "Remux"])
if rprog == "Download":
    main_script()
elif rprog == "Remux":
    ffpth = funcs.setLink_Path().replace("\\bin", "\\ffmpeg")
    cpvs.mux(ffmpegpath=ffpth)
