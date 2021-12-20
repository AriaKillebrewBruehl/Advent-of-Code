def parseInput():
    f = open('input.txt', 'r')
    seq = []
    for l in f.readlines():
        patterns, outputs = l.split(" | ")
        seq += [[patterns.strip().split(" "), outputs.strip().split(" ")]]
    return seq

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

