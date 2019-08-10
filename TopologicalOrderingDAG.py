def deleteEdge(adj_list, start, end):
    if len(adj_list[start]) == 1:
        del adj_list[start]
    else:
        ind = adj_list[start].index(end)
        del adj_list[start][ind]

    return adj_list


def findReverseGraph(adj_list):
    reverse_list = {}
    for elem in adj_list:
        for neighbor in adj_list[elem]:
            if neighbor in reverse_list:
                reverse_list[neighbor].append(elem)
            else:
                reverse_list [neighbor] = [elem]

    return reverse_list


def findTopologicalOrderingDAG(adj_list):
    reverse_list = findReverseGraph(adj_list)

    candidates = []

    final_path = []

    for elem in adj_list:
        if elem not in reverse_list:
            candidates.append(elem)

    while candidates:
        candidate = candidates.pop()
        final_path.append(candidate)

        while candidate in adj_list:
            elem = candidate
            edge = adj_list[elem][0]

            adj_list = deleteEdge(adj_list, elem, edge)
            reverse_list = deleteEdge(reverse_list, edge, elem)

            if edge not in reverse_list:
                candidates.append(edge)

    if not adj_list:
        return final_path

    return None







# with open('rosalind_ba5n.txt', 'r+') as f:
#     split_lines = [line.rstrip().split(' -> ') for line in f]
#     adj_list = {split_lines[i][0]: list(split_lines[i][1].split(',')) for i in range(len(split_lines))}
#     path = findTopologicalOrderingDAG(adj_list)
#     print(', '.join(path))