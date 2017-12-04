total_count = 0
invalid_count = 0

with open('day4_data.csv', 'r') as csvFile:
    for eachRow in csvFile:
        total_count += 1
        rowArray = [word for word in eachRow.split()]
        rowSet = frozenset(rowArray)
        if len(rowArray) - len(rowSet) != 0: invalid_count += 1

print("Part 1:")
print("Number of valid passphrases: ", total_count - invalid_count)

###

total_count = 0
invalid_count = 0

with open('day4_data.csv', 'r') as csvFile:
    for eachRow in csvFile:
        total_count += 1
        rowArray = [frozenset(word) for word in eachRow.split()]
        rowSet = frozenset(rowArray)
        if len(rowArray) - len(rowSet) != 0: invalid_count += 1

print("Part 2:")
print("Number of valid passphrases: ", total_count - invalid_count)
