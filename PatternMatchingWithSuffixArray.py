def suffixArray(text):
    pairs = []
    for i in range(len(text)):
        pairs.append((i, text[i:]))
    pairs = sorted(pairs, key=lambda tup: tup[1])
    suffixArr = [pair[0] for pair in pairs]
    return suffixArr


def greaterThan(pattern, substr):
    if substr[:len(pattern)] < pattern:
        return True
    return False


def equalPatterns(pattern, substr):
    if substr[:len(pattern)] == pattern:
        return True
    return False


def findIndices(pattern, text):
    indices = []
    for i in range(len(text)):
        if pattern == text[i: i + len(pattern)]:
            indices.append(i)
    return indices


def patternMatchingWithSuffixArray(text, pattern, suffixArr):
    minIndex, midIndex, maxIndex = 0, 0, len(text) - 1

    while minIndex <= maxIndex:
        midIndex = (minIndex + maxIndex) // 2

        if greaterThan(pattern, text[suffixArr[midIndex]:]):
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1

    if equalPatterns(pattern, text[suffixArr[minIndex]:]):
        first = minIndex
    else:
        return None

    minIndex = first
    maxIndex = len(text) - 1
    while minIndex <= maxIndex:
        midIndex = (minIndex + maxIndex) // 2
        if equalPatterns(pattern, text[suffixArr[midIndex]:]):
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1
    last = maxIndex

    return first,last


if __name__ == '__main__':
    with open('Datasets/rosalind_ba9h.txt', 'r+') as f:
    # with open('text68.txt', 'r+') as f:
    # with open('extra62.txt', 'r+') as f:
        text = f.readline().rstrip()
        patterns = [line.rstrip() for line in f.readlines()]

    suffixArr = suffixArray(text)
    startPosArr = []

    # inds = findIndices(patterns[0], text)

    pairs = []

    for pat in patterns:
        pair = patternMatchingWithSuffixArray(text, pat, suffixArr)
        pairs.append(pair)
        if pair:
            for i in range(pair[0], pair[1] + 1):
                startPosArr.append(str(suffixArr[i]))
    print(' '.join(sorted(startPosArr, key=lambda str:int(str))))
