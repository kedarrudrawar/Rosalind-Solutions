count = [0]*4
with open('rosalind_dna.txt', 'r+') as f:
    line = f.readline()
    for letter in line:
        if letter == 'A':
            ind = 0
        elif letter == 'C':
            ind = 1
        elif letter == 'G':
            ind = 2
        elif letter == 'T':
            ind = 3
        else:
            break
        count[ind] += 1
retStr = ' '.join(str(e) for e in count)
print(retStr)
