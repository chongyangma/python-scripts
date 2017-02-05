import os
import argparse
import fnmatch

def list_files(input_path, pattern=None, output_file='output.txt'):
    fout = open(output_file, "w")
    count = 0
    for path, subdirs, files in os.walk(input_path):
        for file_name in files:
            if pattern and not fnmatch.fnmatch(file_name, pattern):
                continue
            f = os.path.join(input_path, file_name)
            print(file_name)
            fout.write(str(f) + "\n")
            count = count + 1
    return count

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='List the files in a folder.')
    parser.add_argument('input_path', type=str, help='Path to the input folder')
    parser.add_argument('--output_file', type=str, default='output.txt', help='Output file')
    parser.add_argument('--pattern', type=str, default=None, help='Unix filename pattern')

    args = parser.parse_args()
    input_path = args.input_path
    pattern = args.pattern
    output_file = args.output_file

    list_files(input_path, pattern, output_file)
