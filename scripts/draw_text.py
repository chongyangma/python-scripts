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

def draw_text(input_path, output_path, text=None, font_size=20,
 pos_x=5, pos_y=5, color_r=255, color_g=255, color_b=255):
    #fnt = ImageFont.truetype("Arial.ttf", font_size)
    fnt = ImageFont.load_default().font

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    count = 0
    for path, subdirs, files in os.walk(input_path):
        for filename in files:
            f = os.path.join(path, filename)
            if not is_image(f):
                continue
            img = Image.open(f)
            img = img.convert("RGBA")
            text_to_draw = filename
            if text:
                text_to_draw = text
            draw = ImageDraw.Draw(img)
            draw.text((pos_x, pos_y), text_to_draw, font=fnt, fill=(color_r, color_g, color_b, 255))
            newfilename = os.path.join(output_path, filename)
            img.save(newfilename)
            count = count + 1

    return count


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Draw test over the files in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('output_path', type=str, help='Path to the output folder')
    parser.add_argument('--text', type=str, default=None, help='Text to draw')
    parser.add_argument('--font_size', type=int, default=20, help='Font size')
    parser.add_argument('--pos_x', type=int, default=5, help='Start position X')
    parser.add_argument('--pos_y', type=int, default=5, help='Start position Y')
    parser.add_argument('--color_r', type=int, default=255, help='R value of the text color')
    parser.add_argument('--color_g', type=int, default=255, help='G value of the text color')
    parser.add_argument('--color_b', type=int, default=255, help='B value of the text color')

    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    text = args.text
    font_size = args.font_size
    pos_x = args.pos_x
    pos_y = args.pos_y
    color_r = args.color_r
    color_g = args.color_g
    color_b = args.color_b

    draw_text(input_path, output_path, text, font_size, pos_x, pos_y, color_r, color_g, color_b)
