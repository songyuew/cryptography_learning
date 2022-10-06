import random
import decimal
classSize = 23
numTrials = 1000
dupeCount = 0
for trial in range(numTrials):
    year = [0]*365
    foundDupe = False

    for i in range(classSize):
        newBDay = random.randrange(365)
        year[newBDay] = year[newBDay] + 1
        if year[newBDay] > 1:
            foundDupe = True

    if foundDupe == True:
        dupeCount = dupeCount + 1

prob = float(dupeCount / (numTrials * 1.0))
print('The probability of a shared birthday in a class of', classSize,'is', prob)
