'''chapters = []
for index, items in enumerate(data):
    
    query = GET_VIDEO_CHAPTERS.format(
    id=items.get('id'), after=chapter_page
    )
    resp = gql_query(query=query).json()

    # if not resp["data"]["video"]:
    #     raise GQLItemError(f"Failed to find moments for video `{v['id']}`.")

    resp = resp["data"]["video"]["moments"]
    chapters.append((index, resp))
'''