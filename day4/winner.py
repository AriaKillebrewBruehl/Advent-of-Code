def parseInput():
    f = open('input.txt', 'r')
    nums = f.read().split()
    order = nums[0].split(',')
    nums = nums[1:] # remove first element
    boards = []
    i = 0
    while i < len(nums):
        board = []
        for j in range(5):
            row = []
            for k in range(5):
                row.append(nums[i])
                i += 1
            board.append(row)
        boards.append(board)
    return order, boards

def winRow(row):
    sum = 0
    for col in row:
        sum += int(col)
    if sum == -5:   return True
    else:           return False

def winCol(board, i):
    sum = 0
    for row in board:
        sum += int(row[i])
    if sum == -5:   return True
    else:           return False

def hasWin(board):
    for row in board:
        if winRow(row):
            return True
    for i in range(len(board)):
        if winCol(board, i):
            return True
    return False

def calculateRemaining(board):
    sum = 0
    for row in board:
        for col in row:
            if col != '-1':
                sum += int(col)
    return sum

def drawNumbers(order, boards):
    for num in order:
        for board in boards:
            for row in board:
                if num in row:
                    row[row.index(num)] = '-1'
                if hasWin(board):
                    sum = calculateRemaining(board)
                    return sum, num
        if int(num) == 24:
            print(boards)
    print("No winner found")
    return 0, 0

if __name__ == "__main__":
    order, boards = parseInput()
    for b in boards:
        print(b)
        print()
    sum, num = drawNumbers(order, boards)
    if sum != 0 and num != 0:
        print("Winning number:", num)
        print("Total remaining:", sum)
        print("Total score:", int(num) * int(sum))
