# import os

# dir = r'F:/Music/Musizz/My Shared Folder/'


# for files in os.listdir(dir):
#     print(files)

from datetime import datetime, timezone

timestamp = '02-12-2023'

def days_ago_simple(timestamp):
    """
    Returns:
        int of days ago
    """
    dt = datetime.strptime(timestamp, "%d-%m-%Y")
    now = datetime.now()
    difference = now - dt
    return difference.days

print(days_ago_simple(timestamp))