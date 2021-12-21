def parseInput():
    f = open('tinyInput.txt', 'r')
    connections = {}
    for line in f.readlines():
        enter, exit = f.split('-')
        connections[enter] = exit
    return connections
