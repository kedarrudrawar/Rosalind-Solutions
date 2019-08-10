import copy


def findReverseGraph(adj_list):
    reverse_list = {}
    for elem in adj_list:
        for neighbor in adj_list[elem]:
            if neighbor in reverse_list:
                reverse_list[neighbor].append(elem)
            else:
                reverse_list [neighbor] = [elem]

    return reverse_list


def isSinglyBalanced(node, forward_list, rev_list):
    if node not in forward_list or node not in rev_list:
        return False

    if node in rev_list:
        if len(forward_list[node]) == len(rev_list[node]) == 1:
            return True

    return False


def findIsolatedCycles(adj_list):
    if not adj_list:
        return []

    all_paths = []

    start = list(adj_list.keys())[0]
    curr_path = [start]

    curr = adj_list[start][0]
    del adj_list[start]

    while adj_list:
        if curr != start:
            curr_path.append(curr)
            next = adj_list[curr][0]
            del adj_list[curr]
            curr = next
        else:
            curr_path.append(start)
            all_paths.append(curr_path)
            start = list(adj_list.keys())[0]
            curr_path = [start]
            curr = adj_list[start][0]
            del adj_list[start]

    curr_path.append(start)
    all_paths.append(curr_path)

    return all_paths


def findMaximalNonBranchingPaths(forward_list):
    copy_forward_list = copy.deepcopy(forward_list)

    rev_list = findReverseGraph(adj_list)
    all_paths = []
    for node in forward_list:
        if not isSinglyBalanced(node, forward_list, rev_list):
            for neighbor in forward_list[node]:
                stack = [neighbor]
                curr_path = [node]
                curr = node
                while stack:
                    prev = curr
                    curr = stack.pop()
                    if isSinglyBalanced(curr, forward_list, rev_list):
                        curr_path.append(curr)
                        stack.append(forward_list[curr][0])
                    else:
                        curr_path.append(curr)
                        all_paths.append(curr_path)
                        curr_path = [node]

                    ind = copy_forward_list[prev].index(curr)
                    if len(copy_forward_list[prev]) > 1:
                        del copy_forward_list[prev][ind]
                    else:
                        del copy_forward_list[prev]

    cycles = findIsolatedCycles(copy_forward_list)

    all_paths.extend(cycles)

    return all_paths


def prefix(pattern):
    return pattern[:-1]


def suffix(pattern):
    return pattern[1:]


def deBruijnGraph(patterns):
    adj_dict = {}
    for pattern in patterns:
        if prefix(pattern) in adj_dict:
            adj_dict[prefix(pattern)].append(suffix(pattern))
        else:
            adj_dict[prefix(pattern)] = [suffix(pattern)]
    return adj_dict


def reconstructString(path):
    start = path[0]
    for i in range(1, len(path)):
        start += path[i][-1]

    return start


def generateContigsFromPaths(paths):

    return [reconstructString(path) for path in paths]


with open('rosalind_ba3k.txt', 'r+') as file:
    patterns = [line.rstrip() for line in file]
    adj_list = deBruijnGraph(patterns)
    paths = findMaximalNonBranchingPaths(adj_list)
    contigs = generateContigsFromPaths(paths)
    print(' '.join(contigs))