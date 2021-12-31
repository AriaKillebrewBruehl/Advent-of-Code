from typing import Counter


def parseInput():
    f = open('input.txt', 'r')
    lines = f.readlines()
    pos1 = lines[0].strip().split(' ')[-1]
    pos2 = lines[1].strip().split(' ')[-1]
    return pos1, pos2

count = 0
def deterministicDie():
    global count
    count += 1
    return count % 100

if __name__ == '__main__':
    pos1, pos2 = parseInput()
    print(pos1, pos2)
