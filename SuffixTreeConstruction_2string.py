class TrieNode:

    nucleotideDict = {'A': 0, 'C': 1, 'T': 2, 'G': 3, '$':4, '#': 5}
    index_ntDict = {0: 'A', 1: 'C', 2: 'T', 3: 'G', 4: '$', 5: '#'}

    def __init__(self, base='root', position=-1):
        self.nodes = [None]*6
        self.base = base
        self.position = position
        self.label = -1
        self.length = 1
        self.color = 'gray'
        self.text = ''

    def __str__(self):
        return self.getText()[self.position:self.length + self.position]

    def __repr__(self):
        return self.getText()[self.position:self.length + self.position]

    def print(self):
        return self.base

    # GETTERS

    def getText(self):
        return self.text

    def getColor(self):
        return self.color

    def getBase(self):
        return self.base

    def getNext(self, base=None):
        if base:
            return self.nodes[self.indexBase(base)]
        else:
            for node in self.getNodes():
                if node:
                    return node

    def getNodes(self):
        return self.nodes

    def getRealNodes(self):
        return [node for node in self.nodes if node]

    def getNonLeafNodes(self):
        return [node for node in self.getRealNodes() if not node.isLeaf()]

    def getNonRedNodes(self):
        return [node for node in self.getRealNodes() if node.getColor() != 'red']

    def getPurpleNodes(self):
        return [node for node in self.getRealNodes() if node.getColor() == 'purple']

    def getPosition(self):
        return self.position

    def indexBase(self, base):
        if base in self.nucleotideDict:
            return self.nucleotideDict[base]
        return -1

    def getLabel(self):
        return self.label

    def getLength(self):
        return self.length

    # SETTERS
    def setText(self, text):
        self.text = text

    def setColor(self, color):
        self.color = color

    def setLabel(self, label):
        self.label = label

    def setLength(self, length):
        self.length = length

    def setBase(self, base):
        self.base = base

    def setNode(self, index, node):
        self.nodes[index] = node

    def setPosition(self, position):
        self.position = position

    def isLeaf(self):
        for node in self.nodes:
            if node:
                return False
        return True

    def hasBase(self, base):
        if self.nodes[self.indexBase(base)]:
            return True
        return False

    def addNextNode(self, base, position):
        self.nodes[self.indexBase(base)] = TrieNode(base, position)


    def printTrie(self):
        stack = [(self, node) for node in self.getNodes() if node]

        while stack:
            currPair = stack.pop()
            prev = currPair[0]
            curr = currPair[1]
            print(str(prev.getBase()) + ',' + str(prev.getPosition()), '-->', curr.getBase(), curr.getPosition())

            prev = curr
            for node in curr.getNodes():
                if node:
                    stack.append((prev, node))

    def printTrie2(self):
        stack = [(self, node) for node in self.getNodes() if node]

        while stack:
            currPair = stack.pop()
            prev = currPair[0]
            curr = currPair[1]
            print(str(prev.getBase()) + ',' + str(prev.getPosition()), '-->', curr.getBase(), curr.getPosition(), "length :" , curr.getLength())

            prev = curr
            for node in curr.getNodes():
                if node:
                    stack.append((prev, node))

    def printTree(self, text):
        stack = [node for node in self.getNodes() if node]
        while stack:
            curr = stack.pop()
            print(text[curr.getPosition():curr.getPosition() + curr.getLength()], curr.getColor(), ' position : ', curr.getPosition())

            for node in curr.getNodes():
                if node:
                    stack.append(node)


    def isBalanced(self):
        if len(set(self.getNodes())) == 2:
            return True
        return False

def constructModifiedSuffixTrie(text):
    rootNode = TrieNode()
    # rootNode.setText(text)
    for i in range(len(text)):
        currNode = rootNode
        for j in range(i, len(text)):
            currSym = text[j]
            if currNode.hasBase(currSym):
                currNode = currNode.getNext(currSym)
            else:
                currNode.addNextNode(currSym, j)
                currNode = currNode.getNext(currSym)
                # currNode.setText(text)
        if currNode.isLeaf():
            currNode.setLabel(i)

    return rootNode


def constructSuffixTree(rootNode):
    stack = [rootNode]

    while stack:
        currNode = stack.pop()

        if not currNode.isLeaf():
            for node in currNode.getRealNodes():
                index = currNode.getNodes().index(node)
                position = node.getPosition()
                length = 1
                next = node
                while next.isBalanced():
                    next = next.getNext()
                    length += 1

                next.setPosition(position)
                next.setLength(length)
                next.setBase(node.getBase())
                currNode.setNode(index, next)
                stack.append(next)

    return rootNode


if __name__ == '__main__':
    # with open('test63.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9c.txt', 'r+') as f:
        text = f.readline().rstrip()
    root = constructModifiedSuffixTrie(text)
    root = constructSuffixTree(root)

    root.printTree(text)

