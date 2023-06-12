import os
import subprocess

from numpy import append

import funcs


def ffmpegextract():
    #FIXIT if file is NOT muxed it returns [ALL 0 0 Exit] channels
    check_settings = funcs.loadSettings(['LastSave', 'ffprobepath', 'ffmpegpath'])
    fresh_save = [funcs.is_less_than_30days(check_settings[0])]
    fresh_save.extend(check_settings[1:3])
    print("🐍 File: Stream-Downloader-Util/ffmpegExtract.py | Line: 14 | ffmpegextract ~ fresh_save",fresh_save)

    if not all(fresh_save):
        funcs.ffprobe_factory_init(["ffmpegExtract", "ffmpegextract"])
        funcs.ffmpeg_factory_init(["ffmpegExtract", "ffmpegextract"])
        os.system('cls')
        ffmpegextract()
    ffmpeg_dir = os.path.dirname(check_settings[2])
    probe_dir = os.path.dirname(check_settings[1])

    filename = funcs.file_path_get()
    if not (any(filename.endswith(media_type)
                for media_type in funcs.video_file_types)):
        print("\nNot a Valid File type to Extract Streams From Try again.")
        ffmpegextract()
        
    file_type = funcs.video_file_exetension_return(filename)
    
    mxChann = []
    opus = ""
    try:
        chanReturn = funcs.channelsSplit(probe_dir, filename)
        print("🐍 File: Stream-Downloader-Util/ffmpegExtract.py | Line: 34 | ffmpegextract ~ chanReturn",chanReturn)
        result = chanReturn[1:]
        mxChann = [x for t in result for x in t]
        opus = chanReturn[0] #FIX Opus still not working
        print("🐍 File: Streamlink.Automated.Downloader/ffmpegExtract.py | Line: 40 | ffmpegextract ~ opus",opus)
    except subprocess.CalledProcessError as ce:
        os.system('cls')
        ffmpegextract()
    chan = ["All"] + mxChann + ["Exit"]

    # Inputs questions
    message = "Which audio channels would you like to extract?"
    answers = funcs.multi_choice_dialog(message, chan, "int", "channels")
    selected_channels = answers["channels"]

    if selected_channels == "Exit":
        os.system("cls")
        funcs.main_start()

    message = "Do you want to extract the video stream?"
    answers = funcs.multi_choice_dialog(message, ["Yes", "No"], "int")
    copy_video = answers["Key"] == "Yes"

    # creates adjacent Dir
    name = os.path.splitext(os.path.basename(filename))[0]
    outname = os.path.join(os.path.dirname(filename),
                            f"{name} audio streams", name)
    os.makedirs(os.path.dirname(outname), exist_ok=True)
    
    
    # [] Split to a Class?
    if selected_channels == "All":
        num_channels = int(mxChann[-1])
        if copy_video:
            cmd = f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}{file_type}"'
        else:
            cmd = f'ffmpeg -i "{filename}"'
        for i in range(num_channels):
            cmd += f' -map 0:a:{i} -c copy "{outname}_{i}.aac"'
    else:
        if copy_video == True and opus == "opus":
            cmd = f'ffmpeg -i "{filename}" "{outname}{file_type}"' #FIX anothr line to convert vp9 not just copy and switch needed this copies vp9 atm and if OpUS audio Not vp9 Vid
        channel = int(selected_channels) - 1
        if copy_video:
            cmd = f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}{file_type}"'
        else:
            cmd = f'ffmpeg -i "{filename}"'

        if opus == "opus":
            cmd += f' && ffmpeg -i "{filename}" "{outname}_{channel}.aac"'
        else:
            cmd += f' -map 0:a:{channel} -c copy "{outname}_{channel}.aac"'

    try:
        extct = subprocess.Popen(cmd, shell=True, universal_newlines=True,
                                    cwd=ffmpeg_dir)
        extct.wait()
        os.startfile(os.path.dirname(fr'{outname}'))
    except subprocess.CalledProcessError as ce:
        ffmpegextract()
    except Exception:
        print("Extracting Failed")


    funcs.main_start()

if __name__ == "__main__":
    ffmpegextract()
