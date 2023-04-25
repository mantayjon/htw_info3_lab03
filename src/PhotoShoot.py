class PhotoShoot:

    def __init__(self, photo_shoot_name, all_files):
        self.photo_shoot_name = photo_shoot_name
        self.all_files = all_files
        self.jpeg = []
        self.raw = []
        self.videos = []
        self.other_files = []

    def sort_files(self):
        for file in self.all_files:
            if file.file_extension == 'jpeg' or file.file_extension == 'jpg':
                self.jpeg.append(file)
                print(self.jpeg)
            elif file.file_extension == 'raw' or file.file_extension == 'arw' or file.file_extension == 'CR2':
                self.raw.append(file)
                print(self.raw)
            elif file.file_extension == 'mp4' or file.file_extension == 'MOV' or file.file_extension == 'MPEG-4':
                self.videos.append(file)
                print(self.videos)
            else:
                self.other_files.append(file)
                print(self.other_files)
