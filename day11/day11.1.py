def parseInput():
    f = open('testInput.txt', 'r')
    grid = [[int(digit) for digit in l.strip()] for l in f.readlines()]
    return grid

def incrementAll(grid):
    toFlash = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
            if grid[r][c] > 9:
                toFlash += [[r, c]]
    return toFlash

def getNeighbors(grid, r, c):
    # a b c
    # d x e
    # f g h
    positions = { 'a' : [r-1, c-1],
                  'b' : [r-1, c]  ,
                  'c' : [r-1, c+1],
                  'd' : [r, c-1]  ,
                  'e' : [r, c+1]  ,
                  'f' : [r+1, c-1],
                  'g' : [r+1, c]  ,
                  'h' : [r+1, c+1],
    }
    if r == 0:
        positions.pop('a')
        positions.pop('b')
        positions.pop('c')
    elif r == len(grid) - 1:
        positions.pop('f')
        positions.pop('g')
        positions.pop('h')
    if c == 0:
        if 'a' in positions:    positions.pop('a')
        positions.pop('d')
        if 'f' in positions:    positions.pop('f')
    elif c == len(grid[r]) - 1:
        if 'c' in positions:    positions.pop('c')
        positions.pop('e')
        if 'h' in positions:    positions.pop('h')

    return positions

def flashNeighbors(grid, r, c, flashed):
    neighbors = getNeighbors(grid, r, c)

    for n in neighbors:
        i, j = neighbors[n][0], neighbors[n][1]
        grid[i][j] += 1
        if grid[i][j] == 10:
            flashNeighbors(grid, i, j, flashed)
            flashed += [[i, j]]

def step(grid):
    toFlash = incrementAll(grid)
    flashed = []
    for f in toFlash:
        flashed += [f]
        flashNeighbors(grid, f[0], f[1], flashed)
    for f in flashed:
        grid[f[0]][f[1]] = 0
    return len(flashed)


def getFlashes(grid, steps):
    total = 0
    for i in range(steps):
        total += step(grid)
    return total

if __name__ == '__main__':
    grid = parseInput()
    for r in grid:
        print(r)
    print()
    total = getFlashes(grid, 100)
    for r in grid:
        print(r)
    print()
    print(total)

