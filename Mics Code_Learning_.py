# # # import webbrowser
# # # import os
# # # import time

# # # acptLst = ["yes", "y"]
# # # check_in = 0

# # # def chk_sLink():
# # #     if check_in >= 0:
# # #         isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
# # #         return (isthere)
# # #     elif check_in > 0:
# # #         print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n")
# # #         ipt_asw = input("Launch Website?\ny/n?: ").lower()
# # #         if ipt_asw in acptLst:
# # #             webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")

# # # installed = chk_sLink()


# # # while installed is False:
# # #     check_in = +1
# # #     if check_in > 0:
# # #         print(check_in)
# # #         print(installed)
# # #         time.sleep(7)
# # #         got_it = input("Has the Program been installed yet?\ny/n?:").lower()
# # #         chk_sLink()
# # #     elif check_in == 0:
# # #         print(check_in)
# # #         print(installed)
# # #         chk_sLink()
# # #     else: 
# # #         break
    
    
# # # # ---------------------------------------------------
    
# # import webbrowser
# # import os
# # import time

# # acptLst = ["yes", "y"]
# # check_in = 0
# # isthere = False
# # while True:
# #     isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
# #     if isthere is False and check_in == 0:
# #         print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n")
# #         ipt_asw = input("Auto Launch Website?\ny/n?: ").lower()
# #         if ipt_asw in acptLst:
# #             webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
# #             check_in = +1
# #         else:
# #             check_in = +1
# #             continue
# #     elif check_in >= 0 and isthere == False:
# #         print("\nWaiting for Installation...")
# #         time.sleep(7)
# #         got_it = input("\nHas Streamlink been installed yet?\ny/n?:").lower()
# #         if got_it in acptLst and isthere is False:
# #             got_it = input("\nHaven't Found Stream Link In File Path\nC.Program.Files.Streamlink.bin      Are you sure? y/n?:").lower()
# #         elif got_it not in acptLst:
# #             print("\nWaiting!......")
# #             time.sleep(5)
# #     else:
# #         break
    
    
    
    

# # # def chk_if_got():
# # #     time.sleep(2)
# # #     got_it = input("Has the Program been installed yet?\ny/n?:").lower()
# # #     if got_it in acptLst:
# # #         chk_sLink()
# # #     else:
# # #         return ("no")
# # # done_it = chk_if_got()
# # # print(done_it)


# # # # print(done_it)
# # # while isthere is False:
# # #     if got_it is False:
# # #         chk_sLink
# # #     elif done_it == "no":
# # #         chk_if_got()
# # #     else:
# # #         break




# # # # print("completed")



# # import os
# # import time

# # isthere = False
# # while True:
# #     isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
# #     time.sleep(4)
# #     print(isthere)

# # # from Tryinh_to_Loop_ask_if_have_STLK import acptLst

# # # from threading import Timer
# # # def exit():
# # #     print("Times UP!!!!!!!!!!")
    
# # # input_time=int(5)
# # # t = Timer(input_time, exit)
# # # t.start()
# # # prompt = "You have %d seconds to choose the correct answer.................\n" % input_time
# # # answer = input(prompt)
# # # if answer in acptLst:
# # #     print("Good Job")
# # # else:
# # #     exit()


# # from Tryinh_to_Loop_ask_if_have_STLK import acptLst

# # # url = "https://www.twitch.tv/videos/1655550906?t=03h09m37s"
# # # new_url = url.replace("?filter=archives&sort=time","")
# # # print(new_url)
# # # import subprocess
# import os
# # # ; os.system('start cmd /K python bb.py')
# # # os.system('start cmd /K python bb.py')


# # # import streamlink

# # # streams = streamlink.streams("hls://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8")

# # import subprocess


# # p = subprocess.Popen([r"C:\\Program Files\\Avidemux 2.7 VC++ 64bits\\avidemux.exe", r"E:\\DeleteStreams\\New folder\\wtsFM.mp4"])
# # # ... do other things while notepad is running
# # returncode = p.wait() # wait for notepad to exit

# # def chk_inst(per1, per2):
# #     return per1 + per2
# #     isthere = os.path.isfile(r"C:\Program Files\Streamlink\bin\streamlink.exe")
# #     isthere_86 = os.path.exists(r"C:\Program Files (x86)\Streamlink\bin\streamlink.exe")


# # chk_inst(1, 6)
# # print(type(chk_inst))
# # print("chk_inst")
# # if chk_inst == 7:
# #     print("seven")
# # else:
# #     print("passer")
# import time, os, webbrowser
# from pyperclip import paste


