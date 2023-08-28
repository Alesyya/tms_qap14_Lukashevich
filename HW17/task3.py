#  3
import unittest


from HW17.HW6 import float_to_int


class Testtask3(unittest.TestCase):

    def test(self):
        with open('task3_float.txt', 'w') as file:
            file.write('')

    def test_1(self):
        nums = [2.4, 9.6]
        expected = [5.76, 92.16]
        self.assertEqual(float_to_int(nums), expected)

    def test_2(self):
        nums = [2, 9]
        with self.assertRaises(TypeError):
            float_to_int(nums)

    def test_3(self):
        nums = [2.1, 'a', 7.2]
        with self.assertRaises(TypeError):
            float_to_int(nums)

    def test_4(self):
        nums = []
        expected = []
        self.assertEqual(float_to_int(nums), expected)