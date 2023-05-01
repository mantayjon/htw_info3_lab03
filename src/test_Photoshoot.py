import datetime
import unittest
from unittest.mock import MagicMock, patch
from File import File
from PhotoShoot import PhotoShoot


class TestPhotoShoot(unittest.TestCase):
    def setUp(self):
        # Create mock File objects with mock EXIF data
        self.files = [
            self.create_mock_file("/path/to/file1.jpg", "2023:01:01 12:00:00"),
            self.create_mock_file("/path/to/file2.raw", "2023:01:01 12:29:00"),
            self.create_mock_file("/path/to/file3.mp4", "2023:01:01 13:00:00"),
            self.create_mock_file("/path/to/file4.txt", "2023:12:01 12:10:00")
        ]
        self.photoshoot = PhotoShoot(self.files, 30)

    def create_mock_file(self, file_url, exif_date):
        mock_file = MagicMock(spec=File)
        mock_file.file_url = file_url
        mock_file.creation_date = self.parse_datetime(exif_date).timestamp()
        mock_file.file_extension = file_url.split(".")[-1]
        return mock_file

    def parse_datetime(self, datetime_str):
        return datetime.datetime.strptime(datetime_str, "%Y:%m:%d %H:%M:%S")

    def test_sort_by_shooting(self):
        expected_result = [
            [self.files[0], self.files[1]],
            [self.files[2]],
            [self.files[3]]
        ]
        result = self.photoshoot.sort_by_shooting()
        self.assertEqual(result, expected_result)

    def test_sort_by_filetype(self):
        expected_result = [
            [
                [self.files[0]],
                [self.files[1]],
                [],
                []
            ],
            [
                [],
                [],
                [self.files[2]],
                []
            ],
            [
                [],
                [],
                [],
                [self.files[3]]
            ]
        ]
        result = self.photoshoot.sort_by_filetype()
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
