# import os

# dir = r'F:/Music/Musizz/My Shared Folder/'


# for files in os.listdir(dir):
#     print(files)
import os
import sys
import time


def flush_input():
    """Clears the input buffer."""
    if os.name == 'nt':  # For Windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    # else:  # For Unix/Linux/MacOS
    #     import fcntl
    #     import termios
    #     termios.tcflush(sys.stdin, termios.TCIOFLUSH)


input("what u want")
time.sleep(4)

flush_input()


input("last input")