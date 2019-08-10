def numToSymbol(num):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'C'
    elif num == 2:
        return 'G'
    elif num == 3:
        return 'T'

def numToPattern(i, k):
    if k == 1:
        return numToSymbol(i)
    prefixInd = i // 4
    rem = i % 4
    sym = numToSymbol(rem)
    prefix = numToPattern(prefixInd, k - 1)
    return prefix + sym

def hammingDistance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist

def distance(pattern, text):
    minDist = len(pattern)
    for i in range(len(text) - len(pattern) + 1):
        h = hammingDistance(pattern, text[i: i + len(pattern)])
        if h < minDist:
            minDist = h
    return minDist


def medianString(k, dna):
    import sys
    minSum = sys.maxsize
    minPattern = ''
    for i in range(4**k):
        dist = 0
        pattern = numToPattern(i, k)
        for string in dna:
            dist += distance(pattern, string)
        if dist <= minSum:
            minSum = dist
            minPattern = pattern

    return minPattern

with open('rosalind_ba2b.txt', 'r+') as file:
    k = int(file.readline())
    dna = []
    for line in file:
        dna.append(line.rstrip())
    print(medianString(k, dna))