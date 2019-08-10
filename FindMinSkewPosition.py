def findMinimumSkewPosition(genome):
    skewArr = [0]*len(genome)
    minSkew = 0
    for i in range(1, len(genome)):
        if genome[i-1] == 'C':
            skewArr[i] = skewArr[i-1] - 1
        elif genome[i-1] == 'G':
            skewArr[i] = skewArr[i-1] + 1
        else:
            skewArr[i] = skewArr[i-1]
        if skewArr[i] < minSkew:
            minSkew = skewArr[i]

    minSkewIndices = []
    for i, skew in enumerate(skewArr):
        if skew == minSkew:
            minSkewIndices.append(str(i))

    return minSkewIndices


if __name__ == '__main__':
    with open('rosalind_ba1f.txt', 'r+') as f:
        genome = f.readline().rstrip()
        skewArr = findMinimumSkewPosition(genome)
        print(' '.join(skewArr))
