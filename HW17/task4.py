import unittest
import os

from .HW6 import swap_files


class TestFiles(unittest.TestCase):
    def test_1(self):
        with open('task4_bin.bin', 'wb') as bin_file:
            bin_file.writelines('')

    def test_2(self):
        with open('task4_bin2.bin', 'wb') as bin2_file:
            bin2_file.writelines('')

    def test_3(self):
        self.assertTrue(os.path.exists('task4_bin.bin'))

    def test_4(self):
        self.assertTrue(os.path.exists('task4_bin2.bin'))

    def test_5(self):
        with open('task4_bin.bin', 'rb') as expected_f1:
            expected_f1_text = expected_f1.read()

        with open('task4_bin2.bin', 'rb') as expected_f2:
            expected_f2_text = expected_f2.read()

        swap_files('task4_bin.bin', 'task4_bin2.bin')

        with open('task4_bin.bin', 'rb') as bin_file:
            f1_text = bin_file.read()

        with open('task4_bin2.bin', 'rb') as bin2_file:
            f2_text = bin2_file.read()

        self.assertEqual(expected_f1_text, f2_text)
        self.assertEqual(expected_f2_text, f1_text)
