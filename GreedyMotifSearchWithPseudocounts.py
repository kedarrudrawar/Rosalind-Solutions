ntDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def mostProbableKmer(text, k, profileMat):
    freqKmer = ''
    maxProb = 0.0
    for i in range(len(text) - k + 1):
        kmer = text[i: i + k]
        prob = 1
        for ind, base in enumerate(kmer):
            prob *= profileMat[ntDict[base]][ind]
        if prob > maxProb:
            maxProb = prob
            freqKmer = kmer

    return freqKmer


def initializeMotifMatrix(dna, k, t):
    motif_matrix = [[''] * k for _ in range(t)]
    for i, strand in enumerate(dna):
        for j, base in enumerate(dna[i][:k]):
            motif_matrix[i][j] = base

    return motif_matrix

def generateProfileMatrixWithPseudocounts(motifs_mat):
    kmerCount = len(motifs_mat)*4 + len(motifs_mat)
    profile = [[0] * k for _ in range(4)]
    for l in motifs_mat:
        for i, base in enumerate(l):
            profile[ntDict[base]][i] += 1
    for i in range(len(profile)):
        for j in range(len(l)):
            profile[i][j] += 1
            profile[i][j] /= kmerCount

    return profile


def updateProfileMatrixWithPseudocounts(profile_mat, kmer, kmerCount):
    for x in range(len(profile_mat)):
        for y in range(len(profile_mat[x])):
            profile_mat[x][y] *= kmerCount - 1

    for i, base in enumerate(kmer):
        profile_mat[ntDict[base]][i] += 1

    for x in range(len(profile_mat)):
        for y in range(len(profile_mat[x])):
            profile_mat[x][y] /= (kmerCount + 4)

    return profile_mat


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


def greedyMotifSearch(dna, k, t):
    best_motifs = initializeMotifMatrix(dna, k, t)
    kmerCount = 0
    firstString = dna[0]

    for i in range(len(firstString) - k + 1):
        currKmer = firstString[i: i + k]
        motifs = [list(currKmer)]

        for j in range(1, t):
            kmerCount += 4
            profile = generateProfileMatrixWithPseudocounts(motifs)
            currKmer = mostProbableKmer(dna[j], k, profile)
            motifs.append(list(currKmer))
        if score(best_motifs) > score(motifs):
            best_motifs = motifs


    for l in best_motifs:
        print(''.join(l))


with open('rosalind_ba2e.txt', 'r+') as file:
    values = file.readline().split(' ')
    k, t = int(values[0]), int(values[1])
    dna = [line.rstrip() for line in file]

    greedyMotifSearch(dna, k, t)
