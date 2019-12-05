from tqdm import tqdm


def each_digit_increasing(num):
    stringNum = str(num)
    for i in range(0, len(str(num))-1):
        if int(stringNum[i]) > int(stringNum[i+1]):
            return False
    return True


def has_double_digit(num):
    stringNum = str(num)
    for i in range(0, len(str(num))-1):
        if int(stringNum[i]) == int(stringNum[i+1]):
            return True
    return False


def has_only_double_digit(num):
    stringNum = str(num)
    hasDouble = False
    for i in range(0, len(str(num))):
        isLastDigit = (i == len(str(num))-1)
        isSecondToLastDigit = (i == len(str(num))-2)
        dbl = ( isLastDigit or int(stringNum[i]) == int(stringNum[i+1]) )
        lftNot = (i == 0 or int(stringNum[i-1]) != int(stringNum[i]) )
        rgtNot = (isSecondToLastDigit) or (not isLastDigit and int(stringNum[i+1]) != int(stringNum[i+2]) )
        if dbl and lftNot and rgtNot:
            return True
    return False


def meets_criteria_part1(num):
    stringNum = str(num)
    hasDouble = False
    for i in range(0, len(str(num))-1):
        if int(stringNum[i]) > int(stringNum[i+1]):
            return False
        if int(stringNum[i]) == int(stringNum[i+1]):
            hasDouble = True
    return hasDouble


def meets_criteria_part2(num):
    stringNum = str(num)
    hasDouble = False
    for i in range(0, len(str(num))):
        isLastDigit = (i == len(str(num))-1)
        isSecondToLastDigit = (i == len(str(num))-2)
        dbl = ( isLastDigit or int(stringNum[i]) == int(stringNum[i+1]) )
        lftNot = (i == 0 or int(stringNum[i-1]) != int(stringNum[i]) )
        rgtNot = (isSecondToLastDigit) or (not isLastDigit and int(stringNum[i+1]) != int(stringNum[i+2]) )
        if not isLastDigit and int(stringNum[i]) > int(stringNum[i+1]):
            return False
        if dbl and lftNot and rgtNot:
            hasDouble = True
    return hasDouble


# print(meets_criteria_part2(112233))
# print(meets_criteria_part2(12245))
# print(meets_criteria_part2(1234445))
# print(meets_criteria_part2(111122))
# print(meets_criteria_part2(2232450))

print('Part 1: ', len([x for x in tqdm(range(147981, 691423)) if meets_criteria_part1(x)]))
print('Part 2: ', len([x for x in tqdm(range(147981, 691423)) if meets_criteria_part2(x)]))
