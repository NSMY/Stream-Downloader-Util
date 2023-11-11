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
from re import L

# vod_index = 6
# json_file_path = r'C:\Users\970EVO-Gamer\Documents\Python_cheats\Stream-Downloader-Util\Stream-Downloader-Util\new_mass_gql\jsons_symlink\deadlyslob.json'

# with open(json_file_path, 'r+') as f:
#     data = json.load(f)
#     new_data = data[vod_index:]
#     f.seek(0)
#     json.dump(new_data, f, indent=4)
#     f.truncate()


# # fake test data to stop calls and fasten dev.
# new_strems = 3

# gql_fake_data = {'data': {'user': {'videos': {'totalCount': 334, 'edges': [{'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1973622401', 'title': 'Henry, Master Thief - KCD Hardcore Day 5 - Half Sword Later - !Glasses', 'publishedAt': '2023-11-10T14:44:52Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 18123, 'viewCount': 15944, 'game': {'id': '458912', 'name': 'Kingdom Come: Deliverance'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1973536243', 'title': 'Henry, Master Thief - KCD Hardcore Day 5 - Half Sword Later - !Glasses', 'publishedAt': '2023-11-10T12:02:03Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 9589, 'viewCount': 8708, 'game': {'id': '458912', 'name': 'Kingdom Come: Deliverance'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1972672377', 'title': 'Half Sword - Chasing that Highscore (4410) - !Glasses', 'publishedAt': '2023-11-09T12:09:24Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 27786, 'viewCount': 24941, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1972663957', 'title': 'Half Sword - Chasing that Highscore (4410) - !Glasses', 'publishedAt': '2023-11-09T11:52:13Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 810, 'viewCount': 1057, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1971836501', 'title': 'Morning Half Sword - 4410 High Score - KCD Later! - !Glasses', 'publishedAt': '2023-11-08T12:10:01Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 28625, 'viewCount': 26015, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1970976562', 'title': 'Half Sword - 4410 High Score - Kingdom Come: Deliverance Later - !Glasses', 'publishedAt': '2023-11-07T11:39:44Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 30290, 'viewCount': 28046, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1970170845', 'title': 'Early Morning Coffee & Half Sword - Kingdom Come Deliverance TODAY - !Glasses', 'publishedAt': '2023-11-06T11:48:10Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 28424, 'viewCount': 30573, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1967417346', 'title': "We're Beating Half Sword - !Glasses", 'publishedAt': '2023-11-03T12:07:53Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 24358, 'viewCount': 24951, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1967275983', 'title': 'New Tech Test Stream - !Glasses', 'publishedAt': '2023-11-03T05:08:48Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 2840, 'viewCount': 1951, 'game': {'id': '509658', 'name': 'Just Chatting'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1966532291', 'title': 'Half Sword - Becoming the Ultimate Gladiator - !Glasses', 'publishedAt': '2023-11-02T11:33:14Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 27050, 'viewCount': 29925, 'game': {'id': '1941249372', 'name': 'Half Sword'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1965704937', 'title': 'Road to 200,000 Citizens - Los Pepegos - Day 7 - !Glasses', 'publishedAt': '2023-11-01T11:28:09Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 23748, 'viewCount': 25335, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1964873487', 'title': 'Road to 200,000 Citizens - Los Pepegos - Day 6 - !Glasses', 'publishedAt': '2023-10-31T11:38:16Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 19898, 'viewCount': 20968, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1964080409', 'title': 'Road to 100,000 Citizens - Los Pepegos - Day 5 - !Glasses', 'publishedAt': '2023-10-30T12:28:33Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 23733, 'viewCount': 28526, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1964070619', 'title': 'Road to 100,000 Citizens - Los Pepegos - Day 5 - !Glasses', 'publishedAt': '2023-10-30T12:05:08Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 1327, 'viewCount': 2266, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1961505777', 'title': 'Road to 100,000 Citizens - Los Pepegos - Day 4 - !Glasses', 'publishedAt': '2023-10-27T11:11:50Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 28993, 'viewCount': 30199, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1960693424', 'title': 'Cities Skylines "Master" Building Los Pepegos - Day 3 - !Glasses', 'publishedAt': '2023-10-26T11:23:40Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 27455, 'viewCount': 26549, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1960188971', 'title': 'Cities Skylines "Master" Building Los Pepegos - !Glasses', 'publishedAt': '2023-10-25T19:36:27Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 58, 'viewCount': 958, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1959862412', 'title': 'Cities Skylines "Master" Building Los Pepegos - !Glasses', 'publishedAt': '2023-10-25T10:34:10Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 30236, 'viewCount': 30137, 'game': {'id': '556907291', 'name': 'Cities: Skylines II'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}, {'cursor': '1959081227|40587|2023-10-24T12:02:47Z', 'node': {'id': '1959081227', 'title': 'Tuesday Raids & Coffee - CITIES 2 TODAY - !Glasses', 'publishedAt': '2023-10-24T12:02:47Z', 'broadcastType': 'ARCHIVE', 'status': 'RECORDED', 'lengthSeconds': 33394, 'viewCount': 40587, 'game': {'id': '491931', 'name': 'Escape from Tarkov'}, 'creator': {'id': '12731745', 'login': 'deadlyslob', 'displayName': 'Deadlyslob'}}}]}}}, 'extensions': {'durationMilliseconds': 73, 'requestID': '01HEYEJXN3VC4QH7RRNZJ6V3WT'}}
# # for edges in gql_fake_data['data']['user']['videos']['edges']:
# #     print(edges['node']['title'], f'\nhttps://twitch.tv/{edges['node']['id']}\n')
# #     datd = edges['node']['title'], f'https://twitch.tv{edges['node']['id']}'

# for edges in enumerate(gql_fake_data['data']['user']['videos']['edges']):
#     if edges[0] == new_strems + 1:
#         break
#     print(f'{edges[1]['node']['title']}\n')

# print(gql_fake_data['data']['user']['videos']['edges'][0]['node']['title'])
# print(gql_fake_data['data']['user']['videos']['edges'][1]['node']['title'])
# print(gql_fake_data['data']['user']['videos']['edges'][2]['node']['title'])

# import inquirer

# Now you can use the 'answer' variable in your Inquirer prompts or elsewhere in your application

# questions = [inquirer.List(name='hello', message=message, choices=['yes', 'no']), ]
# print(inquirer.prompt(questions))

# Now you can use the 'answer' variable in your Inquirer prompts or elsewhere in your application


def gettt(**kwargs):
    hello = ('Hello World')
    good = 'Good job'
    print(hello + good)
    print(kwargs)
gettt()