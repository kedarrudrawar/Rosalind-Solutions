class FakeNode:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.children = []

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

    def getColor(self):
        return self.color

    def getNumber(self):
        return self.number

    def getChildren(self):
        return self.children

    def addChild(self, child):
        self.children.append(child)

    def setColor(self, color):
        self.color = color

    def isLeaf(self):
        if len(self.children) == 0:
            return True
        return False

    def printTree(self):
        stack = [self]
        while stack:
            curr = stack.pop()
            print(str(curr.getNumber()) + ': ' + curr.getColor())
            for child in curr.getChildren():
                stack.append(child)

def traverse(root):
    stack = [root]
    while stack:
        curr = stack.pop()
        print(curr)
        stack += curr.getChildren()


def initializeTree(adj_list, color_dict):
    node_dict = {}
    stack = [0]
    root = None
    while stack:
        curr = stack.pop()
        if curr in node_dict:
            currNode = node_dict[curr]
        else:
            currNode = FakeNode(curr, 'gray')
            node_dict[curr] = currNode

        if curr == 0:
            root = currNode

        if curr in adj_list:
            children = adj_list[curr]
            if children:
                for child in children:
                    color = 'gray'
                    if child in color_dict:
                        color = color_dict[child]
                    if child in node_dict:
                        currNode.addChild(node_dict[child])
                    else:
                        childNode = FakeNode(child, color)
                        currNode.addChild(childNode)
                        node_dict[child] = childNode
                    stack.append(child)

    return root

def treeColoringHelper(node):
    if node.isLeaf():
        return node.getColor()

    children = node.getChildren()
    first = treeColoringHelper(children[0])
    same = True
    for i in range(1, len(children)):
        next = treeColoringHelper(children[i])
        if next != first:
            same = False

    if same:
        node.setColor(first)
    else:
        node.setColor('purple')

    return node.getColor()


def treeColoring(root):
    treeColoringHelper(root)
    return root



if __name__ == '__main__':
    # with open('rosalind_ba9p.txt', 'r+') as file:
    with open('/Users/KedarRudrawar/Downloads/rosalind_ba9p-1.txt', 'r+') as file:
        adj_list = {}
        color_dict = {}
        line = file.readline()
        while line != '-':
            start, end = line.rstrip().split('->')
            start = int(start)
            if end != ' {}':
                end = [int(i) for i in end.split(',')]
                adj_list[start] = end
            else:
                adj_list[start] = None

            line = file.readline().rstrip()

        for line in file:
            node, color = line.rstrip().split(': ')
            node = int(node)
            color_dict[node] = color

    root = initializeTree(adj_list, color_dict)
    root = treeColoring(root)
    root.printTree()



