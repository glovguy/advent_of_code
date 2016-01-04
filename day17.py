myinput = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
#myinput = [20, 15, 10, 5, 5, 3, 2]
myinput.sort()

debug = False
verboseOutput = False
secondQuestion = True
totalGallons = 150
#25
if debug is True: print "totalGallons: " + str(totalGallons)

myinput = list(reversed(myinput))

global indices
indices = []
global answer
answer = [0]


def look_for_smaller_container(index, container):
    global indices
    global answer
    iterator = 1
    if debug is True: print "\t" * len(indices) + "iterator: " + str(iterator) + "\t index: " + str(index) + "\t len(myinput)-1: " + str(len(myinput)-1)
    while iterator + index < len(myinput):
        if debug is True: print "\t" * len(indices) + "LOOP i: " + str(iterator)
        if myinput[index+iterator] == container:
            if debug is True: print "hooray!"
            if debug is True: print "indices: " + str(indices + [index+iterator])
            answer = answer + [indices + [index+iterator]]
            answer[0] += 1
        elif myinput[index+iterator] < container:
            if debug is True: print "\t" * len(indices) + "container: " + str(container)
            if debug is True: print "\t" * len(indices) + str(myinput[index+iterator]) + " is less than " + str(container)
            if index+iterator == len(myinput)-1:
                if debug is True: print "\t" * len(indices) + "prune this tree--end of index " + str(index)
                indices = indices[:len(indices)-1]
                return False
            indices = indices + [index+iterator]
            if debug is True: print "\t" * len(indices) + "into recursion"
            look_for_smaller_container(index+iterator, container-myinput[index+iterator])
            if debug is True: print "\t" * len(indices) + "out of recursion"
        '''elif myinput[index+iterator] > container:
            if debug is True: print "\t" * len(indices) + str(myinput[index+iterator]) + " is greater than " + str(container)
            if look_for_smaller_container(index+iterator, container+myinput[index+iterator]) is False:
                return False'''
        iterator += 1
    indices = indices[:len(indices)-1]

# Print out the ordered input with indices
if debug is True:
    for index, container in enumerate(myinput):
        print str(index) + ": " + str(container)

for index, container in enumerate(myinput):
    indices = [index]
    if debug is True: print "Beginning at: " + str(index)
    look_for_smaller_container(index, totalGallons-container)

if debug is True:
    print "\nANSWER: "
    print answer
print "There are " + str(answer[0]) + " different combinations"

if verboseOutput is True:
    for eachCombination in answer[1:]:
        read = ""
        for eachItem in eachCombination:
            read = read + " and " + str(myinput[eachItem])
        print read[5:]

if secondQuestion is True:
    numContainers = [ len(x) for x in answer[1:] ]
    minContainers = min(numContainers)
    secondAnswer = numContainers.count(minContainers)
    print "Second Answer: " + str(secondAnswer)
