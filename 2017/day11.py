import csv
import math

def step(step_string):
    if step_string == 'n': return (0, 1)
    if step_string == 'ne': return (0.5, 0.5)
    if step_string == 'se': return (0.5, -0.5)
    if step_string == 's': return (0, -1)
    if step_string == 'sw': return (-0.5, -0.5)
    if step_string == 'nw': return (-0.5, 0.5)

def dist(x,y):
    return abs(math.ceil(current_x + current_y))


with open('day11_data.csv', 'r') as csvFile:
    file_reader = csv.reader(csvFile)
    steps = list(file_reader)[0]


current_x = 0
current_y = 0
dists = []


for step_str in steps:
    s = step(step_str)
    current_x += s[0]
    current_y += s[1]
    dists.append(dist(current_x, current_y))


print("Final location: %s, %s" % (current_x, current_y))
print("Steps needed to reach: %s" % dist(current_x, current_y))
print("Furthest away: %s" % max(dists))
