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

with open('rosalind_ba3f.txt', 'r+') as file:
    split_lines = [line.rstrip().split(' -> ') for line in file]
    adj_list = {split_lines[i][0]: list(split_lines[i][1].split(',')) for i in range(len(split_lines))}

    path = findEulerianCycle(adj_list)
    print('->'.join(path))