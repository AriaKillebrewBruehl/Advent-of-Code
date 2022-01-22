def parseInput():
    f = open('input.txt', 'r')
    lines = f.readlines()
    pos0 = lines[0].strip().split(' ')[-1]
    pos1 = lines[1].strip().split(' ')[-1]
    player0 = [int(pos0), 0]
    player1 = [int(pos1), 0]
    return [[player0, player1]]

def splits(universe, turn):
    newUniverses = []
    foundWinner = False
    for i in range(1, 4):
        pos = universe[turn][0] + i % 10
        if pos == 0:    pos = 10
        score = universe[turn][1] + i
        if not turn:    newUniverse = [[pos, score], universe[not turn]]
        else:           newUniverse = [universe[not turn], [pos, score]]
        newUniverses += [newUniverse]
        if score >= 21: foundWinner = True
    return newUniverses, foundWinner

def gameStep(universes, turn, newUniverses):
    for i in range(len(universes) - newUniverses, len(universes)):
        universe = universes[i]
        unis, foundWinner = splits(universe, turn)
        universes += [unis]
        if foundWinner: return 0, True
        else:           return len(unis), False

def playGame(universes):
    turn = 0
    newUnis, foundWinner = gameStep(universes, turn, 1)
    while not foundWinner:
        newUnis, foundWinner = gameStep(universes, not turn, newUnis)



def loosingScore(player0, player1):
    count = playGame(player0, player1, 0) * 3
    if player0[1] >= 1000:  return count * player1[1]
    else:                   return count * player0[1]

if __name__ == '__main__':
    universe = parseInput()
    print(loosingScore(player0, player1))


