# async with GQL things is working for chapters. needs gql main call vars to work properly

import json

import httpx

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
    resp = httpx.post(GQL_URL, json=json, data=data, headers=GQL_HEADERS)
    _process_query_errors(resp)
    return resp


def gql_query(query=None, data=None):
    return gql_post(json={"query": query}, data=data)


# VOD chapters query
GET_VIDEO_CHAPTERS = """{{
video(id: {id}) {{
    moments(first:100, momentRequestType: VIDEO_CHAPTER_MARKERS, after: {after}) {{
        edges {{ cursor node {{
            description type positionMilliseconds durationMilliseconds
}}  }}  }}  }}  }}
"""

chapter_page = 'null'
with open('C:/Users/970EVO-Gamer/AppData/Local/Stream-Downloader-Util/jsons/deadlyslob.json', 'r') as f:
    data = json.load(f)

chapters = []
gql_queries = []
for index, items in enumerate(data):
    
    query = GET_VIDEO_CHAPTERS.format(
    id=items.get('id'), after=chapter_page
    )
    gql_queries.append((index, query))
    

import asyncio

import httpx

semaphore = asyncio.Semaphore(10)  # Funky outcomes sometimes 10,50,100 all error.

async def fetch(GQL_URL, gql_query, GQL_HEADERS):
    async with semaphore:
        async with httpx.AsyncClient() as client:
            response = await client.post(GQL_URL, json={"query": gql_query[1]}, headers=GQL_HEADERS)
            _process_query_errors(response)
            return gql_query[0], response.json()  # Return the pairing object with the response

async def fetch_all(GQL_URL, queries, GQL_HEADERS):
    tasks = [fetch(GQL_URL, gql_query, GQL_HEADERS) for gql_query in queries]
    results = await asyncio.gather(*tasks)
    return dict(results)



# Fetch all responses
responses = asyncio.run(fetch_all(GQL_URL, gql_queries, GQL_HEADERS))

chapter_list = []
# Print the responses
for index, response in responses.items():
    video = response.get('data', {}).get('video')
    if video is not None:
        edges = video.get('moments', {}).get('edges')
        if edges is not None and len(edges) > 0:  # Check if edges is not an empty list
            chapter_list.append((index, response))

print(chapter_list)