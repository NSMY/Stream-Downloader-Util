

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

# def create_popup(content):
#     popup = tk.Tk()
#     popup.title("Popup Window")
#     listbox = tk.Listbox(popup)
#     for key, value in content.items():
#         listbox.insert(tk.END, f"{key}: {value}")
#     listbox.pack()
#     button = tk.Button(popup, text="Close", command=popup.destroy)
#     button.pack()
#     # Update the window to calculate the size of the content
#     popup.update_idletasks()
#     # Get the width and height of the content
#     width = popup.winfo_width()
#     height = popup.winfo_height()
#     # Add some padding
#     width += 80
#     height += 80
#     # Set the window size
#     popup.geometry(f"{width}x{height}")
#     popup.mainloop()
import ctypes
import json
import os
import pprint
# # Usage:
# create_popup("This is some text.")
import re
import timeit
import tkinter as tk
from re import L, split
from subprocess import PIPE, Popen
from turtle import title
from urllib.parse import urlparse

# p = Popen('start cmd', stdin=PIPE, shell=True)
# p.communicate(input='Hello, World!\n'.encode())
import m3u8
import requests

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


# def gettt(**kwargs):
#     hello = ('Hello World')
#     good = 'Good job'
#     print(hello + good)
#     print(kwargs)
# gettt()


# [] to build  multiple [list] return of Vods
# ??retrieve data from TK or just have user input range?. 



# data = ('#EXTM3U\n#EXT-X-TWITCH-INFO:ORIGIN="s3",B="false",REGION="OC",USER-IP="119.12.208.21",SERVING-ID="96d3cfabad3c4ee98dd4e78fec8a62f8",CLUSTER="cloudfront_vod",USER-COUNTRY="AU",MANIFEST-CLUSTER="cloudfront_vod"\n#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="chunked",NAME="1080p60",AUTOSELECT=NO,DEFAULT=NO\n#EXT-X-STREAM-INF:BANDWIDTH=8288000,CODECS="avc1.640032,mp4a.40.2",RESOLUTION=1920x1080,VIDEO="chunked",FRAME-RATE=60.000\nhttps://d1m7jfoe9zdc1j.cloudfront.net/dbc98976c975857c67ba_kotton_49693887389_1699812436/chunked/index-dvr.m3u8\n#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="720p60",NAME="720p60",AUTOSELECT=YES,DEFAULT=YES\n#EXT-X-STREAM-INF:BANDWIDTH=3100000,CODECS="avc1.4D0020,mp4a.40.2",RESOLUTION=1280x720,VIDEO="720p60",FRAME-RATE=60.000\nhttps://d1m7jfoe9zdc1j.cloudfront.net/dbc98976c975857c67ba_kotton_49693887389_1699812436/720p60/index-dvr.m3u8\n#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="480p30",NAME="480p",AUTOSELECT=YES,DEFAULT=YES\n#EXT-X-STREAM-INF:BANDWIDTH=1200000,CODECS="avc1.4D001F,mp4a.40.2",RESOLUTION=852x480,VIDEO="480p30",FRAME-RATE=30.000\nhttps://d1m7jfoe9zdc1j.cloudfront.net/dbc98976c975857c67ba_kotton_49693887389_1699812436/480p30/index-dvr.m3u8\n#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="360p30",NAME="360p",AUTOSELECT=YES,DEFAULT=YES\n#EXT-X-STREAM-INF:BANDWIDTH=630000,CODECS="avc1.4D001E,mp4a.40.2",RESOLUTION=640x360,VIDEO="360p30",FRAME-RATE=30.000\nhttps://d1m7jfoe9zdc1j.cloudfront.net/dbc98976c975857c67ba_kotton_49693887389_1699812436/360p30/index-dvr.m3u8\n#EXT-X-MEDIA:TYPE=VIDEO,GROUP-ID="160p30",NAME="160p",AUTOSELECT=YES,DEFAULT=YES\n#EXT-X-STREAM-INF:BANDWIDTH=230000,CODECS="avc1.4D000C,mp4a.40.2",RESOLUTION=284x160,VIDEO="160p30",FRAME-RATE=30.000\nhttps://d1m7jfoe9zdc1j.cloudfront.net/dbc98976c975857c67ba_kotton_49693887389_1699812436/160p30/index-dvr.m3u8')

