import unittest
from unittest.mock import MagicMock, patch
from File import File
from PIL import Image

class TestFile(unittest.TestCase):
    def setUp(self):
        # Create mock file paths
        self.file_paths = [
            "/path/to/file1.jpg",
            "/path/to/file2.cr3",
            "/path/to/file3.mp4",
            "/path/to/file4.txt"
        ]

    @patch('File.exiv2')
    @patch('File.Image')
    @patch('os.path')
    def test_get_creation_date(self, mock_os_path, mock_Image, mock_exiv2):
        mock_exiv_image = MagicMock()
        mock_exiv2.dateTimeOriginal.return_value = "Exif.Photo.DateTimeOriginal: 2023:01:01 12:00:00"
        mock_exiv2.ImageFactory.open.return_value = mock_exiv_image
        mock_os_path.basename.side_effect = lambda path: path.split('/')[-1]
        mock_os_path.splitext.side_effect = lambda path: ('file', '.extension')
        mock_os_path.getctime.return_value = 1672570800  # Mock current timestamp
        mock_os_path.st_birthtime.return_value = 1672570800  # Mock file birth time
        mock_Image.open.return_value._getexif.return_value = {36867: '2023:01:01 12:00:00'}

        for file_path in self.file_paths:
            file_object = File(file_path)
            expected_creation_time = 1672570800  # Mock creation time in epoch format
            self.assertEqual(file_object.creation_date, expected_creation_time)


if __name__ == '__main__':
    unittest.main()
