# import importlib

# base_func_Callback = ["cpyVid_scritp_____1", "mux"]


# module_name = base_func_Callback[0]
# my_module = importlib.import_module(module_name)
# func = getattr(my_module, base_func_Callback[1])
# func()




# import importlib
# import os
# import webbrowser

# import funcs


# class DefaultPathFactory():
#     default_ffPath = ("C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe")
    
#     def __init__(self, 
#                     default_Path: str,
#                     settings_save_Key: str, 
#                     extention_name_Lookup: str, 
#                     parent_func_Callback: list,
#         ):
#         '''default path ("\\Example")
        
#         .settings save Key name ("exampleKey")
        
#         exe name lookup ("Example.exe")
        
#         base_func_Callback: list: from (module name), import (function name)'''
#         self.default_ffPath = default_Path
#         self.settings_key = settings_save_Key
#         self.extentions_name = extention_name_Lookup
#         self.base_func_Callback = parent_func_Callback
        
        
#     def set_default_path(self,): # FIX
#         module_name = self.base_func_Callback[0]
#         my_module = importlib.import_module(module_name)
#         call_back_func = getattr(my_module, self.base_func_Callback[1])
                
#         if os.path.isfile(self.default_ffPath):
#             funcs.saveSettings(self.settings_key, self.default_ffPath)
#             call_back_func()       

#         if not (extention_find_path := funcs.file_search(self.extentions_name)):
#             if self.settings_key == "streamlink":
#                 return self.streamlink_retreive()
#             else:
#                 return self.download_dependencies()
#         funcs.saveSettings(self.settings_key, extention_find_path)
#         call_back_func()

#     def download_dependencies(self):
#         func_name = f"{self.settings_key}_download_an_unzip"
#         func = getattr(funcs, func_name)
#         dload = func()
#         dload.wait()
        
#         module_name = self.base_func_Callback[0]
#         my_module = importlib.import_module(module_name)
#         call_back_func = getattr(my_module, self.base_func_Callback[1])
#         call_back_func()
    
#     def streamlink_retreive(self):
#         print("Cannot find streamlink on your system please download and "
#                 "retry\nEG *streamlink-5.5.1-2-py311-x86_64.exe......\n"
#                 "Download and install then Continue.")
#         slinkURL = "https://github.com/streamlink/windows-builds/releases/latest"
#         webbrowser.open(slinkURL)
#         answer = funcs.multi_choice_dialog("Continue if resolved", ["Continue", "Exit"])
#         if answer == "Continue":
#             module_name = self.base_func_Callback[0]
#             my_module = importlib.import_module(module_name)
#             call_back_func = getattr(my_module, self.base_func_Callback[1])
#             call_back_func()
#         elif answer == "Exit":
#             exit()

            
    #     # Download and unzip the ffmpeg executable
    #     # ffmpegpath = funcs.execute_or_setting(funcs.DL_unZip_ffmpeg, key=settings_save_Key)


    #     os.system("cls")

        # # imports dynamic module for callback.
        # # Calls the base Function to reRun after downloaded ... .
        # module_name = self.base_func_Callback[0]
        # my_module = importlib.import_module(module_name)
        # func = getattr(my_module, self.base_func_Callback[1])
        # func()

    #     return funcs.download_path_get(self.base_func_Callback)





from default_path_factory import DefaultPathFactory

##############################################################################################
default_ffPath = ("C:\\Program Files\\Streamlink\\ffmpeg\\ffmpeg.exe")
saveTo1 = "ffmpegpath"
exe1 = "ffmpeg.exe"
bascall1 = ["cpyVid_scritp_____1", "mux"]

default_ffprbePath = ("C:\\ffmpeg\\ffprbe.exe")
saveTo2 = "ffprobepath"
exe2 = "ffprobe.exe"
bascall2 = ["ffmpegExtract", "ffmpegextract"]

default_slinkPath = ("C:\\Program2 Files\\Streamlink\\bin\\streamlink.exe")
saveTo3 = "streamlinkPath"
exe3 = "streamlindk.exe"
# bascall3 = ["Main", "main_script"]
bascall3 = ["funcs", "initSettings"]




# pathset = DefaultPathFactory(default_ffPath, saveTo1, exe1, bascall1)
# print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 65 | undefined ~ pathset",pathset)
# info = pathset.set_default_path()
# print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 69 | undefined ~ info",info)



# pathset1 = DefaultPathFactory(default_ffprbePath, saveTo2, exe2, bascall2)
# print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 81 | undefined ~ pathset1",pathset1)

# info2=DefaultPathFactory.set_default_path(pathset1)
# print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 82 | undefined ~ info2",info2)

pathset2 = DefaultPathFactory(default_slinkPath, saveTo3, exe3, bascall3)
print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 81 | undefined ~ pathset1",pathset2) #HERE working now mainfile loop problem spoof main got it to work
dada = pathset2.set_default_path()
print("🐍 File: Stream-Downloader-Util/delete11.py | Line: 142 | undefined ~ dada",dada)

# info3=DefaultPathFactory.set_default_path(pathset2)
# print("🐍 File: Streamlink.Automated.Downloader/Tests.py | Line: 82 | undefined ~ info2",info3)