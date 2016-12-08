import unittest
from day2 import *

class test_functions_in_IntentionPrompts(unittest.TestCase):
    def test_current_button(self):
        self.assertEqual(Keypad().current_button(), '5')

    def test_move_position(self):
        self.assertEqual(Keypad().move_position(1,1).current_button(), '3')
        self.assertEqual(Keypad().move_position(-1,-1).current_button(), '7')
        self.assertEqual(Keypad().move_position(-1000,-10000).current_button(), '7')
        self.assertEqual(Keypad().move_position(991000,-9910000).current_button(), '9')
        self.assertEqual(Keypad().move_position(991000,9910000).current_button(), '3')

if __name__ == '__main__':
    unittest.main(verbosity=1)