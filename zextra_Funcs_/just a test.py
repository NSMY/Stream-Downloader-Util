# import os

# dir = r'F:/Music/Musizz/My Shared Folder/'


# for files in os.listdir(dir):
#     print(files)

import os
from datetime import datetime

terminal_Naming = 'balha hahadasdkl'


# save_path = os.path.dirname(download_file_path)
with open(f"C:/Users/970EVO-Gamer/Desktop/downloadCompleteTime.txt", "a") as f:
    f.write(
        datetime.now().strftime(
            f"\nCompleted: {terminal_Naming}\nCompleted at: -- %H:%M:%S --\n"
        )
    )
print(
    datetime.now().strftime(
        f"\nCompleted: {terminal_Naming}\nCompleted at: -- %H:%M:%S --\n"
    )
)