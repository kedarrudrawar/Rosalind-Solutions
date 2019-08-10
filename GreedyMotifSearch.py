ntDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def mostProbableKmer(text, k, profileMat):
    freqKmer = ''
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


def initializeMotifMatrix(dna, k, t):
    motif_matrix = [[''] * k for _ in range(t)]
    for i, strand in enumerate(dna):
        for j, base in enumerate(dna[i][:k]):
            motif_matrix[i][j] = base

    return motif_matrix


def updateProfileMatrix(profile_mat, kmer, j):
    for x in range(len(profile_mat)):
        for y in range(len(profile_mat[x])):
            profile_mat[x][y] *= j - 1

    for i, base in enumerate(kmer):
        profile_mat[ntDict[base]][i] += 1

    for x in range(len(profile_mat)):
        for y in range(len(profile_mat[x])):
            profile_mat[x][y] /= j

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
    profile = [[0] * k for _ in range(4)]
    firstString = dna[0]

    for i in range(len(firstString) - k + 1):
        kmer = firstString[i: i + k]
        motifs = [list(kmer)]

        profile = updateProfileMatrix(profile, kmer, 1)
        for j in range(1,t):
            currKmer = mostProbableKmer(dna[j], k, profile)
            if len(currKmer) == 0:
                currKmer = dna[j][:k]
            motifs.append(list(currKmer))
            profile = updateProfileMatrix(profile, currKmer, j+1)
        if score(best_motifs) >= score(motifs):
            best_motifs = motifs

    for l in best_motifs:
        print(''.join(l))

with open('rosalind_ba2d.txt', 'r+') as file:
    values = file.readline().split(' ')
    k, t = int(values[0]), int(values[1])
    dna = [line.rstrip() for line in file]

    greedyMotifSearch(dna, k, t)