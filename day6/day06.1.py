def parseInput():
    f = open('input.txt', 'r')
    fish = [int(i) for i in f.read().split(',')]
    counts = [0]*9
    for f in fish:
        counts[f] += 1
    return fish, counts

def getCounts(fish, days):
    while days > 0:
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
        days -= 1
    return len(fish)


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
    print(getCounts(fish, 80))
    print(arrayCounts(counts, 80))