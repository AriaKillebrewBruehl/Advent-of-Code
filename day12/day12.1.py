def parseInput():
    f = open('testInput.txt', 'r')
    connections = {}
    for line in f.readlines():
        enter, exit = line.strip().split('-')
        connections[enter] = exit
    return connections

def findPaths(connections):
    numPaths = 0
    for option in connections['start']:
        numPaths += 1
        current = option



if __name__ == '__main__':
    connections = parseInput()
    print(connections)