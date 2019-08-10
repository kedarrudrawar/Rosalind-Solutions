def countBreakpoints(P):
    bpCount = 0
    for i in range(len(P) - 1):
        if int(P[i + 1]) - int(P[i]) != 1:
            bpCount += 1

    return bpCount


with open('rosalind_ba6b.txt', 'r+') as f:
    permline = f.readline().rstrip()[1:-1]
    perm = permline.split()
    perm = ['0'] + perm + ['+' + str(len(perm) + 1)]
    count = countBreakpoints(perm)

    print(count)