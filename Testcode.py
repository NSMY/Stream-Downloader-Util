
# from urllib.parse import urlparse, urlunparse

# # url = 'https://www.twitch.tv/videos/1972875530'
# # url = 'https://www.twitch.tv/videos/1982124389?t=01h14m26s'
# url = 'https://www.twitch.tv/videos/1981192341?filter=archives&sort=time'
# # url = 'https://www.twitch.tv/etalyx'
# # url = 'https://usher.ttvnw.net/api/channel/hls/etalyx.m3u8?acmb=e30%3D&allow_source=true&browser_family=firefox&browser_version=119.0&cdm=wv&fast_bread=true&os_name=Windows&os_version=NT%2010.0&p=5923062&platform=web&play_session_id=4ab5e211d7b0d614e65c23d35533cf7b&player_backend=mediaplayer&player_version=1.23.0&playlist_include_framerate=true&reassignments_supported=true&sig=d34b832292d5a184712b2b230d90a1a1dc824974&supported_codecs=h264&token=%7B%22adblock%22%3Afalse%2C%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22blackout_enabled%22%3Afalse%2C%22channel%22%3A%22etalyx%22%2C%22channel_id%22%3A28054687%2C%22chansub%22%3A%7B%22restricted_bitrates%22%3A%5B%5D%2C%22view_until%22%3A1924905600%7D%2C%22ci_gb%22%3Afalse%2C%22geoblock_reason%22%3A%22%22%2C%22device_id%22%3A%22L8lFfAYG1PKKuwUFH5gJJhtC4mSOAefS%22%2C%22expires%22%3A1700452274%2C%22extended_history_allowed%22%3Afalse%2C%22game%22%3A%22%22%2C%22hide_ads%22%3Afalse%2C%22https_required%22%3Atrue%2C%22mature%22%3Afalse%2C%22partner%22%3Afalse%2C%22platform%22%3A%22web%22%2C%22player_type%22%3A%22site%22%2C%22private%22%3A%7B%22allowed_to_view%22%3Atrue%7D%2C%22privileged%22%3Afalse%2C%22role%22%3A%22%22%2C%22server_ads%22%3Atrue%2C%22show_ads%22%3Atrue%2C%22subscriber%22%3Afalse%2C%22turbo%22%3Afalse%2C%22user_id%22%3A194301647%2C%22user_ip%22%3A%22119.12.208.21%22%2C%22version%22%3A2%7D&transcode_mode=cbr_v1'
# # url = 'https://www.youtube.com/watch?v=NE4Exqt_0z8'

# urlparsed = urlparse(url)
# # print(urlparsed)
# if urlparsed.path.split('/')[-1].isnumeric():
#     if urlparsed.query.startswith('t='):
#         url_ = url
#     elif urlparsed.query.startswith('filter='):
#         new_url_parts = (urlparsed.scheme, urlparsed.netloc, urlparsed.path, '', '', '')
#         url_ = (urlunparse(new_url_parts))
# elif urlparsed.query.startswith('acmb='):
#     url_ = url
# else:
#     url_ = (urlunparse(urlparsed))


# print("🐍 File: Stream-Downloader-Util/Testcode.py | Line: 23 | undefined ~ url_",url_)

# # print(urlparsed.path.split('/'))
# # recombined = urlunparse(urlparsed)
# # print(recombined)


import json

matchid = '1929999644'

with open('C:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/etalyx.json', 'r') as f:
    lkl = json.load(f)
jjk = [(indx, items.get('id')) for indx, items in enumerate(lkl)]


# [] pass the index form vod find?? how to find if only passed vod id -not from file? 
# pass the file res dld'd to the 'download' key, and compare retrieve chosen size
# with actual file size after dld with ffprobe 
jjk
print("🐍 File: Stream-Downloader-Util/Testcode.py | Line: 37 | undefined ~ jjk",jjk)