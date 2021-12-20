def parseInput():
    f = open('testInput.txt', 'r')
    hPos = [int(i) for i in f.read().split(',')]
    return hPos

def findFuel(hPos):
    avg = sum(hPos)/len(hPos)
    target = round(avg)
    total = 0
    for p in hPos:
        dist = abs(p - target)
        fuel = ((1 + dist) * dist)/2
        total += fuel
    return round(total)

if __name__ == "__main__":
    hPos = parseInput()
    print(findFuel(hPos))
