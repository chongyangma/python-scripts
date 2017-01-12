import os
import argparse

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='List the files in a folder.')
    parser.add_argument('folder_path', type=str, help='Path to the folder')
    parser.add_argument('--output_file', type=str, default='output.txt', help='Output file')

    args = parser.parse_args()
    path = args.folder_path
    fout = open(args.output_file, "w")
    for path, subdirs, files in os.walk(path):
        for filename in files:
            f = os.path.join(path, filename)
            print(filename)
            fout.write(str(f) + "\n")
