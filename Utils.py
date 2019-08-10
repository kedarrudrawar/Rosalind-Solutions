nucleotides = ['A', 'C', 'G', 'T']

def reverseComplement(text):
    complement = ''
    for i in range(len(text) - 1, -1, -1):
        if text[i] == 'A':
            complement += 'T'
        elif text[i] == 'G':
            complement += 'C'
        elif text[i] == 'C':
            complement += 'G'
        elif text[i] == 'T':
            complement += 'A'
    return complement

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

def hammingDistance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist



def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffixNeighbors = neighbors(pattern[1:], d)
    for neighbor in suffixNeighbors:
        if hammingDistance(neighbor, pattern[1:]) < d:
            for nucleotide in nucleotides:
                neighborhood.append(nucleotide + neighbor)
        else:
            neighborhood.append(pattern[0] + neighbor)
    return neighborhood