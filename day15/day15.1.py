def parseInput():
    f = open('input.txt', 'r')
    grid = []
    for l in f.readlines():
        l.strip()
        row = [int(digit) for digit in l]
        grid.append(row)
    return grid

def findBestPath(grid):
    current = grid[0][0]
    next = None
    end = grid


