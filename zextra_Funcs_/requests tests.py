import json
from pydoc import html

import requests
from bs4 import BeautifulSoup, SoupStrainer

# from requests_html import HTMLSession

url = 'https://www.twitch.tv/hasanabi/videos?filter=archives'
# url = 'https://httpbin.org/headers'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://www.google.com',
    'DNT': '1'
}

r = requests.get(url, headers=headers)

# Parse the HTML response
soup = BeautifulSoup(r.text, 'html.parser',parse_only=SoupStrainer('head'))
print("🐍 File: Desktop/requests tests.py | Line: 22 | undefined ~ soup",soup)

s = soup.prettify(formatter='html')
print("🐍 File: Desktop/requests tests.py | Line: 22 | undefined ~ s",s)

# Find the video object by its tag name and get its 'name' attribute
script_tag = soup.head.find("script", {"type": "application/ld+json"})
kii = str(script_tag)
lol = kii.split('{"@type"')

for item in lol:
    print('\n', item)
# print("🐍 File: Desktop/requests tests.py | Line: 32 | undefined ~ lol",lol)


# t= soup.
# print("🐍 File: Desktop/requests tests.py | Line: 31 | undefined ~ t",t)

# print(r.text)




# import json
# from pydoc import html

# import requests
# from bs4 import BeautifulSoup, SoupStrainer

# # from requests_html import HTMLSession

# # url = 'https://www.twitch.tv/hasanabi/videos?filter=archives'
# # # url = 'https://httpbin.org/headers'



# GET_CHANNEL_VIDEOS_QUERY = """
# {{  user(login: "{channel_id}") {{
# 		videos( first: {first}, sort: {sort}, after: {after} ) {{
# 			totalCount
# 			edges {{ cursor
# 				node {{
# 					id title publishedAt broadcastType status lengthSeconds
# 					game {{ id name }}
# 					creator {{ id login displayName }}
# }}  }}  }}  }}  }}
# """


# query = GET_CHANNEL_VIDEOS_QUERY.format(
# 			channel_id='deadlyslob',
# 			sort="TIME"
# 		)



# # headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
# #     'Accept-Language': 'en-GB,en;q=0.5',
# #     'Referer': 'https://www.google.com',
# #     'DNT': '1'
# # }

# # r = requests.get(url, headers=headers)

# url = "https://gql.twitch.tv/gql"
# headers = {
#     'Client-ID': 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp', 
#     "Authorization": "Bearer " + 'kd1unb4b3q4t58fwlpcbzcbnm76a8fp'
# }
# params = {'user_id': '123456'}


# url = f"http://usher.ttvnw.net/vod/deadlyslob"

# resp = requests.get(url, timeout=5, params={
#     "nauth": access_token['value'],
#     "nauthsig": access_token['signature'],
#     "allow_source": "true",
#     "player": "twitchweb",
# })


# response = requests.get(url, headers=headers)

# print(response)

# # GQL Query forms
# # Channel VODs query


