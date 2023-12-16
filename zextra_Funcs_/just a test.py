# import os

# dir = r'F:/Music/Musizz/My Shared Folder/'


# for files in os.listdir(dir):
#     print(files)

import subprocess

rw_stream = subprocess.Popen(
    rf'streamlink "https://youtu.be/cvq7Jy-TFAU?list=PLbAqlIAMdRgtQkPnpqCoqZv1hi9xWnsgZ" ',
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
    cwd='c:/Program Files/Streamlink/ffmpeg/',
)
stdout, stderr = rw_stream.communicate()
print("rw_stream", rw_stream)
print("stderr: ", stderr)
print("stdout: ", stdout)
print(f"The command failed with return code {rw_stream.returncode}")
print(f"stderr: {stderr.strip()}")