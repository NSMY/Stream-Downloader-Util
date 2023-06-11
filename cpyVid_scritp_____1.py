import os
import subprocess
import winsound
from sys import exit

from pyperclip import copy, paste
from send2trash import send2trash

import funcs

# TODO webm?


def mux(file_path_inpt=paste()):
    # IF Path is not saved in setting.json or is last saved sett>30days.
    if (funcs.isMoreThan30days(funcs.loadSettings('LastSave')) is True
        or funcs.loadSettings('ffmpegpath') is None
        ):
        funcs.ffmpeg_factory_init(['cpyVid_scritp_____1', 'mux'])
        os.system('cls')
        mux()
    ffmpegpath = funcs.loadSettings('ffmpegpath')
    ffpg = os.path.dirname(str(ffmpegpath))

    file_path = funcs.file_path_get(file_path_inpt)
    if not (any(file_path.endswith(media_type) 
                for media_type in funcs.video_file_types) or file_path == '.'):
        print('\nNot a Valid File type to Remux, Try again.')
        os.system('cls')
        mux()
    if file_path == '.':
        os.system('cls')

    new_file_path = funcs.make_new_dir_from_input(file_path, 'FFMPEG__re-Muxed')
    old_file_name = os.path.basename(file_path)
    new_file_path = os.path.join(new_file_path, old_file_name)
    print(old_file_name)

    """
    checks if file exists if so 
    send file to trash if Overwritten is chosen
    """

    if os.path.isfile(new_file_path):
        exists = funcs.multi_choice_dialog('File already Exists, Overwrite or ' 
                                            'Rename', ['Overwrite', 'Rename']
        )
        if exists == 'Overwrite':
            send2trash(rf'{new_file_path}')
        elif exists == 'Rename':
            new_file_path = funcs.saveFile()

    # opens cmd and uses ffmpeg to re-Mux
    process2 = subprocess.Popen(
        f'ffmpeg -i "{file_path}" -c copy ' f'"{new_file_path}"',
        shell=True,
        universal_newlines=True,
        cwd=ffpg,
        )
    
    winsound.PlaySound('C:\\Windows\\Media\\Chimes.wav', winsound.SND_FILENAME)

    # sends Un-Muxed File to trash ONLY if both old/new exist.
    view_fp = funcs.shorten_path_name(file_path)
    view_nfp = funcs.shorten_path_name(new_file_path)
    
    if os.path.isfile(new_file_path) and os.path.isfile(file_path):
        try:
            send2trash(rf'{file_path}')
        except Exception:
            print(f'Error... with {view_fp} \n or {view_nfp}'
                    '\nTried to move {view_fp} \nto trash\n')
        else:
            if not os.path.isfile(f'{file_path}'):
                winsound.PlaySound(
                    'C:\\Windows\\Media\\Recycle.wav',
                    winsound.SND_FILENAME)
                print(f'\nMoved: {view_fp} \nto Trash...'
                        f'\nSaved in to: {view_nfp}\nRe-Muxed..\n')

    funcs.open_directory_Force_front(new_file_path)

    # exit Options
    closeOptions = funcs.multi_choice_dialog(
        'Remux again, Download, '
        'Extract streams or Exit',
        ['Remux', 'Download', 'Extract', 'Exit'],
        )
    if closeOptions == 'Remux':
        os.system('cls')
        mux()
    elif closeOptions == 'Download':
        os.system('cls')
        from Main import main_script

        main_script()
    elif closeOptions == 'Extract':
        from ffmpegExtract import ffmpegextract

        ffmpegextract()
    else:
        exit()


if __name__ == '__main__':
    mux()
