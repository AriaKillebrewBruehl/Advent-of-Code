def getIncreases():
    f = open("input.txt", "r")

    depths = f.readlines() # create list of depths
    increases = 0
    # the total number of increases is computed by comparing the
    # previous distance to the current distance
    i = 1
    while i < len(depths):
        previous = depths[i - 1]
        current = depths[i]
        if (int(previous) - int(current)) < 0:
            increases += 1
        i += 1

    return increases

