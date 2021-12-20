def parseInput():
    f = open('input.txt', 'r')
    lines = [l.strip() for l in f.readlines()]
    return lines

def findCorruption(lines):
    chunks = {'(' : ')',
             '[' : ']',
             '{' : '}',
             '<' : '>'
             }
    errors = {')' : 0,
             ']' : 0,
             '}' : 0,
             '>' : 0
             }
    for l in lines:
        stack = []
        for c in l:
            if c in chunks.keys():
                stack.append(c)
            elif c in chunks.values():
                if chunks[stack.pop()] != c:
                    errors[c] += 1
                    continue
    return errors

def totalCorruption(lines):
    errors = findCorruption(lines)
    total = 0
    for e in errors:
        if e == ')':   total += 3 * errors[e]
        elif e == ']': total += 57 * errors[e]
        elif e == '}': total += 1197 * errors[e]
        elif e == '>': total += 25137 * errors[e]
    return total

if __name__ == "__main__":
    lines = parseInput()
    print(totalCorruption(lines))
