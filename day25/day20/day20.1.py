def parseInput():
    f = open('testInput.txt', 'r')
    foundImage = False
    enhanceAlg = ''
    inputImage = []
    for line in f.readlines():
        if not foundImage:      enhanceAlg += line.strip()
        elif line.isspace():    foundImage = True
        elif foundImage:        inputImage += [[line]]
    return enhanceAlg, inputImage




