# Python Scripts

[![Build Status](https://travis-ci.org/chongyangma/python-scripts.svg?branch=master)](https://travis-ci.org/chongyangma/python-scripts)

Some useful python scripts (mostly for batch processing of files). Launching each script without any argument will print out the usage information.

## Descriptions

#### [draw_text.py](https://github.com/chongyangma/python-scripts/blob/master/scripts/draw_text.py)

Draw text on images in a folder. [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/) is required.

```
usage: draw_text.py [-h] [--output_folder OUTPUT_FOLDER]
                    [--font_size FONT_SIZE] [--pos_x POS_X] [--pos_y POS_Y]
                    [--color_r COLOR_R] [--color_g COLOR_G]
                    [--color_b COLOR_B]
                    input_path
```

#### [list_files.py](https://github.com/chongyangma/python-scripts/blob/master/scripts/list_files.py)

List files in a folder.

```
usage: list_files.py [-h] [--output_file OUTPUT_FILE]
                     [--partial_name PARTIAL_NAME]
                     input_path
```
