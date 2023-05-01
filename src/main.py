import os
import shutil

from src.File import File
from src.PhotoShoot import PhotoShoot

src_path = "/Users/chriswolter/Downloads/python_test"
dest_path = "/Users/chriswolter/Downloads/"
folder_name = "copied"
time_between_shootings = 30 #Angabe in Minuten, Konvertieren erfolgt in der PhotoShoot Class
files_from_path = []

for path, dirs, files in os.walk(src_path):
    for file in files:
        file_object = File(os.path.join(path,file))
        files_from_path.append(file_object)

photoshoot_object = PhotoShoot(files_from_path, time_between_shootings)
sorted_files = PhotoShoot.sort_by_filetype(photoshoot_object)
sorted_by_time = PhotoShoot.sort_by_shooting(photoshoot_object)

directory_exists = True
directory_index = 1
directory = dest_path + folder_name

while directory_exists:
    if os.path.isdir(directory):
        directory = directory.rsplit("_", 1)[0]
        directory += "_" + str(directory_index)
        directory_index += 1
    else:
        directory_exists = False
os.mkdir(directory)

shooting_index = 0
file_extension = ["JPG", "RAW", "Video", "Other"]
for shooting in sorted_files:
    print("--- shooting ---")
    shooting_directory = directory + "/" + "shooting_" + str(shooting_index)
    os.mkdir(shooting_directory)
    extension_index = 0
    shooting_index += 1
    for index, extension in enumerate(shooting):
        if extension:
            extension_directory = shooting_directory + "/"+file_extension[extension_index]
            os.mkdir(extension_directory)
            for file in extension:
                shutil.copy(file.file_url, extension_directory)
        extension_index += 1
exit()
