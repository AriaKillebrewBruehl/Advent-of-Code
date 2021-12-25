def parseInput():
    f = open('testInput.txt', 'r')
    eCucs = []
    sCucs = []
    r = 0
    for line in f.readlines():
        c = 0
        for pos in line.strip().split():
            if pos == '>':
                eCucs += [[c, r]]
            elif pos == 'v':
                sCucs += [[c, r]]
            c += 1
        r += 1
    return eCucs, sCucs

