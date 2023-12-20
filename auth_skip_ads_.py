import json
import os
import webbrowser
from datetime import datetime, timedelta
from json import dump

from pyperclip import copy, paste

import funcs


def skip_ads():
    print('\nStreamlink Flags to choose from\n')
    main_choice = funcs.multi_choice_dialog('Skip Ads + Authentication, Skip ads or Authentication non skip adds', ['Skip Ads + Auth', 'Skip Ads', 'Auth Non Skip'])

    if main_choice == 'Auth Non Skip':
        return auth_twitch_string()
    if main_choice == 'Skip Ads':
        return '--twitch-disable-ads'
    auth_token_rtrn = auth_twitch_string()
    return f'--twitch-disable-ads {auth_token_rtrn}'


def auth_twitch_string():
    try:
        lsd = load_auth_file(['LastSave'])[0]
    except FileNotFoundError as e:
        save_auth_file()

    auth_differance = auth_file_check()
    
    appdata_path = os.getenv("LOCALAPPDATA")
    auth_file = os.path.join(str(appdata_path),
                            "Stream-Downloader-Util", "auth_key_file.json")
    
    print(f"Auth file can be found at: {auth_file} \nIf Manually editing"
        " is desired, the [LastSave] date\nwill have to be within the "
        "last 2 days to not be Automatically deleted"
        )

    if auth_differance == True:
        print('\nLoaded Auth Token from file')
        auth_Token = load_auth_file(['auth_token'])[0]
        return f'"--twitch-api-header=Authorization=OAuth {auth_Token}"'

    # https://streamlink.github.io/latest/cli/plugins/twitch.html#authentication
    else:
        help = ('\nIn order to get the personal OAuth token\nfrom Twitch'
        ' website which identifies'
        '\nyour account, open Twitch.tv in your web browser and\n'
        'after a successful login, open the developer tools by\n'
        'pressing F12 or CTRL+SHIFT+I. Then navigate to the "Console" tab or '
        'its equivalent\nof your web browser and '
        'execute the following JavaScript snippet,\n'
        'which reads the value of the auth-token cookie, if it exists\n'
        '\nThis Snippet has been copied into your clipboard: '
        'document.cookie.split("; ").find(item=>item.startsWith("auth-token="))?.split("=")[1]'
        '\n\nCopy the resulting string consisting of '
        '30 alphanumerical characters without any quotations("").'
        ' EG: hrfidzseez4vhvjkly35f27eu3acm6\n')

        copy(funcs.loadSettings(["Twitch_snippet_for_auth"])[0])
        print(help)
        webbrowser.open('https://www.twitch.tv')

        token_q = funcs.multi_choice_dialog('Waiting for the Auth token to be copied to clipboard', ['Done, Copied', 'Return to Main'])
        if token_q == 'Done, Copied':
            switch = 0
            while switch == 0:
                auth_Token = paste()
                print('>>>>  ', auth_Token, ' <<<<')
                tok_confirm = funcs.multi_choice_dialog("Is the String Above Your Token?", ["Yes", "No"])
                if tok_confirm == "No":
                    os.system("cls")
                    print('Snippet if Needed >'
                    '',funcs.loadSettings(["Twitch_snippet_for_auth"])[0],'\n'
                    )
                else:
                    switch = 1
                    save_auth_file('auth_token', auth_Token)
                    print(auth_Token, ' Saved auth token to'
                        ' file for 3 days then will have to be'
                        ' refreshed, will be auto deleted'
                        )
                    return f'"--twitch-api-header=Authorization=OAuth {auth_Token}"'
        elif token_q == 'Return to Main':
            funcs.main_start()


def auth_file_check():
    try:
        if not load_auth_file(["auth_token"])[0]:
            return False
        else:
            appdata_path = os.getenv("LOCALAPPDATA")
            auth_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "auth_key_file.json")
            lsd = load_auth_file(['LastSave'])[0]
            datetimeNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            datetime1 = datetime.strptime(datetimeNow, "%d/%m/%Y %H:%M:%S")
            datetime2 = datetime.strptime(lsd, "%d/%m/%Y %H:%M:%S")
            difference = abs(datetime2 - datetime1)
            diff = difference < timedelta(days=3)
            if not diff:
                os.remove(auth_file)
            return diff
    except FileNotFoundError as e:
        save_auth_file()

def save_auth_file(key = None, value = None):
    """To save new Settings Must Pass via Args
    Args:
    key (str, optional=No Change):
    
    value (all, optional=No Change):
    """
    appdata_path = os.getenv("LOCALAPPDATA")
    auth_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "auth_key_file.json")
    LastSave = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    if not os.path.exists(auth_file):
        os.makedirs(os.path.dirname(auth_file), exist_ok=True)
        ls = {'LastSave': LastSave}
        with open(auth_file, "w") as f:
            json.dump(ls, f, indent=4)
    
    with open(auth_file, "r") as f:
        settings = json.load(f)
        
    if key is not None and value is not None:
        settings[key] = value
        settings["LastSave"] = LastSave
        
    with open(auth_file, "w") as f:
        json.dump(settings, f, indent=4)


def load_auth_file(keys: list[str])-> list[str]:
    if keys is None:
        keys = []
    appdata_path = os.getenv("LOCALAPPDATA")
    auth_file = os.path.join(str(appdata_path),
                                    "Stream-Downloader-Util", "auth_key_file.json")
    answers = []
    for key in keys:
        with open(auth_file, "r") as f:
            settings = json.load(f)
            answer = settings.get(key, None) if key is not None else settings
            answers.append(answer)            
    return answers
