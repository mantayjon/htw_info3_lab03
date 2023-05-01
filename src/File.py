from datetime import datetime
import os.path
import PIL
import exiv2
from PIL import Image
import cv2


class File:
    def __init__(self, file_url):
        self.file_url = file_url
        self.file_name = os.path.basename(file_url)
        self.file_extension = self.file_name.split(".")[1].lower()
        self.creation_date = self.get_creation_date(file_url)

    file_types = ["raw", "dng", "cr3", "arw", "cr2", "tiff", "crw", "orf", "nef", "nrw", "rw2", "srf", "sr2", "jpeg", "jpg", "png", "heic", "heif", "gif", "mp4", "mov", "mpeg-4", "avi", "wmv", "avchd", "webm", "flv"]

    def get_creation_date(self, file_path):
        if self.file_extension in self.file_types:
            exiv2.enableBMFF(True)
            exiv_image = exiv2.ImageFactory.open(file_path)
            exiv_image.readMetadata()
            exif_data = exiv_image.exifData()
            exif_dt = exiv2.dateTimeOriginal(exif_data)
            if exif_dt is not None:
                timestamp = str(exif_dt).split(": ")[1]
                creation_time = datetime.strptime(timestamp, "%Y:%m:%d %H:%M:%S").timestamp()
            elif exif_dt is None:
                try:
                    dt_object = Image.open(file_path)._getexif()[36867]
                    creation_time = datetime.strptime(dt_object, "%Y:%m:%d %H:%M:%S").timestamp()
                except PIL.UnidentifiedImageError:
                    creation_time = os.stat(file_path).st_birthtime
                except:
                    creation_time = os.path.getctime(file_path)
            else:
                creation_time = os.path.getctime(file_path)
        else:
            creation_time = os.path.getctime(file_path)
        return creation_time
