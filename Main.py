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
import winsound
import cpyVid_scritp_____1 as cpvs
import funcs


def main_script():


    accp_lst = {"yes": ["y", "yes"], "no": ["n", "no"]}


    #Retrieves Last item in Clipboard(ctrl v)
    #clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
    clp_brd = paste()  # text will have the content of clipboard
    url_ = clp_brd.replace("?filter=archives&sort=time","")
    
    
    stream_lnk_Path = ""
    swtch = 1
    #Runs Check if streamlink is installed and gives link/opens if Not
    while stream_lnk_Path != "c":
        stream_lnk_Path = funcs.setLink_Path()
        slinkURL = "https://github.com/streamlink/windows-builds/releases/latest"
        if stream_lnk_Path == "404 Not Here" and swtch == 1:
            swtch = +2
            ipt_asw = input(f"\nYou do not seem to have streamLink installed.\n\nPlease "
                    f"Visit: {slinkURL}\nTo download "
                    "Streamlink and install it.\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe----\nOR"
                    "\nAuto Launch Website? y/n?: ").lower()
            if ipt_asw in accp_lst["yes"]:
                webbrowser.open(slinkURL)
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
                        webbrowser.open(slinkURL)
                        print("\nWaiting!......")
                        time.sleep(7)
                    elif stream_lnk_Path == "404 Not Here":
                        time.sleep(8)# 21 ----
                        print("\nPlease Check: C\\Program (or {x86}) \\Files\\Streamlink\\bin\\ Path")
                else:
                    time.sleep(12)
                    
        else:
            break
    
    # ffpegPath = funcs.setLink_Path(False)
    # if funcs.has_ffmpeg_dir(ffpegPath):
    #     ffmpeg_path = ffpegPath.replace("bin", "ffmpeg")
    # else:
    #     print(f"\nThe 'ffmpeg', 'pkgs', 'Python' directory does not"
    #             f" exist in the parent directory of: {stream_lnk_Path}\n"
    #                 "   Please Re-Install correctly if needed")
    #     time.sleep(3)
    #     webbrowser.open("https://streamlink.github.io/install.html#windows-binaries")
        
        
        
    if funcs.loadSettings("ffmpegpath") == None or funcs.isMoreThan30days(funcs.loadSettings('LastSave')):
        ffmpegpath = funcs.file_search("ffmpeg.exe") if not os.path.isfile("C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe") else None
        if not ffmpegpath:
            ffmpegpath = funcs.execute_or_setting(funcs.DL_unZip_ffmpeg,  key="ffmpegpath")
            os.system('cls')
            main_script()
        if ffmpegpath:
            funcs.saveSettings("ffmpegpath", ffmpegpath)
    else:
        ffmpegpath = funcs.loadSettings("ffmpegpath")
    ffmpeg_path = os.path.dirname(ffmpegpath)
    
        
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
        
    
    file_path = funcs.saveFile()
    
    
    print("Getting Resolutions...")
    
    
    # jank ass code to get dynamic resolution
    subprocess.call(f'cd {stream_lnk_Path}', shell=True)
    rw_stream = subprocess.Popen(f'cd {stream_lnk_Path} && streamlink "{url_}"', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    rw_stream.wait()
    out_pt = str(rw_stream.communicate()).replace("\\n'", "")
    res_stripped = re.sub(pattern = "[^\w\s]",
            repl = "",
            string = out_pt)
    res_Options = res_stripped.split()
    result = res_Options[9:-1]
    
    
    my_choices = list(reversed(result))
    siz_rtn2 = funcs.mChoiceQeustion("What Size to Download?", my_choices)
    print(siz_rtn2)
    
    
    def slink_Dload():
        process = subprocess.Popen(fr'cd {stream_lnk_Path} && streamlink "{url_}" {siz_rtn2} --stream-segment-threads 5 -o "{file_path}"', shell=True, universal_newlines=True)
        process.wait()
    slink_Dload()
    
    
    print("\nCompletion Time:", datetime.now().strftime("%H:%M:%S------------------------------\n"))
    
    
    winsound.PlaySound('C:\\Windows\\Media\\Windows Proximity Notification.wav', winsound.SND_FILENAME)
    
    
    print("\nBecause of how Video is downloaded (Chunks) sometimes"
                    " Re-Muxing is needed for smooth playback."
                    " \n(Re-Mux)Make a Copy of this file?:\n ")
    convert = funcs.mChoiceQeustion("Convert?", ["yes", "no"])
    if convert == "yes":
        cpvs.mux(ffmpegpath=ffmpeg_path, file_path_inpt=file_path)
        print("\nDone!!")
        
        
    print("\nRe Run Program? if Yes you need to copy the next URL"
                " in the clipboard before answering this:\n")
    exit = funcs.mChoiceQeustion("ReRun or Exit", ["yes", "no"])
    if exit == "yes":
        main_script()
    else:
        sys.exit ()
        
        
        
os.system("title Stream Downloader Util")     
funcs.initSettings()
rprog = funcs.mChoiceQeustion("Download, Re-Mux(Copy) or Extract Streams", ["Download", "Remux", "Extract"])
if rprog == "Download":
    main_script()
elif rprog == "Remux":
    ffpth = funcs.setLink_Path(True).replace("\\bin", "\\ffmpeg")
    cpvs.mux(ffmpegpath=ffpth)
elif rprog == "Extract":
    from ffmpegExtract import ffmpegextract
    ffmpegextract()