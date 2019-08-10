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

def findEulerianCycle(adj_list):
    startNode = list(adj_list.keys())[0]
    currNode = startNode

    final_path = [startNode]

    while adj_list:
        if currNode in adj_list:
            final_path.append(adj_list[currNode][0])
            if len(adj_list[currNode]) == 1:
                del adj_list[currNode]
            else:
                del adj_list[currNode][0]

            currNode = final_path[-1]
        else:
            for i, elem in enumerate(final_path):
                if elem in adj_list:
                    new_path = final_path[i: -1] + final_path[:i + 1]
                    final_path = new_path
                    currNode = elem
                    break

    return final_path


def reconstructString(path):
    start = path[0]
    for i in range(1, len(path)):
        start += path[i][-1]

    return start


def reconstructStringFromKmers(patterns):
    adj_list = deBruijnGraph(patterns)

    path = findEulerianCycle(adj_list)

    final_string = reconstructString(path)

    return final_string

def numToBinary(num, k):
    s = bin(num)[2:]
    missing = k - len(s)
    s = '0' * missing + s
    return s

def kUniversalCircularString(k):
    patterns = []
    for i in range(2**k):
        patterns.append(numToBinary(i, k))

    return reconstructStringFromKmers(patterns)[:-(k-1)]

# with open('rosalind_ba3i.txt', 'r+') as f:
# k = int(f.readline())
k = 4
print(kUniversalCircularString(k))
# print(len(kUniversalCircularString(4)))
