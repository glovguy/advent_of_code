def part1_each_line(line):
    firstChar = lastChar = None
    for char in line:
        if char.isnumeric() and firstChar is None:
            firstChar = char
        if char.isnumeric():
            lastChar = char
    return int(firstChar + lastChar)


SPELLED_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
def part2_each_line(line):
    firstChar = lastChar = None
    for i in range(0, len(line)):
        char = line[i]
        if not char.isnumeric():
            for d in SPELLED_DIGITS:
                ld = len(d)
                if i+1 >= ld and line[i-ld+1:i+1] == d:
                    if firstChar is None:
                        firstChar = SPELLED_DIGITS[d]
                    lastChar = SPELLED_DIGITS[d]
        if char.isnumeric() and firstChar is None:
            firstChar = char
        if char.isnumeric():
            lastChar = char
    return int(firstChar + lastChar)

with open("2023/input_day1.txt", "r") as f:
    lines = f.readlines()
    totalPart1 = 0
    totalPart2 = 0
    for line in lines:
        totalPart1 += part1_each_line(line)
        totalPart2 += part2_each_line(line)
    print(totalPart1)
    print(totalPart2)
    
            
