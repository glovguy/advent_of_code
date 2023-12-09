import re
from math import lcm

dl = {
    "L": 0,
    "R": 1
}
ghostNodes = []

with open("2023/input_day8.txt", "r") as f:
    lines = f.readlines()
    nodes = {}
    directions = lines[0][:-1]
    l = len(directions)
    for line in lines[2:]:
        m = re.search("([a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]) = \(([a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]), ([a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9])\)", line)
        nodeName = m.group(1)
        left = m.group(2)
        right = m.group(3)
        nodes[nodeName] = [left, right]
        if nodeName[2] == "A":
            ghostNodes.append(nodeName)
    currentNode = "AAA"
    iter = 0
    while currentNode != "ZZZ":
        d = directions[iter % l]
        currentNode = nodes[currentNode][dl[d]]
        iter += 1
    print("Part 1: ", iter)

# Part 2

ghostValueLookup = {}
multiples = [None for _ in range(0, len(ghostNodes))]
def allValuesFound():
    for m in multiples:
        if m is None:
            return False
    return True

iter = 0
while not allValuesFound():
    d = directions[iter % l]
    for i in range(0, len(ghostNodes)):
        if multiples[i] is not None:
            continue
        n = ghostNodes[i]
        ghostValueLookup[n] = [i, iter]
        ghostNodes[i] = nodes[n][dl[d]]
        n = ghostNodes[i]
        if n[2] == "Z":
            multiples[i] = iter + 1
            continue
        if ghostValueLookup.get(n) is not None and multiples[ghostValueLookup[n][0]] is not None:
            multiples[i] = ghostValueLookup.get(ghostNodes[i])[i] - multiples[ghostValueLookup[ghostNodes[i]][0]] + iter
    iter += 1

answer = lcm(*multiples)

print("Part 2: ", answer)
