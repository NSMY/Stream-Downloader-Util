import webbrowser
import os
import time

acptLst = ["yes", "y"]

def chk_sLink():
    isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlink.exe")
    if isthere is False:
        print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nTo download Streamlink and install it.\n")
        ipt_asw = input("Launch Website?\ny/n?:").lower()
        if ipt_asw in acptLst:
            webbrowser.open("https://github.com/streamlink/windows-builds/releases/latest")
    return (isthere)
    
installed = chk_sLink
print(installed)
chk_sLink()

# def chk_if_got():
#     time.sleep(2)
#     if got_it in acptLst:
#         chk_sLink()
#     else:
#         return ("no")
# got_it = input("Has the Program been installed yet?\ny/n?:").lower()
# done_it = chk_if_got()


# # print(done_it)
# while isthere is False:
#     if got_it is False:
#         chk_sLink
#     elif done_it == "no":
#         chk_if_got()
#     else:
#         break




# # print("completed")
