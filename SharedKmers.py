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


def reverseComplement(str):
    nucleotide_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ''
    rev = str[::-1]
    for elem in rev:
        complement += nucleotide_dict[elem]

    return complement


def generateFrequencyArray(text, k):
    freqArr = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        currText = text[i:i + k]
        ind = patternToNum(currText)
        freqArr[ind] += 1
    return freqArr


def findKmer(str, kmer):
    indices = []
    for i in range(len(str) - len(kmer) + 1):
        if str[i : i + len(kmer)] == kmer:
            indices.append(i)

    return indices


def findSharedKmerPositions(k, s1, s2):
    freqArr = generateFrequencyArray(s2, k)
    coordinates = []
    for i in range(len(s1) - k + 1):
        kmer = s1[i: i + k]
        reverseKmer = reverseComplement(kmer)
        if freqArr[patternToNum(kmer)] > 0 or freqArr[patternToNum(reverseKmer)] > 0:
            indicesKmer = findKmer(s2, kmer)
            indicesRevKmer = findKmer(s2, reverseKmer)
            for ind in indicesKmer:
                coordinates.append(tuple([i, ind]))
            for ind in indicesRevKmer:
                coordinates.append(tuple([i, ind]))

    return coordinates


with open('rosalind_ba6e.txt') as file:
    k = int(file.readline())
    s1 = file.readline().rstrip()
    s2 = file.readline().rstrip()
    coords = findSharedKmerPositions(k, s1, s2)
    for c in coords:
        print(c)
