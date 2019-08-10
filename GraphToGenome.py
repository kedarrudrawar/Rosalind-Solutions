import re
import math

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


def findEdge(num, edges):
    for edge in edges:
        if num in edge:
            return edge


def nodeToCycleInd(nodeNum):
    return int(math.ceil(nodeNum/2) - 1)


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


def flipNode(num):
    flip = num - 1 if num % 2 == 0 else num + 1
    return flip


def nodeExists(start, edges):
    for elem in edges:
        if elem[0] == start or elem[1] == start:
            return True
    return False


def findNextEdge(start, edges):
    for i, elem in enumerate(edges):
        if elem[0] == start or elem[1] == start:
            return elem, i


def edgesToChromosomes(coloredEdges):
    chromosomes = []
    currChrom = []
    edges_copy = coloredEdges.copy()
    startEdge = edges_copy[0]
    currChrom += [startEdge[1]]

    start = flipNode(startEdge[1])

    while edges_copy:
        if nodeExists(start, edges_copy):
            startEdge, edge_ind = findNextEdge(start, edges_copy)
            del edges_copy[edge_ind]
            if start == startEdge[0]:
                currChrom += startEdge
                start = flipNode(startEdge[1])
            else:
                currChrom += startEdge[::-1]
                start = flipNode(startEdge[0])
        else:
            chromosomes.append(currChrom)
            currChrom = []
            startEdge = edges_copy[0]
            currChrom += [startEdge[1]]

            start = flipNode(startEdge[1])
    chromosomes.append(currChrom)

    return chromosomes


def numToStr(num):
    if num < 0:
        return str(num)
    else:
        return '+' + str(num)


def cycleToChromosome(nodes):
    chrom = ['  '] * int(len(nodes) / 2)
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


with open('test.txt', 'r+') as f:
    graph = f.readline().rstrip()
    sp = re.split('[()]', graph)[1:-1]

    colored_edges = [tuple(int(x) for x in sp[i].split(', ')) for i in range(0, len(sp), 2)]

    genome = graphToGenome(colored_edges)
    for graph in genome:
        print('(' + ' '.join(graph) + ')', end='')