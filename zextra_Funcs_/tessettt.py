


# import os

# dir = r'F:/Music/Musizz/My Shared Folder/'


# for files in os.listdir(dir):
#     print(files)

from urllib.parse import urlencode

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
    print(f'{GQL_URL, json, data, GQL_HEADERS =}')
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
					id title publishedAt broadcastType status lengthSeconds
					game {{ id name }}
					creator {{ id login displayName }}
}}  }}  }}  }}  }}
"""
# Channel Clips query
# period can be LAST_DAY, LAST_WEEK, LAST_MONTH, or ALL_TIME
GET_CHANNEL_CLIPS_QUERY = """
{{  user(login: "{channel_id}") {{
		clips(
			first: {first}, after: {after},
			criteria: {{ period: ALL_TIME, sort: VIEWS_DESC }}
		) {{
			pageInfo {{ hasNextPage }}
			edges {{ cursor node {{
				id slug title createdAt viewCount
				durationSeconds videoOffsetSeconds
				video {{ id }}
				game {{ id name }}
				broadcaster {{ id displayName login }}
				curator {{ id displayName login }}
}}  }}  }}  }}  }}
"""
# Single VOD query
GET_VIDEO_QUERY = """
{{  video(id: "{video_id}") {{
		id title publishedAt
		broadcastType lengthSeconds
		game {{ id name }} creator {{ id login displayName }}
}}  }}
"""
# Single Clip query
GET_CLIP_QUERY = """
{{  clip(slug: "{clip_slug}") {{
		id slug title createdAt viewCount durationSeconds videoOffsetSeconds
		game {{ id name }} video {{ id }}
		videoQualities {{ frameRate quality sourceURL }}
		broadcaster {{ id displayName login }}
		curator {{ id displayName login }}
}}  }}
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
# IRC Chat query
GET_VIDEO_COMMENTS_QUERY = """
{{ video(id: "{video_id}") {{
	comments(contentOffsetSeconds: 0, after: {after}) {{
		edges {{ cursor node {{
			contentOffsetSeconds
			commenter {{ displayName }}
			message {{ userColor fragments {{ mention {{ displayName }} text }} }}
}}  }}  }}  }} }}
"""
# VOD chapters query
GET_VIDEO_CHAPTERS = """{{
video(id: {id}) {{
    moments(first:100, momentRequestType: VIDEO_CHAPTER_MARKERS, after: {after}) {{
        edges {{ cursor node {{
            description type positionMilliseconds durationMilliseconds
}}  }}  }}  }}  }}
"""


VIDEO_ACCESS_QUERY = """
{{  videoPlaybackAccessToken(
		id: {video_id},
		params: {{ platform:"web", playerBackend:"mediaplayer", playerType:"site" }}
	) {{ signature value }}
}}
"""

messages = []
pagination = "null"

query = GET_VIDEO_COMMENTS_QUERY.format(
    video_id="2010087465", first=100, after=pagination
)
resp = gql_query(query=query).json()