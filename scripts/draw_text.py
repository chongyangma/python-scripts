import os
import argparse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def is_image(file_name):
    if ".png" in file_name or ".jpg" in file_name:
        return True
    else:
        return False

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Draw test over the files in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('--output_folder', type=str, default=None, help='Output folder name')
    parser.add_argument('--font_size', type=int, default=20, help='Font size')
    parser.add_argument('--pos_x', type=int, default=5, help='Start position X')
    parser.add_argument('--pos_y', type=int, default=5, help='Start position Y')
    parser.add_argument('--color_r', type=int, default=255, help='R value of the text color')
    parser.add_argument('--color_g', type=int, default=255, help='G value of the text color')
    parser.add_argument('--color_b', type=int, default=255, help='B value of the text color')

    args = parser.parse_args()
    input_path = args.input_path
    output_folder = args.output_folder
    font_size = args.font_size
    pos_x = args.pos_x
    pos_y = args.pos_y
    color_r = args.color_r
    color_g = args.color_g
    color_b = args.color_b

    fnt = ImageFont.truetype("Arial.ttf", font_size)

    if output_folder:
        output_path = os.path.join(input_path, output_folder)
    else:
        output_path = os.path.join(input_path, "new")
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    count = 1;
    for path, subdirs, files in os.walk(input_path):
        for filename in files:
            f = os.path.join(path, filename)
            if not is_image(f):
                continue
            img = Image.open(f)
            img = img.convert("RGBA")
            draw = ImageDraw.Draw(img)
            draw.text((pos_x, pos_y), filename, font=fnt, fill=(color_r, color_g, color_b, 255))
            newfilename = os.path.join(output_path, filename)
            img.save(newfilename)
            count = count + 1