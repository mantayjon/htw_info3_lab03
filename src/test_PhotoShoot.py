import unittest
from File import File
from PhotoShoot import PhotoShoot


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.file_01 = File("/Users/jonasmantay/Desktop/i-D.jpg")
        self.file_02 = File("/Users/jonasmantay/Desktop/i-D.jpg")
        self.file_03 = File("/Users/jonasmantay/Desktop/i-D.jpg")
        self.file_05 = File("/Users/jonasmantay/Desktop/i-D.jpg")
        self.file_04 = File("/Users/jonasmantay/Desktop/i-D.jpg")

        self.files = [self.file_01, self.file_02, self.file_03, self.file_04, self.file_05]

        self.photo_shoot01 = PhotoShoot("shoot01", self.files)

    def test_sortList(self):
        test_jpg = [self.file_01, self.file_05]
        test_raw = [self.file_02]
        test_mov = [self.file_03]
        test_pdf = [self.file_04]

        self.photo_shoot01.sort_files()

        self.assertEqual(self.photo_shoot01.jpeg, test_jpg)
        self.assertEqual(self.photo_shoot01.raw, test_raw)
        self.assertEqual(self.photo_shoot01.videos, test_mov)
        self.assertEqual(self.photo_shoot01.other_files, test_pdf)

    def test_get_date_taken(self):
        self.assertEqual(self.file_01.check_date_taken(), 0)


if __name__ == '__main__':
    unittest.main()
