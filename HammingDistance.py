def hammingDistance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return dist


if __name__ == '__main__':
    with open('rosalind_ba1g.txt', 'r+') as f:
        s1 = f.readline().rstrip()
        s2 = f.readline().rstrip()

        dist = hammingDistance(s1, s2)

        print(dist)
