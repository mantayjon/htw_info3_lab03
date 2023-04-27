from datetime import datetime
import os.path
import time

import exifread as exifread
import filetype as filetype
from PIL import Image
class File:
    def __init__(self, file_url):
        self.file_url = file_url
        self.file_name = os.path.basename(file_url)
        self.file_extension = self.file_name.split(".")[1]
        self.creation_date = self.get_creation_date(file_url)

    def get_creation_date(self, file_path):
        creation_time = 0
        print(file_path)
        if filetype.is_image(file_path) or filetype.is_video(file_path):
            # creation_time = Image.open(file_path)._getexif()
            creation_time = None
            f = open(file_path, 'rb')
            tags = exifread.process_file(f, details=False)
            for key in tags:
                if key == "EXIF DateTimeOriginal":
                    creation_time = str(tags["EXIF DateTimeOriginal"])

            if creation_time is not None:
                # exif_time = creation_time[36867]
                # creation_time = datetime.strptime(exif_time, "%Y:%m:%d %H:%M:%S").timestamp()
                creation_time = 2
            else:
                creation_time = os.path.getctime(file_path)
        return creation_time
