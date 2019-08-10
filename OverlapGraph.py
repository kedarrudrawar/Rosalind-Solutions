def prefix(pattern):
    return pattern[:-1]


def suffix(pattern):
    return pattern[1:]


def overlapGraph(patterns):
    suffix_dict = {}
    adj_dict = {}

    for pattern in patterns:
        if suffix(pattern) in suffix_dict:
            continue
        else:
            suffix_dict[suffix(pattern)] = pattern

    for pattern in patterns:
        if prefix(pattern) in suffix_dict:
            start_pat = suffix_dict[prefix(pattern)]
            if start_pat in adj_dict:
                adj_dict[start_pat] += pattern
            else:
                adj_dict[start_pat] = [pattern]
        else:
            continue

    return adj_dict

with open('rosalind_ba3c.txt', 'r+') as file:
    patterns = [line.rstrip() for line in file]
    adj_list = overlapGraph(patterns)
    for elem in adj_list:
        for item in adj_list[elem]:
            print(elem + ' -> ' + item)