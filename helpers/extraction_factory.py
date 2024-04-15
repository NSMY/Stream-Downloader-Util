
class VideoBlueprint:
    def __init__(
        self,
        filename: str,
        output_name: str,
        copy_video_answer: bool,
        selected_channel,
        total_num_channels: int,
        input_audio_codec_type: str,
        video_file_type: str,
        export_codec=".aac",
    ):
        self.filename = filename
        self.output_name = output_name
        self.copy_video_answer = copy_video_answer
        self.selected_channel = selected_channel
        self.total_num_channels = total_num_channels
        self.input_audio_codec_type = input_audio_codec_type
        self.video_file_type = video_file_type
        self.export_codec = export_codec

    def video_extraction(self):
        command = (f'ffmpeg -i "{self.filename}" -map 0:v -c copy'
                    f' "{self.output_name}{self.video_file_type}"'
                    )
        if self.selected_channel == "All":
            return f'{command}  && ffmpeg -i "{self.filename}" {self.all_audio_channels_extracted()}'
        return f'{command}{self.specified_audio_channel()}'
    
    def non_video_extraction(self):
        if self.selected_channel != "All":
            return self.specified_audio_channel()
        cmd = (f'ffmpeg -i "{self.filename}"')
        cmd += (f'{self.all_audio_channels_extracted()}')
        return cmd

    def opus_factory(self):
        cmd = (f'ffmpeg -i "{self.filename}" -c:v copy -an '
                f'"{self.output_name}{self.video_file_type}"')
        
        if self.selected_channel == "All":
            channels_list = "".join(
                f' -map 0:a:{i} "{self.output_name}_{i}{self.export_codec}"'
                for i in range(self.total_num_channels)
                )
            if self.copy_video_answer == "Yes":
                return f'{cmd} && ffmpeg -i "{self.filename}"{channels_list}'
            else:
                return f'ffmpeg -i "{self.filename}" {channels_list}'
        channel = int(self.selected_channel) -1
        
        if self.copy_video_answer == 'No':
            return (f'ffmpeg -i "{self.filename}" -map 0:a:{channel} '
                    f'"{self.output_name}_{self.selected_channel}{self.export_codec}"'
                    )
        cmd += (f' && ffmpeg -i "{self.filename}" -map 0:a:{channel} '
                f'"{self.output_name}_{self.selected_channel}{self.export_codec}"'
                )
        return cmd

    def specified_audio_channel(self):
        channel = int(self.selected_channel) - 1
        if self.copy_video_answer == "No":
            return (f'ffmpeg -i "{self.filename}" -map 0:a:{channel}'
                    f' -c copy "{self.output_name}_{channel}{self.export_codec}"'
                    )
        return (f'&& ffmpeg -i "{self.filename}" -map 0:a:{channel}'
                    f' -c copy "{self.output_name}_{channel}{self.export_codec}"'
                    )

    def all_audio_channels_extracted(self):
        cmdd = ''
        for i in range(self.total_num_channels):
            cmdd += f' -map 0:a:{i} -c copy "{self.output_name}_{i}{self.export_codec}"'
        return cmdd
    
    def __str__(self):
        return (
            f"filename={self.filename},"
            f"output_name={self.output_name},"
            f"copy_video_answer={self.copy_video_answer},"
            f"selected_channel={self.selected_channel},"
            f"total_num_channels={self.total_num_channels},"
            f"input_audio_codec_type={self.input_audio_codec_type},"
            f"video_file_type={self.video_file_type},"
            f"export_codec={self.export_codec}"
        )

