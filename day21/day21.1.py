from typing import Counter


def parseInput():
    f = open('input.txt', 'r')
    lines = f.readlines()
    pos1 = lines[0].strip().split(' ')[-1]
    pos2 = lines[1].strip().split(' ')[-1]
    player1 = [pos1, 0]
    player2 = [pos2, 0]
    return player1, player2

roll = 0
def deterministicDie():
    global roll
    roll += 1
    return roll % 100

def rollThree():
    r1, r2, r3 = deterministicDie(), deterministicDie(), deterministicDie()
    return r1 + r2 + r3

def playGame(player1, player2):
    if player1[1] >= 1000 or player2[1] >= 1000:
        return 0
    else:
if __name__ == '__main__':
    player1, player2 = parseInput()
    print(pos1, pos2)
