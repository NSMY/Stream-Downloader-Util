import os
from sys import exit
import subprocess
from pyperclip import copy, paste
from  send2trash import send2trash
import winsound
import funcs


def mux(ffmpegpath="C:\\Program Files\\Streamlink\\ffmpeg", file_path_inpt=paste()):

    
    ffpg = fr"{ffmpegpath}".replace("ffmpeg", "ffmpeg && ffmpeg")
    
    file_path = file_path_inpt.replace("/", "\\")
    try:
        if os.path.isfile(file_path):
            file_path.strip().strip('"').strip("'")
        else:
            file_path = funcs.openFile().replace("/", "\\")
            print(file_path)
    except:
        file_path = funcs.openFile().replace("/", "\\")
        print(file_path)


    file_path_2 = os.path.dirname(file_path)

    new_folder_name = f"FFMPEG__re-Muxed" #new Folder Name
    new_folder_path = os.path.join(file_path_2, new_folder_name)

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    old_file_name = os.path.basename(file_path)
    new_file_path = os.path.join(new_folder_path, old_file_name)
    print(old_file_name)
    if os.path.exists(new_file_path):
        exists = funcs.mChoiseQeustion("File already Exists, Overwrite or Rename", ["Overwrite", "Rename"])
        if exists == "Overwrite":
            send2trash(fr"{new_file_path}")
        elif exists == "Rename":
            new_file_path = funcs.saveFile()
            
        
    if os.path.getsize(file_path) > 3 * (1024 ** 3):
        print("File size is large, Program may Hang while Working...")

    process2 = subprocess.Popen(f'cd {ffpg} -i "{file_path}" -c copy "{new_file_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process2.communicate()
    print(output.decode())
    print(error.decode())


    try:
        if os.path.exists(new_file_path) and os.path.exists(file_path):
            send2trash(fr"{file_path}")
            if not os.path.exists(fr"{file_path}"):
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                print(f'\nMoved: {file_path} to Trash...'
                        f'\nSaved in to: {new_file_path}    Re-Muxed..\n')
        else:
            print("Error...     File:", new_file_path, "\n")
    except:
        print("Unable to Recycle     ", file_path, "\n")


    # os.system('cls' if os.name == 'nt' else 'clear')
    new_file_path = f"{new_file_path}"
    path = os.path.dirname(new_file_path)
    path_1 = os.path.realpath(path)
    os.startfile(path_1)


    end = funcs.mChoiseQeustion("Remux again, run Streamlink or Exit", ["Remux", "Streamlink", "Exit"])
    if end == "Remux":
        os.system('cls')
        mux()
    elif end == "Streamlink":
        from Main import main_script
        os.system('cls')
        main_script()
    else:
        exit()

if __name__ == "__main__":
    mux()    




