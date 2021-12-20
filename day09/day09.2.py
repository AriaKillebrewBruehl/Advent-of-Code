import copy
def parseInput():
    f = open('testInput.txt', 'r')
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
                lows += [[i, j]]
    return lows

def findBasins(lows, points):
    topThree = [0, 0, 0]
    print(len(lows))
    for l in lows:
        basin = 0
        p = copy.deepcopy(points)
        print(p)
        p[l[0]][l[1]] = -1
        done = False
        l = r = u = d = False
        while not done:
            for i in range(len(p)):
                for j in range(len(p[i])):
                    if i == 0: u = True
                    else:
                        if p[i - 1][j] == 9:  u = True
                        elif p[i][j] == -1 and p[i - 1][j] > p[i][j]:
                            p[i - 1][j] = -1
                            basin += 1

                    if i == len(p) - 1:   r = True
                    else:
                        if p[i + 1][j] == 9:  d = True
                        elif  p[i][j] == -1 and p[i + 1][j] > p[i][j]:
                            p[i + 1][j]
                            basin += 1

                    if j == 0:    l = True
                    else:
                        if p[i][j - 1] == 9:  l = True
                        if p[i][j] == -1 and p[i][j - 1] > p[i][j]:
                            p[i][j - 1] = -1
                            basin += 1

                    if j == len(p[i]) - 1:    r = True
                    else:
                        if p[i][j] == -1 and p[i][j + 1] > p[i][j]:
                            p[i][j + 1] = -1
                            basin += 1
                        elif p[i][j + 1] == 9: r = True

                    if l and r and u and d:
                        print(basin)
                        done = True

        m = min(topThree)
        if basin > m:
            print("hi")
            topThree[topThree.index(m)] = basin
            print(topThree)
    return topThree

def findTotal(points):
    lows = findLows(points)
    print("found lows")
    topThree = findBasins(lows, points)
    total = 1
    for b in topThree:
        total *= b
    return total

if __name__ == "__main__":
    points = parseInput()
    print(findTotal(points))
