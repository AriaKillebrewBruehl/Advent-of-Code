def parseInput():
    f = open('input.txt', 'r')
    nums = f.read().split()
    order = nums[0].split(',') # create list of the numbers to be called
    nums = nums[1:] # remove first element
    # create list of boards where each board is represented as a list
    # where each entry of said list is a list that represents a row
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


# see if a board has a winning row by computing the sum of each
# row, if any sum is -5, then all the entries have been marked off
def winRow(board):
    for row in board:
        sum = 0
        for col in row:
            sum += int(col)
        if sum == -5:   return True
    return False

# see if a board has a winning column by computing the sum of each
# colum, if any sum is -5, then all the entries have been marked off
def winCol(board):
    for i in range(5):
        sum = 0
        for row in board:
            sum += int(row[i])
        if sum == -5:   return True
    return False


def hasWin(board):
    return winRow(board) or winCol(board)

# sum each entry of of the board, unless said entry is '-1'
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
                    # update number in board to indicate that it has been found
                    row[row.index(num)] = '-1'
                if hasWin(board):
                    sum = calculateRemaining(board)
                    return sum, num
    print("No winner found")
    return 0, 0

if __name__ == "__main__":
    order, boards = parseInput()
    sum, num = drawNumbers(order, boards)
    if sum != 0 and num != 0:
        print("Winning number:", num)
        print("Total remaining:", sum)
        print("Total score:", int(num) * int(sum))
