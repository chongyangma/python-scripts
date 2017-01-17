import sys
sys.path.insert(0, './scripts')

import list_files

if __name__ == '__main__':
    file_count = list_files.list_files("./scripts")
    print("Have listed %d files." % file_count)
