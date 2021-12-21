def parseInput():
    f = open('tinyInput.txt', 'r')
    grid = [[int(digit) for digit in l.strip()] for l in f.readlines()]
    return grid

def incrementAll(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1

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
        positions.pop('a')
        positions.pop('d')
        positions.pop('f')
    elif c == len(grid[r]) - 1:
        positions.pop('c')
        positions.pop('e')
        positions.pop('h')

    return positions

def flashNeighbors(grid, r, c):
    neighbors = getNeighbors(grid, r, c)

    for n in neighbors:
        i, j = neighbors[n][0], neighbors[n][1]
        grid[i][j] += 1
        if grid[i][j] == 9:
            flashNeighbors(grid, i, j)
            grid[i][j] = 0

def step(grid):
    incrementAll(grid)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] >= 9:
                flashNeighbors(grid, r, c)
                grid[r][c] = 0


def getFlashes(grid, steps):
    for i in range(steps):
        step(grid)

if __name__ == '__main__':
    grid = parseInput()
    for r in grid:
        print(r)
    print()
    getFlashes(grid, 1)
    for r in grid:
        print(r)

