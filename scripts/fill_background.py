import os
import argparse
from PIL import Image

def is_image(file_name):
    if ".png" in file_name or ".jpg" in file_name:
        return True
    else:
        return False

def fill_image_background(input_path, output_path, color_r=0, color_g=0, color_b=0):
    img = Image.open(input_path)
    if img.mode != 'RGBA':
        return False
    r, g, b, alpha = img.split()
    output = Image.new(img.mode, img.size, (color_r, color_g, color_b))
    output = Image.alpha_composite(output, img)
    output.save(output_path)
    return True

def fill_background(input_path, output_path, color_r=0, color_g=0, color_b=0):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    count = 0
    for path, subdirs, files in os.walk(input_path):
        for file_name in files:
            if not is_image(file_name):
                continue
            input_file_path = os.path.join(path, file_name)
            output_file_path = os.path.join(output_path, file_name)
            flag = fill_image_background(input_file_path, output_file_path, color_r, color_g, color_b)
            if flag:
                count = count + 1

    return count


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Fill background of images in a folder based on alpha channel.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('output_path', type=str, help='Path to the output folder')
    parser.add_argument('--color_r', type=int, default=0, help='R value of the background color')
    parser.add_argument('--color_g', type=int, default=0, help='G value of the background color')
    parser.add_argument('--color_b', type=int, default=0, help='B value of the background color')

    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    color_r = args.color_r
    color_g = args.color_g
    color_b = args.color_b

    count = fill_background(input_path, output_path, color_r, color_g, color_b)
    print("Have filled the background of " + str(count) + " images.")