# #Retrieves Last item in Clipboard(ctrl v)
# #clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
# clp_brd = paste()  # text will have the content of clipboard
# url_ = clp_brd.replace("?filter=archives&sort=time","")


# accp_lst = {"yes": ["y", "yes"], "no": ["n", "no"]}

# def chk_if_Install():
#     stlink = []
#     stlink.append(os.path.isfile("C:\\Program Files\Streamlink\\bin\\streamlink.exe"))
#     stlink.append(os.path.isfile("C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"))
#     return stlink


# def setLink_Path():
#     if (chk_if_Install()[0]) == True:
#         lnk_pth = "C:\\Program Files\\Streamlink\\bin\\"
#         return lnk_pth
#     elif (chk_if_Install()[1]) == True:
#         lnk_pth = "C:\\Program Files (x86)\\Streamlink\\bin\\"
#         return lnk_pth            
#     else:
#         return ("404 Not Here")

# stream_lnk_Path = ""
# swtch = 1

# while stream_lnk_Path != "c":
#     stream_lnk_Path = setLink_Path()
#     if stream_lnk_Path == "404 Not Here" and swtch == 1:
#         swtch = +2
#         ipt_asw = input(f"\nYou do not seem to have streamLink installed.\n\nPlease "
#                 "Visit: https://github.com/streamlink/windows-builds/releases/latest\nTo download "
#                 "Streamlink and install it.\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe----\nOR"
#                 "\nAuto Launch Website? y/n?: ").lower()
#         if ipt_asw in accp_lst["yes"]:
#             webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
#             print("\nWaiting for Installation...")
#             time.sleep(15)
#         else:
#             print("\nWaiting for Installation...")
#             time.sleep(7)               # TEMPORARY CODE ----15
#     elif swtch >= 0 and stream_lnk_Path == "404 Not Here":
#             swtch = +2
#             got_it = input("\nHas Streamlink been installed?\ny/n?:").lower()
#             stream_lnk_Path = setLink_Path()
#             time.sleep(5)
#             if got_it in accp_lst["yes"] and stream_lnk_Path == "404 Not Here":
#                 stream_lnk_Path = setLink_Path()
#                 lie_chk = input("\nHaven't Found Streamlink In File Path C\\Program (or {x86}) \\Files\\Streamlink\\bin\\"
#                                 "   Are you sure it is there?\nDo you need the website again? y/n?:").lower()
#                 time.sleep(5)
#                 if lie_chk in accp_lst["yes"]:
#                     webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
#                     print("\nWaiting!......")
#                     time.sleep(7)
#                 elif stream_lnk_Path == "404 Not Here":
#                     time.sleep(8)# 21 ----
#                     print("\nPlease Check: C\\Program (or {x86}) \\Files\\Streamlink\\bin\\ Path")
#             else:
#                 time.sleep(12)
                
#     else:
#         break

# # if True in kii:
# #     print('bloop')


# # #########################-old CHeck if installed Loop lol-###############################
# # while True:
# #     isthere = os.path.isfile(r"C:\Program Files\Streamlink\bin\streamlink.exe")
# #     isthere_86 = os.path.exists(r"C:\Program Files (x86)\Streamlink\bin\streamlink.exe")
# #     if check_in == 0 and isthere is False:
# #         if isthere_86 is False:
# #             print(f"\nYou do not seem to have streamLink installed.\nPlease "
# #                     "Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download "
# #                     "Streamlink and install it.\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe----\n")
# #             ipt_asw = input("Auto Launch Website?\ny/n?: ").lower()
# #             if ipt_asw in acptLst:
# #                 webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
# #                 check_in = +1
# #             else:            
# #                 check_in = +1
# #                 continue
# #         else:
# #             break
# #     elif check_in >= 0 and isthere is False:
# #         if isthere_86 is False:
# #             print("\nWaiting for Installation...")
# #             time.sleep(7)
# #             got_it = input("\nHas Streamlink been installed yet?\ny/n?:").lower()
# #             if got_it in acptLst and isthere is False or isthere_86 is False:
# #                 lie_chk = input("\nHaven't Found Stream Link In File Path\nC.Program.Files.Streamlink.bin"
# #                                 "      Are you sure? y/n?:").lower()
# #             elif lie_chk not in acptLst:
# #                 print("\nWaiting!......")
# #                 time.sleep(20)
# #         else:
# #             break
# #     else:
# #         break



