
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

with open('rosalind_ba2h.txt', 'r+') as file:
    pattern = file.readline().rstrip()
    dna = file.readline().rstrip().split()
    sumDist = 0
    for str in dna:
        sumDist += distance(pattern, str)
    print(sumDist)