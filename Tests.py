class VideoBlueprint:
    
    def __init__(self, filename, output_name, copy_video, selected_channel, num_channels, is_opus, codec=".aac"):
        self.filename = filename
        self.output_name = output_name
        self.copy_video = copy_video
        self.selected_channel = selected_channel
        self.num_channels = num_channels
        self.is_opus = is_opus
        self.codec = codec
    
    
    
    def all_audio_channels_extracted(self):
        cpy_str = '' if self.is_opus == "opus" else '-c copy '
        return ''.join(
            f' -map 0:a:{i} {cpy_str}"{self.output_name}_{i}{self.codec}"'
            for i in range(self.num_channels))

    print(all_audio_channels_extracted("output_", 4, "opus", ".aac"))




    def video_extraction(self):
        assigned_channel = int(self.selected_channel) - 1
        if self.copy_video:
            return self.standard_audio(
                f'ffmpeg -i "{self.filename}" -map 0:v -c copy "{self.output_name}{self.filename}"')
            
            
            return f'ffmpeg -i "{self.filename}" "{self.output_name}{self.filename}"'
        else:
            return self.standard_audio('')
        '''
            return f'ffmpeg -i "{self.filename}" "{self.output_name}{self.filename}"' 
        
        
        f'ffmpeg -i "{self.filename}" -c:v copy -an "{self.output_name}{self.filename}"' #No Audio
            webm
        ffmpeg -i Source_File.mov -c:v libvpx-vp9 -pix_fmt yuva420p New_File.webm

        with audio
        ffmpeg -i Source_File.mov -c:v libvpx-vp9 -pix_fmt yuva420p -c:a libvorbis New_File.webm
        '''


    def standard_audio(self, command=''):
        if self.copy_video == False:
            return f'ffmpeg -i "{self.filename}" -map 0:a:{self.selected_channel} -c copy "{self.output_name}_{self.selected_channel}{self.codec}"'
        command += f' && ffmpeg -i "{self.filename}" -map 0:a:{self.selected_channel} -c copy "{self.output_name}_{self.selected_channel}{self.codec}"'
        return command
        


    def specific_audio_extraction(self, cmd, outname, selected_channel, video_inc, is_opus, codec='.aac'):
        cmd += f'{concat_vid_aud}"{self.filename}" -map 0:a:{self.selected_channel} -c copy "{outname}_{self.selected_channel}{codec}"'
    
    
    def opus_factory(self):
        if self.copy_video == True and self.is_opus == "opus":
            cmd = f'ffmpeg -i "{self.filename}" -c:v copy "{self.output_name}{self.filename}"'

            cmd += f' && ffmpeg -i "{self.filename}" "{self.output_name}_{self.selected_channel}{self.codec}"'
    