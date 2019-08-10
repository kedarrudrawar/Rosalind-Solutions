import sys
import copy

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
                reverse_list[neighbor] = [elem]

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


def initializeDistanceDict(weighted_adj_list):
    distanceDict = {}
    for elem in weighted_adj_list:
        distanceDict[elem] = [-sys.maxsize, '']
        for pair in weighted_adj_list[elem]:
            distanceDict[pair[0]] = [-sys.maxsize, '']

    return distanceDict


def getEdgeWeight(prev, curr, weighted_adj_list):
    for pair in weighted_adj_list[prev]:
        if pair[0] == curr:
            return pair[1]

    return None


def findLongestPathDAG(source, sink, weighted_adj_list):
    distance_dict = initializeDistanceDict(weighted_adj_list)
    distance_dict[source] = [0, '']

    adj_list = {}
    for elem in weighted_adj_list:
        adj_list[elem] = [pair[0] for pair in weighted_adj_list[elem]]

    reverse_list = findReverseGraph(adj_list)

    top_order = findTopologicalOrderingDAG(copy.deepcopy(adj_list))

    for curr in top_order:
        if curr not in reverse_list:
            continue

        maxPrevDist = distance_dict[curr][0]
        maxPrevNode = ''

        prevNodes = reverse_list[curr]
        for prevNode in prevNodes:
            currPrevDist = distance_dict[prevNode][0] + getEdgeWeight(prevNode, curr, weighted_adj_list)
            if currPrevDist > maxPrevDist:
                maxPrevDist = currPrevDist
                maxPrevNode = prevNode

        distance_dict[curr] = [maxPrevDist, maxPrevNode]

    final_path = []
    curr = sink
    while curr:
        final_path.append(curr)
        curr = distance_dict[curr][1]

    print(distance_dict[sink][0])

    return final_path[::-1]


with open('rosalind_ba5d.txt', 'r+') as f:
    source = f.readline().rstrip()
    sink = f.readline().rstrip()
    split_lines = [line.rstrip().split('->') for line in f]

    adj_list = {}
    for line in split_lines:
        if line[0] in adj_list:
            pair = line[1].split(':')
            pair[1] = int(pair[1])
            adj_list[line[0]].append(pair)
        else:
            pair = line[1].split(':')
            pair[1] = int(pair[1])
            adj_list[line[0]] = [pair]


    path = findLongestPathDAG(source, sink, adj_list)

    print('->'.join(path))