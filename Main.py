import os
import re
import signal
import subprocess
import sys
import threading
import winsound
from datetime import datetime
from queue import Queue
from urllib.parse import urlparse

from pyperclip import copy, paste

import auth_skip_ads_
import funcs
import init_files
import mux_vid as cpvs
import spinner as spn
from new_mass_gql import get_vods_sizes_m3u8 as m3
from utility_dir import util_functions


def main_script(download_with_Shutdown=None, fromfile=None):
    if fromfile:
        if (
            fromfile[1]["vod_info"].get("status") == "RECORDING"
            and funcs.multi_choice_dialog(
                "VOD is still recording, Continue to download", ["No", "Yes"]
            )
            == "No"
        ):
            from startup import main_start
            main_start()

        fromfile = (
            fromfile[1]["vod_info"]["url"],
            fromfile[1]["index"],
            fromfile[1]["vod_info"],
            f"{fromfile[1]['vod_info']['displayName']} - "
            f"{util_functions.simple_convert_timestamp(fromfile[1]['vod_info']['publishedAt'])} "
            f"{fromfile[1]['vod_info']['title']}_"
            f"{fromfile[1]['vod_info']['gameName']}",
        )

    sd_type = None
    if download_with_Shutdown:
        sd_type = funcs.multi_choice_dialog(
            "Manual shutdown Time or Shutdown after Completion", ["Auto", "Manual"]
        )
        if sd_type == "Manual":
            funcs.manual_shutdown_timer()

    # Retrieves Last item in Clipboard(ctrl v).
    url = paste() if fromfile is None else fromfile[0]

    url_bits = funcs.parse_url_twitch(url)
    url_ = url_bits[0]

    # TODO download at specified time needs work.
    # if not url_bits[1].query.startswith('t='):
    #     timecode = input('Start Download at Spesific Time ? 00h00m00s. enter 6 numbers separated by Space. EG 01 25 35 :').split(' ')
    #     url_ = rf'{url_}?t=h{timecode[0]}m{timecode[1]}s{timecode[2]}'
    #     print("🐍 File: Stream-Downloader-Util/Main.py | Line: 57 | main_script ~ url_",url_)

    # URL CleanUp and isVod check for m3u8 Call.
    is_url_path_vod = url_bits[1].path.split("/", -1)[-1].isnumeric()
    url_path = url_bits[1].path.split("/", -1)[-1]

    def get_urlm3u8_filesize(url_, queue):
        size_of_vod = m3.m3u8_call_init(video_id=url_)
        return queue.put(size_of_vod)

    urlchk = funcs.is_url(url_)
    # Threading start for url check.
    t1 = threading.Thread(target=funcs.is_url, args=(url_,))
    t1.start()

    # Checking Settings.json is available and recently checked.
    try:
        check_settings = funcs.loadSettings(keys=["LastSave", "streamlinkPath"])
    except FileNotFoundError as e:
        print(e)
        init_files.initSettings()
        os.system("cls")
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
            if urlchk == True:  # FIX == True or Is True?.
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
                rf'streamlink "{url_}" {auth_String}',
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                cwd=slinkDir,
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
            print(e, "OSE Error:")

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


    if is_url_path_vod:
        q2 = Queue()
        m3u8 = threading.Thread(target=get_urlm3u8_filesize, args=(url_path, q2))
        m3u8.start()

        # end m3u8 check.

    if fromfile:
        print(fromfile[-1])

    # saving file path.
    download_file_path = funcs.saveFile(fromfile[-1]) if fromfile else funcs.saveFile()

    # Naming the Terminal.
    terminal_Naming = os.path.basename(download_file_path)
    os.system(f"title {terminal_Naming}")
    spinner2 = spn.Spinner()
    spinner2.start()

    # Return of get_vid_resolutions threading.
    result.join()
    spinner2.stop()
    result = q.get()

    my_choices = list(reversed(result))
    chosen_resolution = funcs.multi_choice_dialog("What Size to Download?", my_choices)

    # if not twitch netloc uses default, if twitch asks advanced Options.
    default_download_string = (
        rf'streamlink "{url_}" {chosen_resolution} '
        f'--stream-segment-threads 5 -o "{download_file_path}"'
    )
    if not is_it_a_twitch_url:
        download_string = default_download_string
    else:
        twitch_options_choice = funcs.multi_choice_dialog(
            "Streamlink Twitch Flags Download:"
            "Standard, Advanced(No Ads, Auth Token)"
            "",
            ["Standard", "Advanced"],
        )
        if twitch_options_choice == "Advanced":
            skip_ads_rtrn = auth_skip_ads_.skip_ads()
            download_string = (
                rf'streamlink {skip_ads_rtrn} "{url_}" {chosen_resolution}'
                f' --stream-segment-threads 5 -o "{download_file_path}"'
            )
        elif twitch_options_choice == "Standard":
            download_string = default_download_string

    print("\nCTRL + C to CANCEL Download early if necessary")

    if is_url_path_vod:
        spinner1 = spn.Spinner()
        spinner1.start()
        m3u8.join()
        spinner1.stop()
        m3u8_data = q2.get()
        try:
            if chosen_resolution == "best":
                gb_of_vod = list(m3u8_data.values())[0][0]
            elif chosen_resolution == "worst":
                gb_of_vod = list(m3u8_data.values())[-1][0]
            else:
                gb_of_vod = m3u8_data[chosen_resolution][0]
            print(
                "{:<5}\n{:>31}".format(
                    f"Quality Chosen: {chosen_resolution}", f"{gb_of_vod} GB\n"
                )
            )
        except UnboundLocalError and KeyError:
            print("Quality Chosen: ", chosen_resolution, "\n")
    else:
        print("Quality Chosen: ", chosen_resolution, "\n")

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
    # BUG if i cancel i got a synatx error ??
    # Reset the signal handler for SIGINT to its default behavior (kill terminal)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # if is_url_path_vod:

    #     # FIX will need to include ffprobe in main settings checks to use this.
    #     get_len_of_vod_file = subprocess.Popen(
    #         rf'ffprobe -i "{download_file_path}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
    #         shell=False,
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE,
    #         universal_newlines=True,
    #         cwd='c:/ffmpeg/'  # FIX replace me.
    #     )
    #     stdout, stderr = get_len_of_vod_file.communicate()
    #     get_len_of_vod_file.wait()
    #     len_of_vod = int(stdout.split('.')[0]) #    len_of_vod = int(stdout.split('.')[0]) ValueError: invalid literal for int() with base 10: '' ## cant get len_of_vod bcoz not muxed
    #     # print("🐍 File: zextra_Funcs_/Testcode.py | Line: 126 | undefined ~ len_of_vod",len_of_vod)

    #     if (ulr_query := urlparse(url).query).startswith('t='):
    #         url_split = re.split('[=hms]', ulr_query)
    #         secs_to_subt_from_file = util_functions.encode_hms_to_seconds(':'.join(url_split[1:-1]))
    #         # if len_of_vod - secs_to_subt_from_file == 0:
    #         if len_of_vod - secs_to_subt_from_file == 0:
    #             # LOOK Temp code to make feat work as proof more complex here than necessary
    #             # needs more comparing, this changes every time not if complete and or further comparisons
    #             # working Great, need a Pointer to file/or date dld in file??.
    #             util_functions.update_downloaded_to_resolution(
    #                 urlparse(url_).path.split("/")[-1], chosen_resolution
    #             )
    #     elif len_of_vod - fromfile[2].get('lengthSeconds') == 0:

    #         # LOOK Temp code to make feat work as proof more complex here than necessary
    #         # needs more comparing, this changes every time not if complete and or further comparisons
    #         # working Great, need a Pointer to file/or date dld in file??.
    #         util_functions.update_downloaded_to_resolution(
    #             urlparse(url_).path.split("/")[-1], chosen_resolution
    #         )# BUG seemed not to trigger on 14-10 vod of kotton maybe dl size dont match close enough?.

    # HERE have the dld conformation be size GB and/or seconds(len) of vid and be like 5 seconds adjustable

    if download_with_Shutdown:
        if sd_type == "Auto":
            save_path = os.path.dirname(download_file_path)
            with open(f"{save_path}/downloadCompleteTime.txt", "a") as f:
                f.write(
                    datetime.now().strftime(
                        f"{terminal_Naming}\nCompleted at:---- %H:%M:%S ----\n"
                    )
                )
            cpvs.mux(download_file_path)
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
        print(download_file_path)
        if convert == "yes":
            cpvs.mux(download_file_path)
            print("\nDone!!")
        else:
            funcs.open_directory_Force_front(download_file_path)

        # print(
        #     "\nRe Run Program? if Yes you need to copy the next URL"
        #     " in the clipboard before answering this."
        # )
        # exit = funcs.multi_choice_dialog("Run Again or Exit?", ["Run Again", "EXIT"])
        # if exit == "Run Again":
        from startup import main_start

        main_start()
        # else:
        #     sys.exit()


if __name__ == "__main__":
    from startup import main_start
    main_start()
