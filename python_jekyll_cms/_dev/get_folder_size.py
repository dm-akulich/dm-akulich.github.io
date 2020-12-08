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


print(convert_size(sz))
