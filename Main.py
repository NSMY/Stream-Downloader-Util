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

import mux_vid as cpvs
from pyperclip import copy, paste

import auth_skip_ads_
import funcs
import init_files


def main_script():
    # Retrieves Last item in Clipboard(ctrl v).
    url_ = paste().replace("?filter=archives&sort=time","")
    urlchk = funcs.is_url(url_)
    
    t1 = threading.Thread(target=funcs.is_url, args=(url_,))
    t1.start()
    
    # Checking Settings.json is available and recently checked.
    try:
        check_settings = funcs.loadSettings(keys=['LastSave', 'streamlinkPath'])
    except FileNotFoundError as e:
        init_files.initSettings()
        main_script()
    
    is_a_fresh_save = [funcs.is_less_than_30days(check_settings[0])]
    is_a_fresh_save.extend(check_settings[1:2])
    if not all(is_a_fresh_save):
        funcs.streamlink_factory_init(["Main", "main_script"])
        os.system('cls')
        main_script()
    slinkDir = os.path.dirname(check_settings[1])


    message = ("Clipboard is NOT a URL, Copy URL Again......")
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
    
    
    # Checks if a Twitch URL.
    twitch_netloc = ["www.twitch.tv", "usher.ttvnw.net"]
    result = urlparse(url_)[1]
    is_it_a_twitch_url = False
    if result in twitch_netloc:
        is_it_a_twitch_url = True
    
    # Start of Getting get_vid_resolutions threading.
    q = Queue()
    result = threading.Thread(target=get_vid_resolutions, args=(slinkDir, url_, q))
    result.start()
    
    file_path = funcs.saveFile()
    
    # Naming the Terminal.
    terminal_Naming = os.path.basename(file_path)
    os.system(f"title {terminal_Naming}")

    # Return of get_vid_resolutions threading.
    result.join()
    result = q.get()
    
    my_choices = list(reversed(result))
    siz_rtn2 = funcs.multi_choice_dialog("What Size to Download?", my_choices)
    
    
    # if not twitch netloc uses default, if twitch asks advanced Options.
    default_download_string = (fr'streamlink "{url_}" {siz_rtn2} '
                            f'--stream-segment-threads 5 -o "{file_path}"'
                            )
    if not is_it_a_twitch_url:
        download_string = default_download_string
    else:
        dload_via = funcs.multi_choice_dialog('Streamlink Twitch Flags Download:'
                                            'Standard, Advanced(No Ads, Auth Token)'
                                            '', ['Standard', 'Advanced']
                                            )
        if dload_via == 'Advanced':
            skip_ads_rtrn = auth_skip_ads_.skip_ads()
            download_string = (fr'streamlink {skip_ads_rtrn} "{url_}" {siz_rtn2}'
                            f' --stream-segment-threads 5 -o "{file_path}"'
                            )
        elif dload_via == 'Standard':
            download_string = default_download_string


    print("\nQuality Chosen: ", siz_rtn2, "\n")
    print("CTRL + C to CANCEL Download early if necessary\n")


    # Main Download Process
    process = subprocess.Popen(download_string, shell=True, universal_newlines=True, cwd=slinkDir)


    # Define a signal handler for SIGINT using a lambda function
    # changing ctrl+c to kill the subprocess instead of the terminal.
    handle_sigint = lambda signal, frame: funcs.kill_process(process)
    # Register the signal handler for SIGINT
    signal.signal(signal.SIGINT, handle_sigint)
    # Start a thread to wait for the subprocess to complete
    thread_popen = threading.Thread(target=funcs.wait_for_subprocess, args=(process,))

    thread_popen.start()
    # Wait for the thread to finish
    thread_popen.join()

    # Reset the signal handler for SIGINT to its default behavior (kill terminal)
    signal.signal(signal.SIGINT, signal.SIG_DFL)


    print("\nCompletion Time:", datetime.now().strftime("---- %H:%M:%S ----\n"))
    
# def timer_shutdown(wait_time:int = 300):
#     '''wait_time is the number of seconds'''
#     os.system(f"shutdown -s -t {wait_time}") #FEATURE take out this sends shutdown cmd?
#     with open('downloadCompleteTime.txt', 'w') as f:
#         f.write(datetime.now().strftime("%H:%M:%S---------\n"))

    # Plays Sound at this point.
    winsound.PlaySound(sound='C:\\Windows\\Media\\Windows Proximity Notification.wav'
                        , flags=winsound.SND_FILENAME)
    
    print("\nBecause of how Video is downloaded (Chunks) sometimes"
                    " Re-Muxing is needed for smooth playback."
                    " \n(Re-Mux)Make a Copy of this file?:\n ")
    
    # sends the file(name) to be mux'd via cpyVid_script____1.py
    convert = funcs.multi_choice_dialog("Convert?", ["yes", "no"])
    print(file_path)
    if convert == "yes":
        cpvs.mux(file_path)
        print("\nDone!!")
    else:
        funcs.open_directory_Force_front(file_path)


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