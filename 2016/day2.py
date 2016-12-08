from input_day2 import *

debug = True

class Keypad(object):
	'''1 2 3
	   4 5 6
	   7 8 9'''

	def __init__(self):
		self.x = 1
		self.y = 1

	def current_button(self):
		if self.x == 0 and self.y == 0: return str(7)
		if self.x == 1 and self.y == 0: return str(8)
		if self.x == 2 and self.y == 0: return str(9)
		if self.x == 0 and self.y == 1: return str(4)
		if self.x == 1 and self.y == 1: return str(5)
		if self.x == 2 and self.y == 1: return str(6)
		if self.x == 0 and self.y == 2: return str(1)
		if self.x == 1 and self.y == 2: return str(2)
		if self.x == 2 and self.y == 2: return str(3)

	def move_position(self, inx, iny):
		self.x += inx
		self.y += iny
		if self.x > 2: self.x = 2
		if self.x < 0: self.x = 0
		if self.y > 2: self.y = 2
		if self.y < 0: self.y = 0
		return self


if __name__ == '__main__':
    if debug is True: unittest.main(verbosity=1)