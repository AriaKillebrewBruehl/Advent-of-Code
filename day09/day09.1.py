def parseInput():
    f = open('input.txt', 'r')
    points = []
    for l in f.readlines():
        points += [[int(digit) for digit in l.strip()]]
    return points

def findLows(points):
    lows = []
    for i in range(len(points)):
        for j in range(len(points[i])):
            l = r = u = d = True
            if i != 0:
                if points[i - 1][j] <= points[i][j]:
                    u = False
            if i != len(points) - 1:
                if points[i + 1][j] <= points[i][j]:
                    d = False
            if j != 0:
                if points[i][j - 1] <= points[i][j]:
                    l = False
            if j != len(points[i]) - 1:
                if points[i][j + 1] <= points[i][j]:
                    r = False
            if l and r and u and d:
                lows.append(points[i][j])
    return lows

def totalRisk(points):
    lows = findLows(points)
    total = len(lows)
    for l in lows:
        total += l
    return total

if __name__ == "__main__":
    points = parseInput()
    print(totalRisk(points))
