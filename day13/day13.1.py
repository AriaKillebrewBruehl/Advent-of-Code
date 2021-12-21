def parseInput():
    f = open('input.txt', 'r')
    instructions = []
    dots = []
    for l in f.readlines():
        if 'fold' in l:
            fold = l.strip().split(' ')
            plane, pos = fold[2].split('=')
            instructions += [[plane, int(pos)]]
        elif l.isspace(): continue
        else:
            x, y = l.strip().split(',')
            x, y = int(x), int(y)
            dots += [[x, y]]
    return dots, instructions

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

if __name__ == "__main__":
    dots, instructions = parseInput()
    singleFold(dots, instructions)
    print(len(dots))