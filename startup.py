
import os
import threading

import auth_skip_ads_
import funcs
import init_files
from ffmpegExtract import ffmpegextract
from new_mass_gql import check_new_streams, gql_main_call, tk_get_file_list
from utility_dir import get_single_vod_
from utils import video_data_cross_checker


def main_start(impt_data=None):

    def download():
        from Main import main_script
        main_script()

    def remux():
        from mux_vid import mux
        mux(ran_as_main=True)

    def extract():
        ffmpegextract()

    def download_shutdown():
        from Main import main_script
        main_script(True)

    def exit_program():
        exit()

    def making_vods_list():
        gql_main_call.First_making_cmds()

    def check_streams():
        mn_rtrn = check_new_streams.start_new_vods()
        main_start()

    def retrieve_saved_vod():
        if impt_data:
            aad = get_single_vod_.Run_get_vod('')
        aad = get_single_vod_.Run_get_vod('')
        # print(aad)
        from Main import main_script

        # from new_mass_gql import tk_get_file_list
        # print(aad[0])
        # tk_get_file_list.call_tk_vod_view(f'c:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/{aad[0]}.json') # FIX sloppy af.
        if funcs.multi_choice_dialog('Download Type', ['Normal', 'Auto Shutdown']) == "Normal":
            main_script(fromfile=aad)
        else:
            main_script(download_with_Shutdown=True, fromfile=aad)

    def list_view():
        tk_get_file_list.call_as_solo()
        main_start()

    def crosscheck_vod_details():
        video_data_cross_checker.main()
        os.system('cls')
        main_start()

    # Define your dictionary
    switch = {
        'Download': download,
        'Remux': remux,
        'Extract': extract,
        'Download-Shutdown': download_shutdown,
        'Get Vod from File': retrieve_saved_vod,
        'Create Streamer Vods File': making_vods_list,
        'Check for New Vods': check_streams,
        'List View': list_view,
        'Cross-check Vods to Json Data': crosscheck_vod_details,
        'Exit': exit_program,
    }

    os.system("title Stream Downloader Util")
    t1 = threading.Thread(target=auth_skip_ads_.auth_file_check)
    t1.start()
    t2 = threading.Thread(target=init_files.init_links_file)
    t2.start()

    init_files.version_check()

    question = ('Start Commands')
    responses = [
        'Download',
        'Remux',
        'Extract',
        'Download-Shutdown',
        'Get Vod from File',
        'Check for New Vods',
        'Create Streamer Vods File',
        'List View',
        'Cross-check Vods to Json Data',
        'Exit'
    ]
    rprog = funcs.multi_choice_dialog(question, responses)

    # Get the function from the dictionary
    func = switch.get(rprog)  #ignore: E262
    # when_= 4-8
    # Call the function if it's not None
    if func:
        func()
    else:
        print("Invalid option")


if __name__ == '__main__':
    main_start()
