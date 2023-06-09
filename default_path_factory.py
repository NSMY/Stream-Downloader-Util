import importlib
import os
import webbrowser

import funcs


class DefaultPathFactory():
    
    def __init__(self, 
                    default_Path: str,
                    settings_save_Key: str, 
                    extension_name_Lookup: str, 
                    parent_func_Callback: list,
        ):
        '''default path ("\\Example")
        
        .settings save Key name ("exampleKey")
        
        exe name lookup ("Example.exe")
        
        base_func_Callback: list: from (module name), import (function name)'''
        self.default_ffPath = default_Path
        self.settings_key = settings_save_Key
        self.extension_name = extension_name_Lookup
        self.base_func_Callback = parent_func_Callback
        
        
    def set_default_path(self):
        module_name = self.base_func_Callback[0]
        my_module = importlib.import_module(module_name)
        call_back_func = getattr(my_module, self.base_func_Callback[1])
                
        if os.path.isfile(self.default_ffPath):
            funcs.saveSettings(self.settings_key, self.default_ffPath)
            print("🐍 File: Stream-Downloader-Util/default_path_factory.py | Line: 36 | set_default_path ~ call_back_func",call_back_func)
            call_back_func()       

        if not (extention_find_path := funcs.file_search(self.extension_name)):
            if self.settings_key == "streamlinkPath":
                funcs.saveSettings(self.settings_key, extention_find_path)
                return self.streamlink_retreive()
            else:
                return self.download_dependencies()
        funcs.saveSettings(self.settings_key, extention_find_path)
        print("🐍 File: Stream-Downloader-Util/default_path_factory.py | Line: 46 | set_default_path ~ call_back_func",call_back_func)
        call_back_func()

    def download_dependencies(self):
        func_name = f"{self.settings_key}_download_an_unzip"
        func = getattr(funcs, func_name)
        dload = func()
        dload.wait()
        
        module_name = self.base_func_Callback[0]
        my_module = importlib.import_module(module_name)
        call_back_func = getattr(my_module, self.base_func_Callback[1])
        call_back_func()
    
    def streamlink_retreive(self):
        print("Cannot find streamlink on your system please download and "
                "retry\nEG *streamlink-5.5.1-2-py311-x86_64.exe......\n"
                "Download and install then Continue.")
        slinkURL = "https://github.com/streamlink/windows-builds/releases/latest"
        webbrowser.open(slinkURL)
        answer = funcs.multi_choice_dialog("Continue if resolved", ["Continue", "Exit"])
        if answer == "Continue":
            module_name = self.base_func_Callback[0]
            my_module = importlib.import_module(module_name)
            call_back_func = getattr(my_module, self.base_func_Callback[1])
            call_back_func()
        elif answer == "Exit":
            exit()
            
        
    def __str__(self):
        return f'Default path={self.default_ffPath}, .SettingsKey={self.settings_key}, Extension={self.extension_name}, Call Back To={self.base_func_Callback})'