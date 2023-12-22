# gets sizes of vods id's using m3u8 gql query calls.

# from urllib.parse import urlparse
# from pyperclip import copy, paste

import logging
import os
from urllib.error import HTTPError
from urllib.parse import urlencode

# import gql_main_call as gql
import m3u8
import requests

from . import gql_main_call as gql


# get est file size.
def estimate_video_size(bandwidth_bps, total_secs):
    # Calculate the total size in bits
    total_bits = bandwidth_bps * total_secs
    return total_bits / 8 / 1024 / 1024 / 1024


def get_playlist_uris(
    *,
    video_id: str,
    access_token: dict,
    lengthSeconds=None,
    minus_time=0,
    attempt=0
) -> dict:

    """
    Grabs the URI's for accessing each of the video chunks.

    Returns: Dict
            key(resolution): dict{vod_GB, VariantURI}
    """
    url = f"http://usher.ttvnw.net/vod/{video_id}"

    params = {
        "nauth": access_token["value"],
        "nauthsig": access_token["signature"],
        "allow_source": "true",
        "player": "twitchweb",
    }

    data = f'{url}?{urlencode(params)}'
    try:
        playlist = m3u8.load(data)
    except HTTPError:
        return {'': 'Likely Sub Only Vod'}

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
        if attempt > 5:
            print("\nMax attempts reached, request failed, Bandwidth == 0")
            return {"Failed retrieving Bandwidth ": "N/A"}
        elif bandwidth == 0: # Maybe a Temp Twitch Bug Maybe Outdated Streamlink(6.0.1), sometimes Bandwidth Fails to populate retrying fixes
            logging.info(f'{os.path.basename(__file__)} data ' '%s', data)
            logging.info(f'{os.path.basename(__file__)} get_variant_url ' '%s', stream_info)
            logging.info(f'{os.path.basename(__file__)} bandwidth ' '%s', bandwidth)
            print(f"Bandwidth == 0, Attempt {attempt} failed, retrying...")
            attempt += 1
            return get_playlist_uris(
                attempt=attempt,
                video_id=video_id,
                access_token=access_token,
                lengthSeconds=lengthSeconds,
                minus_time=minus_time
            )
        name = mea.name.lower()
        # size = "{:.2f}".format(
        #     estimate_video_size(
        #         bandwidth_bps=bandwidth,
        #         total_secs=seconds_ - minus_time
        #     )
        # )
        size = f"{estimate_video_size(bandwidth_bps=bandwidth, total_secs=seconds_ - minus_time):.2f}"

        dictt[name] = [size, pl.uri]
        # print("{:<5} {:<10}".format(resolution, f'{size} GB'))
    # print(dictt)
    return dictt


def get_totalsecs_from_playlist(line, lineno, data, state):
    if line.startswith("#EXT-X-TWITCH-TOTAL-SECS"):
        custom_tag = line.split(":")
        data["#EXT-X-TWITCH-TOTAL-SECS"] = custom_tag[1].strip()


def m3u8_call_init(video_id, tot_seconds=None, minus_time=0) -> dict:
    """_summary_

    Args:
        video_id (Str): id path of twitch url
        tot_seconds (int, optional): total_seconds of vod if less than maximum. Defaults to None and gets from m3u8 data.

    Returns:
        dict: vod_sizes{[sizeGB, URI]}
    """
    netlock = "https://usher.ttvnw.net"
    url = f"{netlock}/vod/{video_id}.m3u8"
    access_token = gql.get_access_token(video_id)

    return get_playlist_uris(video_id=video_id, access_token=access_token, lengthSeconds=tot_seconds, minus_time=minus_time)