# # if chk_inst == 7:
# #     print("seven")
# # else:
# #     print("passer")
# """
# import subprocess

# subprocess.run({fr"C:\Program Files\Avidemux 2.7 VC++ 64bits\avidemux.exe"}) """

import subprocess, re, sys, time, os
import os
os.system('cls' if os.name == 'nt' else 'clear')
# file_path = fr"C:\Users\970EVO-Gamer\Desktop\2rdfolder\4thfolder\file.txt"


# #dir is not keyword
# def makemydir(whatever):
#     try:
#         os.makedirs(whatever)
#     except OSError:
#         print("already exists")
#         pass
#     # let exception propagate if we just can't
#     # cd into the specified directory
#     os.chdir(whatever)
# makemydir(file_path)

#     '''Thanks https://stackoverflow.com/questions/57562590/how-
# to-insert-a-directory-in-the-middle-of-a-file-path-in-python'''
# file_path0 = f"{file_path}"
# p = PurePath(file_path0)
# p.parts
# ('dir1', 'dir2', 'dir3', 'dir4', 'file.txt')
# spam = list(p.parts)
# newpart = spam.insert(-1, 'Re_Copied')
# new_path = PurePath('').joinpath(*spam)
# PurePosixPath('dir1/dir2/new_dir/dir3/dir4/file.txt')

# print(new_path)


# file_path = fr"C:\Users\970EVO-Gamer\Desktop\File_Name.mp4"
# # process2 = subprocess.Popen(fr'cd C:\Program Files\Streamlink\ffmpeg && ffmpeg -i "E:\DeleteStreams\New folder\fasaf.mp4" -c copy "C:\Users\970EVO-Gamer\Desktop\fasaf.mp4"', shell=True)
# new_file = f"{file_path}".replace(".mp4", ".mov")
# new_file2 = new_file.split("\\")
# print(new_file)
# print(new_file2)
# new_file2.insert(-1,"Re_Copied")
# print(new_file2)
# new_file3 = new_file2
# print(new_file3)




# # jank ass code to get dynamic 
# subprocess.call('cd C:\\Program Files\\Streamlink\\bin', shell=True)
# stream = subprocess.Popen("streamlink https://www.youtube.com/watch?v=SNq4C988FjU", stdout=subprocess.PIPE, universal_newlines=True)
# out = str(stream.communicate())
# out1 = out.replace("\\n'", "")
# string = re.sub(pattern = "[^\w\s]",
#         repl = "",
#         string = out1)
# str2 = string.split()
# sss = str(str2[10:-1])


# print(out)
# print(string)
# print(sss)

# def chk_if_Install():
#     print("Re Run")

# # subprocess.call('cd C:\\Program Files\\Streamlink\\bin', shell=True)
# process = subprocess.Popen(f"cd C:\\Program Files\\Streamlink\\bin && streamlink https://www.youtube.com/watch?v=SNq4C988FjU 480p", shell=True)
# process.wait()
# out = str(process.communicate())

# time.sleep(10)
# exit = input("\nRe Run Program? y/n:").lower()  
# if exit == "yes":
#     chk_if_Install()
# else:
#     sys.exit ()

# out1 = out.replace("\\n'", "")
# string = re.sub(pattern = "[^\w\s]",
#         repl = "",
#         string = out1)
# str2 = string.split()
# sss = str(str2[10:-1])


# print(out)
# print(string)
# print(sss)





# ress = ('out: {0}'.format(out))


# ress1 = ress.replace("\\n", "")
# ress2 = ress1.replace("'", "")

# ress3 = ress2.split()
# sss = str(ress3[10:-1])
# print(sss)
# print(str(ress3[10:-1]))
# # ress3.sort[8]
# out1 = out.split()
# print(out1)
# print(ress)
# print(ress1)
# print(ress2)
# print(ress3)


# ress = subprocess.run('cd C:\Program Files\Streamlink\\bin && streamlink https://www.twitch.tv/videos/1658617982', shell=True, stdout=subprocess.PIPE, text=True)

# # # stream = subprocess.Popen(streamlink https://www.twitch.tv/videos/1658617982", stdout=subprocess.PIPE, universal_newlines=True)
# # # out = stream.communicate()

# # ress1 = ('ress: {0}'.format(ress))

# ress.stdout
# ress1 = str(ress.split())
# # ress2 = ress1.split(",")
# print(ress1)
# # print(ress1)
