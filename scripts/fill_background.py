import os
import argparse
from PIL import Image

def is_image(file_name):
    if ".png" in file_name or ".jpg" in file_name:
        return True
    else:
        return False

def fill_image_background(input_path, output_path):
    img = Image.open(input_path)
    r, g, b, alpha = img.split()
    output = Image.new(img.mode, img.size, "black")
    output = Image.alpha_composite(output, img)
    output.save(output_path)

def fill_background(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    count = 0
    for path, subdirs, files in os.walk(input_path):
        for file_name in files:
            if not is_image(file_name):
                continue
            input_file_path = os.path.join(path, file_name)
            output_file_path = os.path.join(output_path, file_name)
            fill_image_background(input_file_path, output_file_path)
            count = count + 1

    return count


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Fill background of images in a folder based on alpha channel.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('output_path', type=str, help='Path to the output folder')

    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path

    fill_background(input_path, output_path)
