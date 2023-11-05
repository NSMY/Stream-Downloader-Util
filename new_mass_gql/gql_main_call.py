import json
import os
import pprint
import timeit

import requests

from new_mass_gql.utility_dir import util_functions as util

start_time = timeit.default_timer()


gql_client: str = "kd1unb4b3q4t58fwlpcbzcbnm76a8fp"
GQL_URL = "https://gql.twitch.tv/gql"
GQL_HEADERS = {"Client-ID": ""}


class GQLException(Exception):
    pass


class GQLItemError(Exception):
    pass


# We use Twitch's private client ID for GQL calls
def set_client_id(client_id: str):
    global GQL_HEADERS
    GQL_HEADERS["Client-ID"] = client_id


def _process_query_errors(resp):
    j = resp.json()
    if 400 <= resp.status_code < 500 or "errors" in j:
        raise GQLException(j)


def gql_post(json=None, data=None):
    global GQL_URL, GQL_HEADERS
    resp = requests.post(GQL_URL, json=json, data=data, headers=GQL_HEADERS)
    _process_query_errors(resp)
    return resp


def gql_query(query=None, data=None):
    return gql_post(json={"query": query}, data=data)


def get_access_token(video_id):
    """
    Gets the VOD player access token, used to stream the VOD to the host.
    """
    query = VIDEO_ACCESS_QUERY.format(video_id=video_id)

    resp = gql_query(query=query).json()

    return resp["data"]["videoPlaybackAccessToken"]


# GQL Query forms
# Channel VODs query
GET_CHANNEL_VIDEOS_QUERY = """
{{  user(login: "{channel_id}") {{
        videos( first: {first}, sort: {sort}, after: {after} ) {{
            totalCount
            edges {{ cursor
                node {{
                    id title publishedAt broadcastType status lengthSeconds viewCount
                    game {{ id name }}
                    creator {{ id login displayName }}
}}  }}  }}  }}  }}
"""

VIDEO_ACCESS_QUERY = """
{{  videoPlaybackAccessToken(
        id: {video_id},
        params: {{ platform:"web", playerBackend:"mediaplayer", playerType:"site" }}
    ) {{ signature value }}
}}
"""

# Single Channel info query
GET_CHANNEL_QUERY = """
{{  user(login: "{channel_id}") {{
        id login displayName
        description createdAt
        roles {{ isAffiliate isPartner }}
        stream {{
            id title type viewersCount createdAt game {{ id name }}
}}  }}  }}
"""

# VOD chapters query
GET_VIDEO_CHAPTERS = """{{
video(id: {id}) {{
    moments(first:100, momentRequestType: VIDEO_CHAPTER_MARKERS, after: {after}) {{
        edges {{ cursor node {{
            description type positionMilliseconds durationMilliseconds
}}  }}  }}  }}  }}
"""

set_client_id(gql_client)


# get videos of multiple types
# past streams = ARCHIVE, segment of stream = HIGHLIGHT, upload = UPLOAD, premiere = PAST_PREMIERE


# Sort by View Count
# query = GET_CHANNEL_VIDEOS_QUERY.format(
#     channel_id=user_id,
# 	after=pagination, first=100,
#     sort="VIEWS"
# )


def query_channel_vods(
    streamer_user_name: str, num_of_streams: int = 100, sort_by: str = "TIME"
):
    """
    Args:
        streamer_user_name (str): User Name of the streamer.
        num_of_streams (int, optional): MAX No. of VODs returned
        . Defaults to 100.
        sort_by (CAPstr, optional): TIME/VIEWS/TRENDING. Defaults to "TIME".


    Returns:
        GQL Map: [lsit{dict}] of streams info
    """
    pagination = "null"

    return GET_CHANNEL_VIDEOS_QUERY.format(
        channel_id=streamer_user_name,
        after=pagination,
        first=num_of_streams,
        sort=sort_by,
    )


# [x]HUGE GAINS.


# TODO Combine new with old from testttt and resave _ sep class and the saving of the class.

# resp2 = json.loads(resp)


# print(resp2)
# print(type(resp2))
# print(resp2.get("id"))
# print("🐍 File: Desktop/gql.py | Line: 72 | undefined ~ resp",resp)
# for item in resp:
#     print(item['1'])


# pprint.pprint(resp)

# # Loop over the dictionaries in the list
# for item in resp:
#     # Get the 'title' field
#     title = item['title']

#     # Filter out non-alphabet characters from the title
#     filtered_title = ''.join(c for c in title if c.isalpha() or c.isspace())

#     # Replace the 'title' field with the filtered title
#     item['title'] = filtered_title


