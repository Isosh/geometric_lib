import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 8)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 2, 0)
        self.assertEqual(res, 2)

    def test_str_area(self):
        res = area('2', '4')
        self.assertEqual(res, "Error: can't work with not integer or not float types")

    def test_str_perimeter(self):
        res = perimeter('2', '8', '5')
        self.assertEqual(res, "Error: can't work with not integer or not float types")

    def test_negative_area(self):
        res = area(2, -3)
        self.assertEqual(res, "Error: values can't be negative")

    def test_negative_perimeter(self):
        res = perimeter(3, -12, -2)
        self.assertEqual(res, "Error: values can't be negative")

    def test_right_area(self):
        res = area(3, 8)
        self.assertEqual(res, 12)

    def test_right_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

if __name__ == '__main__':
    unittest.main()
