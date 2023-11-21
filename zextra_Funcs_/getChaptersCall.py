'''chapters = []
for index, items in enumerate(data):
    
    query = GET_VIDEO_CHAPTERS.format(
    id=items.get('id'), after=chapter_page
    )
    resp = gql_query(query=query).json()
    print("🐍 File: Stream-Downloader-Util/Testcode.py | Line: 701 | undefined ~ resp",resp)

    # if not resp["data"]["video"]:
    #     raise GQLItemError(f"Failed to find moments for video `{v['id']}`.")

    resp = resp["data"]["video"]["moments"]
    chapters.append((index, resp))
print("🐍 File: Stream-Downloader-Util/Testcode.py | Line: 699 | undefined ~ resp",resp)
'''