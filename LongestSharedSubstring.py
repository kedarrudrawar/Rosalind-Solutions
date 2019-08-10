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

def initialColoring(rootNode, text):
    queue = rootNode.getRealNodes()
    ripeNodes = []

    while queue:
        curr = queue.pop()
        if curr.isLeaf():
            pos = curr.getPosition()
            suffix = text[pos:]
            if '#' in suffix:
                curr.setColor('blue')
            else:
                curr.setColor('red')
        else:
            ripeNodes.append(curr)
            for node in curr.getRealNodes():
                queue.insert(0, node)

    return rootNode, ripeNodes

def TreeColoring(text):
    root = constructModifiedSuffixTrie(text)
    root = constructSuffixTree(root)

    root.printTree(text)

    rootNode, ripeNodes = initialColoring(root, text)

    ripeNodes = ripeNodes[::-1]

    for node in ripeNodes:
        red = False
        blue = False
        purple = False
        for child in node.getRealNodes():
            if child.getColor() == 'blue':
                blue = True
            elif child.getColor() == 'red':
                red = True
            elif child.getColor() == 'purple':
                purple = True
        if purple or (red and blue):
            node.setColor('purple')
        elif red:
            node.setColor('red')
        else:
            node.setColor('blue')


    return rootNode


def findLongestSharedSubstring(text):
    # Node dict:
    # NODE : (End position, Length)

    root = TreeColoring(text)
    node_dict = {node : (node.getPosition() + node.getLength(), node.getLength()) for node in root.getPurpleNodes()}
    queue = [node for node in root.getPurpleNodes()]

    while queue:
        curr = queue.pop()
        for child in curr.getPurpleNodes():
            node_dict[child] = (child.getPosition() + child.getLength(), node_dict[curr][1] + child.getLength())
            queue.insert(0, child)

    position, length = node_dict[max(node_dict, key=lambda key:node_dict[key][1])]

    print(text[position - length: position])

    return text[position - length: position]


if __name__ == '__main__':
    # with open('test2Strings2.txt', 'r+') as file:
    with open('Datasets/rosalind_ba9e.txt', 'r+') as file:
        str1 = file.readline().rstrip() + '#'
        str2 = file.readline().rstrip() + '$'
        text = str1 + str2

    substr = findLongestSharedSubstring(text)
