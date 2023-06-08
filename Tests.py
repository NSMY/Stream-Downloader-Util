# import signal
# import subprocess
# import threading
# import time

# import psutil


# def kill_process(process):
#     try:
#         parent = psutil.Process(process.pid)
#         for child in parent.children(recursive=True):
#             child.kill()
#         parent.kill()
#         print("Subprocess killed")
#     except psutil.NoSuchProcess as e:
#         print("Subprocess already closed")


# def wait_for_subprocess(process):
#     process.wait()
#     # Run some code after the subprocess has completed

# # Start the subprocess
# process = subprocess.Popen(f'cd C:\\Program Files\\Streamlink\\bin && streamlink "https://www.twitch.tv/videos/1838550978" best --stream-segment-threads 5 -o "E:\\DeleteStreams\\New folder\\Title_Hsd3213asere.mp4"', shell=True, universal_newlines=True)

# # Define a signal handler for SIGINT using a lambda function
# handle_sigint = lambda signal, frame: kill_process(process)

# # Register the signal handler for SIGINT
# signal.signal(signal.SIGINT, handle_sigint)

# # Start a thread to wait for the subprocess to complete
# thread_popen = threading.Thread(target=wait_for_subprocess, args=(process,))
# thread_popen.start()

# # Wait for the thread to finish
# thread_popen.join()

# # Reset the signal handler for SIGINT to its default behavior
# signal.signal(signal.SIGINT, signal.SIG_DFL)

# input("Afterr")





# # import threading
# # import psutil

# # def ask_question(proc):
# #     answer = input("Enter 'r' to restart or 'c' to cancel: ")
# #     if answer == "r":
# #         # Restart the subprocess
# #         proc.terminate()
# #         proc = subprocess.Popen(["your_download_command"])
# #     elif answer == "c":
# #         # Cancel the subprocess
# #         proc.terminate()

# # # Start the download subprocess
# # proc = subprocess.Popen(f'cd C:\\Program Files\\Streamlink\\bin && streamlink "https://www.twitch.tv/videos/1838550978" best --stream-segment-threads 5 -o "E:\\DeleteStreams\\New folder\\Title_Here.mp4"', shell=True, universal_newlines=True)

# # # Start the ask_question function in a separate thread and pass the subprocess object
# # t = threading.Thread(target=ask_question, args=(proc,))
# # t.start()

# # # Monitor the subprocess
# # while proc.poll() is None:
# #     # Check if the subprocess is taking too long
# #     if psutil.Process(proc.pid).cpu_percent() > 80:
# #         print("Subprocess is taking too long")
# #         proc.terminate()
# #         break

# # # Wait for the ask_question thread to finish
# # t.join()

# def harry():
    
#     stream_lnk_Path = ""
#     swtch = 1
#     #Runs Check if streamlink is installed and gives link/opens if Not.
#     while stream_lnk_Path != "c":
#         stream_lnk_Path = funcs.setLink_Path()
#         slinkURL = "https://github.com/streamlink/windows-builds/releases/latest"
#         if stream_lnk_Path == "404 Not Here" and swtch == 1:
#             swtch = +2
#             ipt_asw = input(f"\nYou do not seem to have streamLink installed."
#                             "\n\nPlease Visit: {slinkURL}\nTo download"
#                             " Streamlink and install it."
#                             "\n\n----Look For EG: streamlink-5.1.0-1-py310-x86_64.exe"
#                             "----\nOR \nAuto Launch Website? y/n?: ").lower()
#             if ipt_asw in accp_lst["yes"]:
#                 webbrowser.open(slinkURL)
#                 print("\nWaiting for Installation...")
#                 time.sleep(15)
#             else:
#                 print("\nWaiting for Installation...")
#                 time.sleep(7)
#         elif swtch >= 0 and stream_lnk_Path == "404 Not Here":
#                 swtch = +2
#                 got_it = input("\nHas Streamlink been installed?\ny/n?:").lower()
#                 stream_lnk_Path = funcs.setLink_Path()
#                 time.sleep(5)
#                 if got_it in accp_lst["yes"] and stream_lnk_Path == "404 Not Here":
#                     stream_lnk_Path = funcs.setLink_Path()
#                     lie_chk = input("\nHaven't Found Streamlink In File Path "
#                                     "C\\Program (or {x86}) \\Files\\Streamlink\\bin\\"
#                                     "   Are you sure it is there?\n"
#                                     "Do you need the website again? y/n?:").lower()
#                     time.sleep(5)
#                     if lie_chk in accp_lst["yes"]:
#                         webbrowser.open(slinkURL)
#                         print("\nWaiting!......")
#                         time.sleep(7)
#                     elif stream_lnk_Path == "404 Not Here":
#                         time.sleep(8)# 21 ----
#                         print("\nPlease Check: C\\Program (or {x86}) \\Files\\Streamlink\\bin\\ Path")
#                 else:
#                     time.sleep(12)
import os

# os.system("shutdown -s -t 300")
import funcs

answers = funcs.mChoiceQeustion("whats this", ["chan", "Mike"])
print(answers)