def parseInput():
    f = open('testInput.txt', 'r')
    lines = f.readlines()
    enhanceAlg = lines[0].strip()
    inputImage = [list(lines[i].strip()) for i in range(2, len(lines))]
    return enhanceAlg, inputImage

def padImage(inputImage):
    for r in inputImage:
        r.insert(0, '.')
        r.append('.')
    darkRow = ['.' for i in range(len(inputImage[0]))]
    inputImage.insert(0, darkRow)
    input.append(darkRow)

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
        positions['a'] = '.'
        positions['b'] = '.'
        positions['c'] = '.'
    elif r == len(grid) - 1:
        positions['f'] = '.'
        positions['g'] = '.'
        positions['h'] = '.'
    if c == 0:
        positions['a'] = '.'
        positions['d'] = '.'
        positions['f'] = '.'
    elif c == len(grid[r]) - 1:
        positions['c'] = '.'
        positions['e'] = '.'
        positions['h'] = '.'

    return positions

def getBinary(inputImage, r, c):
    neighbors = getNeighbors(inputImage, r, c)
    binary = ''
    for n in neighbors:
        if neighbors[n] == '.':
            pixel = '.'
        else:
            i, j = neighbors[n][0], neighbors[n][1]
            pixel = inputImage[i][j]
        if pixel == '.':    binary += '0'
        else:               binary += '1'
    return binary

def getNewPixel(enhanceAlg, binary):
    decimal = int(binary, 2)
    newPixel = enhanceAlg[decimal]
    return newPixel

def enhanceImage(enhanceAlg, inputImage):
    newImage = []
    i = 0
    while i < len(inputImage):
        newRow = []
        j = 0
        while j < len(inputImage[i]):
            binary = getBinary(inputImage, i, j)
            newPixel = getNewPixel(enhanceAlg, binary)
            newRow.append(newPixel)
            j += 1
        newImage.append(newRow)
        i += 1
    return newImage

def enhance(enhanceAlg, inputImage, times):
    for r in inputImage:
        print(''.join(r))
    print()
    if times == 0:  return inputImage
    else:           enhance(enhanceAlg, enhanceImage(enhanceAlg, inputImage), times - 1)

def countLit(inputImage):
    count = 0
    for r in inputImage:
        for c in r:
            if c == '#':    count += 1

    return count

if __name__ == '__main__':
    enhanceAlg, inputImage = parseInput()
    newImage = enhance(enhanceAlg, inputImage, 2)
    for r in newImage:
        print(''.join(r))
    lit = countLit(newImage)
    print(lit)


