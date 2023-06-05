import os
from sys import exit
import subprocess
from pyperclip import copy, paste
from send2trash import send2trash
import winsound
import funcs
from ffmpegExtract import media_file_Types
#TODO webm?


def mux(ffmpegpath = "C:\\Program Files\\Streamlink\\ffmpeg",
        file_path_inpt = paste()):
    
    if (funcs.loadSettings("ffmpegpath")
        == None or funcs.isMoreThan30days(funcs.loadSettings('LastSave'))): #TESTING downloads ffmpeg on main pc without (.settings i assume)
        
        default_ffPath = ("C:\\Program Files\\Streamlink"
                                                "\\ffmpeg\\ffmpeg.exe")
        if not os.path.isfile(default_ffPath):
            ffmpegpath = funcs.file_search("ffmpeg.exe")
            if not ffmpegpath:
                ffmpegpath = False
        else: ffmpegpath = default_ffPath
        
        if not ffmpegpath:
            ffmpegpath = funcs.execute_or_setting(funcs.DL_unZip_ffmpeg,
                                                    key="ffmpegpath")
            os.system('cls')
            mux()
        if ffmpegpath:
            funcs.saveSettings("ffmpegpath", ffmpegpath)
    else:
        ffmpegpath = funcs.loadSettings("ffmpegpath")
    
    
    ffpg = fr"{ffmpegpath}"
    
    #[x] make File be valid type media_file_Types  
    
    file_path = funcs.getFile(file_path_inpt)
    
    if not (any(file_path.endswith(media_type)
                for media_type in media_file_Types)):
        print("\nNot a Valid File type to Remux, Try again.")
        mux()
        
    
    if file_path == ".":
        os.system('cls')
        mux()
    
    file_path_2 = os.path.dirname(file_path)
    
    new_folder_name = f"FFMPEG__re-Muxed" #new Folder Name
    new_folder_path = os.path.join(file_path_2, new_folder_name)
    
    if not os.path.exists(new_folder_path): #makes new Folder if NOT
        os.makedirs(new_folder_path)
        
    #renames File with newfolder 
    old_file_name = os.path.basename(file_path)
    new_file_path = os.path.join(new_folder_path, old_file_name)
    print("\n", old_file_name)
    
    
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




