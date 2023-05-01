import os
from File import File
import PhotoShoot
from PhotoShoot import PhotoShoot


src_path = "/Users/jonasmantay/Jonas/Pictures/personal/2022/11 November/cover/pics copy"
dest_path = "/Users/jonasmantay/Jonas/Pictures/personal/2022/11 November/cover/pics copy python"
folder_name = "sorted"
time_between_shootings = 30
files_from_path = []

for path, dirs, files in os.walk(src_path):
    for file in files:
        file_object = File(os.path.join(path, file))
        files_from_path.append(file_object)

print(files_from_path)

sorted_files = PhotoShoot(files_from_path, 30).sort_files(files_from_path)
file_names = os.listdir(src_path)
print(file_names)