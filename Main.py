import json
import logging
import os
import re
import signal
import subprocess
import sys
import threading
import winsound
from datetime import datetime
from queue import Queue
from urllib.parse import urlparse, urlsplit

from pyperclip import copy, paste

import auth_skip_ads_
import funcs
import init_files
import mux_vid as cpvs
import spinner as spn
from new_mass_gql import get_vods_sizes_m3u8 as m3
from utility_dir import util_functions


def main_script(download_with_Shutdown=None, fromfile=None):
    ''' download_with_shutdown enables == Pc shutdown after completion
        fromfile == Json data dict.
    '''

    # Checking Settings.json is available and recently checked.
    try:
        check_settings = funcs.loadSettings(
            keys=["LastSave", "streamlinkPath", "ffprobepath"]
        )
    except FileNotFoundError as e:
        print(e)
        init_files.initSettings()
        os.system("cls")
        main_script()

    is_a_fresh_save = [funcs.is_less_than_30days(check_settings[0])]  # type: ignore possible unbound

    is_a_fresh_save.extend(check_settings[1:2])  # type: ignore possible unbound

    if not all(is_a_fresh_save):
        funcs.streamlink_factory_init(["Main", "main_script"])
        funcs.ffprobe_factory_init(["Main", "main_script"])
        os.system("cls")
        main_script()

    slinkDir = os.path.dirname(check_settings[1])  # type: ignore possible unbound

    ffprobe_dir = os.path.dirname(check_settings[2])  # type: ignore possible unbound

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
            # File Naming Convention formed here
            f"{fromfile[1]['vod_info']['displayName']} - "
            f"{util_functions.simple_convert_timestamp(fromfile[1]['vod_info']['publishedAt'])} "
            f"{fromfile[1]['vod_info']['title']}_"
            f"{fromfile[1]['vod_info']['gameName']}",
        )

    sd_type = None

    funcs.flush_cmd_input()
    if download_with_Shutdown:
        sd_type = funcs.multi_choice_dialog(
            "Manual shutdown Time or Shutdown after Completion", ["Auto", "Manual", "**Cancel**"]
        )
        if sd_type == "**Cancel**":
            os.system('cls')
            from startup import main_start
            main_start()
        elif sd_type == "Manual":
            funcs.manual_shutdown_timer()

    # Retrieves Last item in Clipboard(ctrl v).
    url = paste() if fromfile is None else fromfile[0]
    # TODO maybe have it get the title of url if == twitch??.

    url_bits = funcs.parse_url_twitch(url)

    url_ = url_bits[0]
    print("🐍 File: Stream-Downloader-Util/Main.py | Line: 98 | main_script ~ url_",url_)
    print(fromfile)
    def start_at_specified_time(url) -> tuple:
        """-> Returns tup(url, timecode)"""
        timecode = input(
            "Start Download at Specific Time ? 00h00m00s. "
            "enter 6 numbers separated by Space. EG 01-25-35 :"
        ).split("-")
        url = rf"{url}?t={timecode[0]}h{timecode[1]}m{timecode[2]}s"
        return url, timecode

    def calc_remaining_time(timecode: int, from_file_seconds_data: int) -> int:
        full_seconds = from_file_seconds_data
        return full_seconds - timecode

    def convert_url_query_timecode(url_timecode_query):
        hrs, min, sec = (
            url_timecode_query.replace("t=", "")
            .replace("h", "-")
            .replace("m", "-")
            .replace("s", "")
            .split("-", maxsplit=3)
        )
        return int(hrs) * 3600 + int(min) * 60 + int(sec)

    def get_urlm3u8_filesize(url_, queue, minus_time):
        url_path = urlsplit(url_).path.rsplit("/", 1)[1]
        if not minus_time:
            size_of_vod = m3.m3u8_call_init(
                video_id=url_path,
                tot_seconds=remaining_time
            )
            return queue.put(size_of_vod)
        size_of_vod = m3.m3u8_call_init(
            video_id=url_path,
            tot_seconds=remaining_time,
            minus_time=minus_time
        )
        return queue.put(size_of_vod)

    remaining_time = None

    minus_time = 0

    funcs.flush_cmd_input()
    if (
        fromfile
        and funcs.multi_choice_dialog("Start at Specified time?", ["No", "Yes"])
        == "Yes"
    ):
        print(f'Vod length: {util_functions.decode_seconds_to_hms(fromfile[2]["lengthSeconds"])}')
        url_, timecode = start_at_specified_time(url_)
        timecodej = "-".join(timecode)
        timecodei = util_functions.encode_hms_to_seconds(timecodej, split_on="-")
        remaining_time = calc_remaining_time(timecodei, fromfile[2]["lengthSeconds"])
    else:
        if url_bits[1].query.startswith("t="):
            minus_time = convert_url_query_timecode(urlsplit(url_).query)

    is_url_path_twitch_vod = url_bits[1].path.split("/", -1)[-1].isnumeric()

    # TRACK why and i threading this?
    # is_url_thread = threading.Thread(target=funcs.is_url, args=(url_,))
    # is_url_thread.start()
    urlchk = False
    (urlchk := funcs.is_url(url_))
    # FIX want this to be better upto date with my curr knowledge
    message = "Clipboard is NOT a URL, Copy URL Again......"
    while not urlchk:
        print(f"ERROR: ({url_}) Is NOT a Url.\n")
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

    # Sub Only tested works but no est size of vod as Likely gql auth is
    # [] general oauth not personal key maybe can hackaround (sub only prints out (L GB)).
    def get_vid_resolutions(slinkDir, url_, queue, auth_String=""):
        # FIX later This Ugly POS is because theres a current twitch m3u8 bandwidth get Bug -> 0.
        # & in the Streamlink Code it double errors with Sub Only/w no access.
        loops = 0
        while loops < 5:
            loops += 1
            try:
                stream_reso = subprocess.Popen(
                    rf'streamlink "{url_}" {auth_String}',
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True,
                    cwd=slinkDir,
                )
                # # stdout, stderr = rw_stream.communicate()

                stream_reso.wait()
                for line in iter(stream_reso.stdout.readline, ''):
                    # print(line.rstrip())
                    if 'error: No play' in line.rstrip():
                        logging.info("File: Stream-Downloader-Util/Main.py | Line: 208 | get_vid_resolutions ~ line rw_stream %s", line.rstrip())
                        raise ValueError
                    elif 'error: This plugin' in line.rstrip():
                        os.system('cls')
                        print('DMCA', line) # FEATURE Maybe Implement YTDL later
                        raise SyntaxError
                    elif "Available streams:" in line:
                        result = re.sub(r"[^\w\s]", "", line).split()[2:]
                        return queue.put(result)
                stream_reso.communicate()
                raise OSError
            except SyntaxError:
                return queue.put('Error')
            except OSError:
                print(
                    "\nError: Likely a Sub Only Vod\n\n",
                )
                auth = auth_skip_ads_.auth_twitch_string()
                auth_String = auth
            except ValueError:
                pass
        return queue.put('Error')
        # result1.join()

    # Checks if a Twitch URL.
    twitch_netloc = ["www.twitch.tv", "usher.ttvnw.net"]

    url_netlock = urlparse(url_)[1]

    is_it_a_twitch_url = False

    if url_netlock in twitch_netloc:
        is_it_a_twitch_url = True

    # Start of Getting get_vid_resolutions threading.
    q = Queue()
    get_res_opts = threading.Thread(target=get_vid_resolutions, args=(slinkDir, url_, q))
    get_res_opts.start()

    if is_url_path_twitch_vod:
        q2 = Queue()
        m3u8 = threading.Thread(
            target=get_urlm3u8_filesize, args=(url_, q2, minus_time)
        )
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
    get_res_opts.join()
    spinner2.stop()
    get_res_opts = q.get()

    # TRACK Shouldn't be needed, as should be handled in
    # the get_vid_resolutions Func
    if get_res_opts == 'Error':
        print('Errored Too many attempts')
        from startup import main_start
        main_start()

    my_choices = list(reversed(get_res_opts))

    funcs.flush_cmd_input()
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
        if twitch_options_choice == "Advanced": # [] Add a input in the .skipads to be able to input any sLink Opts??
            skip_ads_rtrn = auth_skip_ads_.skip_ads()
            download_string = (
                rf'streamlink {skip_ads_rtrn} "{url_}" {chosen_resolution}'
                f' --stream-segment-threads 5 -o "{download_file_path}"'
            )
            print("🐍 File: Stream-Downloader-Util/Main.py | Line: 306 | get_vid_resolutions ~ download_string",download_string)
        elif twitch_options_choice == "Standard":
            download_string = default_download_string

    print("\nCTRL + C to CANCEL Download early if necessary")

    if is_url_path_twitch_vod:
        spinner1 = spn.Spinner()
        spinner1.start()
        m3u8.join()
        m3u8_data = q2.get()
        spinner1.stop()

        try:
            if chosen_resolution == "best" or "source":
                gb_of_vod = list(m3u8_data.values())[0][0]
            elif chosen_resolution == "worst":
                gb_of_vod = list(m3u8_data.values())[-1][0]
            else:
                gb_of_vod = m3u8_data[chosen_resolution][0]
            print(f"\nQuality Chosen: {chosen_resolution},\t({gb_of_vod} GB)\n")
        except (UnboundLocalError, KeyError) as e:
            print(e, "\nQuality Chosen: ", chosen_resolution, "\n")
    else:
        print("\nQuality Chosen: ", chosen_resolution, "\n")

    # Main Download Process
    # BUG Twitch is Bugging out and returns no streams available but retry works
    # prob same m3u8 bandwidth -> 0 bug 21-12-2023.
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

    # FIX errors is Canceled 
    def compare_with_tolerance(size1, size2, tolerance=10) -> bool:
        """
        This function compares two file sizes with a certain tolerance.
        """
        return abs(size1 - size2) <= tolerance


    # FIX errors is Canceled find way to not enter if Canceled 
    if is_url_path_twitch_vod and os.path.isfile(download_file_path):
        get_len_of_vod_file = subprocess.Popen(
            rf'ffprobe -i "{download_file_path}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd=ffprobe_dir
        )
        stdout, stderr = get_len_of_vod_file.communicate()
        get_len_of_vod_file.wait()
        len_secs = int(stdout.split('.')[0])
        if compare_with_tolerance(remaining_time, len_secs, 20):
            # FIX Lazy temp solution to get json name (could error from mods name being this)
            chosen_json_path = f"{util_functions.get_appdata_dir()}/jsons/{fromfile[2]['login']}.json"

            with open(chosen_json_path, 'r') as f:
                filedata = json.load(f)
            chosenindex = fromfile[1]

            filedata[chosenindex]['downloaded'] = chosen_resolution

            with open(chosen_json_path, 'w') as f:
                json.dump(filedata, f, indent=4)

    if download_with_Shutdown:
        if sd_type == "Auto":
            save_path = os.path.dirname(download_file_path)
            with open(f"{save_path}/downloadCompleteTime.txt", "a") as f:
                f.write(datetime.now().strftime(
                        f"\nCompleted: {terminal_Naming}\nCompleted at: -- %H:%M:%S --\n"
                        ))

            cpvs.mux(download_file_path)
            os.system("shutdown -s -t 180")
            os.system("cls")
            print(
                "If you want to Cancel the Shutdown CMD, "
                "Open the Terminal and type: shutdown -a\nExecute"
            )
    else:
        print(
            datetime.now().strftime(
                f"\nCompleted: {terminal_Naming}\nCompleted at: -- %H:%M:%S --\n"
            ))
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
        funcs.flush_cmd_input()
        convert = funcs.multi_choice_dialog("Convert?", ["yes", "no"])
        print(download_file_path)
        if convert == "yes":
            cpvs.mux(download_file_path)
            os.system('cls')
            print("\nDone!!")
        # else:
            # funcs.open_directory_Force_front(download_file_path)

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
