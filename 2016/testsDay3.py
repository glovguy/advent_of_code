import unittest
from day3 import *

class test_day3(unittest.TestCase):
    def test_is_valid_triangle(self):
        self.assertEqual(is_valid_triangle([2,3,4]), True)
        self.assertEqual(is_valid_triangle([4,3,2]), True)
        self.assertEqual(is_valid_triangle([3,2,4]), True)
        self.assertEqual(is_valid_triangle([1,2,4]), False)
        self.assertEqual(is_valid_triangle([1,2,10]), False)

    def test_string_to_list(self):
        first = '''    4   21  894'''
        second = '''    4   21  894
  419  794  987
  424  797  125'''
        self.assertEqual(string_to_list(first), [[4,21,894]])
        self.assertEqual(string_to_list(second), [[4,21,894],[419,794,987],[424,797,125]])

if __name__ == '__main__':
    unittest.main(verbosity=1)