# start_time = timeit.default_timer()

# playlist = m3u8.loads(data)
# # Hack for temp results make better.
# url = data.split('\n')[4]
# seconds_of_Vod = requests.get(url)
# bandwidth = int(re.search(r'#EXT-X-TWITCH-TOTAL-SECS:(\d+)', seconds_of_Vod.text).group(1))


# end_time = timeit.default_timer()
# execution_time = end_time - start_time
# print(f"The script took {execution_time} seconds to run.")
# print(bandwidth)
# start_time = timeit.default_timer()

# playlist = m3u8.loads(data)
# # Hack for temp results make better.
# url = data.split('\n')[4]
# seconds_of_Vod = requests.get(url)
# s = seconds_of_Vod.text.split()[7]
# s2 = s.split(':')
# s3 = float(s2[1])



# end_time = timeit.default_timer()
# execution_time = end_time - start_time
# print(f"The script took {execution_time} seconds to run.")
# print(s3)




'''
# dad = ('https://usher.ttvnw.net/vod/1975700991.m3u8?acmb=e30%3D&allow_source=true&cdm=wv&p=2325758&play_session_id=596d3e072599b1bbde0ad336732c756c&player_backend=mediaplayer&player_version=1.23.0&playlist_include_framerate=true&reassignments_supported=true&sig=1fdb105cd2789968727c1202b8896c136c41ae06&supported_codecs=avc1&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22chansub%22%3A%7B%22restricted_bitrates%22%3A%5B%5D%7D%2C%22device_id%22%3A%22L8lFfAYG1PKKuwUFH5gJJhtC4mSOAefS%22%2C%22expires%22%3A1699909269%2C%22https_required%22%3Atrue%2C%22privileged%22%3Afalse%2C%22user_id%22%3A194301647%2C%22version%22%3A2%2C%22vod_id%22%3A1975700991%7D&transcode_mode=cbr_v1')
# dad = ('https://usher.ttvnw.net/vod/1976617855.m3u8?acmb=e30%3D&allow_source=true&cdm=wv&p=8204494&play_session_id=d6cdaaecb26c58dafaf16474b5a8eaee&player_backend=mediaplayer&player_version=1.23.0&playlist_include_framerate=true&reassignments_supported=true&sig=f2e612f877cc77067c7940183a8c7a3eae2721a3&supported_codecs=avc1&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22chansub%22%3A%7B%22restricted_bitrates%22%3A%5B%5D%7D%2C%22device_id%22%3A%22L8lFfAYG1PKKuwUFH5gJJhtC4mSOAefS%22%2C%22expires%22%3A1699989123%2C%22https_required%22%3Atrue%2C%22privileged%22%3Afalse%2C%22user_id%22%3A194301647%2C%22version%22%3A2%2C%22vod_id%22%3A1976617855%7D&transcode_mode=cbr_v1')
dad = 'https://usher.ttvnw.net/vod/1976337345.m3u8?acmb=e30%3D&allow_source=true&cdm=wv&p=5813174&play_session_id=88d4ecbd8b6a3fa67f198c78f4715f84&player_backend=mediaplayer&player_version=1.23.0&playlist_include_framerate=true&reassignments_supported=true&sig=369eae4dff1be072caf96a0f7920d99eb483cd27&supported_codecs=avc1&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22chansub%22%3A%7B%22restricted_bitrates%22%3A%5B%5D%7D%2C%22device_id%22%3A%22L8lFfAYG1PKKuwUFH5gJJhtC4mSOAefS%22%2C%22expires%22%3A1700007287%2C%22https_required%22%3Atrue%2C%22privileged%22%3Afalse%2C%22user_id%22%3A194301647%2C%22version%22%3A2%2C%22vod_id%22%3A1976337345%7D&transcode_mode=cbr_v1'
# dad =  'https://www.twitch.tv/videos/1976721992'

# dad = 'https://d2nvs31859zcd8.cloudfront.net/d95f4532519561cb9e6c_hasanabi_43057162779_1699905626/720p60/index-dvr.m3u8'

# print(dad[2])

variant_m3u8 = m3u8.load(dad)
# variant_m3u8.is_variant    # in this case will be True
# print(variant_m3u8.dumps())
# print(variant_m3u8.playlists[0])
# print(variant_m3u8)
for playlist, media in zip(variant_m3u8.playlists, variant_m3u8.media):
    # print(playlist.uri, '\n')
    # print(playlist.media, '\n')
    print(f'{media.name} {playlist.stream_info.bandwidth} {playlist.uri}\n')
#     # print("{:<5} {:<5} {:<5}".format(playlist.stream_info.frame_rate,playlist.stream_info.resolution[1],playlist.stream_info.bandwidth))

# variant_m3u8 = m3u8.load(dad)
# variant_m3u8.is_variant    # in this case will be True
''''''
# for playlist in variant_m3u8.playlists:
#     print(playlist.uri)
#     print(playlist.stream_info.bandwidth)
# get_variant_url = str(variant_m3u8.playlists[0])
# base_uri = get_variant_url.split('\n')[1]
# for pl in variant_m3u8.playlists:
#     stream_info = pl.stream_info
#     print( pl.uri)

# variant_m3u8 = m3u8.load(dad, custom_tags_parser=get_totalsecs_from_playlist)
# print(variant_m3u8.data['#EXT-X-TWITCH-TOTAL-SECS'])
# yo = urlparse(dad)[2].split('/')

# aa = yo[-1].replace(".m3u8", "")
# print(aa.isnumeric())
'''




