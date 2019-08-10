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

with open('rosalind_ba3e.txt', 'r+') as file:
    patterns = [line.rstrip() for line in file]
    adj_list = deBruijnGraph(patterns)
    for elem in adj_list:
        print(elem + ' -> ' + ','.join(adj_list[elem]))

