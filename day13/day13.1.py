def parseInput():
    f = open('testInput.txt', 'r')
    instructions = []
    dots = []
    maxX = 0
    maxY = 0
    for l in f.readlines():
        if 'fold' in l:
            fold = l.strip().split(' ')
            plane, pos = fold[2].split('=')
            instructions += [[plane, pos]]
        elif l.isspace(): continue
        else:
            x, y = l.strip().split(',')
            x, y = int(x), int(y)
            if x > maxX:    maxX = x
            if y > maxY:    maxY = y
            dots += [[x, y]]
    grid = [['.' for i in range(maxX)] for j in range(maxY)]
    print(maxX, maxY)
    return dots, instructions, grid

def markPaper(dots, grid):
    for d in dots:
        x, y = d[0], d[1]
        grid[y][x] = '#'

def singleFold(grid, instructions):
    fold = instructions[0]
    if fold[0] == 'x':
        line = fold[1]
    else:
        line = fold[1]
        newGrid = [grid[i] for i in range(line)]
        for i in range(line + 1, len(grid)):
            for j in grid[i]:
                newGrid[line - 1 - i][j] = grid[i][j]
    return newGrid

def countMarks(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                total += 1
    return total

if __name__ == "__main__":
    dots, instructions, grid = parseInput()
    for g in grid:
        print(g)
    markPaper(dots, grid)
    folded = singleFold(grid)
    print(countMarks(folded))