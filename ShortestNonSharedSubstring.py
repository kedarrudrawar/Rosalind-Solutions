from HW.Week7.TreeColoring import TreeColoring

def shortestNonsharedSubstring(text):
    root = TreeColoring(text)

    stack = root.getPurpleNodes()

    nonHashtagNodes = root.getNonRedNodes()
    for i, node in enumerate(nonHashtagNodes):
        if node.getBase() == '#':
            del nonHashtagNodes[i]
            break

    node_dict = {node : (node.getPosition() + node.getLength(), node.getLength()) for node in nonHashtagNodes}

    while stack:
        curr = stack.pop()
        children = curr.getNonRedNodes()
        for child in children:
            if child.getColor() == 'blue':
                node_dict[child] = (child.getPosition() + child.getLength(), node_dict[curr][1] + child.getLength())
            elif child.getColor() == 'purple':
                node_dict[child] = (child.getPosition() + child.getLength(), node_dict[curr][1] + child.getLength())
                stack.append(child)
        del node_dict[curr]

    # print(node_dict)

    pos, len = node_dict[min(node_dict, key=lambda key:node_dict[key][1])]

    print(text[pos - len: pos])



    return ''


if __name__ == '__main__':
    # with open('test66.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9f.txt', 'r+') as f:
        s1 = f.readline().rstrip() + '#'
        s2 = f.readline().rstrip() + '$'

    text = s1 + s2
    str = shortestNonsharedSubstring(text)