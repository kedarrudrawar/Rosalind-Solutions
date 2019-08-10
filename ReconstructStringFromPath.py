def reconstructString(path):
    start = path[0]
    for i in range(1, len(path)):
        start += path[i][-1]

    return start

with open('rosalind_ba3b.txt', 'r+') as f:
    path = [line.rstrip() for line in f]
    print(reconstructString(path))