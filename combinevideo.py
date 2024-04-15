# ffmpeg -f concat -safe 0 -i mylist.txt -c copy "output.mp4"
import os
import subprocess

from helpers import funcs

combine_return = funcs.multi_choice_dialog(mssg="Combine Video Files", choice_s=["Yes", "Cancel"])

if combine_return == "Cancel":
    print("restart")
    pass


print("Select Main Video File\n")

video_file_list = []
def gather_video_files(video_file_list):
    video_file = funcs.openFile()
    video_file_list.append(f'file "{video_file}"')
    if len(video_file_list) >= 2:
        [print(funcs.shorten_path_name(item)) for item in video_file_list]
        continue_appending = funcs.multi_choice_dialog(mssg="Append More Files?", choice_s=["Yes", "Cancel"])
        if continue_appending == "Cancel":
            return video_file_list
        print("Choose video file to append\n")
        return gather_video_files(video_file_list)
    else:
        print("Choose video file to append\n")
        [print(funcs.shorten_path_name(item)) for item in video_file_list]
        return gather_video_files(video_file_list)

vid_list = gather_video_files(video_file_list)


save_path = funcs.saveFile(kwargs=os.path.basename(vid_list[0]))

cpy = subprocess.Popen(rf'ffmpeg -f concat -safe 0 -i "{vid_list}" -c copy "{save_path}"', universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="c:/Program Files/Streamlink/ffmpeg/")

stdout, stderr = cpy.communicate()
print(stdout)

# .txt Eg, it need to be in the cwd of the video??? 
# file 'Kotton - 25-10-2023 Not Sure If Surviving or Thriving 500 BrutalCassandra  mods_RimWorld.mp4'
# file '2Kotton - 25-10-2023 Not Sure If Surviving or Thriving 500 BrutalCassandra  mods_RimWorld.mp4'



print(vid_list)