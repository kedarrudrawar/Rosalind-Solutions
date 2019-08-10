with open('rosalind_ba1d.txt', 'r+') as f:
    pattern = f.readline().rstrip()
    text = f.readline().rstrip()

    indList = []

    for i in range(len(text) - len(pattern)):
        if text[i:len(pattern) + i] == pattern:
            indList.append(str(i))

print(' '.join(indList))