def read_dld_vod_filelength():
    dload_predicted_size = ''
    dld_filepath = r'E:\DeleteStreams\FFMPEG__re-Muxed\Kotton - 18-11-2023 Selling Base Today  Archonexus pt 2  500 BrutalCassandra mods RimWorld.mp4'
    slinkDir = 'C:/ffmpeg/'
    string = f'ffprobe -i "{dld_filepath}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1'
    dld_vid_size = subprocess.Popen(string, stdout=subprocess.PIPE, text=True, cwd=slinkDir)
    out_pt = dld_vid_size.stdout.read()
    # print(str(out_pt.strip()).split("'")[1])
    print(int(float(out_pt)))
    print(utill.decode_seconds_to_hms(int(float(out_pt))))