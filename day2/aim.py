#
# Goal: Calculate the horizontal position and depth you would have after
# following the planned course. What do you get if you multiply your final
# horizontal position by your final depth?
#
# Commands:
#   down X increases your aim by X units.
#   up X decreases your aim by X units.
# forward X does two things:
#       It increases your horizontal position by X units.
#       It increases your depth by your aim multiplied by X.
#

def getPosition():
    f = open("input.txt", "r")

    commands = f.readlines()

    x = 0
    d = 0
    a = 0
    for command in commands:
        direction = command.split()[0]
        amount = int(command.split()[1])
        if direction == "forward":
            x += amount
            d += (a * amount)
        elif direction == "up":
            a -= amount
        else:
            a += amount

    return x, d, x*d