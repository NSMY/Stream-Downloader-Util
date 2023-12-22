import os
import threading

import init_dir.init_files as init_files
from helpers import auth_skip_ads_, check_new_streams
from helpers import funcs as funcs
from helpers import gql_main_call
from helpers import help as hlp
from helpers import tk_get_file_list
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
        exit()

    def making_vods_list():
        gql_main_call.First_making_cmds()

    def check_streams():
        mn_rtrn = check_new_streams.start_new_vods()
        main_start()

    def retrieve_saved_vod():
        if impt_data:
            aad = get_single_vod_.Run_get_vod("")
        aad = get_single_vod_.Run_get_vod("")
        # print(aad)
        from Main import main_dld_start

        # from new_mass_gql import tk_get_file_list
        # print(aad[0])
        # tk_get_file_list.call_tk_vod_view(f'c:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/{aad[0]}.json') # FIX sloppy af.
        if (
            shutdown := funcs.multi_choice_dialog(
                "Download Type", ["Normal", "Auto Shutdown", "**Cancel**"]
            )
            == "Normal"
        ):
            main_dld_start(fromfile=aad)
        elif shutdown == "**Cancel**":
            os.system("cls")
            main_start()
        else:
            main_dld_start(download_with_Shutdown=True, fromfile=aad)

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
        "Re-Mux": remux,
        "Extract Audio/Video": extract,
        "Download W/ Shutdown": download_shutdown,
        "Vod from File": retrieve_saved_vod,
        "Update Vods File": check_streams,
        "List View of File": list_view,
        "Create New Vods File": making_vods_list,
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
    init_files.logger_setup()

    question = "Start Commands"
    responses = [
        "Standard Download",
        "Re-Mux",
        "Extract Audio/Video",
        "Download W/ Shutdown",
        "Vod from File",
        "Update Vods File",
        "List View of File",
        "Create New Vods File",
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
