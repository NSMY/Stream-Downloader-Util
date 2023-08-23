import os
import subprocess

from numpy import append

import funcs
import init_files
from extraction_factory import VideoBlueprint


def ffmpegextract():
    #FIXIT if file is NOT muxed it returns [ALL 0 0 Exit] channels
    try:
        check_settings = funcs.loadSettings(['LastSave', 'ffprobepath', 'ffmpegpath'])
    except FileNotFoundError as e:
        init_files.initSettings()
        ffmpegextract()
    fresh_save = [funcs.is_less_than_30days(check_settings[0])]
    fresh_save.extend(check_settings[1:3])

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
        chanReturn = funcs.audio_channel_get_info(probe_dir, filename)
        result = chanReturn[1:]
        mxChann = [x for t in result for x in t]
        opus = chanReturn[0] #FIX Opus still not working
    except subprocess.CalledProcessError as ce:
        os.system('cls')
        ffmpegextract()
    channels_list = ["All"] + mxChann + ["Exit"]

    # Inputs questions
    message = "Which audio channels would you like to extract?"
    Channel_answers = funcs.multi_choice_dialog(message, channels_list, "int", "channels")
    selected_channels = Channel_answers["channels"]

    if selected_channels == "Exit":
        os.system("cls")
        funcs.main_start()

    message = "Do you want to extract the video stream?"
    video_answers = funcs.multi_choice_dialog(message, ["Yes", "No"], "int")
    copy_video = video_answers["Key"]
    
    # creates adjacent Dir
    name = os.path.splitext(os.path.basename(filename))[0]
    outname = os.path.join(os.path.dirname(filename),
                            f"{name} audio streams", name)
    os.makedirs(os.path.dirname(outname), exist_ok=True)
    
    num_channels = int(mxChann[-1])
    
    ###########factory Here<<<<<<<<<
    vid_initializer = VideoBlueprint(
    filename=filename,
    output_name=outname,
    copy_video_answer=copy_video,
    selected_channel=selected_channels,
    total_num_channels=num_channels,
    input_audio_codec_type=opus,
    video_file_type=file_type,
    export_codec=".aac", #non implemented choice export codec
    )
    
    
    if opus == "opus":
        command = vid_initializer.opus_factory()
    elif copy_video == "Yes":
        command = vid_initializer.video_extraction()
    else:
        command = vid_initializer.non_video_extraction()

    try:
        extct = subprocess.Popen(command, shell=True, universal_newlines=True,
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
