import unittest
from day3 import *

class test_day3(unittest.TestCase):
    def test_is_valid_triangle(self):
        self.assertEqual(is_valid_triangle([2,3,4]), False)
        self.assertEqual(is_valid_triangle([4,3,2]), False)
        self.assertEqual(is_valid_triangle([3,2,4]), False)
        self.assertEqual(is_valid_triangle([1,2,4]), True)
        self.assertEqual(is_valid_triangle([1,2,10]), True)

if __name__ == '__main__':
    unittest.main(verbosity=1)