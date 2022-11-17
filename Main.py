import os
from pyperclip import copy, paste
#clipboard.copy("goosfrabe")  # now the clipboard content will be string "abc"
text = paste()  # text will have the content of clipboard

def chk_sLink():
    isthere = os.path.exists(r"C:\Program Files\Streamlink\bin\streamlink.exe")
    if isthere is False:
        print("\nYou do not seem to have streamLink installed.\nPlease Visit:\nhttps://github.com/streamlink/windows-builds/releases/latest\nto download Streamlink and install it\n")

chk_sLink()

sizes = ["worst", "160p", "360p", "480p", "720p", "720p60", "1080p", "1080p60", "source", "best"]
name_of_File = input("Enter File Name:\n")

# dir_path = ""


file_path = fr'"E:\DeleteStreams\New folder\{name_of_File}.mp4"'


def check_size(Vid_size):
    # print(Vid_size in sizes) Checks if True/False
    if Vid_size in sizes:
        return fr'cd C:\Program Files\Streamlink\bin && streamlink "{text}" {Vid_size} --hls-segment-threads 5 -o {file_path}'
    else:
        return ("Enter a Valid Size")     
Fake_ = ""
while True:
    if Fake_ == "":  
        Size_string = input("Please enter size of Vid, worst, 160p, 360p, 480p, 720p, 720p60, 1080p60, source, best:\n").lower()  #stores Input into size_string Variable
        cmd_Str = check_size(Size_string)       #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
        Fake_ = "1"
    
    elif cmd_Str == "Enter a Valid Size":
        Size_string = input("Enter a Valid Size\nworst, 160p, 360p, 480p, 720p, 720p60, 1080p60, source, best:\n")  #stores Input into size_string Variable
        cmd_Str = check_size(Size_string)       #Runs Check_Size with Size_string {inputDATA} and Returns(stores) check-size if/else into cmd_Str Var
    else:
        print(cmd_Str)
        os.system(f'cmd /k "echo {cmd_Str}"')
        break
