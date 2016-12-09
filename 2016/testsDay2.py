import unittest
from day2 import *

class test_day2(unittest.TestCase):
    def test_current_button(self):
        self.assertEqual(Keypad().current_button(), '5')

    def test_move_position(self):
        self.assertEqual(Keypad().move_position([1,1]).current_button(), '3')
        self.assertEqual(Keypad().move_position([-1,-1]).current_button(), '7')
        self.assertEqual(Keypad().move_position([-1000,-10000]).current_button(), '7')
        self.assertEqual(Keypad().move_position([991000,-9910000]).current_button(), '9')
        self.assertEqual(Keypad().move_position([991000,9910000]).current_button(), '3')
        self.assertEqual(Keypad().move_position([-991000,9910000]).current_button(), '1')

    def test_vectorize(self):
        self.assertEqual(vectorize('U'), [0,1])
        self.assertEqual(vectorize('L'), [-1,0])
        self.assertEqual(vectorize('R'), [1,0])
        self.assertEqual(vectorize('D'), [0,-1])

if __name__ == '__main__':
    unittest.main(verbosity=1)