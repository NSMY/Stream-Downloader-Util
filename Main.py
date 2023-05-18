def main_script():
    import re
    import os
    import sys
    import time
    import subprocess
    from pyperclip import copy, paste
    import webbrowser
    from tkinter import filedialog
    import inquirer
    from urllib.parse import urlparse



    accp_lst = {"yes": ["y", "yes"], "no": ["n", "no"]}


    # checks path ----
    def chk_if_Install():
        stlink = []
        stlink.append(os.path.isfile("C:\\Program Files\Streamlink\\bin\\streamlink.exe"))
        stlink.append(os.path.isfile("C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"))
        return stlink


    def setLink_Path():
        if (chk_if_Install()[0]) == True:
            lnk_pth = "C:\\Program Files\\Streamlink\\bin\\"
            return lnk_pth
        elif (chk_if_Install()[1]) == True:
            lnk_pth = "C:\\Program Files (x86)\\Streamlink\\bin\\"
            return lnk_pth            
        else:
            return ("404 Not Here")

    #Retrieves Last item in Clipboard(ctrl v)
    #clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
    def is_url(variable):
        try:
            result = urlparse(variable)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
    clp_brd = paste()  # text will have the content of clipboard
    url_ = clp_brd.replace("?filter=archives&sort=time","")


    stream_lnk_Path = ""
    swtch = 1
    #Runs Check if streamlink is installed and gives link/opens if Not
    while stream_lnk_Path != "c":
        stream_lnk_Path = setLink_Path()
        if stream_lnk_Path == "404 Not Here" and swtch == 1:
            swtch = +2
            ipt_asw = input(f"\nYou do not seem to have streamLink installed.\n\nPlease "
                    "Visit: https://github.com/streamlink/windows-builds/releases/latest\nTo download "
                    "Streamlink and install it.\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe----\nOR"
                    "\nAuto Launch Website? y/n?: ").lower()
            if ipt_asw in accp_lst["yes"]:
                webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
                print("\nWaiting for Installation...")
                time.sleep(15)
            else:
                print("\nWaiting for Installation...")
                time.sleep(7)
        elif swtch >= 0 and stream_lnk_Path == "404 Not Here":
                swtch = +2
                got_it = input("\nHas Streamlink been installed?\ny/n?:").lower()
                stream_lnk_Path = setLink_Path()
                time.sleep(5)
                if got_it in accp_lst["yes"] and stream_lnk_Path == "404 Not Here":
                    stream_lnk_Path = setLink_Path()
                    lie_chk = input("\nHaven't Found Streamlink In File Path C\\Program (or {x86}) \\Files\\Streamlink\\bin\\"
                                    "   Are you sure it is there?\nDo you need the website again? y/n?:").lower()
                    time.sleep(5)
                    if lie_chk in accp_lst["yes"]:
                        webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
                        print("\nWaiting!......")
                        time.sleep(7)
                    elif stream_lnk_Path == "404 Not Here":
                        time.sleep(8)# 21 ----
                        print("\nPlease Check: C\\Program (or {x86}) \\Files\\Streamlink\\bin\\ Path")
                else:
                    time.sleep(12)
                    
        else:
            break

    ffmpeg_path = stream_lnk_Path.replace("\\bin\\","\\ffmpeg\\")
    
    urlchk = is_url(url_)
    while urlchk == False:   
        if urlchk == False:
            print(f"ERROR: {url_}\n")
            rs = [
                inquirer.List(
                "OP",
                message="Clipboard is NOT a URL, Copy Link Again. Recycle Program?.",
                choices=["yes", "no"],
                ),
                ]
            rs1 = inquirer.prompt(rs)
            rs2 = ''.join([str(value) for value in rs1.values()])
            if rs2 == "yes":
                #rs = input('\nClipboard is NOT a URL "y" to Restart...:').lower
                os.system('cls' if os.name == 'nt' else 'clear')
                main_script()
            elif rs2 == "no":
                sys.exit ()
        else:
            continue
        
    #opens Windows Save Folder browser and stores chosen path
    def saveFile():
        print("Save File To:... \n")
        file = filedialog.asksaveasfilename(defaultextension='.mp4',
                                            filetypes=[
                                                ("MP4 files",".mp4"),    
                                                ("MOV files",".mov"),    
                                                ("All files",".*"),
                                            ])
        if len(file) == 0: #closes Program if No Save path is Entered
            check = input("Canceled. Run again? y/n: ").lower()
            if check in accp_lst["yes"]:
                main_script()
            else:
                print("Exiting")
                sys.exit ()
        return (file)
    file_path = saveFile()

    print("Getting Resolutions...")

    # jank ass code to get dynamic resolution
    subprocess.call(f'cd {stream_lnk_Path}', shell=True)
    rw_stream = subprocess.Popen(f"streamlink {url_}", stdout=subprocess.PIPE, universal_newlines=True)
    out_pt = str(rw_stream.communicate())
    res_str_edt = out_pt.replace("\\n'", "")
    res_stripped = re.sub(pattern = "[^\w\s]",
            repl = "",
            string = res_str_edt)
    res_Options = res_stripped.split()[10:-1]
    #  -Old way-
    #res_Options = res_split[10:-1]
    #res_Options = str(res_split[10:-1])
    
    
    my_choices = list(reversed(res_Options))
    questions = [
        inquirer.List(
            "size",
            message="What size do you want?",
            choices=my_choices,
        ),
    ]
    siz_rtn = inquirer.prompt(questions)
    siz_rtn2 = ''.join([str(value) for value in siz_rtn.values()])
    print(siz_rtn2)

    #old Code
    # name_of_File = input("Enter File Name:\n")
    # file_path = fr'"E:\DeleteStreams\New folder\{name_of_File}.mp4"'

    # print(Vid_size in sizes) Checks if True/False
    def check_size(Vid_size):
        if 1<2: #Vid_size in siz_rtn:
            return fr'cd {stream_lnk_Path} && streamlink "{url_}" {Vid_size} --stream-segment-threads 5 -o "{file_path}"'
        else:
            return ("404") 
        
        
        
    Fake_ = ""
    while True:
        if Fake_ == "":  
            # Size_string = input(f"Please enter Resolution you want to download, No Quote (\'\') marks EG 720p:\n\n{siz_rtn}: ").lower()    #stores Input into size_string Variable
            cmd_Str = check_size(siz_rtn2)   #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
            Fake_ = "1"
        
        elif cmd_Str == "404":
            time.sleep(1)
            # Size_string = input(f"Enter a Valid Size, No Quote (\'\') marks EG 720p:\n{siz_rtn}: ").lower()
            cmd_Str = check_size(siz_rtn2)   #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
        else:
            process = subprocess.Popen(f"{cmd_Str}", shell=True)
            process.wait()
            break

    # Old script run ----
        # else:
        #     os.system(fr'cmd /k "{cmd_Str}"')
        #     break
    # time.sleep(10)

    convert = input("\nBecause of how Video is downloaded (Chunks) sometimes"
                    " it's needed to combine via a Re-Copying for smooth playback."
                    " \nDo you want to make a Copy of this file?\ny/n: ").lower()

    if convert in accp_lst["yes"]:
        print("\nNew File Save path....")
        new_path = filedialog.asksaveasfilename(defaultextension='.mp4',
                                            filetypes=[
                                                ("MP4 files",".mp4"),    
                                                ("MOV files",".mov"),    
                                                ("All files",".*"),
                                            ])
        process2 = subprocess.Popen(f'cd "{ffmpeg_path}" &&ffmpeg -i "{file_path}" -c copy "{new_path}"', shell=True)
        process2.wait()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nDone!!")

    exit = input("\nRe Run Program? if Yes you need to copy the next URL"
                " in the clipboard before answering this.\ny/n:").lower()  
    if exit in accp_lst["yes"]:
        main_script()
    else:
        sys.exit ()

main_script()