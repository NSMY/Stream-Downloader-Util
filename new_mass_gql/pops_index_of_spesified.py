import json

import pretty_errors

id = "jsons/deadlyslob"

file_path = rf"{id}.json"

with open(file_path, "r") as f:
    data = json.load(f)

ids = [(vod["url"], vod["publishedAt"], vod["gameName"], vod["title"]) for vod in data]

for id in ids:
    print(id)


target_id = "RECORDING"

# Loop over the dictionaries in the list
for i, d in enumerate(data):
    # If the 'id' field of the dictionary is the target ID, print the index and break the loop
    if d["id"] == target_id:
        print(f"The target ID is at index {i} in the list.")
        # data.pop(i)
        # data.insert(i, {"hello world!": "world"})
        # with open(file_path, 'w') as f:
        #     json.dump(data, f, indent=4)
        break


# Idents index of list via the 'status' within dicts.
# Loop over the dictionaries in the list
for i, d in enumerate(data):
    # If the 'id' field of the dictionary is the target ID, print the index and break the loop
    if d["status"] == target_id:
        print(f"The target ID is at index {i} in the list.")
        print(data[i])
        break
