import unittest
from File import File


class MyTestCase(unittest.TestCase):
    def setUp(self):
        file_01 = File("01.jpeg", 2)
        file_02 = File("01.raw", 1)
        file_03 = File("01.MOV", 4)
        file_04 = File("01.pdf", 3)

    def test_sortList(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
