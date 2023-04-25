class File:

    def __init__(self, file_name, creation_date):
        self.file_name = file_name

        extension = file_name.split(".")

        self.file_extension = extension[1]
        self.creation_date = creation_date

