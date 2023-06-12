import os
import re
import signal
import subprocess
import sys
import threading
import time
import webbrowser
import winsound
from datetime import datetime
from urllib.parse import urlparse

from pyperclip import copy, paste

import cpyVid_scritp_____1 as cpvs
import funcs

# FEATURE customTKinter GUI??
# TODO do i ad multi File processing? mp4 wav etc
# TODO do i make Combine streams Aud/Vid
# TODO make WEBP converter? New File?
# TODO make separate download/main thats can get lives and restart if dropouts maybe scheduled  maybe seek notos?
# [] Somehow incorporate auto download from noto?
# [] Win Alert notos? 


def main_script():
    #Retrieves Last item in Clipboard(ctrl v).
    url_ = paste().replace("?filter=archives&sort=time","")
    
    check_settings = funcs.loadSettings(['LastSave', 'streamlinkPath'])
    fresh_save = [funcs.is_less_than_30days(check_settings[0])]
    fresh_save.extend(check_settings[1:2])
    if not all(fresh_save):
        funcs.streamlink_factory_init(["Main", "main_script"])
        os.system('cls')
        main_script()
    slinkDir = os.path.dirname(check_settings[1])

    urlchk = funcs.is_url(url_)
    message = ("Clipboard is NOT a URL, Copy URL Again......")
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

    file_path = funcs.saveFile()

    # Naming the Terminal.
    terminal_Naming = os.path.basename(file_path)
    os.system(f"title {terminal_Naming}")

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

    my_choices = list(reversed(result))

    siz_rtn2 = funcs.multi_choice_dialog("What Size to Download?", my_choices)

    print("Quality Chosen: ", siz_rtn2, "\n")

    process = subprocess.Popen(fr'cd {slinkDir} && streamlink '
        f'"{url_}" {siz_rtn2} --stream-segment-threads 5 -o "{file_path}"'
                                , shell=True, universal_newlines=True)

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


    print("\nCompletion Time:", datetime.now().strftime("%H:%M:%S---------\n"))

    # os.system("shutdown -s -t 300") #FEATURE take out this sends shutdown cmd?
    #[] completion Print to a a Log ?

    winsound.PlaySound('C:\\Windows\\Media\\Windows Proximity Notification.wav'
                        , winsound.SND_FILENAME)


    print("\nBecause of how Video is downloaded (Chunks) sometimes"
                    " Re-Muxing is needed for smooth playback."
                    " \n(Re-Mux)Make a Copy of this file?:\n ")

    convert = funcs.multi_choice_dialog("Convert?", ["yes", "no"])

    if convert == "yes":
        cpvs.mux(file_path_inpt=file_path)
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
    main_script()