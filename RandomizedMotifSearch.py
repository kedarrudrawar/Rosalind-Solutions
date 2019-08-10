import random
import sys

ntDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def generateRandomMotifs(dna, k, t):
    motifs = []
    for strand in dna:
        startInd = random.randrange(len(dna[0]) - k)
        motifs.append(list(strand[startInd: startInd + k]))

    return motifs


def mostProbableKmer(text, k, profileMat):
    freqKmer = text[:k]
    maxProb = 0.0
    for i in range(len(text) - k + 1):
        kmer = text[i: i+k]
        prob = 1
        for ind, base in enumerate(kmer):
            prob *= profileMat[ntDict[base]][ind]
        if prob > maxProb:
            maxProb = prob
            freqKmer = kmer
    return freqKmer




def generateProfileMatrixWithPseudocounts(motifs_mat):
    kmerCount = 4 + len(motifs_mat) #len(motifs_mat)*4 + len(motifs_mat)
    profile = [[0] * k for _ in range(4)]

    for l in motifs_mat:
        for i, base in enumerate(l):
            profile[ntDict[base]][i] += 1

    for i in range(len(profile)):
        for j in range(len(l)):
            profile[i][j] += 1
            profile[i][j] /= kmerCount

    return profile


def score(motifs):
    k = len(motifs[0])
    score = 0

    for j in range(k):
        freqArray = [0] * 4
        for i in range(len(motifs)):
            base = motifs[i][j]
            freqArray[ntDict[base]] += 1
        score += (sum(freqArray) - max(freqArray))

    return score


def randomizedMotifSearch(dna, k, t):
    best_motifs = generateRandomMotifs(dna, k, t)
    while True:
        profile = generateProfileMatrixWithPseudocounts(best_motifs)
        print(profile)

        motifs = []
        for elem in dna:
            motifs.append(list(mostProbableKmer(elem, k, profile)))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


with open('rosalind_ba2f.txt', 'r+') as file:
    values = file.readline().split()
    k, t = int(values[0]), int(values[1])
    dna = [line.rstrip() for line in file.readlines()]

    currBestScore = sys.maxsize
    best_motifs = None
    for i in range(1000):
        motifs = randomizedMotifSearch(dna, k, t)
        if score(motifs) < currBestScore:
            currBestScore = score(motifs)
            best_motifs = motifs


    print(best_motifs)
    for elem in best_motifs:
        print(''.join(elem))


