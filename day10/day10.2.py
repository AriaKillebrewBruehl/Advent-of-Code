def parseInput():
    f = open('input.txt', 'r')
    lines = [l.strip() for l in f.readlines()]
    return lines

def filterIncomplete(lines):
    chunks = {'(' : ')',
             '[' : ']',
             '{' : '}',
             '<' : '>'
             }
    bad = []
    for l in lines:
        stack = []
        for c in l:
            if c in chunks.keys():
                stack.append(c)
            elif c in chunks.values():
                if chunks[stack.pop()] != c:
                    bad.append(l)
                    continue
        if len(stack) == 0:
            if l not in bad: bad.append(l)
    for b in bad:
        lines.remove(b)

def findPair(s):
    chunks = {'(' : ')',
              '[' : ']',
              '{' : '}',
              '<' : '>'
             }
    for c in chunks:
        if c == s:
            return chunks[c]

def autoComplete(lines):
    chunks = {'(' : ')',
              '[' : ']',
              '{' : '}',
              '<' : '>'}
    completions = []
    for l in lines:
        stack = []
        for c in l:
            if c in chunks.keys():      stack.append(c)
            elif c in chunks.values():  stack.pop()
        if len(stack) != 0:
            stack.reverse()
            remaining = ''
            for s in stack:
                remaining += findPair(s)
            completions.append(remaining)
    scores = calcScores(completions)
    return scores[len(scores)//2]

def calcScores(completions):
    scores = []
    table = {')' : 1,
             ']' : 2,
             '}' : 3,
             '>' : 4}
    for s in completions:
        total = 0
        for c in s:
            total *= 5
            total += table[c]
        scores.append(total)
    scores.sort()
    return scores


if __name__ == "__main__":
    lines = parseInput()
    filterIncomplete(lines)
    print(autoComplete(lines))


