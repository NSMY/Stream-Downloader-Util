
# import json
import json
import os
from urllib.parse import urlparse, urlunparse

import m3u8

from new_mass_gql.utility_dir import util_functions as utill

# url = 'https://www.twitch.tv/videos/1972875530'
# url = 'https://www.twitch.tv/videos/1982124389?t=01h14m26s'
# url = 'https://www.twitch.tv/videos/1981192341?filter=archives&sort=time'
# # url = 'https://www.twitch.tv/etalyx'
# # url = 'https://usher.ttvnw.net/vod/1982669879.m3u8?acmb=e30%3D&allow_source=true&browser_family=firefox&browser_version=119.0&cdm=wv&os_name=Windows&os_version=NT%2010.0&p=602199&platform=web&play_session_id=4829124e3474f79b5cb7c29f5c7e7e65&player_backend=mediaplayer&player_version=1.23.0&playlist_include_framerate=true&reassignments_supported=true&sig=3432efaaeef66d80b6920db6f0718e9ab21fd391&supported_codecs=h264&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22chansub%22%3A%7B%22restricted_bitrates%22%3A%5B%5D%7D%2C%22device_id%22%3A%22L8lFfAYG1PKKuwUFH5gJJhtC4mSOAefS%22%2C%22expires%22%3A1700633570%2C%22https_required%22%3Atrue%2C%22privileged%22%3Afalse%2C%22user_id%22%3A194301647%2C%22version%22%3A2%2C%22vod_id%22%3A1982669879%7D&transcode_mode=cbr_v1'
# # url = 'https://www.youtube.com/watch?v=NE4Exqt_0z8'
# # url = 'https://d2nvs31859zcd8.cloudfront.net/0a8060ce24c8559879af_trash_dev_43092903451_1700500921/chunked/index-dvr.m3u8'

# urlparsed = urlparse(url)
# # print(urlparsed)
# def parse_url_twitch(url):
#     if not urlparsed.path.split('/')[-1].isnumeric():
#         return urlunparse(urlparsed)
#     if urlparsed.query.startswith(('t=', 'acmb=')):
#         return url
#     elif urlparsed.query.startswith('filter='):
#         new_url_parts = (urlparsed.scheme, urlparsed.netloc, urlparsed.path, '', '', '')
#         return urlunparse(new_url_parts)
#     else:
#         return url
# url_ = parse_url_twitch(url)
# # playlist = m3u8.load(url)
# # get_variant_url = str(playlist.playlists[0])
# # print("🐍 File: zextra_Funcs_/Testcode.py | Line: 26 | undefined ~ get_variant_url",get_variant_url)
# print("🐍 File: Stream-Downloader-Util/Testcode.py | Line: 23 | undefined ~ url_",url_)

# # print(urlparsed.path.split('/'))
# # recombined = urlunparse(urlparsed)
# # print(recombined)


# import subprocess

# # # [] pass the index form vod find?? how to find if only passed vod id -not from file? 
# # # pass the file res dld'd to the 'download' key, and compare retrieve chosen size
# # # with actual file size after dld with ffprobe 
# # jjk
# # print("🐍 File: Stream-Downloader-Util/Testcode.py | Line: 37 | undefined ~ jjk",jjk) 
# # from new_mass_gql.utility_dir import util_functions
# # from new_mass_gql.utility_dir import util_functions as utill

# # matchid = '1929999644'
# # target_id = '1874626710'

# # with open('C:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/etalyx.json', 'r') as f:
# #     lkl = json.load(f)
# # jjk = [(indx, items.get('id')) for indx, items in enumerate(lkl)]



# # dirr = r'C:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/'

# dld_filepath = r'C:\Users\970EVO-Gamer\Desktop\Deadlyslob - 20-11-2023 Richard Heads Sturgian Conquest  Day 4  Join just once  Glasses Mount  Blade II Bannerlord.mp4'
# size = os.path.getsize(dld_filepath)
# def convert_bytes(num):
#     """
#     this function will convert bytes to MB.... GB... etc
#     """
#     for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
#         if num < 1024.0:
#             return num
#         num /= 1024.0
#     return num



# def compare_sizes(size1, size2, tolerance):
#     """
#     This function compares two file sizes with a certain tolerance.
#     """
#     return abs(size1 - size2) <= tolerance

# # xfile = 34.6  # size of the first file in GB
# xfile = int(convert_bytes(size))
# zfile = 11.03  # size of the second file in GB

# print(xfile /20)
# print(compare_sizes(xfile, zfile, xfile/20 ))

# # [] have to  make a if file is dld voa nested iffs if len if size if title?? if date?
# # [] then have to check if the input is ?t=04h55m35s then offset timecode with total 
# # [] to get true len/size
# # [] maybe need pass total seconds from get vodsize call in order to get non file vods
# # [] also might need to do the pipout stdOut and look for stream ended / error etc
# # however it may block streamlink y/n questions??.


# # dload_predicted_size = ''
# # dld_filepath = r'E:\DeleteStreams\FFMPEG__re-Muxed\Kotton - 18-11-2023 Selling Base Today  Archonexus pt 2  500 BrutalCassandra mods RimWorld.mp4'
# # slinkDir = 'C:/ffmpeg/'
# # string = f'ffprobe -i "{dld_filepath}" -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1'
# # dld_vid_size = subprocess.Popen(string, stdout=subprocess.PIPE, text=True, cwd=slinkDir)
# # out_pt = dld_vid_size.stdout.read()
# # # print(str(out_pt.strip()).split("'")[1])
# # print(int(float(out_pt)))
# # print(utill.decode_seconds_to_hms(int(float(out_pt))))


target_id = '1709345985'
new_value = '720p60'




