def prefix(pattern):
    return pattern[:-1]


def suffix(pattern):
    return pattern[1:]


def deBruijnGraph_pairs(paired_patterns):
    adj_dict = {}
    for pair in paired_patterns:
        pat1 = pair[0]
        pat2 = pair[1]
        pre_pair = prefix(pat1) + ' ' + prefix(pat2)
        suf_pair = suffix(pat1) + ' ' + suffix(pat2)
        if pre_pair in adj_dict:
            adj_dict[pre_pair].append(suf_pair)
        else:
            adj_dict[pre_pair] = [suf_pair]
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

def reconstructString_pairs(d, path):
    start = path[0].split()[0]

    for i in range(1, len(path)):
        start += path[i].split()[0][-1]

    start += path[-d-2].split()[1]

    for i in range(d, -1, -1):
        start += path[-i-1].split()[1][-1]

    return start


def reconstructStringFromReadPairs(k, d, paired_patterns):
    adj_list = deBruijnGraph_pairs(paired_patterns)
    path = findEulerianPath(adj_list)
    final_string = reconstructString_pairs(d, path)

    return final_string



with open('rosalind_ba3j.txt', 'r+') as f:
    values = f.readline().split()
    k, d = int(values[0]), int(values[1])
    paired_patterns = [line.rstrip().split('|') for line in f]
    final_string = reconstructStringFromReadPairs(k, d, paired_patterns)
    print(final_string)
