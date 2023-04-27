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
        for shooting in self.sorted_by_timestamp:
            shooting_result = [[], [], [], []]
            for file in shooting:
                file_extension = file.file_extension.lower()
                if file_extension == 'jpeg' or file_extension == 'jpg':
                    shooting_result[0].append(file)
                elif file_extension == 'raw' or file_extension == 'arw' or file_extension == 'cr3':
                    shooting_result[1].append(file)
                elif file_extension == 'mp4' or file_extension == 'mov' or file_extension == 'mpeg-4':
                    shooting_result[2].append(file)
                else:
                    shooting_result[3].append(file)
            result.append(shooting_result)
        return result
