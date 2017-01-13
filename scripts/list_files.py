import os
import argparse

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='List the files in a folder.')
    parser.add_argument('folder_path', type=str, help='Path to the folder')
    parser.add_argument('--output_file', type=str, default='output.txt', help='Output file')
    parser.add_argument('--partial_name', type=str, default=None, help='Part of file name')

    args = parser.parse_args()
    path = args.folder_path
    part = args.partial_name

    fout = open(args.output_file, "w")
    for path, subdirs, files in os.walk(path):
        for file_name in files:
            if part and part not in file_name:
                continue
            f = os.path.join(path, file_name)
            print(file_name)
            fout.write(str(f) + "\n")
