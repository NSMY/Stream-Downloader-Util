import os
import winsound

from send2trash import send2trash

dir = r'C:\Users\970EVO-Gamer\AppData\Local\Stream-Downloader-Util'
for files in os.listdir(dir):
    if not os.path.isdir(files):
        print(f'{dir}/{files}')

# def send_to_trash(input_name):
#     send2trash(input_name)
#     if not os.path.isfile(input_name) or os.path.isdir(input_name):
#         print(f"sent {input_name} to recycler")
#         winsound.PlaySound(
#             sound="C:\\Windows\\Media\\Recycle.wav",
#             flags=winsound.SND_FILENAME
#         )
#         return True
#     return False


# send_to_trash(r"C:\Users\970EVO-Gamer\Desktop\whaaa")

