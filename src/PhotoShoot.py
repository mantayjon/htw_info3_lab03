class PhotoShoot:

    def __init__(self, all_files, time_between):
        self.all_files = all_files
        self.time_between = time_between * 60
        self.sorted_by_timestamp = self.sort_by_shooting()

    def sort_by_shooting(self):
        sorted_time = 0
        return sorted_time

    def sort_files(self, list_objects):
        all_files = list_objects
        jpeg = []
        raw = []
        videos = []
        other_files = []

        for file in all_files:
            if file.file_extension == 'jpeg' or file.file_extension == 'jpg' or file.file_extension == 'JPG':
                jpeg.append(file)
            elif file.file_extension == 'raw' or file.file_extension == 'arw' or file.file_extension == 'CR2':
                raw.append(file)
            elif file.file_extension == 'mp4' or file.file_extension == 'MOV' or file.file_extension == 'MPEG-4':
                videos.append(file)
            else:
                other_files.append(file)

        print("jpg")
        print(jpeg)
        print("raw")
        print(raw)
        print("vid")
        print(videos)
        print("other")
        print(other_files)
