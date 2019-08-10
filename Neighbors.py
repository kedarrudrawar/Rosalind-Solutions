nucleotides = ['A', 'C', 'G', 'T']

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

with open('rosalind_ba1n.txt', 'r+') as f:
    text = f.readline().rstrip()
    d = int(f.readline().rstrip())

    neighbors = neighbors(text, d)
    for elem in neighbors:
        print(elem)