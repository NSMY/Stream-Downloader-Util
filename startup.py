
import os
import sys
import threading
from os import path

import auth_skip_ads_
import funcs
import init_files
from ffmpegExtract import ffmpegextract
from new_mass_gql import check_new_streams, gql_main_call
from new_mass_gql.utility_dir import get_single_vod_


def main_start():

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
        check_new_streams.start_new_vods()

    def retrieve_saved_vod():
        aad = get_single_vod_.Run_get_vod('')
        from Main import main_script
        main_script(fromfile=aad)

    # Define your dictionary
    switch = {
        'Download': download,
        'Remux': remux,
        'Extract': extract,
        'Download-Shutdown': download_shutdown,
        'Get-Vod-from-File': retrieve_saved_vod,
        'Make-New-Vods-File': making_vods_list,
        'Check-for-New-Vods': check_streams,
        'Exit': exit_program,
    }

    os.system("title Stream Downloader Util")

    t1 = threading.Thread(target=auth_skip_ads_.auth_file_check)
    t1.start()
    t2 = threading.Thread(target=init_files.init_links_file)
    t2.start()

    init_files.version_check()

    question = ('"Download, Re-Mux(Copy), Extract Streams, Vods-File, Check-New-Vods or "'
                '"Download with PC Shutdown Command Once Finished"')
    responses = [
        'Download',
        'Remux',
        'Extract',
        'Download-Shutdown',
        'Get-Vod-from-File',
        'Check-for-New-Vods',
        'Make-New-Vods-File',
        'Exit'
    ]
    rprog = funcs.multi_choice_dialog(question, responses)

    # Get the function from the dictionary
    func = switch.get(rprog)  #ignore: E262

    # Call the function if it's not None
    if func:
        func()
    else:
        print("Invalid option")


if __name__ == '__main__':
    main_start()
