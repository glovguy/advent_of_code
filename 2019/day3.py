from inputs import day3


def lines_from_instructions(instructions, start=[0,0]):
    instr = instructions.split(',')
    loc = start
    yield loc
    for i in instr:
        command = i[0]
        stepCount = float(i[1:])
        if command == 'U':
            loc = [loc[0],loc[1]+stepCount]
        elif command == 'R':
            loc = [loc[0]+stepCount,loc[1]]
        elif command == 'L':
            loc = [loc[0]-stepCount,loc[1]]
        elif command == 'D':
            loc = [loc[0],loc[1]-stepCount]
        else:
            raise 'Err'
        yield loc


def points_in_line(p1,p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    step = [xDiff/abs(xDiff),0] if xDiff!=0 else [0,yDiff/abs(yDiff)]
    loc = tuple(p1)
    yield loc
    while loc != tuple(p2):
        loc = (loc[0]+step[0],loc[1]+step[1])
        yield loc


def points_from_instructions(instr):
    lines = [l for l in lines_from_instructions(instr)]
    points = []
    for i in range(0, len(lines)-1):
        points += (p for i, p in enumerate(points_in_line(lines[i],lines[i+1])) if i != 0)
    return points


def intersections(instr1, instr2):
    points1 = points_from_instructions(instr1)
    points2 = points_from_instructions(instr2)
    return set(points1) & set(points2)


def intersections_with_step_count(instr1, instr2):
    points1 = points_from_instructions(instr1)
    points2 = points_from_instructions(instr2)
    intersection = set(points1) & set(points2)
    pwi1 = [[p, i] for i, p in enumerate(points1, 1) if p in intersection and p != (0,0)]
    pwi2 = [[p, i] for i, p in enumerate(points2, 1) if p in intersection and p != (0,0)]
    intr_with_step = []
    for p1, i in pwi1:
        for p2, j in pwi2:
            if p1 != p2: continue
            score = i + j
            intr_with_step.append([p1, score])
    return intr_with_step


def intersection_with_lowest_step(instr1, instr2):
    allIntersections = intersections_with_step_count(instr1, instr2)
    return sorted(allIntersections, key=lambda p: p[1])[0]

def nearest_intersection(instr1, instr2):
    allIntersections = intersections(instr1, instr2)
    allIntersections.discard((0,0))
    return sorted(allIntersections, key=manhattan)[0]


def manhattan(point):
    return abs(point[0]) + abs(point[1])


def puzzle1(ins1, ins2):
    print('Solution1: ', manhattan(nearest_intersection(ins1, ins2)))


def puzzle2(ins1, ins2):
    print('Solution2: ', intersection_with_lowest_step(ins1, ins2)[1])


# puzzle1('R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83')
# puzzle1('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
puzzle1(day3[0], day3[1])
puzzle2(day3[0], day3[1])
