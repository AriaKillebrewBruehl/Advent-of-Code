def getIncreases():
    f = open("input.txt", "r")

    depths = f.readlines() # create list of depths
    increases = 0
    previous = depths[0] # the first depth begins as the previous
    i = 1
    # the total number of increases is computed by comparing the
    # previous distance to the current distance
    while i < len(depths):
        current = depths[i]
        if (int(current) - int(previous)) < 0:
            increases += 1
        previous = current
        i += 1

    return increases

