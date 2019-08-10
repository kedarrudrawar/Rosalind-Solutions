nucleotideDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def mostProbableKmer(text, k, profileMat):
    freqKmer = text[:k]
    maxProb = 0.0
    for i in range(len(text) - k + 1):
        kmer = text[i: i+k]
        prob = 1
        for ind, base in enumerate(kmer):
            prob *= profileMat[nucleotideDict[base]][ind]
        if prob > maxProb:
            maxProb = prob
            freqKmer = kmer
    return freqKmer

with open('rosalind_ba2c.txt', 'r+') as file:
    text = file.readline().rstrip()
    k = int(file.readline())
    profile = []
    for line in file:
        profile.append([float(i) for i in line.rstrip().split(' ')])

    print(mostProbableKmer(text, k, profile))

