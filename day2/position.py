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