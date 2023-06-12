def all_audio_channels_extracted(outname, num_channels, is_opus, codec='.aac'):
    cpy_str = '' if is_opus == "opus" else '-c copy '
    return ''.join(
        f' -map 0:a:{i} {cpy_str}"{outname}_{i}{codec}"'
        for i in range(num_channels))

print(all_audio_channels_extracted("output_", 4, "opus", ".aac"))




def video_extraction():
    assigned_channel = int(selected_channels) - 1
    if copy_video == True and opus == "opus":
        f'ffmpeg -i "{filename}" -c:v copy -an "{outname}{file_type}"' #No Audio
    if copy_video:
        return f'ffmpeg -i "{filename}" -map 0:v -c copy "{outname}{file_type}"'
    if encode == True and opus == "opus":
        return f'ffmpeg -i "{filename}" "{outname}{file_type}"' #FIX anothr line to convert vp9 not just copy and switch needed this copies vp9 atm and if OpUS audio Not vp9 Vid
    else:
        return  ''

''' webm
ffmpeg -i Source_File.mov -c:v libvpx-vp9 -pix_fmt yuva420p New_File.webm

with audio
ffmpeg -i Source_File.mov -c:v libvpx-vp9 -pix_fmt yuva420p -c:a libvorbis New_File.webm
'''


def specific_audio_extraction(cmd, outname, channel, video_inc, is_opus, codec='.aac'):
    concat_vid_aud = '' if video_inc == "opus" else ' && ffmpeg -i '
    if is_opus == "opus":
        cmd += f'{concat_vid_aud}"{filename}" "{outname}_{channel}{codec}"'
    cmd += f'{concat_vid_aud}"{filename}" -map 0:a:{channel} -c copy "{outname}_{channel}{codec}"'