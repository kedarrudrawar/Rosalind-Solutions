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

def generateKmers(k, text):
    return [text[i: i + k] for i in range(len(text) - k + 1)]

with open('dbg.txt', 'r+') as file:
    k = int(file.readline())
    text = file.readline().rstrip()
    patterns = generateKmers(k, text)
    adj_list = deBruijnGraph(patterns)

with open('output.txt', 'w') as file:
    for elem in adj_list:
        file.write(elem + ' -> ' + ','.join(adj_list[elem]) + '\n')
