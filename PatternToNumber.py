def symbolToNum(sym):
    if sym == 'A':
        return 0
    elif sym == 'C':
        return 1
    elif sym == 'G':
        return 2
    elif sym == 'T':
        return 3

def patternToNum(pattern):
    if len(pattern) == 0:
        return 0
    if len(pattern) == 1:
        return symbolToNum(pattern)

    return 4 * patternToNum(pattern[:-1]) + symbolToNum(pattern[-1])

if __name__ == '__main__':
    with open('rosalind_ba1l.txt', 'r+') as f:
        text = f.readline().rstrip()
        print(patternToNum(text))