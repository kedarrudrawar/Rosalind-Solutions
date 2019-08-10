def hammingDistance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist

def approxPatternMatching(pattern, text, d):
    indices = []
    for i in range(len(text) - len(pattern)):
        currText = text[i: i + len(pattern)]
        if hammingDistance(currText, pattern) <= d:
            indices.append(str(i))
    return indices

if __name__ == '__main__':
    with open('rosalind_ba1h.txt', 'r+') as f:
        pattern = f.readline().rstrip()
        text = f.readline().rstrip()
        d = int(f.readline())

        indices = approxPatternMatching(pattern, text, d)

    print(' '.join(indices))
