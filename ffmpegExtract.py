import os
import funcs
import subprocess

def ffmpegextract():
    if funcs.loadSettings("ffprobepath") == False:
        ZipComboran = False
    elif funcs.loadSettings("ffprobepath") == True:
        ZipComboran = True
    
    if ZipComboran == False:
        probeDir = funcs.DloadZipCombo()
        funcs.saveSettings("ffprobepath", probeDir)
    elif ZipComboran == True:
        probeDir = funcs.loadSettings("ffprobepath")
        if not probeDir:
            probeDir = funcs.findExe("ffprobe.exe")
    filename = funcs.getFile()
    mxChann = funcs.channelsSplit(probeDir, filename)
    chan = ["All"] + mxChann

    ffmpegDir = funcs.setLink_Path(True)
    if funcs.has_ffmpeg_dir(ffmpegDir):
        ffmpeg_path = ffmpegDir.replace("\\Streamlink\\bin\\", "\\Streamlink\\ffmpeg\\")

    # Inputs questions
    message = "Which audio channels would you like to extract?"
    answers = funcs.mChoiceQeustion(message, chan, "int", "channels")
    selected_channels = answers["channels"]

    message = "Do you want to extract the video stream?"
    answers = funcs.mChoiceQeustion(message, ["Yes", "No"], "int")
    copy_video = answers["Key"] == "Yes"

    # create Dir
    name = os.path.splitext(os.path.basename(filename))[0]
    outname = os.path.join(os.path.dirname(filename), f"{name} audio streams", name)
    print(outname)
    os.makedirs(os.path.dirname(outname), exist_ok=True)

    #parse code
    if selected_channels == "All":
        num_channels = int(mxChann[-1])
        if copy_video:
            cmd = f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}.mp4"'
        else:
            cmd = f'ffmpeg -i "{filename}"'
        for i in range(num_channels):
            cmd += f' -map 0:a:{i} -c copy "{outname}_{i}.aac"'
    else:
        channel = int(selected_channels) - 1
        if copy_video:
            cmd = f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}.mp4"'
        else:
            cmd = f'ffmpeg -i "{filename}"'
        cmd += f' -map 0:a:{channel} -c copy "{outname}_{channel}.aac"'
    try:
        extct = subprocess.Popen(cmd, shell=True, universal_newlines=True,cwd=ffmpeg_path)
        extct.wait()
        os.startfile(os.path.dirname(fr'{outname}'))
    except:
        print("Extracting Failed")
        
        
    #exit Options
    closeOptions = funcs.mChoiceQeustion("Extract again, Download Again, Remux media or Exit", ["Extract", "Download", "Remux", "Exit"])
    if closeOptions == "Remux":
        from cpyVid_scritp_____1 import mux
        os.system('cls')
        mux()
    elif closeOptions == "Download":
        os.system('cls')
        from Main import main_script
        main_script()
    elif closeOptions == "Extract":
        ffmpegextract()
    else:
        exit()

if __name__ == "__main__":
    ffmpegextract()
