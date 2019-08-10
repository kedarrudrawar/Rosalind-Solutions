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

def findUnbalancedNode(adj_list):
    count_dict = {}
    for elem in adj_list:
        neighbors = adj_list[elem]
        if elem in count_dict:
            count_dict[elem][0] += len(neighbors)
        else:
            count_dict[elem] = [len(neighbors),0]

        for n in neighbors:
            if n in count_dict:
                count_dict[n][1] += 1
            else:
                count_dict[n] = [0,1]

    for elem in count_dict:
        if count_dict[elem][0] > count_dict[elem][1]:
            return elem

    return -1

def findEulerianPath(adj_list):
    startNode = findUnbalancedNode(adj_list)

    if startNode == -1:
        startNode = list(adj_list.keys())[0]

    stack = [startNode]
    currNode = startNode

    final_path = []

    while stack:
        if currNode in adj_list:
            stack.append(currNode)
            nextNode = adj_list[currNode][-1]

            if len(adj_list[currNode]) == 1:
                del adj_list[currNode]
            else:
                del adj_list[currNode][-1]

            currNode = nextNode

        else:
            final_path.append(currNode)
            currNode = stack.pop()

    return final_path[::-1]


def reconstructString(path):
    start = path[0]
    for i in range(1, len(path)):
        start += path[i][-1]

    return start


def reconstructStringFromKmers(patterns):
    adj_list = deBruijnGraph(patterns)

    path = findEulerianPath(adj_list)

    final_string = reconstructString(path)

    return final_string



def reconstructStringFromGappedPatterns(gapped_patterns, k, d):
    firstPatterns = [pat[0] for pat in gapped_patterns]
    secondPatterns = [pat[1] for pat in gapped_patterns]

    prefix = reconstructString(firstPatterns)
    suffix = reconstructString(secondPatterns)

    for i in range(len(prefix) - k - d):
        if prefix[i + k + d] != suffix[i]:
            return None

    return prefix + suffix[-(k + d):]





with open('rosalind_ba3l.txt', 'r+') as f:
    values = f.readline().split()
    k, d = int(values[0]), int(values[1])
    paired_patterns = [line.rstrip().split('|') for line in f]
    final_string = reconstructStringFromGappedPatterns(paired_patterns, k, d)

    if final_string:
        print(final_string)
