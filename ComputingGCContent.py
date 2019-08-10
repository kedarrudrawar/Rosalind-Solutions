max_id = ''
max_content = 0
with open('rosalind_gc.txt', 'r+') as f:
    line = f.readline()
    currLine = ''
    curr_id = line[1:]
    for line in f:
        if line[0] == '>':
            count = 0
            for base in currLine:
                if base == 'C' or base == 'G':
                   count += 1
            if (count / len(currLine)) > max_content:
                max_content = count / len(currLine)
                max_id = curr_id

            currLine = ''
            curr_id = line[1:]
        else:
            currLine += line.strip()

count = 0
for base in currLine:
    if base == 'C' or base == 'G':
       count += 1
if (count / len(currLine)) > max_content:
    max_content = count / len(currLine)
    max_id = curr_id


print(max_id + '\n' + str(max_content * 100) + '%')
