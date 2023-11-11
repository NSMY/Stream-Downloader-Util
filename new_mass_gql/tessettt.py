# import json
# import os
# import pprint
# import threading
# from operator import getitem

# from numpy import append
# from utility_dir import util_functions as utl

# import gql

# json_id = "jsons/deadlyslob"

# file_path = fr'{json_id}.json'
# # with open(file_path, 'r') as f:
# #     data = json.load(f)

# # print(data[2].get('title', 'displayName'))
# # print(len(data))
# # json_ids = [(vod['url'], vod['displayName'], vod['publishedAt'], vod['gameName'], vod['title']) for vod in data]
# # json_ids = [(vod) for vod in data]
# # print(type(json_ids))

# # stream_index:int = 3

# # for key in json_ids[stream_index]:
# #     print(key.get(**key))

# # streams = []
# # for id in json_ids:
# #     streams
# #     # pprint.pprint(id, indent=4)
# #     # print(id)
# # print(json_ids[0]["displayName"]['gameName'])


# # new_json_str = '[{"new_key1": "new_value1"}, {"new_key2": "new_value2"}]'

# # # Convert the new JSON string to a Python list of dictionaries:
# # new_dicts = json.loads(new_json_str)




# # file_path = [
# #         {
# #         "creatorId": "12731745",
# #         "login": "deadlyslob",
# #         "displayName": "Deadlyslob",
# #         "idd": "1948982158",
# #         "title": "SOLO Tarkov  Boss Hunting  Glasses",
# #         "publishedAt": "2023-10-12T11:13:23Z",
# #         "broadcastType": "ARCHIVE",
# #         "status": "RECORDED",
# #         "lengthSeconds": 28655,
# #         "viewCount": 20137,
# #         "gameId": "491931",
# #         "gameName": "Escape from Tarkov",
# #         "url": "https://www.twitch.tv/videos/1948982158",
# #         "not_downloaded": True
# #     },
# #     {
# #         "creatorId": "12731745",
# #         "login": "deadlyslob",
# #         "displayName": "Deadlyslob",
# #         "id": "1948189219",
# #         "title": "SOLO TARKOV  Boss Hunting  Ranked  Glasses",
# #         "publishedAt": "2023-10-11T11:45:26Z",
# #         "broadcastType": "ARCHIVE",
# #         "status": "RECORDED",
# #         "lengthSeconds": 26115,
# #         "viewCount": 19212,
# #         "gameId": "491931",
# #         "gameName": "Escape from Tarkov",
# #         "url": "https://www.twitch.tv/videos/1948189219",
# #         "not_downloaded": True
# #     },
# # ]




# # store = get_index_of_target_id(input_content=file_path, target_id="1948189219")
# # print(store)


# # to get data from dict
#     # for objects, dictkey in enumerate(content):
#     #     if dictkey.get("id") == target_id:
#     #         # print(f'The target ID is at index {objects} in the list.') # FIX Not needed Later on in build.
#     #         index_id = objects
#     #         # print(content[index_id])
#     #         # iii = content[index_id] to get the dict
#     #         return index_id
    
    
    
    
# # with open("jsons\\kotton.json", 'r') as f:
# #     data = json.load(f)
# # timestamp = data[25]['publishedAt']
# # print(utl.simple_convert_timestamp(timestamp))





# '''
# vods_dir = r'jsons\\'
# vods_list = []
# for files in os.listdir(vods_dir):
#     vods_list.append(files.removesuffix('.json'))

# print(vods_list)
# print(vods_list[1])
# print(len(vods_list))
# '''
# # def vod_data_extraction(x):
# #     with open(
# #     for i in range(x):

import json
import pprint

vod_index = 6
json_file_path = r'C:\Users\970EVO-Gamer\Documents\Python_cheats\Stream-Downloader-Util\Stream-Downloader-Util\new_mass_gql\jsons_symlink\deadlyslob.json'

with open(json_file_path, 'r+') as f:
    data = json.load(f)
    new_data = data[vod_index:]
    f.seek(0)
    json.dump(new_data, f, indent=4)
    f.truncate()