with open('day6_data.csv', 'r') as csvFile:
    blocks = [int(item) for row in csvFile for item in row.split()]

block_snapshots = set()
cycles = 0
puzzle_one = True

while True:
    i = blocks.index(max(blocks))
    banks = blocks[i]
    blocks[i] = 0
    cycles += 1

    for eachBank in range(0, banks):
        i += 1
        if i >= len(blocks):
            i = 0
        blocks[i] += 1

    snap = str(blocks)
    if snap in block_snapshots:
        if puzzle_one:
            print("Found the loop!")
            print(cycles)
            block_snapshots = set()
            cycles = 0
            puzzle_one = False
        else:
            print("Saw the loop again!")
            print(cycles)
            break
    block_snapshots = block_snapshots | set([snap])
