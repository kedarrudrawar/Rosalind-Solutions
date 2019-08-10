ntDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

import random

def randomProbableKmer(text, k, prob_array):
    sumVal = float(sum(prob_array))
    rand = random.random()
    currSum = 0

    for ind, val in enumerate(prob_array):
        currSum += val
        if currSum/sumVal >= rand:
            return text[ind: ind + k]

def generateRandomMotifs(dna, k ,t):
    motifs = []
    for elem in dna:
        rand = random.randint(0, len(elem) - k)
        motifs.append(list(elem[rand : rand + k]))
    return motifs

def generateProbabilityArray(text, k, profile):
    freqArray = [0] * (len(text) - k + 1)
    for i in range(len(text) - k + 1):
        currProb = 1
        for ind, base in enumerate(text[i: i + k]):
            currProb *= profile[ntDict[base]][ind]
        freqArray[i] = currProb
    return freqArray


def generateProfileMatrixWithPseudocounts(motifs_mat):
    kmerCount = 4 + len(motifs_mat)
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


def gibbsSampler(dna, k, t, N):
    best_motifs = generateRandomMotifs(dna, k, t)
    motifs = best_motifs
    for i in range(N):
        rand = random.randint(0, len(motifs) - 1)
        new_motifs = motifs[:rand] + motifs[rand + 1:]
        profile = generateProfileMatrixWithPseudocounts(new_motifs)
        prob_array = generateProbabilityArray(dna[rand], k, profile)
        motifs[rand] = randomProbableKmer(dna[rand], k, prob_array)

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


with open('test.txt', 'r+') as file:
    values = file.readline().split()
    k, t, N = int(values[0]), int(values[1]), int(values[2])
    dna = [line.rstrip() for line in file]

    best_motifs = gibbsSampler(dna, k, t, N)
    best_score = score(best_motifs)
    for i in range(20):
        motifs = gibbsSampler(dna, k, t, N)
        if score(motifs) < best_score:
            best_motifs = motifs
            best_score = score(motifs)

    for elem in best_motifs:
        print(''.join(elem))


