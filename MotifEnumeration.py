nucleotides = ['A', 'C', 'T', 'G']

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

def motifEnumeration(dna, k, d):
    patterns = []
    firstString = dna[0]
    for i in range(len(firstString) - k + 1):
        kmer = firstString[i: i + k]
        neighborhood = neighbors(kmer, d)
        for neighbor in neighborhood:
            contains = True
            for str in dna[1:]:
                contains2 = False
                neighborhood2 = neighbors(neighbor, d)
                for n in neighborhood2:
                    if n in str:
                        contains2 = True
                        continue
                if not contains2:
                    contains = False
                    break
            if contains:
                patterns.append(neighbor)
    patterns = list(set(patterns))
    return patterns

with open('rosalind_ba2a.txt', 'r+') as file:
    values = file.readline().split(' ')
    k, d = int(values[0]), int(values[1])
    dna = []
    for line in file:
        dna.append(line.rstrip())
    print(' '.join(motifEnumeration(dna, k, d)))
