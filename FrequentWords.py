with open('rosalind_ba1b.txt', 'r+') as f:
    text = f.readline()
    k = int(f.readline())
    freqDict = {}
    max_freq = 1

    for i in range(len(text) - k):
        if text[i:i+k] in freqDict:
            freqDict[text[i:i+k]] += 1
            if freqDict[text[i:i+k]] > max_freq:
                max_freq = freqDict[text[i:i+k]]
        else:
            freqDict[text[i:i+k]] = 1

    kmerList = []

    for elem in freqDict:
        if freqDict[elem] == max_freq:
            kmerList.append(elem)

print(' '.join(kmerList))
