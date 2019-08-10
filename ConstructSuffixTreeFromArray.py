from HW.Week7.SuffixTreeConstruction import TrieNode


def construct_suffix_tree_from_array(text, suffix_arr, lcp_array):
    root = TrieNode('root', position=0)
    root.setText(text)
    v = root

    for i, overlap in enumerate(lcp_array):
        while overlap < v.getDescent():
            v = v.getParent()

        if overlap == v.getDescent():
            x = TrieNode(position=suffix_arr[i] + overlap)
            x.setText(text[suffix_arr[i] + overlap:])
            x.setParent(v)
            x.setLength(len(x.getText()))
            v.addNode(x)
            x.setDescent(v.getDescent() + x.getLength())
            v = x

        elif overlap > v.getDescent():
            w = v.getLastNode()
            y = TrieNode(position=suffix_arr[i] + v.getDescent())
            y.setText(text[y.getPosition(): y.getPosition() + overlap - v.getDescent()])

            y.setDescent(overlap)
            y.setParent(v)
            v.addNode(y)

            w.setText(text[suffix_arr[i-1] + overlap : suffix_arr[i - 1] + w.getDescent()])

            y.addNode(w)
            w.setParent(y)

            x = TrieNode(suffix_arr[i] + overlap)
            x.setText(text[suffix_arr[i] + overlap:])
            x.setParent(y)
            x.setLength(len(x.getText()))
            x.setDescent(y.getDescent() + x.getLength())
            y.addNode(x)

            v = x

    return root


if __name__ == '__main__':
    # with open('test/test78.txt', 'r+') as file:
    with open('Datasets/rosalind_ba9r.txt', 'r+') as file:
        text = file.readline().rstrip()
        suffix_arr = [int(i) for i in file.readline().rstrip().split(', ')]
        lcp_array = [int(i) for i in file.readline().rstrip().split(', ')]

    root = construct_suffix_tree_from_array(text, suffix_arr, lcp_array)
    root.printTree(text)
