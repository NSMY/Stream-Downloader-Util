# gets sizes of vods id's using m3u8 gql query calls.

# from urllib.parse import urlparse
# from pyperclip import copy, paste

# import gql_main_call as gql
import m3u8
import requests

from . import gql_main_call as gql


# get est file size.
def estimate_video_size(bandwidth_bps, total_secs):
    # Calculate the total size in bits
    total_bits = bandwidth_bps * total_secs

    return total_bits / 8 / 1024 / 1024 / 1024


def get_playlist_uris(video_id: str, access_token: dict, lengthSeconds=None) -> dict:
    """
    Grabs the URI's for accessing each of the video chunks.

    Returns: Dict
            key(resolution): dict{vod_GB, VariantURI}
    """
    url = f"http://usher.ttvnw.net/vod/{video_id}"

    # Requests is calling and -> a string but m3u8.
    # just needs the URL and doesn't use the -> data from the req call.
    # Meaningless Call.
    resp = requests.get(
        url,
        timeout=5,
        params={
            "nauth": access_token["value"],
            "nauthsig": access_token["signature"],
            "allow_source": "true",
            "player": "twitchweb",
        },
    )
    data = resp.url
    # resp.raise_for_status()
    # data = resp.content.decode("utf-8") # decodes if needs the -> data.
    playlist = m3u8.load(data)

    if not lengthSeconds:
        get_variant_url = str(playlist.playlists[0])
        base_uri = get_variant_url.split("\n")[1]
        variant_m3u8 = m3u8.load(
            base_uri, custom_tags_parser=get_totalsecs_from_playlist
        )
        string_seconds = variant_m3u8.data["#EXT-X-TWITCH-TOTAL-SECS"]
        seconds_ = int(float(string_seconds))
    else:
        seconds_ = lengthSeconds

    dictt = {}
    for mea, pl in zip(playlist.media, playlist.playlists):
        stream_info = pl.stream_info
        bandwidth = stream_info.bandwidth
        name = mea.name.lower()
        size = "{:.2f}".format(
            estimate_video_size(bandwidth_bps=bandwidth, total_secs=seconds_)
        )
        dictt[name] = [size, pl.uri]
        # print("{:<5} {:<10}".format(resolution, f'{size} GB'))
    # print(dictt)
    return dictt


def get_totalsecs_from_playlist(line, lineno, data, state):
    if line.startswith("#EXT-X-TWITCH-TOTAL-SECS"):
        custom_tag = line.split(":")
        data["#EXT-X-TWITCH-TOTAL-SECS"] = custom_tag[1].strip()


def m3u8_call_init(video_id):
    # def m3u8_call_init():
    # video_id = urlparse(paste())[2].strip("videos/")
    netlock = "https://usher.ttvnw.net"
    url = f"{netlock}/vod/{video_id}.m3u8"

    # Grab access token
    access_token = gql.get_access_token(video_id)

    # Get M3U8 playlist, and parse them
    # (first URI is always source quality!)
    resolutions_uris = get_playlist_uris(video_id, access_token)
    # for key, value in resolutions_uris[0].items():
    #     print("{:<5} {:<10}".format(f'{key}', f'{value} GB'))
    # value = uris[0]['720']
    # print("🐍 File: new_mass_gql/my_Test_m3u8.py | Line: 67 | m3u8_call_init ~ value",value)
    # print("{:<5} {:<10}".format(f'{key}', f'{value} GB'))
    # source_uri = uris[1][0]
    # print("🐍 File: new_mass_gql/my_Test_m3u8.py | Line: 123 | undefined ~ source_uri",source_uri)
    return resolutions_uris


# m3u8_call_init()

# passd_size = '1008'

# print("{:<5} {:<10}".format(passd_size, f'{m3u8_call_init(video_id='1975917753')[0][passd_size]} GB'))
