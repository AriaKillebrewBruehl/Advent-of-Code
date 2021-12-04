#
# Goal: Calculate the horizontal position and depth you would have after
# following the planned course. What do you get if you multiply your
# final horizontal position by your final depth?
#
# Commands:
#    forward X increases the horizontal position by X units.
#    down X increases the depth by X units.
#    up X decreases the depth by X units.
#

def getPosition():
    f = open("input.txt", "r")

    commands = f.readlines()

    x = 0
    d = 0
    for command in commands:
        direction = command.split()[0]
        amount = command.split()[1]
        if direction == "forward":
            x += int(amount)
        elif direction == "up":
            d -= int(amount)
        else:
            d += int(amount)

    return x, d, x*d