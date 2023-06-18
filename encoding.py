import funcs

try:
    funcs.loadSettings(["lastSave"])
except FileNotFoundError as e:
    funcs.initSettings()
