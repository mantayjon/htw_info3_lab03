import datetime

import File


class PhotoShoot:

    def __init__(self, all_files, time_between):
        self.all_files = all_files
        self.time_between = time_between * 60
        self.sorted_by_timestamp = self.sort_by_shooting()

    def sort_by_shooting(self):
        sorted_files_by_time = sorted(self.all_files, key=lambda time: time.creation_date)
        start = sorted_files_by_time[0].creation_date
        index = 0
        result = [[]]
        for file in sorted_files_by_time:
            if start <= file.creation_date <= start + self.time_between:
                result[index].append(file)
            else:
                new_shooting = [file]
                result.append(new_shooting)
                start = file.creation_date
                index += 1
        return result

    def sort_by_filetype(self):
        result = []
        raw_files = ["raw", "dng", "cr3", "arw", "cr2", "tiff", "crw", "orf", "nef", "nrw", "rw2", "srf", "sr2"]
        non_raw_files = ["jpeg", "jpg", "png", "heic", "heif", "gif"]
        video_files = ["mp4", "mov", "mpeg-4", "avi", "wmv", "avchd", "webm", "flv"]

        for shooting in self.sorted_by_timestamp:
            shooting_result = [[], [], [], []]
            for file in shooting:
                file_extension = file.file_extension.lower()
                if file_extension in non_raw_files:
                    shooting_result[0].append(file)
                elif file_extension in raw_files:
                    shooting_result[1].append(file)
                elif file_extension in video_files:
                    shooting_result[2].append(file)
                else:
                    shooting_result[3].append(file)
            result.append(shooting_result)
        return result
