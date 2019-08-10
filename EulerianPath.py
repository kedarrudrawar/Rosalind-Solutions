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

def findEulerianPath(adj_list):
    edgeCountDict = {}
    finalPath = []

    for elem in adj_list:
        if elem in edgeCountDict:
            edgeCountDict[elem][0] += 1
        else:
            edgeCountDict[elem] = [1,0]


        for i, item in enumerate(adj_list[elem]):
            if i > 0:
                edgeCountDict[elem][0] += 1
            if item in edgeCountDict:
                edgeCountDict[item][1] += 1
            else:
                edgeCountDict[item] = [0,1]


    startNode = ''

    for node in edgeCountDict:
        if edgeCountDict[node][0] > edgeCountDict[node][1]:
            startNode = node
            break

    if startNode == '':
        return findEulerianCycle(adj_list)


    prev_dict = {}

    stack = [startNode]

    finalPath = []
    circuit = []

    while stack and adj_list:
        currNode = stack.pop()
        neighbors = []
        if currNode in adj_list:
            # print(currNode)
            finalPath.append(currNode)
            neighbors = adj_list[currNode]
            for n in neighbors:
                stack.append(n)

            if len(finalPath) > 1:
                prev = finalPath[-2]
                if len(adj_list[prev]) > 1:
                    del adj_list[prev][-1]
                else:
                    del adj_list[prev]
        else:
            circuit.append(currNode)
            if len(finalPath) > 0:
                prev = finalPath[-1]
                if len(adj_list[prev]) > 1:
                    del adj_list[prev][-1]
                else:
                    del adj_list[prev]

                for i in range(len(finalPath) - 1, -1, -1):
                    if finalPath[i] not in adj_list:
                        circuit.append(finalPath[i])
                        del finalPath[i]
                    else:
                        break


    circuit += finalPath[::-1]
    finalPath = circuit[::-1]




    return finalPath



with open('rosalind_ba3g.txt', 'r+') as file:
    split_lines = [line.rstrip().split(' -> ') for line in file]
    adj_list = {split_lines[i][0]: list(split_lines[i][1].split(',')) for i in range(len(split_lines))}


    path = findEulerianPath(adj_list)
    print('->'.join(path))