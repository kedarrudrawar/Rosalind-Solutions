retString = ""
with open('rosalind_rna.txt', 'r') as f:
    line = f.readline()
    for base in line:
        if base == 'T':
            retString += 'U'
        elif base == 'A' or base == 'C' or base == 'G':
            retString += base
        else:
            break
print(retString)
