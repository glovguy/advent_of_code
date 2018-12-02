import json


freqChanges = json.load(open('2018/day1_data.json', 'r'))

##############
## Part One ##
##############

print('Solution One: ', sum([int(c) for c in freqChanges]))


##############
## Part Two ##
##############

def repeated_frequency(freqChanges):
    currentFreq = 0
    seenFreqs = set([currentFreq])
    while True:
        for c in freqChanges:
            currentFreq += int(c)
            if currentFreq in seenFreqs: return currentFreq
            seenFreqs.update([currentFreq])

print('Solution Two: ', repeated_frequency(freqChanges))
