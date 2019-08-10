import re

def findCycleCount(coloredEdges, max_val):
    cycles = findCycles_double_chrom(coloredEdges, max_val)
    # print(cycles)
    return len(list(set(cycles)))


def findCycles_double_chrom(coloredEdges, max_val):
    cycle_ind_array = [i for i in range(max_val)]
    for edge in coloredEdges:
        start, end = edge[0] - 1, edge[1] - 1
        orig_start = cycle_ind_array[start]
        orig_end = cycle_ind_array[end]
        cycle_ind_array[start] = min(cycle_ind_array[start], cycle_ind_array[end])
        cycle_ind_array[end] = min(cycle_ind_array[start], cycle_ind_array[end])
        for i, elem in enumerate(cycle_ind_array):
            if elem == orig_start or elem == orig_end:
                cycle_ind_array[i] = cycle_ind_array[start]

    return cycle_ind_array


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


def coloredEdges_poly(chroms):
    edges = []
    for chrom in chroms:
        nodes = chromosomeToCycle(chrom)
        nodes += [nodes[0]]
        for j in range(1, len(chrom) + 1):
            edges.append((nodes[2*j - 1], nodes[2*j]))

    edges_sorted = sorted(edges, key=lambda tup: tup[0])

    # str_edges_sorted = [str(elem) for elem in edges_sorted]

    return edges_sorted


with open('rosalind_ba6c.txt', 'r+') as file:
    genomeA = file.readline().rstrip()
    genomeB = file.readline().rstrip()

    spA = re.split('[()]', genomeA)
    spB = re.split('[()]', genomeB)

    chromsA = [chrom.split() for chrom in spA if chrom]
    colored_edges_A = coloredEdges_poly(chromsA)
    chromsB = [chrom.split() for chrom in spB if chrom]
    colored_edges_B = coloredEdges_poly(chromsB)

    total_edges = colored_edges_A + colored_edges_B
    max_val = max(max(total_edges, key=lambda tup:max(tup)))


    synt_blocks = 0
    for elem in chromsA:
        curr = int(max(elem, key=lambda str:int(str)))
        if curr > synt_blocks:
            synt_blocks = curr
    for elem in chromsB:
        curr = int(max(elem, key=lambda str: int(str)))
        if curr > synt_blocks:
            synt_blocks = curr

    print(synt_blocks)

    cycle_count = findCycleCount(total_edges, max_val)

    print(synt_blocks - cycle_count)
