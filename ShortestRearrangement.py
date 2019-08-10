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


def nodeToCycleInd(nodeNum):
    return int(math.ceil(nodeNum/2) - 1)


def findEdge(num, edges):
    for edge in edges:
        if num in edge:
            return edge

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


def edgesToChromosomes_OLD(coloredEdges):
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

    str_edges_sorted = [str(elem) for elem in edges_sorted]

    # print(', '.join(str_edges_sorted))
    return edges_sorted

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

    new_edges.append((coords[0], coords[2]))
    new_edges.append((coords[1], coords[3]))

    return new_edges

def cycleToChromosome(nodes):
    chrom = [''] * int(len(nodes) / 2)
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



def hasNonTrivialCycles(edges):
    b, ind = findNonTrivialCycles(edges)
    return b


# returns the number of the set that represents the cycle
def findNonTrivialCycles(edges):
    max_val = max(max(edges, key=lambda tup:max(tup)))

    cycle_ind_array = findCycles_double_chrom(edges, max_val)

    cycle_dict = {}

    set = None

    for elem in cycle_ind_array:
        if elem in cycle_dict:
            cycle_dict[elem] += 1
            if cycle_dict[elem] > 2:
                set = elem
        else:
            cycle_dict[elem] = 0

    return set, cycle_ind_array


def findEnd(edges, start):
    for i, edge in enumerate(edges):
        if start == edge[0]:
            return edge[1], i
        elif start == edge[1]:
            return edge[0], i


def printGraph(P):
    for graph in P:
        print('(' + ' '.join(graph) + ')', end='')
    print()


def two_break_sorting(P, Q):
    printGraph(P)

    redEdges = coloredEdges_poly(P)
    blueEdges = coloredEdges_poly(Q)

    total_edges = redEdges + blueEdges
    coords = [0]*4

    while hasNonTrivialCycles(total_edges) is not None:
        set, cycle_ind_array = findNonTrivialCycles(total_edges)
        original_red = list(redEdges)
        for edge in blueEdges:
            if cycle_ind_array[edge[1] - 1] == set:
                coords[0], coords[2] = edge[0], edge[1]
                coords[1], ind1 = findEnd(redEdges, coords[0])
                coords[3], ind2 = findEnd(redEdges, coords[2])

                # Account for deletion of first edge here
                if ind2 > ind1:
                    ind2 -= 1

                del redEdges[ind1]
                del redEdges[ind2]

                if ind2 >= ind1:
                    ind2 += 1

                redEdges.insert(ind1, (coords[0], coords[2]))
                redEdges.insert(ind2, (coords[1], coords[3]))

                break

        total_edges = redEdges + blueEdges

        P = two_break_on_genome(original_red, coords)
        printGraph(P)


with open('rosalind_ba6d.txt', 'r+') as f:
    genomeP = f.readline().rstrip()
    spP = re.split('[()]', genomeP)
    chromsP = [chrom.split() for chrom in spP if chrom]

    genomeQ = f.readline().rstrip()
    spQ = re.split('[()]', genomeQ)
    chromsQ = [chrom.split() for chrom in spQ if chrom]

    two_break_sorting(chromsP, chromsQ)