"""def create_popup(windowName, content):
    global selected_items
    popup = tk.Tk()
    popup.overrideredirect(False)
    popup.title(windowName)
    popup.configure(
        bg="#0b0b13",
        border=10,
    )

    # Create a label
    label = tk.Label(
        popup,
        text=(
            "Selection/s made by clicking on a Vod/s with Mouse\nUse 'CLOSE' "
            "(Bottom Right) Button to make selection Dont use (Windows)X"
        ),
        bg="#0b0b13",
        fg="white",
        highlightcolor="white",
        justify="left"
    )
    # Place the label in the grid
    label.grid(row=2, column=1, sticky='s')

    # Calculate the maximum length of the content
    max_length = max(len(value) for value in content)

    listbox = tk.Listbox(
        popup,
        selectmode='MULTIPLE',
        width=max_length - 55,
        height=17,
        font="Calibri",
        background="#0b0b13",
        foreground='white',
        activestyle='underline',
        highlightbackground='#191325',
        highlightcolor="#433361",
        highlightthickness=5,
        selectbackground='#131b25',
        selectforeground="#129b00",
        selectborderwidth=5,
    )
    for value in content:
        listbox.insert(tk.END, f" {value}")
    listbox.grid(row=1, column=1, sticky='nsew')  # Use grid instead of pack

    # Function to get the selected item(s)
    def get_selection(event):
        global selected_items
        # Get the index of the clicked item
        clicked_index = listbox.nearest(event.y)

        # Get the text of the clicked item
        clicked_item = listbox.get(clicked_index)

        # If the item is already in the list, remove it
        if clicked_item in selected_items:
            selected_items.remove(clicked_item)
        # Otherwise, add it to the list
        else:
            selected_items.append(clicked_item)

    # Create a label
    label2 = tk.Label(
        popup,
        text=(f'Vods List for: {windowName.strip('.json').title()}'),
        bg="#0b0b13",
        fg="white",
        highlightcolor="white",
        justify="center",
        font="calabri"
    )
    # Place the label in the grid
    label2.grid(row=0, column=1, sticky='nw')

    # Bind the function to the listbox
    listbox.bind("<ButtonRelease-1>", get_selection)
    # # Set the window size
    button1 = tk.Button(
        popup,
        text="Make Selection-Close",
        command=lambda: popup.quit(),
        height=2,
        width=17,
        highlightcolor='yellow',
        background='#296d8f',
        foreground='white',
        activebackground='red',
        activeforeground='white'
    )
    button1.grid(row=2, column=1, sticky='se')  # Use grid and place at bottom right

    # Configure the grid weights
    popup.grid_columnconfigure(1, weight=1)
    popup.grid_rowconfigure(1, weight=1)

    # Update the window to calculate the size of the content
    popup.update_idletasks()

    # Get the width and height of the content
    width = popup.winfo_width()
    height = popup.winfo_height()

    # Add some padding
    width += 5
    height += 5

    # Set the window size
    popup.geometry(f"{width}x{height}")
    popup.mainloop()

    # Destroy the window
    popup.destroy()






file = "C:\\Users\\970EVO-Gamer\\AppData\\Local\\Stream-Downloader-Util\\jsons\\deadlyslob.json"
winName = os.path.basename(file)
with open(file, 'r') as f:
    jsond = json.load(f)
list1 = [('{:5}    {:25}    {:20}    {:30}    {:65}    {:25}'.format("Index", "Downloaded", "Vod Style", "VodID", "Game Name", "Title"))]
# list1 = []
for index, items in enumerate(jsond):

    list0 = items['title']
    list2 = items['id']
    list3 = items['gameName']
    list4 = items['broadcastType']
    list5 = items['downloaded']
    list6 = items['publishedAt']
    llist = ('{:7}    {:25}    {:15}    {:25}    {:60}    {:25}'.format(index, f"Downloaded:    {list5}", list4, list2, list3, list0))
    # llist = (index, list5, list4, list6, list2, list3, list0)
    list1.append(f'{llist}')

# # print("🐍 File: new_mass_gql/tk_get_file_list.py | Line: 137 | undefined ~ list1",list1)

# create_popup(winName, list1)
# lists = [items.split() for items in selected_items]
# listIndexs = [index[0] for index in lists]
# if "Index" in listIndexs:
#     listIndexs
# print("🐍 File: new_mass_gql/tessettt.py | Line: 196 | undefined ~ hhe",listIndexs)
# for index in listIndexs:
#     print(jsond[int(index)].get('title'))

"""

