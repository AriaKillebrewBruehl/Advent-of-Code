def parseInput():
    f = open('input.txt', 'r')
    fish = [int(i) for i in f.read().split(',')]
    counts = [0]*9
    for f in fish:
        counts[f] += 1
    return fish, counts

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

def getCounts(fish):
    total = 0
    for i in range(len(fish)):
        spawnDays = fish[i][1] - fish[i][0]
        numOffspring = spawnDays // 7
        total += 1
        for j in range(numOffspring):
            total += getTotalChildren([8, spawnDays])
        print(fish)
    return total

def arrayCounts(counts, days):
    while days > 0:
        newFish = counts[0]
        for i in range(len(counts) - 1):
            counts[i] = counts[i+1]
        counts[6] += newFish
        counts[-1] = newFish
        days -= 1
    total = sum(counts)
    return total


if __name__ == "__main__":
    fish, counts = parseInput()
    print(arrayCounts(counts, 256))
