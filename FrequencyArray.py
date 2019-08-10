
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


def generateFrequencyArray(text, k):
    freqArr = [0] * (4 ** k)
    for i in range(len(text) - k):
        currText = text[i:i + k]
        ind = patternToNum(currText)
        freqArr[ind] += 1
    return freqArr

if __name__ == '__main__':
    with open('rosalind_ba1k.txt', 'r+') as f:
        text = f.readline()
        k = int(f.readline())
        arr = generateFrequencyArray(text, k)

    print(' '.join(str(x) for x in arr))