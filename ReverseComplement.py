def reverseComplement(str):
    nucleotide_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement = ''
    rev = str[::-1]
    for elem in rev:
        complement += nucleotide_dict[elem]

    return complement


with open('rosalind_ba1c.txt', 'r+') as f:
    line = f.readline()
    for i in range(len(line) - 1, -1, -1):
        if line[i] == 'A':
            complement += 'T'
        elif line[i] == 'G':
            complement += 'C'
        elif line[i] == 'C':
            complement += 'G'
        elif line[i] == 'T':
            complement += 'A'
print(complement)