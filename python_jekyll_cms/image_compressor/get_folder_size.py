from pathlib import Path
import math


def get_bytes_size(path):
    root_directory = Path(path)
    sz = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
    return sz


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


# В одной функции
def get_directory_size(path):  # path to folder with images
    root_directory = Path(path)
    sz = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())

    def convert_size(sz):
        if sz == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(sz, 1024)))
        p = math.pow(1024, i)
        s = round(sz / p, 2)
        return "%s %s" % (s, size_name[i])

    size = convert_size(sz)

    return size



