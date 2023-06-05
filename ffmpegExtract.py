import os
import funcs
import subprocess

media_file_Types = [".mp4", ".mov", ".mkv", ".ts",]

def ffmpegextract():
    #FIXIT if file is NOT muxed it returns [ALL 0 0 Exit] channels
    # IF Path is not saved in setting.json or is last saved sett>30days.
    if (funcs.loadSettings("ffprobepath")
        == None or funcs.isMoreThan30days(funcs.loadSettings('LastSave'))):
    
        probeDir = (funcs.file_search("ffprobe.exe")
                    if not os.path.isfile("C:\\ffmpeg\\ffprobe") else None)
        
        if not probeDir:
            probeDir = funcs.execute_or_setting(funcs.DL_unZip_ffprobe,
                                                    key="ffprobepath")
            os.system('cls')
            ffmpegextract()
        if probeDir:
            funcs.saveSettings("ffprobepath", probeDir)
    else:
        probeDir = funcs.loadSettings("ffprobepath")
        
        
    filename = funcs.getFile()
    
    if not (any(filename.endswith(file_type)
            for file_type in media_file_Types)):
        print("\nNot a Valid File type to Extract Streams From Try again.")
        ffmpegextract()
    
    for file_type in media_file_Types:
        if filename.endswith(file_type):
            print(file_type)
            break
    
    try:
        chanReturn = funcs.channelsSplit(probeDir, filename)
        mxChann = chanReturn[0]
        opus = chanReturn[-1]
    except subprocess.CalledProcessError as ce:
        from Main import main_script
        os.system('cls')
        main_script()
    chan = ["All"] + mxChann + ["Exit"]

    ffmpegDir = funcs.setLink_Path(True)

    if funcs.has_ffmpeg_dir(ffmpegDir):
        ffmpeg_path = ffmpegDir.replace("\\Streamlink\\bin\\",
                                            "\\Streamlink\\ffmpeg\\")

    # Inputs questions
    message = "Which audio channels would you like to extract?"
    answers = funcs.mChoiceQeustion(message, chan, "int", "channels")
    selected_channels = answers["channels"]
    
    if selected_channels == "Exit":
        from Main import main_script
        os.system('cls')
        main_script()
        
    message = "Do you want to extract the video stream?"
    answers = funcs.mChoiceQeustion(message, ["Yes", "No"], "int")
    copy_video = answers["Key"] == "Yes"
    
    # create Dir
    name = os.path.splitext(os.path.basename(filename))[0]
    outname = os.path.join(os.path.dirname(filename),
                            f"{name} audio streams", name)

    print(outname)
    os.makedirs(os.path.dirname(outname), exist_ok=True)
    
    #parse code
    if selected_channels == "All":
        num_channels = int(mxChann[-1])
        if copy_video:
            cmd = f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}{file_type}"'
        else:
            cmd = f'ffmpeg -i "{filename}"'
        for i in range(num_channels):
            cmd += f' -map 0:a:{i} -c copy "{outname}_{i}.aac"'
    
    else:
        channel = int(selected_channels) - 1
        if copy_video and opus != "opus":
            cmd = f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}{file_type}"'
        elif copy_video and opus == "opus":
            cmd = f'ffmpeg -i "{filename}" "{outname}{file_type}"' #FIX anothr line to convert vp9 not just copy and switch needed this copies vp9 atm and if OpUS audio Not vp9 Vid
        else:
            cmd = f'ffmpeg -i "{filename}"'
        
        if opus == "opus":
            cmd += f' && ffmpeg -i "{filename}" "{outname}_{channel}.aac"'
        else:
            cmd += f' -map 0:a:{channel} -c copy "{outname}_{channel}.aac"'
    
    try:
        extct = subprocess.Popen(cmd, shell=True, universal_newlines=True,
                                    cwd=ffmpeg_path)
        extct.wait()
        os.startfile(os.path.dirname(fr'{outname}'))
    
    except subprocess.CalledProcessError as ce:
        ffmpegextract()
    except:
        print("Extracting Failed")
        
        
    #exit Options
    closeOptions = funcs.mChoiceQeustion("Extract again, Download Again, "
                                        "Remux media or Exit",
                                    ["Extract", "Download", "Remux", "Exit"])
    
    if closeOptions == "Remux":
        from cpyVid_scritp_____1 import mux
        os.system('cls')
        mux()
    
    elif closeOptions == "Download":
        os.system('cls')
        from Main import main_script
        main_script()
    elif closeOptions == "Extract":
        os.system('cls')
        ffmpegextract()
    else:
        exit()

if __name__ == "__main__":
    ffmpegextract()
