import os
import argparse
import math
from PIL import Image

def compose_images(input_path, output_file):
    images = []
    for path, subdirs, files in os.walk(input_path):
        for file_name in files:
            try:
                file_path = os.path.join(path, file_name)
                im = Image.open(file_path)
                # im.verify()
                images.append(im)
            except:
                continue

    num = len(images)
    wd = 10
    ht = math.ceil(num / wd)
    sz = images[0].size
    new_im = Image.new('RGB', (wd * sz[0], ht * sz[1]), (255, 255, 255))

    for idx, im in enumerate(images):
        x = idx % wd
        y = int(idx / wd)
        new_im.paste(im, (x * sz[0], y * sz[1]))

    new_im.save(output_file)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='List the files in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('--output_file', type=str, default='output.png', help='Output file')

    args = parser.parse_args()
    input_path = args.input_path
    output_file = args.output_file

    compose_images(input_path, output_file)
