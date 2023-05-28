import os
from sys import exit
import subprocess
from pyperclip import copy, paste
from  send2trash import send2trash
import winsound
import funcs


def mux(ffmpegpath="C:\\Program Files\\Streamlink\\ffmpeg", file_path_inpt=paste()):
    
    
    ffpg = fr"{ffmpegpath}".replace("ffmpeg", "ffmpeg && ffmpeg")
    
    
    file_path = funcs.getFile(file_path_inpt)
    
    
    file_path_2 = os.path.dirname(file_path)
    
    new_folder_name = f"FFMPEG__re-Muxed" #new Folder Name
    new_folder_path = os.path.join(file_path_2, new_folder_name)
    
    if not os.path.exists(new_folder_path): #makes new Folder if NOT
        os.makedirs(new_folder_path)
        
    #renames File with newfolder 
    old_file_name = os.path.basename(file_path)
    new_file_path = os.path.join(new_folder_path, old_file_name)
    print(old_file_name)
    
    #checks if file exists if so send file to trash if Overwritten is chosen
    if os.path.exists(new_file_path):
        exists = funcs.mChoiceQeustion("File already Exists, Overwrite or Rename", ["Overwrite", "Rename"])
        if exists == "Overwrite":
            send2trash(fr"{new_file_path}")
        elif exists == "Rename":
            new_file_path = funcs.saveFile()
                
    if os.path.getsize(file_path) > 3 * (1024 ** 3):
        print("File size is large, Program may Hang while Working...")
        
    #opens cmd and uses ffmpeg to re-Mux
    process2 = subprocess.Popen(f'cd {ffpg} -i "{file_path}" -c copy "{new_file_path}"', shell=True, universal_newlines=True) #, cwd=ffpg <alt code to change dir undecided addition
    process2.wait()
    
    winsound.PlaySound('C:\\Windows\\Media\\Chimes.wav', winsound.SND_FILENAME)
    
    # output, error = process2.communicate()
    # print(output.decode())
    # print(error.decode())
    
    #sends Un-Muxed File to trash ONLY if both old/new exist
    try:
        if os.path.exists(new_file_path) and os.path.exists(file_path):
            send2trash(fr"{file_path}")
            if not os.path.exists(fr"{file_path}"):
                winsound.PlaySound('C:\\Windows\\Media\\Recycle.wav', winsound.SND_FILENAME)
                print(f'\nMoved: {file_path} to Trash...'
                        f'\nSaved in to: {new_file_path}    Re-Muxed..\n')
        else:
            print("Error...     File:", new_file_path, "\n")
    except:
        print("Unable to Recycle     ", file_path, "\n")
        
        
    path = os.path.dirname(new_file_path)
    os.startfile(os.path.realpath(path))
    
    #exit Options
    closeOptions = funcs.mChoiceQeustion("Remux again, Download Again, Extract streams or Exit", ["Remux", "Download", "Extract", "Exit"])
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




