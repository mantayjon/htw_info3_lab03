import os
from File import File
import PhotoShoot
from PhotoShoot import PhotoShoot

src_path = "/Users/jonasmantay/Jonas/Pictures/personal/2022/11 November/cover/pics copy"


def print_file_list(path):
    file_names = os.listdir(path)

    print(file_names)


def get_file_urls(folder_path):
    file_names = os.listdir(folder_path)
    file_urls = []

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        file_urls.append(file_path)
    return file_urls

print_file_list(src_path)

file_url_list = get_file_urls(src_path)
print(file_url_list)


def put_files_in_list(url_list):
    file_list = []

    for url in url_list:
        file_object = File(url)
        file_list.append(file_object)
    return file_list




file_object_list = put_files_in_list(file_url_list)
print(file_object_list)


