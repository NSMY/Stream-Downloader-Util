import os
import re
import signal
import subprocess
import sys
import threading
import time
import webbrowser
import winsound
from ast import arg
from datetime import datetime
from queue import Queue
from urllib.parse import urlparse

from pyperclip import copy, paste

import auth_skip_ads_
import cpyVid_scritp_____1 as cpvs
import funcs
import init_files

# TODO more robust dependency searching and downloading (if deleted between sett Checks)
# FEATURE customTKinter GUI??
# TODO do i ad multi File processing? mp4 wav etc
# TODO do i make Combine streams Aud/Vid
# TODO make WEBP converter? New File?
# TODO make separate download/main thats can get lives and restart if dropouts maybe scheduled  maybe seek notos?
# [] Somehow incorporate auto download from noto?
# [] Win Alert notos?
# []Keep both Copies Main and With Shutdown?????.

def main_script():
    #Retrieves Last item in Clipboard(ctrl v).
    url_ = paste().replace("?filter=archives&sort=time","")
    urlchk = funcs.is_url(url_)
    
    t1 = threading.Thread(target=funcs.is_url, args=(url_,))
    t1.start()
    
    message = ("Clipboard is NOT a URL, Copy URL Again......")
    
    try:
        check_settings = funcs.loadSettings(['LastSave', 'streamlinkPath'])
    except FileNotFoundError as e:
        init_files.initSettings()
        main_script()
    
    fresh_save = [funcs.is_less_than_30days(check_settings[0])]
    fresh_save.extend(check_settings[1:2])
    if not all(fresh_save):
        funcs.streamlink_factory_init(["Main", "main_script"])
        os.system('cls')
        main_script()
    slinkDir = os.path.dirname(check_settings[1])

# [] make a Func?
    while not urlchk:
        print(f"ERROR: ( {url_}) Is NOT a Url.\n")
        choices = ["Done", "Exit", "Manual Input URL"]
        rs2 = funcs.multi_choice_dialog(message, choices)
        if rs2 == "Done":
            os.system('cls' if os.name == 'nt' else 'clear')
            main_script()
        elif rs2 == "Manual Input URL":
            url_ = input("Type or paste (Must Include http://www.) "
                        "URL HERE: ").replace("?filter=archives&sort=time","")
            urlchk = funcs.is_url(url_)
            if urlchk == True:
                print(url_)
                break
            main_script()
        elif rs2 == "Exit":
            sys.exit ()
    
    
    def get_vid_resolutions(slinkDir, url_, queue):
        print("Getting Resolutions...")
        
        subprocess.call(f'cd {slinkDir}', shell=True)
        rw_stream = subprocess.Popen(f'cd {slinkDir} && streamlink "{url_}"'
                                    , shell=True, stdout=subprocess.PIPE,
                                        universal_newlines=True)
        rw_stream.wait()
        out_pt = str(rw_stream.communicate()).replace("\\n'", "")
        res_stripped = re.sub(pattern = "[^\\w\\s]",
                repl = "",
                string = out_pt)
        res_Options = res_stripped.split()
        result = res_Options[9:-1]
        queue.put(result)
    
    q = Queue()
    result = threading.Thread(target=get_vid_resolutions, args=(slinkDir, url_, q))
    result.start()
    
    file_path = funcs.saveFile()
    
    # Naming the Terminal.
    terminal_Naming = os.path.basename(file_path)
    os.system(f"title {terminal_Naming}")


    result.join()
    result = q.get()
    
    my_choices = list(reversed(result))

    siz_rtn2 = funcs.multi_choice_dialog("What Size to Download?", my_choices)

    dload_via = funcs.multi_choice_dialog('Streamlink Twitch Flags Download:'
        'Standard, Advanced(No Ads, Auth Token)', ['Standard', 'Advanced']
        )
    if dload_via == 'Advanced':
        skip_ads_rtrn = auth_skip_ads_.skip_ads()
        download_string = subprocess.Popen(fr'cd {slinkDir} && streamlink {skip_ads_rtrn} '
            f'"{url_}" {siz_rtn2} --stream-segment-threads 5 -o "{file_path}"'
                                    , shell=True, universal_newlines=True)
    else:
        download_string = subprocess.Popen(fr'cd {slinkDir} && streamlink '
            f'"{url_}" {siz_rtn2} --stream-segment-threads 5 -o "{file_path}"'
                                    , shell=True, universal_newlines=True)

    print("\nQuality Chosen: ", siz_rtn2, "\n")
    print("CTRL + C to CANCEL Download early if necessary\n")


    # Main Download Process
    process = download_string


    # Define a signal handler for SIGINT using a lambda function
    handle_sigint = lambda signal, frame: funcs.kill_process(process)
    # Register the signal handler for SIGINT
    signal.signal(signal.SIGINT, handle_sigint)
    # Start a thread to wait for the subprocess to complete
    thread_popen = threading.Thread(target=funcs.wait_for_subprocess, args=(process,))

    thread_popen.start()

    # Wait for the thread to finish
    thread_popen.join()

    # Reset the signal handler for SIGINT to its default behavior
    signal.signal(signal.SIGINT, signal.SIG_DFL)


    print("\nCompletion Time:", datetime.now().strftime("---- %H:%M:%S ----\n"))
    
# def timer_shutdown(wait_time:int = 300):
#     '''wait_time is the number of seconds'''
#     os.system(f"shutdown -s -t {wait_time}") #FEATURE take out this sends shutdown cmd?
#     with open('downloadCompleteTime.txt', 'w') as f:
#         f.write(datetime.now().strftime("%H:%M:%S---------\n"))

    winsound.PlaySound('C:\\Windows\\Media\\Windows Proximity Notification.wav'
                        , winsound.SND_FILENAME)


    print("\nBecause of how Video is downloaded (Chunks) sometimes"
                    " Re-Muxing is needed for smooth playback."
                    " \n(Re-Mux)Make a Copy of this file?:\n ")

    convert = funcs.multi_choice_dialog("Convert?", ["yes", "no"])
    print(file_path)
    if convert == "yes":
        cpvs.mux(file_path)
        print("\nDone!!")


    print("\nRe Run Program? if Yes you need to copy the next URL"
                " in the clipboard before answering this:\n")

    exit = funcs.multi_choice_dialog("Run Again or Exit?", ["Run Again", "EXIT"])

    if exit == "Run Again":
        main_script()
    else:
        sys.exit ()
        
        
    funcs.main_start()


if __name__ == "__main__":
    funcs.main_start()