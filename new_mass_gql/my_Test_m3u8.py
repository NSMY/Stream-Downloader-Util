# import json
import pprint

import gql_main_call as gql
import m3u8
import requests

# def get_m3u8_from_response(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     response = requests.get(url, headers=headers)
#     print("🐍 File: Desktop/m3u8.py | Line: 11 | get_m3u8_from_response ~ response",response)
#     rews = response.json()
#     print("🐍 File: Desktop/m3u8.py | Line: 13 | get_m3u8_from_response ~ rews",rews)
#     if response.status_code == 200:
#         data = json.loads(response.text)
#         m3u8_url = data.get('m3u8_url')  # replace 'm3u8_url' with the actual key in the response
#         return m3u8_url
#     else:
#         return None


# url = "https://www.twitch.tv/theprimeagen"  # replace with your actual API endpoint
# m3u8_url = get_m3u8_from_response(url)

# if m3u8_url is not None:
#     print(m3u8_url)
# else:
#     print("Failed to retrieve the M3U8 URL.")


# get est file size.
def estimate_video_size(bandwidth_bps, total_secs):
    # Calculate the total size in bits
    total_bits = bandwidth_bps * total_secs

    # Convert bits to gigabytes
    total_gb = total_bits / 8 / 1024 / 1024 / 1024

    return total_gb

# # Bandwidth in bits per second
# bandwidth_bps = 8660544

# # Total duration in seconds
# total_secs = 33882.973

# # Estimate the video size
# estimated_size_gb = estimate_video_size(bandwidth_bps, total_secs)

# print(f"The estimated size of the video is approximately {estimated_size_gb:.2f} GB.")


def get_playlist_uris(video_id: str, access_token: dict):
    """
    Grabs the URI's for accessing each of the video chunks.
    """
    url = f"http://usher.ttvnw.net/vod/{video_id}"

    resp = requests.get(url, timeout=5, params={
        "nauth": access_token['value'],
        "nauthsig": access_token['signature'],
        "allow_source": "true",
        "player": "twitchweb",
    })
    resp.raise_for_status()

    data = resp.content.decode("utf-8")

    playlist = m3u8.loads(data)
    # Hack for temp results make better.
    url = data.split('\n')[4]
    seconds_of_Vod = requests.get(url)
    s = seconds_of_Vod.text.split()[7]
    s2 = s.split(':')
    s3 = float(s2[1])

    for pl in playlist.playlists:
        stream_info = pl.stream_info
        bandwidth = stream_info.bandwidth
        print(f'{estimate_video_size(bandwidth_bps=bandwidth, total_secs=s3):.2f} GB')

    return [p.uri for p in playlist.playlists]


vodid = '1962354205'
netlock = 'https://usher.ttvnw.net'

url = f'{netlock}/vod/{vodid}.m3u8'

# params = '?acmb=e30=&allow_source=true&cdm=wv&p=1624678&play_session_id=52cdab5bfaed022d084cc1b8f79ba508&player_backend=mediaplayer&player_version=1.23.0&playlist_include_framerate=true&reassignments_supported=true&sig=7f75edda18029f7a9f0eac2f03f4306ed28570af&supported_codecs=avc1&token={"authorization":{"forbidden":false,"reason":""},"chansub":{"restricted_bitrates":[]},"device_id":"hWRkqsm5Bz5Ze9dLlxNGjeVVZ4YDDPzO","expires":1699237483,"https_required":true,"privileged":false,"user_id":null,"version":2,"vod_id":1962354205}&transcode_mode=cbr_v1'
# url1 = url + params

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }
# response = requests.get(url1, headers=headers)
# print(response)
# rews = response.text.split("#")
# pprint.pprint(rews)


# master = m3u8.loads(response.text)
# dd = master.data['playlists'][0]["uri"]
# rr = requests.get(dd, headers=headers)
# playlist = m3u8.loads(rr.text)
# pprint.pprint(playlist.data)


video_id = vodid

# Grab access token
access_token = gql.get_access_token(video_id)

# Get M3U8 playlist, and parse them
# (first URI is always source quality!)
uris = get_playlist_uris(video_id, access_token)
source_uri = uris[0]

# Fetch playlist at proper quality
resp = requests.get(source_uri)
resp.raise_for_status()
# playlist = m3u8.loads(resp.text)
