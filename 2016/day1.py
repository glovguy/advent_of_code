from input_day1 import *

class Vector(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash(int(str(self.x) + str(self.y)))

loc = Vector(0,0)
orientation = 0
num = ''
debug = True
probtwo = True
locset = []

directions = test + ' '
# directions = prod + ' '

for l in directions:
	if l is 'R':
		orientation += 1
		if debug is True: print "turn right"
	if l is 'L':
		orientation -= 1
		if debug is True: print "turn left"
	if l is ' ':
		if orientation%4==0:
			loc.y += int(num)
			if debug is True: print "North " + str(num) + " steps"
		if orientation%4==1:
			loc.x += int(num)
			if debug is True: print "East " + str(num) + " steps"
		if orientation%4==2:
			loc.y -= int(num)
			if debug is True: print "South " + str(num) + " steps"
		if orientation%4==3:
			loc.x -= int(num)
			if debug is True: print "West " + str(num) + " steps"
		num = ''
		if probtwo is True:
			if debug is True: print("current location: " + str(loc.x) + ", " + str(loc.y))
			if loc in locset:
				print "DUPLICATE LOCATION: " + str(loc.x) + ", " + str(loc.y)
				# break
			else:
				locset.append(loc)
	if l.isdigit():
		num += l

if probtwo is False:
	print "Distance: " + str(abs(loc.x) + abs(loc.y))
elif probtwo is True:
	print "Distance to duplicate location: " + str(abs(loc.x) + abs(loc.y))