import unittest
from input_day2 import *

debug = False

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
        raise Exception("Keypad has invalid position: " + str(self.x) + str(self.y))

    def move_position(self, *vector):
        if type(vector) is tuple:
            vector = list(vector)
            vector = [list(i) for i in vector][0]
        self.x += vector[0]
        self.y += vector[1]
        if debug is True: print("Move " + str(vector))
        if self.x > 2: self.x = 2
        if self.x < 0: self.x = 0
        if self.y > 2: self.y = 2
        if self.y < 0: self.y = 0
        if debug is True: print("Button is now: " + str(self.current_button()))
        return self


def vectorize(strIn):
    out = [0,0]
    if strIn is "U": out = [0,1]
    if strIn is "L": out = [-1,0]
    if strIn is "R": out = [1,0]
    if strIn is "D": out = [0,-1]
    return out

if __name__ == '__main__':
    if debug is True: stream = test
    else: stream = prod

    myKeypad = Keypad()
    for l in stream:
        if debug is True: print("Stream input: " + unicode(l).decode())
        if l == "\n": print(myKeypad.current_button())
        else: myKeypad.move_position(i for i in vectorize(l))
    print(myKeypad.current_button())
