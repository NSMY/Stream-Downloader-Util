# import os

# dir = r'F:/Music/Musizz/My Shared Folder/'


# for files in os.listdir(dir):
#     print(files)

def compare_with_tolerance(size1, size2, tolerance=10):
    """
    This function compares two file sizes with a certain tolerance.
    """
    return abs(size1 - size2) <= tolerance

print(compare_with_tolerance(152, 159, 15))