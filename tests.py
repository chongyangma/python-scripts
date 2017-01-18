import sys
sys.path.insert(0, './scripts')

import list_files
import draw_text

if __name__ == '__main__':
    test_data_path = "./data"
    list_file_count = list_files.list_files(test_data_path)
    print("Have listed %d files." % list_file_count)
    draw_file_count = draw_text.draw_text(test_data_path, './output')
    print("Have drawn %d images." % draw_file_count)
