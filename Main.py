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
import funcs
import init_files
import mux_vid as cpvs


def main_script(download_with_Shutdown=None, fromfile=None):
    sd_type = None
    if download_with_Shutdown:
        sd_type = funcs.multi_choice_dialog(
            "Manual shutdown Time or Shutdown after Completion", ["Auto", "Manual"]
        )
        if sd_type == "Manual":
            funcs.manual_shutdown_timer()

    # Retrieves Last item in Clipboard(ctrl v).
    if fromfile is None:
        url_ = paste().replace("?filter=archives&sort=time", "")
    else:
        url_ = fromfile[0]
    urlchk = funcs.is_url(url_)

    t1 = threading.Thread(target=funcs.is_url, args=(url_,))
    t1.start()

    # Checking Settings.json is available and recently checked.
    try:
        check_settings = funcs.loadSettings(keys=["LastSave", "streamlinkPath"])
    except FileNotFoundError as e:
        init_files.initSettings()
        main_script()

    is_a_fresh_save = [funcs.is_less_than_30days(check_settings[0])]  # type: ignore possible unbound
    is_a_fresh_save.extend(check_settings[1:2])  # type: ignore possible unbound
    if not all(is_a_fresh_save):
        funcs.streamlink_factory_init(["Main", "main_script"])
        os.system("cls")
        main_script()
    slinkDir = os.path.dirname(check_settings[1])  # type: ignore possible unbound

    message = "Clipboard is NOT a URL, Copy URL Again......"
    while not urlchk:
        print(f"ERROR: ( {url_}) Is NOT a Url.\n")
        choices = ["Done", "Exit", "Manual Input URL"]
        rs2 = funcs.multi_choice_dialog(message, choices)
        if rs2 == "Done":
            os.system("cls" if os.name == "nt" else "clear")
            main_script()
        elif rs2 == "Manual Input URL":
            url_ = input(
                "Type or paste (Must Include http://www.) " "URL HERE: "
            ).replace("?filter=archives&sort=time", "")
            urlchk = funcs.is_url(url_)
            if urlchk == True:
                print(url_)
                break
            main_script()
        elif rs2 == "Exit":
            sys.exit()

    # [] Untested fix to sub only Vods Res Check.
    # As not subbed to any sub only vod streamers.
    def get_vid_resolutions(slinkDir, url_, queue, auth_String=""):
        try:
            rw_stream = subprocess.Popen(
                rf'cd "{slinkDir}" && streamlink "{url_}" {auth_String}',
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
            stdout, stderr = rw_stream.communicate()

            if stderr:
                print(
                    "\nError: Likely a Sub Only Vod\n\n",
                )
                auth = auth_skip_ads_.auth_twitch_string()
                get_vid_resolutions(slinkDir, url_, queue, auth)  # type: ignore
            else:
                rw_stream.wait()
                out_pt, _ = rw_stream.communicate()
                result = re.sub(r"[^\w\s]", "", out_pt).split()[10:]
                queue.put(result)
        except Exception as e:
            print("OSE Error:")

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

    # saving file path.
    file_path = funcs.saveFile(fromfile[1]) if fromfile else funcs.saveFile()

    # Naming the Terminal.
    terminal_Naming = os.path.basename(file_path)
    os.system(f"title {terminal_Naming}")

    # Return of get_vid_resolutions threading.
    result.join()
    result = q.get()

    my_choices = list(reversed(result))
    siz_rtn2 = funcs.multi_choice_dialog("What Size to Download?", my_choices)

    # if not twitch netloc uses default, if twitch asks advanced Options.
    default_download_string = (
        rf'streamlink "{url_}" {siz_rtn2} '
        f'--stream-segment-threads 5 -o "{file_path}"'
    )
    if not is_it_a_twitch_url:
        download_string = default_download_string
    else:
        dload_via = funcs.multi_choice_dialog(
            "Streamlink Twitch Flags Download:"
            "Standard, Advanced(No Ads, Auth Token)"
            "",
            ["Standard", "Advanced"],
        )
        if dload_via == "Advanced":
            skip_ads_rtrn = auth_skip_ads_.skip_ads()
            download_string = (
                rf'streamlink {skip_ads_rtrn} "{url_}" {siz_rtn2}'
                f' --stream-segment-threads 5 -o "{file_path}"'
            )
        elif dload_via == "Standard":
            download_string = default_download_string

    print("\nQuality Chosen: ", siz_rtn2, "\n")
    print("CTRL + C to CANCEL Download early if necessary\n")

    # Main Download Process
    process = subprocess.Popen(
        download_string, shell=True, universal_newlines=True, cwd=slinkDir
    )

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

    if download_with_Shutdown:
        if sd_type == "Auto":
            savepath = os.path.dirname(file_path)
            with open(f"{savepath}/downloadCompleteTime.txt", "w") as f:
                f.write(
                    datetime.now().strftime(
                        f"{terminal_Naming}\nCompleted at:---- %H:%M:%S ----\n"
                    )
                )
            cpvs.mux(file_path)
            os.system("shutdown -s -t 200")
    else:
        print(
            "\nCompletion Time:",
            datetime.now().strftime(
                f"{terminal_Naming}\nCompleted at:---- %H:%M:%S ----\n"
            ),
        )

        # Plays Sound at this point.
        winsound.PlaySound(
            sound="C:\\Windows\\Media\\Windows Proximity Notification.wav",
            flags=winsound.SND_FILENAME,
        )

        print(
            "\nBecause of how Video is downloaded (Chunks) sometimes"
            " Re-Muxing is needed for smooth playback."
            " \n(Re-Mux)Make a Copy of this file?:\n "
        )

        # sends the file(name) to be mux'd via mux_vid.py
        convert = funcs.multi_choice_dialog("Convert?", ["yes", "no"])
        print(file_path)
        if convert == "yes":
            cpvs.mux(file_path)
            print("\nDone!!")
        else:
            funcs.open_directory_Force_front(file_path)

        print(
            "\nRe Run Program? if Yes you need to copy the next URL"
            " in the clipboard before answering this:\n"
        )
        exit = funcs.multi_choice_dialog("Run Again or Exit?", ["Run Again", "EXIT"])
        if exit == "Run Again":
            from startup import main_start
            main_start()
        else:
            sys.exit()


if __name__ == "__main__":
    from startup import main_start
    main_start()
