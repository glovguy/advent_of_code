import re

def is_valid_triangle(*triangle):
    if type(triangle) is tuple:
        triangle = list(triangle)
        triangle = [list(i) for i in triangle][0]
    triangle.sort()
    if triangle[2] <= triangle[0] + triangle[1]: return False
    else: return True

def string_to_list(triangles):
	re.sub