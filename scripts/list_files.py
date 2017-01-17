import os
import argparse

def list_files(input_path, partial_name=None, output_file='output.txt'):
    fout = open(output_file, "w")
    for path, subdirs, files in os.walk(input_path):
        for file_name in files:
            if partial_name and partial_name not in file_name:
                continue
            f = os.path.join(input_path, file_name)
            print(file_name)
            fout.write(str(f) + "\n")

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='List the files in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('--output_file', type=str, default='output.txt', help='Output file')
    parser.add_argument('--partial_name', type=str, default=None, help='Part of file name')

    args = parser.parse_args()
    input_path = args.input_path
    partial_name = args.partial_name
    output_file = args.output_file

    list_files(input_path, partial_name, output_file)
