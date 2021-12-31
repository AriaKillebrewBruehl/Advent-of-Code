from typing import Counter


def parseInput():
    f = open('testInput.txt', 'r')
    lines = f.readlines()
    pos0 = lines[0].strip().split(' ')[-1]
    pos1 = lines[1].strip().split(' ')[-1]
    player0 = [int(pos0), 0]
    player1 = [int(pos1), 0]
    return player0, player1

roll = 0
def deterministicDie():
    global roll
    roll += 1
    return roll % 100

def rollThree():
    r1, r2, r3 = deterministicDie(), deterministicDie(), deterministicDie()
    return r1 + r2 + r3

def playGame(player0, player1, turn):
    if player0[1] >= 1000 or player1[1] >= 1000:
        return 0
    else:
        move = rollThree()
        if not turn:
            player0[0] = (player0[0] + move) % 11
            player0[1] += player0[0]
        else:
            player1[0] = (player1[0] + move) % 11
            player1[1] += player1[0]
        print(player0, player1)
        return playGame(player0, player1, not turn) + 1

if __name__ == '__main__':
    player0, player1 = parseInput()
    print(player0, player1)
    print(playGame(player0, player1, 0))
