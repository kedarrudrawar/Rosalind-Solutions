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


with open('rosalind_ba3g.txt', 'r+') as file:
    split_lines = [line.rstrip().split(' -> ') for line in file]
    adj_list = {split_lines[i][0]: list(split_lines[i][1].split(',')) for i in range(len(split_lines))}

    path = findEulerianPath(adj_list)
    print('->'.join(path))