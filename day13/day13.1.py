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
    plane, pos = instructions[0]
    if plane == 'x':
        for d in dots:
            if d[0] > pos:
                dist = d[0] - pos
                newPos = [pos - dist, d[1]]
                dots.remove(d)
                if newPos not in dots:
                    dots.append(d)
    else:
        for d in dots:
            if d[1] > pos:
                dist = d[1] - pos
                newPos = [d[0], pos - dist]
                dots.remove(d)
                if newPos not in dots:
                    dots.append(d)

if __name__ == "__main__":
    dots, instructions = parseInput()
    print(len(dots))
    print(instructions)
    singleFold(dots, instructions)
    print(len(dots))
    print(len(dots))