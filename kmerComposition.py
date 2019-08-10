def generateKmers(k, text):
    return [text[i: i + k] for i in range(len(text) - k + 1)]

with open('rosalind_ba3a.txt', 'r+') as file:
    k = int(file.readline())
    text = file.readline().rstrip()
    kmers = generateKmers(k, text)

with open('output.txt', 'w+') as file:
    file.write(kmers[0])
    for i in range(1, len(kmers)):
        file.write('\n' + kmers[i])