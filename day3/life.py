def parseInput():
    f = open("input.txt", "r")
    lines = f.readlines()
    return lines

def findMostCommon(lines, i):
    count = 0
    for line in lines:
        if line[i] == "1": count += 1
        else:              count -= 1

    if count >= 0: return 1
    else:          return 0

def findLeastCommon(lines, i):
    return (1 + findMostCommon(lines, i)) % 2

def reduce(lines, i, select, oRate = True):
    if len(lines) != 1 and i < len(lines[0]) - 1:
        newLines = []
        for line in lines:
            if int(line[i]) == select:
                newLines.append(line)
        if len(newLines) == 0:
            newLines = lines
        if oRate:
            return reduce(newLines, i+1, findMostCommon(newLines, i+1))
        else:
            return reduce(newLines, i+1, findLeastCommon(newLines, i+1), False)
    else:
        return lines[0]

def calcRates(lines):
    oLines = lines.copy()
    oRate = reduce(oLines, 0, findMostCommon(oLines, 0))
    o = int(oRate, 2)
    cLines = lines.copy()
    cRate = reduce(cLines, 0, findLeastCommon(cLines, 0), False)
    c = int(cRate, 2)
    return o, c, o * c

def main():
    lines = parseInput()
    print(calcRates(lines))