

import json
import os
import pprint

import requests

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
	return gql_post(json={"query":query}, data=data)

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

streamer_user_name = 'workthespace'


# get videos of multiple types
# past streams = ARCHIVE, segment of stream = HIGHLIGHT, upload = UPLOAD, premiere = PAST_PREMIERE


# Sort by View Count
# query = GET_CHANNEL_VIDEOS_QUERY.format(
#     channel_id=user_id,
# 	after=pagination, first=100,
#     sort="VIEWS"
# )

def query_channel_vods(
    streamer_user_name: str,
    num_of_streams: int=100,
    sort_by: str="TIME"
    ):
        """
        Args:
            streamer_user_name (str): User Name of the streamer.
            num_of_streams (int, optional): MAX No. of VODs returned
            . Defaults to 100.
            sort_by (CAPstr, optional): TIME/VIEWS/TRENDING. Defaults to "TIME".
            

        Returns:
            GQL Map: dict of streams info
        """
        pagination = "null"
        
        query = GET_CHANNEL_VIDEOS_QUERY.format(
            channel_id=streamer_user_name,
            after=pagination, first=num_of_streams,
            sort=sort_by
        )
        return query

# gets last Vod.
# query = GET_CHANNEL_VIDEOS_QUERY.format(
#     channel_id=user_id,
# 	after=pagination, first=1,
#     sort="TIME"
# )


query = query_channel_vods(streamer_user_name, 100, "TIME")
resp = gql_query(query=query).json()

print("🐍 File: Desktop/gql.py | Line: 72 | undefined ~ resp",resp)
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
    """Creates a Vod Class instance
    """
    def __init__(self, node):
        self.creatorId = node['creator']['id']
        self.login = node['creator']['login']
        self.displayName = node['creator']['displayName']
        self.id = node['id']
        self.title = node['title']
        self.publishedAt = node['publishedAt']
        self.broadcastType = node['broadcastType']
        self.status = node['status']
        self.lengthSeconds = node['lengthSeconds']
        self.viewCount = node['viewCount']
        if node.get('game'):  # Check if 'game' exists in the node and is not None
            self.gameId = node['game']['id']
            self.gameName = node['game']['name']
        else:
            self.gameId = "N/A"
            self.gameName = "N/A"
        self.url = f"https://www.twitch.tv/videos/{self.id}"
        self.not_downloaded = True

    def __repr__(self):
        # ID by STREAMER at DATETIME, LENGTH vodbot description
        return f"Vod({self.id}, {self.login}, {self.broadcastType}, {self.status}, {self.publishedAt}, {self.lengthSeconds}s, {self.title})"

    
# for loops that 1 filter out ineligible characters in 'title' then creates vod instance/s.
vods = [Vod({**edge['node'], 'title': ''.join(c for c in edge['node']['title'] if c.isalnum() or c.isspace())}) for edge in resp['data']['user']['videos']['edges']]


file_path = fr'jsons/{streamer_user_name}.json'

# Convert Vod instances to dictionaries
vods_dict = [vars(vod) for vod in vods]

file_check_path = os.path.exists(file_path)




first_dict_check = vods_dict[0]
first_gql_index_id = first_dict_check['id']
gql_status_check = first_dict_check['status']
print("🐍 File: New-twitch-mass-downloader/gql.py | Line: 161 | undefined ~ gql_status_check",gql_status_check)
print(first_gql_index_id)


# Writing to json.
if file_check_path:
    with open(file_path, 'r') as f:
        json_dicts = json.load(f)
    
    # vars for the if checks.
    first_json_dict = json_dicts[0]
    first_json_index_id = first_json_dict['id']
    
    if first_gql_index_id != first_json_index_id:
        new_dict = first_dict_check
        json_dicts.insert(0, new_dict)
        json_dicts.pop(-1) # Deletes Last entry.
        with open(file_path, 'w') as f:
            json.dump(json_dicts, f, indent=4)


if not file_check_path:
    with open(file_path, 'w') as json_file:
        json.dump(vods_dict, json_file, indent=4)

# Now you can print each Vod instance
for vod in vods:
    print(vod)

# # And you can find out how many there are
# # print(len(vods))







# # # d = str(resp)
# # # dd = d.split("{\'cursor\'")
# # # print("🐍 File: Desktop/gql.py | Line: 97 | undefined ~ d",dd)
# # with open(file_path, 'w') as json_file:
# #     json.dump(vods, json_file, indent=4)


class Vod:
    """Creates a Vod Class instance
    """
    def __init__(self, node):
        self.creatorId = node['creator']['id']
        self.login = node['creator']['login']
        self.displayName = node['creator']['displayName']
        self.id = node['id']
        self.title = node['title']
        self.publishedAt = node['publishedAt']
        self.broadcastType = node['broadcastType']
        self.status = node['status']
        self.lengthSeconds = node['lengthSeconds']
        self.viewCount = node['viewCount']
        if node.get('game'):  # Check if 'game' exists in the node and is not None
            self.gameId = node['game']['id']
            self.gameName = node['game']['name']
        else:
            self.gameId = "N/A"
            self.gameName = "N/A"
        self.url = f"https://www.twitch.tv/videos/{self.id}"
        self.not_downloaded = True
        
    def __repr__(self):
        # ID by STREAMER at DATETIME, LENGTH vodbot description
        return f"Vod({self.id}, {self.login}, {self.broadcastType}, {self.status}, {self.publishedAt}, {self.lengthSeconds}s, {self.title})"


# # INIT- for loops that 1 filter out ineligible characters in 'title' then creates vod instance/s.
# vods = [Vod({**edge['node'], 'title': ''.join(c for c in edge['node']['title'] if c.isalnum() or c.isspace())}) for edge in resp['data']['user']['videos']['edges']]
