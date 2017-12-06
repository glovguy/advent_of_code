def load_data():
    with open('day5_data.csv', 'r') as csvFile:
        return [float(row) for row in csvFile]

i = 0
jump_count = 0
arr = load_data()

while i >= 0 and i < len(arr):
    jump_count += 1
    next_jump = arr[i]
    arr[i] += 1
    i = int(next_jump + i)

print('Part 1 jump count: %s' % jump_count)

i = 0
jump_count = 0
arr = load_data()

while i >= 0 and i < len(arr):
    jump_count += 1
    next_jump = arr[i]
    if next_jump >= 3:
        arr[i] -= 1
    else:
        arr[i] += 1
    i = int(next_jump + i)

print('Part 2 jump count: %s' % jump_count)
