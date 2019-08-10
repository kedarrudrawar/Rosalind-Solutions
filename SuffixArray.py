from HW.Week7.SuffixTreeConstruction import constructSuffixTree

def suffixArrayHelper(node, suffixArr, suffix):
    if node.isLeaf():
        suffixArr.append(suffix + str(node))
        return suffixArr
    for child in node.getRealNodes():
        suffixArrayHelper(child, suffixArr, suffix + str(node))

    return suffixArr


def suffixArrayWithTree(text):
    rootNode = constructSuffixTree(text)
    suffixArr = suffixArrayHelper(rootNode, [], '')
    return suffixArr


def suffixArray(text):
    pairs = []
    for i in range(len(text)):
        pairs.append((i, text[i:]))
    pairs = sorted(pairs, key=lambda tup: tup[1])
    suffixArr = [str(pair[0]) for pair in pairs]
    return suffixArr

if __name__ == '__main__':
    # with open('test67.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9g.txt', 'r+') as f:
        text = f.readline().rstrip()
    suffixArr = suffixArray(text)
    print(', '.join(suffixArr))