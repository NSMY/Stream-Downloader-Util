from pyperclip import copy, paste
import subprocess
import os

file_path = paste().strip('"')
print(f'file_path: {file_path}')

file_path_2 = os.path.dirname(file_path)
print(f'file_path_2: {file_path_2}')

new_folder_name = f"FFMPEG__Encoded"
new_folder_path = os.path.join(file_path_2, new_folder_name)
print(f'new_folder_path: {new_folder_path}')

if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

old_file_name = os.path.basename(file_path)
print(f'old_file_name: {old_file_name}')
new_file_path = os.path.join(new_folder_path, old_file_name)
print(f'new_file_path: {new_file_path}')

process2 = subprocess.Popen(f'cd C:\\Program Files\\Streamlink\\ffmpeg && ffmpeg -i "{file_path}" -c copy "{new_file_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process2.communicate()
print(output.decode())
print(error.decode())

# os.system('cls' if os.name == 'nt' else 'clear')
new_file_path = f"{new_file_path}"
path = os.path.dirname(new_file_path)
path_1 = os.path.realpath(path)
os.startfile(path_1)
input('\nPress Enter to exit...')