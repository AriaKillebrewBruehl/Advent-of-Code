def parseInput():
    f = open('input.txt', 'r')
    cucMap = [list(r.strip()) for r in f.readlines()]
    return cucMap

def stepEast(cucMap):
    madeChange = False
    for r in cucMap:
        i = 0
        while i < len(r) - 1:
            if r[i] == '>' and r[i + 1] == '.':
                r[i] = 'x'
                r[i + 1] = '<'
                madeChange = True
                i += 1
            i += 1
        if r[len(r) - 1] == '>' and r[0] == '.':
            r[len(r) - 1] = 'x'
            r[0] = '<'
            madeChange = True
    fixMap(cucMap)
    return madeChange

def stepSouth(cucMap):
    madeChange = False
    i = 0
    lenRow = len(cucMap[0])
    while i < len(cucMap) - 1:
        j = 0
        while j < lenRow:
            if cucMap[i][j] == 'v' and cucMap[i + 1][j] == '.':
                cucMap[i][j] = 'x'
                cucMap[i + 1][j] = '^'
                madeChange = True
            j += 1
        i += 1
    j = 0
    lastRow = len(cucMap) - 1
    while j < lenRow:
        if cucMap[lastRow][j] == 'v' and cucMap[0][j] == '.':
            cucMap[lastRow][j] = 'x'
            cucMap[0][j] = '^'
            madeChange = True
        j += 1
    fixMap(cucMap)
    return madeChange

def fixMap(cucMap):
    i = 0
    while i <len(cucMap):
        j = 0
        while j < len(cucMap[i]):
            if cucMap[i][j] == '<':     cucMap[i][j] = '>'
            elif cucMap[i][j] == '^':   cucMap[i][j] = 'v'
            elif cucMap[i][j] == 'x':   cucMap[i][j] = '.'
            j += 1
        i += 1

def findSolid(cucMap):
    numSteps = 0
    while True:
        eastChange = stepEast(cucMap)
        southChange = stepSouth(cucMap)
        if eastChange or southChange:
            numSteps += 1
        else:                           break
    return numSteps + 1

if __name__ == '__main__':
    cucMap= parseInput()
    # for r in cucMap:
    #     print(''.join(r))
    # print()
    numSteps = findSolid(cucMap)
    print(numSteps)