# print("🐍 File: New-twitch-mass-downloader/gql.py | Line: 124 | undefined ~ resp",resp)


class Vod:
    """
    A class to represent a Video on Demand (Vod).
    Methods
    -------
    __repr__():
        Returns a string representation of the Vod instance.

    create_vods_from_edges(edges: list):
        Class method that creates a list of Vod instances from a list of edges, each containing a 'node' dictionary.
        It cleans up the title of each node and creates a new Vod instance from each cleaned node.
        Returns a list of these Vod instances.

        How to call using a gqlquery map return:
        vods = Vod.create_vods_from_edges(resp['data']['user']['videos']['edges'])
    """

    def __init__(self, node):
        self.creatorId = node["creator"]["id"]
        self.login = node["creator"]["login"]
        self.displayName = node["creator"]["displayName"]
        self.id = node["id"]
        self.title = node["title"]
        self.publishedAt = node["publishedAt"]
        self.broadcastType = node["broadcastType"]
        self.status = node["status"]
        self.lengthSeconds = node["lengthSeconds"]
        self.viewCount = node["viewCount"]
        if node.get("game"):  # Check if 'game' exists in the node and is not None
            self.gameId = node["game"]["id"]
            self.gameName = node["game"]["name"]
        else:
            self.gameId = "N/A"
            self.gameName = "N/A"
        self.url = f"https://www.twitch.tv/videos/{self.id}"
        self.not_downloaded = True

    def __repr__(self):
        # ID by STREAMER at DATETIME, LENGTH vodbot description
        return f"Vod({self.id}, {self.login}, {self.broadcastType}, {self.status}, {self.publishedAt}, {self.lengthSeconds}s, {self.title}, {self.gameName})"

    @classmethod
    def create_vods_from_edges(cls, edges):
        vods = []
        for edge in edges:
            edge["node"]["title"] = "".join(c for c in edge["node"]["title"] if c.isalnum() or c.isspace())

            edge["node"]["game"]["name"] = "".join(g for g in edge["node"]["game"]["name"] if g.isalnum() or g.isspace())
            vods.append(cls(edge["node"]))
        return vods


# streamer_user_name = 'kotton'
# query = query_channel_vods(streamer_user_name, 100, "TIME")
# resp = gql_query(query=query).json()
# print("🐍 File: New-twitch-mass-downloader/gql.py | Line: 214 | undefined ~ resp",resp)


def First_making_cmds():
    streamer_user_name = input("Enter Streamer User Name: ").lower()
    # if file exist ?? .
    query = query_channel_vods(streamer_user_name, 100, "TIME")
    query_resp = gql_query(query=query)
    resp = query_resp.json()
    # [] still need to sort our the recording/archive/highlight/upload/premiere
    if query_resp.status_code != 200:
        print("Error retrieving Data from GraphQL Twitch API")
        return
    elif resp['data']['user'] is None:
        print("Error No User Found")
        First_making_cmds()
        return
    elif resp['data']['user']['videos']['totalCount'] == 0:
        print("Error No Videos Found")
        First_making_cmds()
        return

    # file_path = f"jsons/{streamer_user_name}.json"
    file_path = rf"{util.get_appdata_dir()}\jsons\{streamer_user_name}.json"

    vods = Vod.create_vods_from_edges(resp["data"]["user"]["videos"]["edges"])

    # Convert Vod instances to dictionaries
    vods_dict = [vars(vod) for vod in vods]
    # pprint.pprint(vods_dict)
    util.dump_json_ind4(file_path=file_path, content_dump=vods_dict)
    # Now you can print each Vod instance
    # for vod in vods:
    #     print(vod)

    pprint.pprint(vods)

    # And you can find out how many there are
    # print(f'Found :{len(vods)} Vods')


# First_making_cmds()
# file_check_path = os.path.exists(file_path)


# first_dict_check = vods_dict[0]
# first_gql_index_id = first_dict_check['id']
# gql_status_check = first_dict_check['status']
# print("🐍 File: New-twitch-mass-downloader/gql.py | Line: 161 | undefined ~ gql_status_check",gql_status_check)
# print(first_gql_index_id)


# with open(file_path, 'r') as f:
#     content = json.load(f)


# # # d = str(resp)
# # # dd = d.split("{\'cursor\'")
# # # print("🐍 File: Desktop/gql.py | Line: 97 | undefined ~ d",dd)
# # with open(file_path, 'w') as json_file:
# #     json.dump(vods, json_file, indent=4)





# Your script here

end_time = timeit.default_timer()
execution_time = end_time - start_time
print(f"The script took {execution_time} seconds to run.")