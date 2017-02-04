import os
import argparse
import fnmatch
from shutil import copyfile

def reverse_sequence(input_path, output_path, pattern):
    files = os.listdir(input_path)
    if pattern:
        files = fnmatch.filter(files, pattern)
    file_num = len(files)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    count = 0
    for file_name in files:
        old_file_path = os.path.join(input_path, file_name)
        new_file_name = files[file_num - count - 1]
        new_file_path = os.path.join(output_path, new_file_name)
        copyfile(old_file_path, new_file_path)
        count = count + 1
    return count

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Reverse the order of files in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('output_path', type=str, help='Path to the output folder')
    parser.add_argument('--pattern', type=str, default=None, help='Unix filename pattern')

    args = parser.parse_args()
    input_path = args.input_path
    output_path = args.output_path
    pattern = args.pattern

    reverse_sequence(input_path, output_path, pattern)
