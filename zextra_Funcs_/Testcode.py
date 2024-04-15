import json
with open(r'C:\Users\970EVO-Gamer\AppData\Local\Stream-Downloader-Util\download_links.txt', "r") as r:
    hll = json.load(r)
print(hll['_Version'])