import filetype as filetype
from PIL import Image
import os


class File:
    def __init__(self, file_url):
        self.file_name = os.path.basename(file_url)
        self.file_extension = self.file_name.split(".")[1]
        self.file_url = file_url
        self.creation_date = self.get_creation_date(file_url)

    def get_creation_date(self, file_path):
        time_stamp = 0

        if filetype.is_image(file_path) or filetype.is_video(file_path):
            time_stamp = Image.open(file_path).getexif()
            if time_stamp is not None:
                exif_time = time_stamp[36867]
                time_stamp = exif_time.strptime(exif_time, "%Y:%m:%d %H:%M:%S:").timestamp()
            else:
                time_stamp = os.path.getctime(file_path)

        return time_stamp
