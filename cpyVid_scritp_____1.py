from pyperclip import copy, paste
import subprocess
import os
from Main import openFile

def mux(ffmpegpath="C:\\Program Files\\Streamlink\\ffmpeg && ffmpeg", file_path=paste().strip('"')):
    file_path = ""
    if file_path == "":
        file_path = paste().strip('"')

    file_path_2 = os.path.dirname(file_path)

    new_folder_name = f"FFMPEG__Encoded"
    new_folder_path = os.path.join(file_path_2, new_folder_name)

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    old_file_name = os.path.basename(file_path)
    new_file_path = os.path.join(new_folder_path, old_file_name)

    process2 = subprocess.Popen(f'cd {ffmpegpath} -i "{file_path}" -c copy "{new_file_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process2.communicate()
    print(output.decode())
    print(error.decode())

    # os.system('cls' if os.name == 'nt' else 'clear')
    new_file_path = f"{new_file_path}"
    path = os.path.dirname(new_file_path)
    path_1 = os.path.realpath(path)
    os.startfile(path_1)
