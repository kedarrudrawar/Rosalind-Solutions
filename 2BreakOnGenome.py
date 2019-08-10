import re
import math

def findEdge(num, edges):
    for edge in edges:
        if num in edge:
            return edge


def nodeToCycleInd(nodeNum):
    return int(math.ceil(nodeNum/2) - 1)


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

def two_break_on_genome_graph(colored_edges, coords):
    new_edges = []
    start1 = 0
    start2 = 0
    end1 = 0
    end2 = 0

    for edge in colored_edges:
        if edge[0] == coords[0]:
            start1 = coords[0]
            end1 = coords[2]
            continue
        elif edge[0] == coords[1]:
            start2 = coords[1]
            end2 = coords[3]
            continue
        elif edge[0] == coords[2]:
            start1 = coords[2]
            end1 = coords[0]
            continue
        elif edge[0] == coords[3]:
            start2 = coords[3]
            end2 = coords[1]
            continue
        else:
            new_edges.append((edge[0], edge[1]))

    new_edges.append((start1, end1))
    new_edges.append((start2, end2))

    return new_edges


def coloredEdges_poly(chroms):
    edges = []

    for chrom in chroms:
        nodes = chromosomeToCycle(chrom)
        nodes += [nodes[0]]
        for j in range(1, len(chrom) + 1):
            edges.append((nodes[2*j - 1], nodes[2*j]))

    edges_sorted = sorted(edges, key=lambda tup: tup[0])

    str_edges_sorted = [str(elem) for elem in edges_sorted]

    # print(', '.join(str_edges_sorted))
    return edges_sorted


def findCycles_single_chrom(coloredEdges, max_val):
    cycle_ind_array = [i for i in range(max_val // 2)]
    for edge in coloredEdges:
        start, end = edge[0], edge[1]
        start_ind = nodeToCycleInd(start)
        end_ind = nodeToCycleInd(end)

        orig_start = cycle_ind_array[start_ind]
        orig_end = cycle_ind_array[end_ind]

        cycle_ind_array[start_ind] = min(cycle_ind_array[start_ind], cycle_ind_array[end_ind])
        cycle_ind_array[end_ind] = min(cycle_ind_array[start_ind], cycle_ind_array[end_ind])

        for i, elem in enumerate(cycle_ind_array):
            if elem == orig_start or elem == orig_end:
                cycle_ind_array[i] = cycle_ind_array[start_ind]

    # print(cycle_ind_array)

    return cycle_ind_array


def edgesToChromosomes(coloredEdges):
    max_val = max(max(coloredEdges, key=lambda tup:max(tup)))

    cycle_ind_array = findCycles_single_chrom(coloredEdges, max_val)
    cycle_ind_distinct = list(set(cycle_ind_array))

    cycle_count = len(cycle_ind_distinct)

    chromosomes = [[] for _ in range(cycle_count)]

    # iterate by 2, starting with 1
    for i in range(1, max_val + 1, 2):
        edge = findEdge(i, coloredEdges)
        cycle_ind = cycle_ind_distinct.index(cycle_ind_array[nodeToCycleInd(i)])

        if i == edge[1]:
            chromosomes[cycle_ind].append(i)
            chromosomes[cycle_ind].append(i + 1)
        else:
            chromosomes[cycle_ind].append(i + 1)
            chromosomes[cycle_ind].append(i)

    return chromosomes


def numToStr(num):
    if num < 0:
        return str(num)
    else:
        return '+' + str(num)


def cycleToChromosome(nodes):
    chrom = [0] * int(len(nodes) / 2)
    for j in range(1, len(chrom) + 1):
        if nodes[2*j - 1 - 1] < nodes[2*j - 1]:
            chrom[j - 1] = numToStr(nodes[2*j - 1] // 2)
        else:
            chrom[j - 1] = numToStr(-(nodes[2*j - 1 - 1 ] // 2))

    return chrom


def graphToGenome(coloredEdges):
    cycles = edgesToChromosomes(coloredEdges)
    chromosomes = []
    for cycle in cycles:
        chromosomes.append(cycleToChromosome(cycle))

    return chromosomes


def two_break_on_genome(colored_edges, coords):
    new_edges = two_break_on_genome_graph(colored_edges, coords)
    return graphToGenome(new_edges)


with open('rosalind_ba6k.txt', 'r+') as f:
    genome = f.readline().rstrip()
    sp = re.split('[()]', genome)
    chroms = [chrom.split() for chrom in sp if chrom]

    coords1 = f.readline().rstrip().split(', ')
    coords = [int(x) for x in coords1]
    colored_graph = coloredEdges_poly(chroms)


    new_edges = two_break_on_genome(colored_graph, coords)
    for graph in new_edges:
        print(' (' + ' '.join(graph) + ')', end='')
    # print(new_edges)