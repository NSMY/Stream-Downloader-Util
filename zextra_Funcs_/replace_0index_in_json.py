import json

import pretty_errors

id = "deadlyslob"

file_path = rf"{id}.json"

# with open(file_path, 'r') as f:
#     data = json.load(f)

# ids = [(vod['url'], vod['publishedAt'], vod['gameName'], vod['title']) for vod in data]

# for id in ids:
#     print(id)


# def convert_seconds(total_seconds):
#     hours = total_seconds // 3600
#     minutes = (total_seconds % 3600) // 60
#     seconds = total_seconds % 60
#     return f"{hours}:{minutes}:{seconds}"

# print(convert_seconds(29553))


# Load the JSON file into a Python list of dictionaries
# with open(file_path, 'r') as f:
#     list_of_dicts = json.load(f)

# The new dictionary you want to insert
new_dict = {
    "creatorId": "12225555",
    "login": "hasan",
    "displayName": "hasan",
    "id": "2555555",
    "title": "Just Live",
    "publishedAt": "2023-10-13T11:03:44Z",
    "broadcastType": "ARCHIVE",
    "status": "RECORDING",
    "lengthSeconds": 35222,
    "gameId": "22222",
    "gameName": "Just Chatting",
    "url": "https://www.twitch.tv/videos/2555555",
}

# Insert the new dictionary at the beginning of the list
list_of_dicts.insert(0, new_dict)

# Write the updated list back to the JSON file
with open(file_path, "w") as f:
    json.dump(list_of_dicts, f, indent=4)
