import sys
sys.path.insert(0, './scripts')

import list_files
import draw_text
import resize_images

if __name__ == '__main__':
    test_data_path = "./data"
    list_file_count = list_files.list_files(test_data_path)
    print("Have listed %d files." % list_file_count)
    draw_file_count = draw_text.draw_text(test_data_path, './draw_output')
    print("Have drawn %d images." % draw_file_count)
    resize_file_count = resize_images.resize_images(test_data_path, './resize_output')
    print("Have resized %d images." % resize_file_count)
