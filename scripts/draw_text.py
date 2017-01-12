import os
import argparse
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Draw test over the files in a folder.')
    parser.add_argument('folder_path', type=str, help='Path to the folder')

    args = parser.parse_args()
    path = args.folder_path
    output_path = os.path.join(path, "new")
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    count = 1;
    for path, subdirs, files in os.walk(path):
        for filename in files:
            f = os.path.join(path, filename)
            if not ".png" in f:
                continue
            img = Image.open(f)
            draw = ImageDraw.Draw(img)
            draw.text((5, 5), filename, (255, 255, 0))
            newfilename = os.path.join(output_path, filename)
            img.save(newfilename)
            count = count + 1
