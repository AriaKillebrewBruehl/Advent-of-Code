def parseInput():
    f = open('testInput.txt', 'r')
    days = 256
    fish = [[int(i), days] for i in f.read().split(',')]
    return fish

def getTotalChildren(fish):
    currentDay = fish[0]
    spawnDays = fish[1] - currentDay
    children = [[8, spawnDays - 1] for i in range(spawnDays // 7)]
    total = 0
    for child in children:
        total += 1
        childCurrentDay = child[0]
        childSpawnDays = child[0] - childCurrentDay
        if childSpawnDays // 7 >= 1:
            for i in range(childSpawnDays):
                total += getTotalChildren([8, childSpawnDays])
    return total

def getCounts(fish, days):
    total = 0
    for i in range(len(fish)):
        spawnDays = fish[i][1] - fish[i][0]
        numOffspring = spawnDays // 7
        total += 1
        for j in range(numOffspring):
            total += getTotalChildren([8, spawnDays])
        print(fish)
    return total

if __name__ == "__main__":
    fish = parseInput()
    print(getCounts(fish, 256))
