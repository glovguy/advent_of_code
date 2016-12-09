import re
from input_day3 import *

debug = False

def is_valid_triangle(*triangle):
    if type(triangle) is tuple:
        triangle = list(triangle)
        triangle = [list(i) for i in triangle][0]
    triangle.sort()
    if triangle[2] < triangle[0] + triangle[1]: return True
    else: return False

def string_to_list(triangles):
    tNums = re.findall(
        r"([0-9]+)",
        triangles)
    tNums = [int(x) for x in tNums]
    tList = []
    for i in range(len(tNums)/3):
        tList += [tNums[i*3:i*3+3]]
    return tList

if __name__ == '__main__':
    if debug is True: stream = test
    if debug is False: stream = prod
    triangles = string_to_list(stream)
    print "Total number of triangles: " + str(len(triangles))
    print "Number of possible triangles: " + str(len([x for x in triangles if is_valid_triangle(x) is True]))
    print "Number of impossible triangles: " + str(len([x for x in triangles if is_valid_triangle(x) is False]))