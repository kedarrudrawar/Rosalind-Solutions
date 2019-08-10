def numToStr(num):
    if num < 0:
        return str(num)
    else:
        return '+' + str(num)


def cycleToChromosome(nodes):
    chrom = [''] * int(len(nodes) / 2)
    for j in range(1, len(chrom) + 1):
        if nodes[2*j - 1 - 1] < nodes[2*j - 1]:
            chrom[j - 1] = numToStr(nodes[2*j - 1] // 2)
        else:
            chrom[j - 1] = numToStr(-(nodes[2*j - 1 - 1 ] // 2))

    return chrom


with open('testC2C', 'r+') as f:
    permline = f.readline().rstrip()[1:-1]
    nodes = [int(x) for x in permline.split()]
    print(nodes)
    chrom = cycleToChromosome(nodes)

    print('(' + ' '.join(chrom) + ')')