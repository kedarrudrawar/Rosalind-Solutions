def symbolToNum(sym):
    return 'ACGT'.index(sym)

def patternToNum(pattern):
    if len(pattern) == 0:
        return 0
    if len(pattern) == 1:
        return symbolToNum(pattern)

    return 4 * patternToNum(pattern[:-1]) + symbolToNum(pattern[-1])

if __name__ == '__main__':
    print(patternToNum('AA'))
    # with open('rosalind_ba1l.txt', 'r+') as f:
        # text = f.readline().rstrip()
        # print(patternToNum(text))
