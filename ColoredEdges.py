import re

def chromosomeToCycle(chromosome):
    # print(chromosome)
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

def addEdge(dict, start, end):
    if start in dict:
        dict[start] += end
    else:
        dict[start] = [end]
    return dict


def coloredEdges_poly(chroms):
    edges = []
    for chrom in chroms:
        nodes = chromosomeToCycle(chrom)
        # print(nodes)
        nodes += [nodes[0]]
        # print(nodes)
        for j in range(1, len(chrom) + 1):
            edges.append((nodes[2*j - 1], nodes[2*j]))

    edges_sorted = sorted(edges, key=lambda tup: tup[0])

    str_edges_sorted = [str(elem) for elem in edges_sorted]

    print(', '.join(str_edges_sorted))
    return edges_sorted



def coloredEdges_linear(chroms):
    undir_graph = {}
    for chrom in chroms:
        nodes = chromosomeToCycle(chrom)
        nodes += [nodes[0]]
        for j in range(1, len(chrom) + 1):
            undir_graph = addEdge(undir_graph, nodes[2*j - 1], nodes[2*j])

    edges = []
    for elem in undir_graph:
        for end in undir_graph[elem]:
            edges.append(str((elem, end)))

    print(', '. join(edges))

    return undir_graph


with open('test.txt', 'r+') as f:
    genome = f.readline().rstrip()
    sp = re.split('[()]', genome)
    chroms = [chrom.split() for chrom in sp if chrom]
    colored_graph = coloredEdges_poly(chroms)
