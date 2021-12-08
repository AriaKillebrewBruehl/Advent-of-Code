def parseInput():
    f = open('input.txt', 'r')
    fish = [int(i) for i in f.read().split(',')]
    return fish

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

if __name__ == "__main__":
    fish = parseInput()
    print(getCounts(fish, 80))