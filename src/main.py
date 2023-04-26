import os
from src.File import File

src_path = "/Users/chriswolter/Downloads"
dest_path = "/Users/chriswolter/Downloads/backup"
files_from_path = []

for path, dirs, files in os.walk(src_path):
    for file in files:
        file_object = File(os.path.join(path,file), file)
        files_from_path.append(file_object)

for file in files_from_path:
    print(file.creation_date)


