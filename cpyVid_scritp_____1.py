import os
import subprocess
import winsound
from sys import exit

from pyperclip import copy, paste
from send2trash import send2trash

import funcs

#TODO webm?


def mux(file_path_inpt = paste()):
    
    # Check if the ffmpeg path is already saved in the settings
    ffmpegpath = funcs.loadSettings("ffmpegpath")
    if not ffmpegpath or funcs.isMoreThan30days(funcs.loadSettings('LastSave')):
        ffmpegpath = funcs.get_ffmpeg_path()



    ffpg = os.path.dirname(fr"{ffmpegpath}")

    file_path = funcs.getFile(file_path_inpt)

    if not (any(file_path.endswith(media_type)
                for media_type in funcs.video_file_types)):
        print("\nNot a Valid File type to Remux, Try again.")
        mux()


    if file_path == ".":
        os.system('cls')
        mux()

    new_file_path = funcs.make_new_dir_from_path(file_path, "FFMPEG__re-Muxed")

    '''
    checks if file exists if so 
    send file to trash if Overwritten is chosen
    '''
    if os.path.exists(new_file_path):
        exists = funcs.mChoiceQeustion("File already Exists, Overwrite or "
                                        "Rename", ["Overwrite", "Rename"])
        if exists == "Overwrite":
            send2trash(fr"{new_file_path}")
        elif exists == "Rename":
            new_file_path = funcs.saveFile()

    if os.path.getsize(file_path) > 3 * (1024 ** 3):
        print("File size is large, Program may Hang while Working...")

    #opens cmd and uses ffmpeg to re-Mux
    process2 = subprocess.Popen(f'ffmpeg -i "{file_path}" -c copy '
                                f'"{new_file_path}"', shell=True,
                                    universal_newlines=True, cwd=ffpg)
    winsound.PlaySound('C:\\Windows\\Media\\Chimes.wav', winsound.SND_FILENAME)


    # sends Un-Muxed File to trash ONLY if both old/new exist.
    view_fp = funcs.shorten_path_name(file_path)
    view_nfp = funcs.shorten_path_name(new_file_path)
    try:
        if os.path.exists(new_file_path) and os.path.exists(file_path):
            send2trash(fr"{file_path}")

            if not os.path.exists(fr"{file_path}"): #TEST on laptop not working had file open so couldn't recycle but played seems OK on PC
                winsound.PlaySound('C:\\Windows\\Media\\Recycle.wav',
                                    winsound.SND_FILENAME)

                print(f'\nMoved: {view_fp} \nto Trash...'
                        f'\nSaved in to: {view_nfp}\nRe-Muxed..\n')

        else:
            print(f"Error... with {view_fp} \n or {view_nfp}"
                    "\nTried to move {view_fp} \nto trash\n")
    except:
        print("\nUnable to Recycle     ", view_fp, "\n")


    path = os.path.dirname(new_file_path)
    os.startfile(os.path.realpath(path))

    #exit Options
    closeOptions = funcs.mChoiceQeustion("Remux again, Download Again, "
                    "Extract streams or Exit"
                    , ["Remux", "Download", "Extract", "Exit"])

    if closeOptions == "Remux":
        os.system('cls')
        mux()
    elif closeOptions == "Download":
        os.system('cls')
        from Main import main_script
        main_script()
    elif closeOptions == "Extract":
        from ffmpegExtract import ffmpegextract
        ffmpegextract()
    else:
        exit()
        
if __name__ == "__main__":
    mux()    




