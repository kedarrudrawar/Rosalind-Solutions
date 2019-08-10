class PrefixTrieNode:

    nucleotideDict = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
    index_ntDict = {0: 'A', 1: 'C', 2: 'T', 3: 'G'}

    def __init__(self, nodeNumber, base=None, pattern=None):
        self.nodeNumber = nodeNumber
        self.nodes = [None]*4
        self.base = base
        self.pattern = pattern

    # GETTERS

    def getVal(self):
        return self.nodeNumber

    def getBase(self):
        return self.base

    def getNext(self, base):
        return self.nodes[self.indexBase(base)]

    def getNodes(self):
        return self.nodes

    def getPattern(self):
        return self.pattern

    def indexBase(self, base):
        if base in self.nucleotideDict:
            return self.nucleotideDict[base]
        return -1

    def isLeaf(self):
        for node in self.nodes:
            if node:
                return False
        return True

    def hasBase(self, base):
        if self.nodes[self.indexBase(base)]:
            return True
        return False

    def addNextNode(self, base, nodeNumber, pattern):
        self.nodes[self.indexBase(base)] = PrefixTrieNode(nodeNumber, base, pattern)



    def printTrie(self):
        stack = [(self, node) for node in self.getNodes() if node]

        while stack:
            currPair = stack.pop()
            prev = currPair[0]
            curr = currPair[1]
            print(str(prev.getVal()) + '->' + str(curr.getVal()) + ':' + curr.getBase())

            prev = curr
            for node in curr.getNodes():
                if node:
                    stack.append((prev, node))


def trieConstruction(patterns):
    rootNode = PrefixTrieNode(0)

    currNodeVal = 0
    for pattern in patterns:
        currNode = rootNode
        for i in range(len(pattern)):
            base = pattern[i]
            if currNode.hasBase(base):
                currNode = currNode.getNext(base)
            else:
                currNodeVal += 1
                currNode.addNextNode(base, currNodeVal, pattern[:i + 1])
                currNode = currNode.getNext(base)

    return rootNode


def prefixTrieMatching(text, trieRoot):
    # print('text : ', text)
    i = 0
    currNode = trieRoot
    while i < len(text):
        currSym = text[i]
        if currNode.hasBase(currSym):
            currNode = currNode.getNext(currSym)
            i += 1
        elif currNode.isLeaf():
            return currNode.getPattern()
        else:
            return None

    if currNode.isLeaf():
        return currNode.getPattern()

    return None


def trieMatching(text, trieRoot):
    indices = []
    for i in range(len(text)):
        curr = text[i:]
        if prefixTrieMatching(curr, trieRoot):
            indices.append(i)

    return indices



if __name__ == '__main__':
    # with open('test62.txt') as f:
    # with open('extra62.txt') as f:
    with open('Datasets/rosalind_ba9b.txt') as f:
        text = f.readline().rstrip()
        patterns = [line.rstrip() for line in f.readlines()]

    rootNode = trieConstruction(patterns)
    indices = trieMatching(text, rootNode)
    print(' '.join([str(x) for x in indices]))



