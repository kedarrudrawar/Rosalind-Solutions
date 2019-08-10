retString = ''
with open('rosalind_revc.txt', 'r+') as f:
    line = f.readline()
    for i in range(len(line) - 1, -1, -1):
        if line[i] == 'A':
            retString += 'T'
        elif line[i] == 'G':
            retString += 'C'
        elif line[i] == 'C':
            retString += 'G'
        elif line[i] == 'T':
            retString += 'A'
print(retString)


