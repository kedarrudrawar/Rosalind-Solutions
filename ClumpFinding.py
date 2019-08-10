def numToSymbol(num):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'C'
    elif num == 2:
        return 'G'
    elif num == 3:
        return 'T'


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


def numToPattern(i, k):
    if k == 1:
        return numToSymbol(i)
    prefixInd = i // 4
    rem = i % 4
    sym = numToSymbol(rem)
    prefix = numToPattern(prefixInd, k - 1)

    return prefix + sym


def computeFrequencies(text, k):
    freqArr = [0] * (4 ** k)
    for i in range(len(text) - k):
        currText = text[i:i + k]
        ind = patternToNum(currText)
        freqArr[ind] += 1
    return freqArr


with open('rosalind_ba1e.txt', 'r+') as f:
    text = f.readline()
    values = f.readline().split(' ')
    k = int(values[0])
    L = int(values[1])
    t = int(values[2])

    clumpBoolArr = [False] * (4 ** k)
    patternArr = []
    textCurr = text[:L]
    freqArr = computeFrequencies(textCurr, k)
    for ind, elem in enumerate(freqArr):
        if elem >= t:
            clumpBoolArr[ind] = True

    for i in range(1, len(text) - L):
        pattern = text[i - 1: i + k - 1]
        index = patternToNum(pattern)
        freqArr[index] -= 1

        pattern = text[i + L - k: i + L]
        index = patternToNum(pattern)
        freqArr[index] += 1
        if freqArr[index] >= t:
            clumpBoolArr[index] = True
    for i, elem in enumerate(clumpBoolArr):
        if elem:
            patternArr.append(numToPattern(i, k))

print(' '.join(patternArr))
