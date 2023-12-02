import re

def count_colors(round):
    redMatch = re.search("(\d+) red", round)
    if redMatch:
        red = int(redMatch.group(1))
    else:
        red = 0
    greenMatch = re.search("(\d+) green", round)
    if greenMatch:
        green = int(greenMatch.group(1))
    else:
        green = 0
    blueMatch = re.search("(\d+) blue", round)
    if blueMatch:
        blue = int(blueMatch.group(1))
    else:
        blue = 0
    return [red, green, blue]

def is_round_invalid(round):
    [red, green, blue] = count_colors(round)
    if red > 12 or green > 13 or blue > 14:
        return True
    return False

def is_game_valid(rounds):
    for round in rounds:
        if is_round_invalid(round):
            return False
    return True

def power_of_game(rounds):
    redMax = greenMax = blueMax = 0
    for round in rounds:
        [red, green, blue] = count_colors(round)
        if red > redMax:
            redMax = red
        if green > greenMax:
            greenMax = green
        if blue > blueMax:
            blueMax = blue
    return redMax * greenMax * blueMax


with open("2023/input_day2.txt", "r") as f:
    lines = f.readlines()
    validGameChecksum = powerSum = 0

    for line in lines:
        gameMatches = re.search("Game (\d+): (.*)", line)
        gameNum = int(gameMatches.group(1))
        rounds = gameMatches.group(2).split("; ")
        if is_game_valid(rounds):
            validGameChecksum += gameNum
        powerSum += power_of_game(rounds)
    print(validGameChecksum)
    print(powerSum)
