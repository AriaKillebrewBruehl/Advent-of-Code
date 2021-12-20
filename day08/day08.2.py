def parseInput():
    f = open('input.txt', 'r')
    seq = []
    for l in f.readlines():
        patterns, outputs = l.split(" | ")
        seq += [[patterns.strip().split(" "), outputs.strip().split(" ")]]
    return seq
def mapUnique(seq):
    uniqueDict = {}
    for s in seq:
        for o in s[0]:
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                uniqueDict[len(o)] = o
        for o in s[1]:
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                uniqueDict[len(o)] = o
    return uniqueDict

def findMapping(seq):
    uniqueDict = mapUnique(seq)
    #  aaaa
    # b    c
    # b    c
    #  dddd
    # e    f
    # e    f
    #  gggg
    mapping = {'a' : None, 'b' : None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
    if 1 in uniqueDict and 4 in uniqueDict:
        mapping['c']
def uniqueOutputs(seq):
    total = 0
    for s in seq:
        for o in s[1]:
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                total += 1
    return total

if __name__ == "__main__":
    seq = parseInput()
    print(uniqueOutputs(seq))

