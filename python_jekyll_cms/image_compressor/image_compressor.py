import os
from PIL import Image, ImageDraw
from pathlib import Path
import math


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

def crawler(path):
    old_directory_size = get_directory_size(path)
    list_of_images = []
    list_of_dirs_files = os.walk(path)
    for i in list_of_dirs_files:
        if i[2]:
            for image_name in i[2]:
                if image_name.endswith('.jpg') or image_name.endswith('.png'):
                    if i[0].endswith('/'):
                        list_of_images.append(i[0] + image_name)
                    else:
                        list_of_images.append(i[0] + '/' + image_name)

    def compressor(lst):
        set_of_images = lst
        for img_path in set_of_images:
            image = Image.open(img_path)
            image.save(img_path, optimize=True, quality=10)

    compressor(list_of_images)
    new_directory_size = get_directory_size(path)
    print('Before =>', old_directory_size, '\nAfter =>', new_directory_size)
    print('OK')


if __name__ == "__main__":
    crawler(input('Input full path to directory with images\n'))
