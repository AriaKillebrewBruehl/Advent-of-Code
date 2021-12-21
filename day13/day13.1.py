def parseInput():
    f = open('testInput.txt', 'r')
    instructions = []
    dots = []
    maxX = 0
    maxY = 0
    for l in f.readlines():
        if 'fold' in l:
            fold = l.split(' ')
            plane, pos = fold[2].split('=')
            instructions += [[plane, pos]]
        else:
            x, y = l.split(',')
            if x > maxX:    maxX = x
            if y > maxY:    maxY = y
            dots += [[x, y]]
    grid = [['.' for x in maxX] for y in maxY]
    return dots, instructions, grid

def markPaper(dots):

if __name__ == "__main__":
    dots, instructions, grid = parseInput()