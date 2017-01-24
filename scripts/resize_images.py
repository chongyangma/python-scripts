import os
import argparse
from PIL import Image

def is_image(file_name):
    if ".png" in file_name or ".jpg" in file_name:
        return True
    else:
        return False

def resize_image(input_path, output_path, wd=0, ht=0):
    img = Image.open(input_path)
    # Resize the image
    sz = img.size
    if wd == 0:
        wd = sz[0] / 2
    if ht == 0:
        ht = sz[1] / 2
    ratio_dst = float(wd) / float(ht)
    ratio_src = float(sz[0]) / float(sz[1])
    if ratio_src > ratio_dst:
        wd_new = int(ht * ratio_src)
        img = img.resize((wd_new, ht), Image.ANTIALIAS)
    else:
        ht_new = int(wd / ratio_src)
        img = img.resize((wd, ht_new), Image.ANTIALIAS)
    # Crop the image
    sz = img.size
    px = 0
    py = 0
    if sz[0] > wd:
        px = (sz[0] - wd) / 2
    if sz[1] > ht:
        py = (sz[1] - ht) / 2
    if px > 0 or py > 0:
        img = img.crop((px, py, px + wd, ht))
    # Save the output image
    img.save(output_path)

def resize_images(input_path, output_path, wd=0, ht=0):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    count = 0
    for path, subdirs, files in os.walk(input_path):
        for file_name in files:
            if not is_image(file_name):
                continue
            input_file_path = os.path.join(path, file_name)
            output_file_path = os.path.join(output_path, file_name)
            resize_image(input_file_path, output_file_path, wd, ht)
            count = count + 1

    return count


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Resize images in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('output_path', type=str, help='Path to the output folder')
    parser.add_argument('--wd', type=int, default=0, help='Target width')
    parser.add_argument('--ht', type=int, default=0, help='Target height')

    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    wd = args.wd
    ht = args.ht

    resize_images(input_path, output_path, wd, ht)
