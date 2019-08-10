def chromosomeToCycle(chromosome):
    nodes = [0] * (2 * len(chromosome))
    for j in range(1, len(chromosome) + 1):
        i = int(chromosome[j-1])
        if i > 0:
            nodes[2*j - 1 - 1] = 2*i - 1
            nodes[2*j - 1] = 2*i
        else:
            nodes[2*j - 1 - 1] = -2*i
            nodes[2*j - 1] = -2*i - 1

    return nodes

with open('test.txt', 'r+') as f:
    permline = f.readline().rstrip()[1:-1]
    perm = permline.split()
    nodes = chromosomeToCycle(perm)

    print('(' + ' '.join([str(x) for x in nodes]) + ')')
