import os
from urllib.parse import urlparse
# import re
import subprocess
import sys
import time
from  send2trash import send2trash
from tkinter import filedialog
import inquirer
from pyperclip import copy, paste  
import requests
from tqdm import tqdm
import winsound
from  send2trash import send2trash
import zipfile
import json



def setLink_Path(findFpeg=False):
    """pass True if setting ffmpeg Path"""
    paths = ["C:\\Program Files\\Streamlink\\bin\\streamlink.exe",
                "C:\\Program Files (x86)\\Streamlink\\bin\\streamlink.exe"]
    for path in paths:
        if os.path.isfile(path):
            return os.path.dirname(path)
    if findFpeg == True:
        fpath = os.path.dirname(findExe("ffmpeg.exe"))
    if not os.path.exists(fpath):
        print("Streamlink path not Found...\nPlease Find streamlink.exe...."
                "EG path (Streamlink\\bin\\streamlink.exe)")
        fpath = openFile().replace("/streamlink.exe", "")
    else:
        pass
    return fr'{fpath}'

def is_url(variable):
    """Checks if str is URL"""
    try:
        result = urlparse(variable)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def has_ffmpeg_dir(stream_lnk_Path):
    store_path = os.path.join(os.path.dirname(stream_lnk_Path), "ffmpeg")
    return os.path.isdir(store_path)


def openFile():
    """Opens File dialog box

    Returns:
        str:
        
    loops if canceled
    """
    # print("Open File From:... \n")
    filep = filedialog.askopenfilename(defaultextension=".*",
                                    filetypes=[
                                        ("All files", ".*"),
                                        ("MP4 files", ".mp4"),
                                        ("MOV files", ".mov"),
                                        ("EXE files", ".exe"),
                                    ])
    file = os.path.normpath(filep)
    if not filep: #closes Program if No Save path is Entered
        check = mChoiceQeustion("Canceled Open File: Try again?", ["yes", "no"])
        if check == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            openFile()
        else:
            print("Exiting")
            time.sleep(3)
            sys.exit ()
    return file


def mChoiceQeustion(mssg, choice, oPT_type="str", keyName="Key"):
    """Scrollable Multi Choice coe.
    
        mssg = str | choice = [""]
        """
    questions = [
        inquirer.List(
            keyName,
            message=mssg,
            choices=choice,
        ),
    ]
    answer = inquirer.prompt(questions)
    if oPT_type == "str":
        qstnStrRtn = ''.join([str(value) for value in answer.values()])
        return qstnStrRtn
    return answer


def saveFile():
    """Opens: Save File Explorer

    Returns:
        Save Path
    """
    print("Save File To:... \n")
    filep = filedialog.asksaveasfilename(defaultextension='.mp4',
                                        filetypes=[
                                            ("MP4 files",".mp4"),    
                                            ("MOV files",".mov"),    
                                            ("All files",".*"),
                                        ])
    file = os.path.normpath(filep)
    if not filep: #closes Program if No Save path is Entered
        check = mChoiceQeustion("Canceled Save Path: Try again?", ["yes", "no"])
        if check == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            saveFile()
        else:
            print("Exiting")
            time.sleep(3)
            sys.exit ()
    return (file)



def is_installed(program_name):
    """Checks if Program is installed in path.
    
    EG: python
    
    returns:
        True/False
    """
    try:
        result = subprocess.check_output([program_name, '-version'])
        return True
    except FileNotFoundError:
        return False

def get_path(program_name):
    """Gets Program file path, but only if its in 'the Path'.
    """
    try:
        where = subprocess.check_output(['where', program_name])
        return where.decode('utf-8').strip()
    except FileNotFoundError:
        return None
    
    
