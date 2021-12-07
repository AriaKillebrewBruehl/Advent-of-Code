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
        if x0 == x1 or y0 == y1:
            if maxX < max(x0, x1):
                maxX = max(x0, x1)
            if maxY < max(y0, y1):
                maxY = max(y0, y1)
            pairs.append([[x0, y0], [x1, y1]])
    grid = [[0 for i in range(maxX + 1)] for j in range(maxY + 1)]
    return pairs, grid

def mark(positions, grid):
    for pos in positions:
        # same y-coordinate, so mark all x-cooridantes in the range
        if pos[0][1] == pos[1][1]:
            start = min(pos[0][0], pos[1][0])
            end = max(pos[0][0], pos[1][0])
            row = grid[pos[0][1]]
            for i in range (start, end + 1):
                row[i] += 1
        # same x-coordinate, so mark all y-coordinates in the range
        else:
            col = int(pos[0][0])
            start = min(pos[0][1], pos[1][1])
            end = max(pos[0][1], pos[1][1])
            for i in range(start, end + 1):
                grid[i][col] += 1
    return grid

def findDanger(grid):
    overlaps = 0
    for row in grid:
        for col in row:
            if col > 1:
                overlaps += 1
    return overlaps

if __name__ == "__main__":
    pairs, grid = parseInput()
    marked = mark(pairs, grid)
    print(findDanger(marked))






