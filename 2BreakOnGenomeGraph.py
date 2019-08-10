import re

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


with open('test.txt', 'r+') as f:
    graph = f.readline().rstrip()
    sp = re.split('[()]', graph)[1:-1]

    colored_edges = [tuple(int(x) for x in sp[i].split(', ')) for i in range(0, len(sp), 2)]


    coords1 = f.readline().rstrip().split(', ')
    coords = [int(x) for x in coords1]
    new_edges = two_break_on_genome_graph(colored_edges, coords)
    print(new_edges)