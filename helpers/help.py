def main():
    import os

    import startup
    os.system('cls')
    print("{:<35} {:<10}".format('\nStandard Download: ', 'Downloads the URL thats stored in your Clipboard'))
    print("{:<35} {:<10}".format('\nRe-Mux:', 'Mux\'es (if not discontinuous/Chunked just copies) Combines Chunked Streams into a continuous File.'))
    print("{:<35} {:<10}".format('\nExtract Audio/Video:', 'Extracts the Audio/Video Streams of a File into their own Files, Preserves Original File.'))
    print("{:<35} {:<10}".format('\nDownload W/ Shutdown:', 'Downloads Chosen source and Calls Shutdown Command after completion'))
    print("{:<35} {:<10}".format('', '(Default 3min after Completion OR can be set to Custom Time in the future with [Manual] option).'))
    print("{:<35} {:<10}".format('\nVod From File:', 'Creates a Popup of Vods from x person (Created from: Create New Vods File) and downloads a file selected.'))
    print("{:<35} {:<10}".format('\nUpdate Vods File:', 'Updates already existing files with new Vods not existing in the file list.'))
    print("{:<35} {:<10}".format('\nList View File:', 'Creates a popup of x streamers Vods for manual changing of download status and General view of available vods.'))
    print("{:<35} {:<10}".format('\nCross-check Vods to Json Data:', 'Cross-checks Video Files properties (from selected Parent folder) with stored json data to check if the file is "downloaded"'))
    print("{:<35} {:<10}".format('', 'and sets to Json "downloaded" Status if criteria met.'))
    print("{:<35} {:<10}".format('Criteria', '[Not previously set, VideoUsername==JsonDisplayName, VideoTitle==JsonTitle, VideoLength==JsonLength]'))
    print("{:<35} {:<10}".format('Naming Files Convention == ', '(Username) (YYYY-MM-DD) (TitleOfStream)_StreamCategory\n\n\n'))
    return startup.main_start()


if __name__ == '__main__':
    main()
