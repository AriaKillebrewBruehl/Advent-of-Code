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
            instructions += [[plane, int(pos)]]
        elif l.isspace(): continue
        else:
            x, y = l.strip().split(',')
            x, y = int(x), int(y)
            if x > maxX:    maxX = x
            if y > maxY:    maxY = y
            dots += [[x, y]]
    grid = [['.' for i in range(maxX + 1)] for j in range(maxY + 1)]
    return dots, instructions, grid

def markPaper(dots, grid):
    for d in dots:
        x, y = d[0], d[1]
        grid[y][x] = '#'

def singleFold(dots, instructions):
    fold = instructions[0]
    if fold[0] == 'x':
        line = fold[1]
    else:
        line = fold[1]
        for d in dots:
            if d[1] > line:
                dist = d[1] - line
                newY = line - dist
                newPos = [d[0], newY]
                dots.remove(d)
                if newPos not in dots:
                    dots.append(d)
    return

def countMarks(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                total += 1
    return total

if __name__ == "__main__":
    dots, instructions, grid = parseInput()
    markPaper(dots, grid)
    for g in grid:
        print(g)
    print()
    singleFold(dots, instructions)
    print(len(dots))