import subprocess

# choseendir = 'E:/DeleteStreams/FFMPEG__re-Muxed/'
# for files in os.listdir(choseendir):
#     # print(files)
#     fp = os.path.join(choseendir, files)
#     # print("🐍 File: new_mass_gql/tessettt.py | Line: 368 | undefined ~ fp",fp)

#     dldVid_sizs = subprocess.Popen(
#         rf'ffprobe -i "{fp}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1',
#         shell=False,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         universal_newlines=True,
#         cwd='c:/ffmpeg/'
#     )
#     stdout, stderr = dldVid_sizs.communicate()
#     out_pt, _ = dldVid_sizs.communicate()
#     dldVid_sizs.wait()
#     files = files.split('-')
#     print(f'{out_pt.split('.')[0]}  {files}')
    
# # result = re.sub(r"[^\w\s]", "", out_pt).split()[10:]


cmdd = r"C:/Program Files/Streamlink/ffmpeg/"
process = subprocess.Popen(r'streamlink https://www.twitch.tv/videos/1981304674 worst --hls-segment-threads 5 -o "C:\Users\970EVO-Gamer\Desktop\junkme.mp4"', stdout=subprocess.PIPE, universal_newlines=True,  cwd=cmdd)
# stdout, stderr = process.communicate()
line = ''
while True:
    char = process.stdout.read(1)
    if char == '\n' or char == '\r':
        print(line)
        line = ''
    else:
        line += char
    if '[cli][info] Stream ended' in line:
        print("success")
    if process.poll() is not None:
        break

'''# stdout, stderr = process.communicate()
for line in iter(process.stdout.readline, ''):
    print(line.rstrip())
    if '[download]' in line.rstrip():
        print('Downloading file')
'''


# dd ='[cli][info] Closing currently open stream...'
# if "Closing " in dd:
#     print('True')
# if "Closing " not in dd:
#     print('False')