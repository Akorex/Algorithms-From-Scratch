import os
import math

def compute_usage(path):
    """
    Computes the amount in bytes of space occupied by a given path and any decendents in the system
    
    path      the file directory to calculate the disk usage of
    """
    total = os.path.getsize(path)
    
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += compute_usage(childpath)

    return total

def convert_size(bytes):
    """Converts the file size in bytes"""

    if bytes == 0:
        return '0B'
    tags = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(bytes, 1024)))
    p = math.pow(1024, i)
    s = round(bytes / p, 2)

    return "%s %s" % (s, tags[i])
if __name__ == '__main__':
    path = r'C:\Users\HP Probook\Videos\Hollywood\Series'
    print(convert_size(compute_usage(path)))

