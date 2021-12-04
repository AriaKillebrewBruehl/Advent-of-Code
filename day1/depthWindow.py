def getIncrease():
    f = open("input.txt", "r")
    depths = f.readlines()
    windowSize = 3

    increases = 0
    i = windowSize

    while i < (len(depths)):
        sum1 = depths[i - windowSize]
        sum2 = depths[i]
        if int(sum1) < int(sum2):
            increases += 1
        i += 1
    return increases