# import webbrowser
# import os
# import time

# acptLst = ["yes", "y"]
# check_in = 0

# def chk_sLink():
#     if check_in >= 0:
#         isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
#         return (isthere)
#     elif check_in > 0:
#         print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n")
#         ipt_asw = input("Launch Website?\ny/n?: ").lower()
#         if ipt_asw in acptLst:
#             webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")

# installed = chk_sLink()


# while installed is False:
#     check_in = +1
#     if check_in > 0:
#         print(check_in)
#         print(installed)
#         time.sleep(7)
#         got_it = input("Has the Program been installed yet?\ny/n?:").lower()
#         chk_sLink()
#     elif check_in == 0:
#         print(check_in)
#         print(installed)
#         chk_sLink()
#     else: 
#         break
    
    
# # ---------------------------------------------------
    
import webbrowser
import os
import time

acptLst = ["yes", "y"]
check_in = 0
isthere = False
while True:
    isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
    if isthere is False and check_in == 0:
        print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n")
        ipt_asw = input("Auto Launch Website?\ny/n?: ").lower()
        if ipt_asw in acptLst:
            webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
            check_in = +1
        else:
            check_in = +1
            continue
    elif check_in >= 0 and isthere == False:
        print("\nWaiting for Installation...")
        time.sleep(7)
        got_it = input("\nHas Streamlink been installed yet?\ny/n?:").lower()
        if got_it in acptLst and isthere is False:
            got_it = input("\nHaven't Found Stream Link In File Path\nC.Program.Files.Streamlink.bin      Are you sure? y/n?:").lower()
        elif got_it not in acptLst:
            print("\nWaiting!......")
            time.sleep(5)
    else:
        break
    
    
    
    

# def chk_if_got():
#     time.sleep(2)
#     got_it = input("Has the Program been installed yet?\ny/n?:").lower()
#     if got_it in acptLst:
#         chk_sLink()
#     else:
#         return ("no")
# done_it = chk_if_got()
# print(done_it)


# # print(done_it)
# while isthere is False:
#     if got_it is False:
#         chk_sLink
#     elif done_it == "no":
#         chk_if_got()
#     else:
#         break




# # print("completed")



import os
import time

isthere = False
while True:
    isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlinkAA.exe")
    time.sleep(4)
    print(isthere)

# from Tryinh_to_Loop_ask_if_have_STLK import acptLst

# from threading import Timer
# def exit():
#     print("Times UP!!!!!!!!!!")
    
# input_time=int(5)
# t = Timer(input_time, exit)
# t.start()
# prompt = "You have %d seconds to choose the correct answer.................\n" % input_time
# answer = input(prompt)
# if answer in acptLst:
#     print("Good Job")
# else:
#     exit()


# k = "https://www.twitch.tv/videos/1655550906?filter=archives&sort=time"
# print("/".join(k.split("/")[:-1]))

# url = "https://www.twitch.tv/videos/1655550906?t=03h09m37s"
# new_url = url.replace("?filter=archives&sort=time","")
# print(new_url)
# import subprocess
import os
# ; os.system('start cmd /K python bb.py')
# os.system('start cmd /K python bb.py')


