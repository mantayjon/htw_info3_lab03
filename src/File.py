import filetype as filetype
from PIL import Image
class File:
    def __init__(self, file_url, file_name):
        self.file_url = file_url
        self.file_name = file_name
        self.file_extension = self.file_name.split(".")[1]
        self.creation_date = self.get_creation_date(file_url)

    def get_creation_date(self, file_name):
        print(file_name)
        time = 0
        if filetype.is_image(file_name):
            time = Image.open(file_name)._getexif()
            if time is not None:
                time = time[36868]
        return time
