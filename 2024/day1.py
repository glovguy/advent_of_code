
from collections import defaultdict


left = []
right = []
with open("inputs/input_day1.txt") as f:
    for line in f:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

distTotal = 0

for i in range(0, len(left)):
    distTotal += abs(left[i] - right[i])

print(distTotal)

# Part 2

rCount = defaultdict(int)
for i in range(0, len(right)):
    rCount[right[i]] += 1

simScore = 0
for l in left:
    simScore += l*rCount[l]

print("Part 2: ", simScore)
