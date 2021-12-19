def parseInput():
    f = open('input.txt', 'r')
    hPos = [int(i) for i in f.read().split(',')]
    return hPos

def mergeSort(list):
    if len(list) > 1:
        s = len(list)//2
        l, r = list[:s], list[s:]
        mergeSort(l)
        mergeSort(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                list[k] = l[i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            list[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            list[k] = r[j]
            j += 1
            k += 1

def findMedian(hPos):
    mergeSort(hPos)
    return hPos[len(hPos)//2]

def findFuel(hPos):
    target = findMedian(hPos)
    total = 0
    for p in hPos:
        total += abs(p - target)
    return total


if __name__ == "__main__":
    hPos = parseInput()
    print(findFuel(hPos))