def dldURL(url, dloadFilePath, dlmssg = ""):
    """Downloads the url to dloadFilepath using Requests

    Args:
        url (str): URLdownload link
        
        dloadFilePath (str): Download Path
        
        dlmssg (str, optional): Transparency mssg whats happening. Defaults to "".
    """
    if not os.path.exists(dloadFilePath):
        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            if dlmssg:
                print(dlmssg)
            with open(dloadFilePath, 'wb') as f:
                for data in tqdm(response.iter_content(block_size), total=total_size//block_size, unit='KB'):
                    f.write(data)
            return True
        except requests.exceptions.HTTPError as errh:
            print(f'HTTP Error: {errh}')
            return False
        except requests.exceptions.ConnectionError as errc:
            print(f'Error Connecting: {errc}')
            return False
        except requests.exceptions.Timeout as errt:
            print(f'Timeout Error: {errt}')
            return False
        except requests.exceptions.RequestException as err:
            print(f'Something went wrong. Error: {err}')
            return False

def Unzip(dloadFilePath, outputDir, specificFile="", mssg=""):
    """Unzips files or specific File into outputDir,
    moves Old .zip to Bin if both exist.

    Args:
        dloadFilePath (str): C:\\example\\file.type
        
        outputDir (str): C:\\OutPutFolder\\
        
        specificFile (str, optional): fileType.exe Defaults to "none".
        
        mssg (str, optional): Trash mssg Defaults to "".
    """
    if not os.path.exists(f"{outputDir}{specificFile}"):
        try:
            zip_file = (dloadFilePath)
            print(zip_file)
            output_dir = outputDir
            
            if specificFile:
                with zipfile.ZipFile(zip_file, 'r') as zf:
                    zf.extract(specificFile, output_dir)
            else:
                with zipfile.ZipFile(zip_file, 'r') as zf:
                    zf.extractall(output_dir)
            print(f"\nSuccessful Extraction To {output_dir}")
            if os.path.isfile(dloadFilePath) and os.path.isfile(f"{outputDir}{specificFile}"):
                send2trash(dloadFilePath)
                print(mssg)
                winsound.PlaySound('C:\\Windows\\Media\\Recycle.wav', winsound.SND_FILENAME)
                return True
        except:
            print(f"\n\nERROR: Could not extract {dloadFilePath} \n")
            fldr = dloadFilePath.replace(specificFile,"")
            os.startfile(fldr)
            return False
            
            
def findExe(exeName, timeout=40):
    appDatasearch = os.path.expanduser('~\\Appdata')
    directories = ['C:\\ffprobe\\', 'C:\\Program Files', 'C:\\Program Files (x86)', appDatasearch]
    filename = exeName
    found = False
    start_time = time.time()
    for directory in directories:
        if found:
            return exePth
        for root, dirs, files in os.walk(directory):
            if filename in files:
                exePth = (os.path.join(root, filename))
                found = True
                break
            if time.time() - start_time > timeout:
                return f"Search timed out after {timeout} seconds"
    return f"{exeName} Could NOT be Found"


def channelsSplit(fprobeDir, filename):
    pathDir = os.path.dirname(fprobeDir)
    if pathDir:
        command = (f'cd {pathDir} && ffprobe -v error -show_entries stream=index'
                    f' -select_streams a -of csv=p=0 "{filename}"')
        output = subprocess.check_output(command, shell=True).decode('utf-8').strip()
        audChannels = output.split()
        return audChannels
    else:
        print(f"\nCould Not Find '{fprobeDir}' on your Computer\n")
        while True:
            try:
                audChannels = int(input(f"Couldn't Auto retrieve Maximum number of Audio Channels, How Many Channels does {filename} have?:"))
                break
            except ValueError:
                print("Please enter a numerical value(int) EG: 3.")
        channels_list = []
        for i in range(1, audChannels+1):
            channels_list.append(i)
        return channels_list
    
    
def DloadZipCombo():
    if not os.path.isfile("C:\\ffprobe\\ffprobe.exe"):
        exename = 'ffprobe.exe'
        exeanswer = os.path.dirname(findExe(exename)) + "\\ffprobe.exe"
        if not exeanswer:
            user_path = os.path.expanduser('~\\Desktop')
            dloadFilePath = os.path.join(user_path, "ffprobe-4.4.1-win-64.zip")
            url = 'https://github.com/ffbinaries/ffbinaries-prebuilt/releases/download/v4.4.1/ffprobe-4.4.1-win-64.zip'
            dlmssg = ("\n---------------Downloading ffprobe from OFFICIAL FFMPEG link (45mb - 110mb Extracted) "
                        f" LINK >>> https://ffbinaries.com/downloads <<<---------------\n ----------------to {dloadFilePath} "
                        "and will auto extract to C:\\ffprobe\\ ------------------\n")
            save_Dir = "C:\\ffprobe\\"
            spefFile = 'ffprobe.exe'
            zipmssg = "\nSent .zip to Recycle Bin (no longer required)\n"
            
            dld = dldURL(url, dloadFilePath, dlmssg)
            zp = Unzip(dloadFilePath, save_Dir, spefFile, zipmssg)
            if dld and zp ==True:
                exeanswer = ("C:\\ffprobe\\ffprobe.exe")
                return exeanswer
    elif os.path.isfile("C:\\ffprobe\\ffprobe.exe"):
        exename = 'ffprobe.exe'
        exeanswer = findExe(exename) + "\\ffprobe.exe"
    return exeanswer
        
        
def getFile(file_path_inpt=paste()):
    '''If no Arg uses Paste Clipboard checks if 
    paste is a File if Not Opens File Finder.
    Returns File Path'''
    file_path = os.path.normpath(file_path_inpt)
    if not os.path.isfile(file_path):
        file_path = os.path.normpath(openFile())
        print(file_path)
    return file_path



def initSettings():
    # Get the path to the local AppData folder
    appdata_path = os.getenv('LOCALAPPDATA')

    # Define the path to the settings file
    settings_file = os.path.join(appdata_path, 'StreamlinkDownload', 'SlDloadsettings.json')

    # Check if the settings file already exists
    if not os.path.exists(settings_file):
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(settings_file), exist_ok=True)

        # Define the initial settings as a dictionary
        settings = {
            'ExamplePath': '/path/to/file',
            'Example_feature': True,
            'Initialize': True,
        }

        # Save the initial settings to the file
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=4)


def saveSettings(key=None, value=None):
    """To save new Settings Must Pass via Args

    Args:
        key (srt, optional=No Change):
        
        value (all, optional=No Change):
    """
    # Initialize the settings file with initial values if it doesn't exist
    initSettings()

    # Get the path to the local AppData folder
    appdata_path = os.getenv('LOCALAPPDATA')

    # Define the path to the settings file
    settings_file = os.path.join(appdata_path, 'StreamlinkDownload', 'SlDloadsettings.json')

    # Load settings from the file
    with open(settings_file, 'r') as f:
        settings = json.load(f)

    # Update the settings dictionary with the new key-value pair if key and value are provided
    if key is not None and value is not None:
        settings[key] = value

    # Save the updated settings to the file
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=4)


def loadSettings(key=None):
    """iF Known pass in via Args the Key 
    you want to know the Value of to call
    Keys must be in a 'string'"""
    # Initialize the settings file with initial values if it doesn't exist
    initSettings()
    
    # Get the path to the local AppData folder
    appdata_path = os.getenv('LOCALAPPDATA')

    # Define the path to the settings file
    settings_file = os.path.join(appdata_path, 'StreamlinkDownload', 'SlDloadsettings.json')

    # Load settings from the file
    with open(settings_file, 'r') as f:
        settings = json.load(f)

    # Return the value associated with the key if a key is provided
    if key is not None:
        return settings.get(key, None)
    # Otherwise, return the entire settings dictionary
    else:
        return settings
    