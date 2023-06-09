# import importlib

# base_func_Callback = ["cpyVid_scritp_____1", "mux"]


# module_name = base_func_Callback[0]
# my_module = importlib.import_module(module_name)
# func = getattr(my_module, base_func_Callback[1])
# func()





import importlib
import os

import funcs


class DefaultPathFactory():
    default_ffPath = ("C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe")
    
    def __init__(self, 
                    default_Path: str,
                    settings_save_Key: str, 
                    extention_name_Lookup: str, 
                    base_func_Callback: list,
        ):
        '''default path ("\\Example")
        
        .settings save Key name ("exampleKey")
        
        exe name lookup ("Example.exe")
        
        base_func_Callback: list: from (module name), import (function name)'''
        self.default_ffPath = default_Path
        self.settings_key = settings_save_Key
        self.extentions_name = extention_name_Lookup
        self.base_func_Callback = base_func_Callback
        
        
    def set_default_path(self,): # FIX
        
        if os.path.isfile(self.default_ffPath):
            funcs.saveSettings(self.settings_key, self.default_ffPath)
            return self.default_ffPath        

        if not (extention_find_path := funcs.file_search(self.extentions_name)):
            return self.download_dependencies()
        funcs.saveSettings(self.settings_key, extention_find_path)
        return extention_find_path

    # TODO Rename this here and in `set_default_path`
    def download_dependencies(self):
        
        
        return self
    #     # Download and unzip the ffmpeg executable
    #     # ffmpegpath = funcs.execute_or_setting(funcs.DL_unZip_ffmpeg, key=settings_save_Key)


    #     os.system("cls")

    #     # imports dynamic module for callback.
    #     # Calls the base Function to reRun after downloaded ... .
    #     module_name = self.base_func_Callback[0]
    #     my_module = importlib.import_module(module_name)
    #     func = getattr(my_module, self.base_func_Callback[1])
    #     func()

    #     return funcs.download_path_get(self.base_func_Callback)







##############################################################################################
default_ffPath = ("C:\\Program Filees\\Streamlink\\ffmpeg\\ffmpeg.exe")
saveTo1 = "ffmpegpath"
exe1 = "ffmpeg.exe"
bascall1 = ["cpyVid_scritp_____1.py", "mux"]

default_ffprbePath = ("C:\\ffmpeeeg\\ffprbe.exe")
saveTo2 = "ffprobepath"
exe2 = "ffprobe.exe"
bascall2 = ["ffprobeExtract", "ffprobe_extract"]

default_slinkPath = ("C:\\Program Fileees\\Streamlink\\bin\\streamlink.exe")
saveTo3 = "streamlinkPath"
exe3 = "streamlink.exe"
bascall3 = ["streamlinkExtract", "streamlink_extract"]




pathset = DefaultPathFactory(default_ffPath, saveTo1, exe1, bascall1)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 65 | undefined ~ pathset",pathset)
info=DefaultPathFactory.set_default_path(pathset)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 69 | undefined ~ info",info)


pathset1 = DefaultPathFactory(default_ffprbePath, saveTo2, exe2, bascall2)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 81 | undefined ~ pathset1",pathset1)

info2=DefaultPathFactory.set_default_path(pathset1)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 82 | undefined ~ info2",info2)

pathset2 = DefaultPathFactory(default_slinkPath, saveTo3, exe3, bascall3)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 81 | undefined ~ pathset1",pathset1)

info3=DefaultPathFactory.set_default_path(pathset2)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 82 | undefined ~ info2",info3)