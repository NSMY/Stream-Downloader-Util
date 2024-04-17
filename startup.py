import os
import sys
import threading

import init_dir.init_files as init_files
from helpers import auth_skip_ads_, check_new_streams, gql_main_call, tk_get_file_list
from helpers import funcs as funcs
from helpers import help as hlp
from my_utils import get_single_vod_, video_data_cross_checker
from my_utils.ffmpegExtract import ffmpegextract


def main_start(impt_data=None):
    def download():
        from Main import main_dld_start

        main_dld_start()

    def remux():
        from my_utils.mux_vid import mux

        mux(ran_as_main=True)

    def extract():
        ffmpegextract()

    def download_shutdown():
        from Main import main_dld_start

        main_dld_start(True)

    def exit_program():
        sys.exit()

    def making_vods_list():
        gql_main_call.First_making_cmds()

    def check_streams():
        mn_rtrn = check_new_streams.start_new_vods()
        main_start()

    def retrieve_saved_vod():
        if impt_data:
            rgv_rtrn_data = get_single_vod_.Run_get_vod("")
        rgv_rtrn_data = get_single_vod_.Run_get_vod("")

        print(f'\n\nChosen: {rgv_rtrn_data[0]['streamer']}, {rgv_rtrn_data[1]['vod_info']['title']}\n')

        from Main import main_dld_start

        shutdown = funcs.multi_choice_dialog("Download Type", ["Normal", "Auto Shutdown", "**Cancel**"])
        if shutdown == "Normal":
            main_dld_start(fromfile=rgv_rtrn_data)
        elif shutdown == "**Cancel**":
            os.system("cls")
            return main_start()
        else:
            main_dld_start(download_with_Shutdown=True, fromfile=rgv_rtrn_data)

    def list_view():
        tk_get_file_list.call_as_solo()
        main_start()

    def crosscheck_vod_details():
        video_data_cross_checker.main()
        main_start()

    def helpstr():
        hlp.main()

    # Define your dictionary
    switch = {
        "Standard Download": download,
        "Vod from File": retrieve_saved_vod,
        "Update Vods File": check_streams,
        "Create New Vods File": making_vods_list,
        "List View of File": list_view,
        "Re-Mux": remux,
        "Extract Audio/Video": extract,
        "Download W/ Shutdown": download_shutdown,
        "Cross-check Vods to Json Data": crosscheck_vod_details,
        "Help": helpstr,
        "Exit": exit_program,
    }

    os.system("title Stream Downloader Util")
    t1 = threading.Thread(target=auth_skip_ads_.auth_file_check)
    t1.start()
    t2 = threading.Thread(target=init_files.init_links_file)
    t2.start()

    init_files.version_check()
    # init_files.logger_setup()

    question = "Start Commands"
    responses = [
        "Standard Download",
        "Vod from File",
        "Update Vods File",
        "List View of File",
        "Create New Vods File",
        "Re-Mux",
        "Extract Audio/Video",
        "Download W/ Shutdown",
        "Cross-check Vods to Json Data",
        "Help",
        "Exit",
    ]
    rprog = funcs.multi_choice_dialog(question, responses)

    # Get the function from the dictionary
    func = switch.get(rprog)  # ignore: E262
    # when_= 4-8
    # Call the function if it's not None
    if func:
        func()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main_start()
