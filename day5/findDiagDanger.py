def parseInput():
    f = open('input.txt', 'r')
    pairs = []
    maxX = 0
    maxY = 0
    for line in f.readlines():
        pair0, pair1 = line.strip().split(' -> ')
        x0, y0 = pair0.split(',')
        x1, y1 = pair1.split(',')
        x0, y0, x1, y1 =  int(x0), int(y0), int(x1), int(y1)
        # if difX == difY then line is at a 45 degree angle
        difX = abs(x0 - x1)
        difY = abs(y0 - y1)
        if x0 == x1 or y0 == y1 or difX == difY:
            if maxX < max(x0, x1):  maxX = max(x0, x1)
            if maxY < max(y0, y1):  maxY = max(y0, y1)
            pairs.append([[x0, y0], [x1, y1]])
    grid = [[0 for i in range(maxX + 1)] for j in range(maxY + 1)]
    return pairs, grid

def mark(positions, grid):
    for pos in positions:
        # same y-coordinate, so mark all x-cooridantes in the range
        if pos[0][1] == pos[1][1]:
            start, end  = min(pos[0][0], pos[1][0]), max(pos[0][0], pos[1][0])
            row = grid[pos[0][1]]
            for i in range (start, end + 1):
                row[i] += 1
        # same x-coordinate, so mark all y-coordinates in the range
        elif pos[0][0] == pos[1][0]:
            col = pos[0][0]
            start, end = min(pos[0][1], pos[1][1]), max(pos[0][1], pos[1][1])
            for i in range(start, end + 1):
                if i >= len(grid):
                    print("i:", i)
                if col >= len(grid[0]):
                    print("col:", col)
                grid[i][col] += 1
        # diagonal line
        else:
            # find left-most x position
            if pos[0][0] < pos[1][0]:
                startX, startY = pos[0][0], pos[0][1]
                endX, endY = pos[1][0], pos[1][1]
            else:
                startX, startY = pos[1][0], pos[1][1]
                endX, endY = pos[0][0], pos[0][1]
                # if the startY is larger than the endY we are looping through the y positions in reverse
            if startY > endY :
                yPos = [i for i in range(startY, endY - 1, -1)]
            else:
                yPos = [i for i in range(startY, endY + 1)]
            i = startX
            while i <= endX:
                for y in yPos:
                    grid[y][i] += 1
                    i += 1
    return grid

def findDanger(grid):
    overlaps = 0
    for row in grid:
        for col in row:
            if col >= 2:
                overlaps += 1
    return overlaps

if __name__ == "__main__":
    pairs, grid = parseInput()
    marked = mark(pairs, grid)
    print(findDanger(marked))






