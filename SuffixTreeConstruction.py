class TrieNode:

    nucleotideDict = {'$': 0, 'A': 1, 'C': 2, 'T':3, 'G': 4}

    def __init__(self, base=None, position=-1):
        self.nodes = [None]*27
        self.base = base
        self.position = position
        self.label = -1
        self.length = 1
        self.descent = 0
        self.parent = None
        self.text = ''

    def __str__(self):
        if self.base == 'root':
            return self.base
        return self.getText()#[self.position:self.length + self.position]

    def __repr__(self):
        if self.base == 'root':
            return self.base
        return self.getText()#[self.position:self.length + self.position]

    def print(self):
        if self.base == 'root':
            return self.base
        return self.getText()#

    # GETTERS

    def getText(self):
        return self.text

    def getBase(self):
        return self.base

    def getNext(self, base=None):
        if base:
            return self.nodes[self.indexBase(base)]
        else:
            for node in self.getNodes():
                if node:
                    return node

    def getDescent(self):
        return self.descent

    def getNodes(self):
        return self.nodes

    def getRealNodes(self):
        return [node for node in self.nodes if node]

    def getLastNode(self):
        return self.getRealNodes()[-1]

    def getNonLeafNodes(self):
        return [node for node in self.getRealNodes() if not node.isLeaf()]

    def getPosition(self):
        return self.position

    def indexBase(self, base):
        if base == '$':
            return 0
        else:
            return ord(base) - 64

        # if base in self.nucleotideDict:
        #     return self.nucleotideDict[base]
        # return -1

    def getLabel(self):
        return self.label

    def getLength(self):
        return self.length

    def getParent(self):
        return self.parent

    # SETTERS

    def setText(self, text):
        self.text = text

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

    def setParent(self, parentNode):
        self.parent = parentNode

    def setDescent(self, descent):
        self.descent = descent

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

    def addNode(self, node):
        base = node.getText()[0]
        self.nodes[self.indexBase(base)] = node



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
            # print(text[curr.getPosition():curr.getPosition() + curr.getLength()], 'position : ', curr.getPosition())
            print(curr)

            for node in curr.getNodes():
                if node:
                    stack.append(node)


    def isBalanced(self):
        if len(set(self.getNodes())) == 2:
            return True
        return False




def constructModifiedSuffixTrie(text):
    rootNode = TrieNode()
    rootNode.setText(text)
    for i in range(len(text)):
        currNode = rootNode
        for j in range(i, len(text)):
            currSym = text[j]
            if currNode.hasBase(currSym):
                currNode = currNode.getNext(currSym)
            else:
                currNode.addNextNode(currSym, j)
                currNode = currNode.getNext(currSym)
                currNode.setText(text)
        if currNode.isLeaf():
            currNode.setLabel(i)

    return rootNode


def constructSuffixTree(text):
    rootNode = constructModifiedSuffixTrie(text)

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
    text = 'ACT$'
    root = constructSuffixTree(text)
    root.printTree(text)