#
# Goal: Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
# then multiply them together. What is the power consumption of the submarine?
# (Be sure to represent your answer in decimal, not binary.)
#
# gamma/epsilon rate: Each bit in the gamma/epsilon rate can be determined by finding the most common
# bit (or least common bit for the epsilon rate) in the corresponding position of all numbers in the
# diagnostic report.

def parseInput():
    f = open("input.txt", "r")
    lines = f.readlines()
    return lines

#
# getCounts updates an array to keep track of the number of 1s seen in each
# position of each line with the last element of the array corresponding to
# the total number of lines.
#   gamma = [number of 1s in position 0,
#            number of 1s in position 1,
#            ...                       ,
#            number of 1s in position k,
#            number of lines read]
#
def getCounts(lines):

    gamma = [0] * (len(lines[0]) - 1) # must have -1 because of /n
    gamma.append(len(lines))
    for line in lines:
        i = 0
        while i < len(line):
            bit = line[i]
            if bit == "1":
                gamma[i] += 1
            i += 1
    return gamma

#
# getGamma loops though the array, if the count at an index is greater or equal to
# the total number of lines / 2 then a 1 is appended to gamma and a 0 is appened to
# epsilon.
#
def getGamma(gamma):
    g = ""
    e = ""
    i = 0
    while i < len(gamma) - 1:
        count = gamma[i]
        if count >= gamma[-1]/2:
            g += "1"
            e += "0"
        else:
            g += "0"
            e += "1"
        i += 1
    return int(g, 2), int(e, 2) # convert to binary


def main():
    lines = parseInput()
    gamma = getCounts(lines)
    g, e =  getGamma(gamma)
    return g, e, g * e
