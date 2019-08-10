def create_index_column(column):
    col_dict = {}
    for i, elem in enumerate(column):
        if elem in col_dict:
            col_dict[elem] += 1
        else:
            col_dict[elem] = 1
        column[i] = (elem, col_dict[elem])

    return column


def invert_bwt(last_column):
    text = ''

    last_index_column = create_index_column(list(last_column))
    first_index_column = create_index_column(sorted(last_column))

    curr = first_index_column[0]
    while len(text) < len(last_index_column):
        index = last_index_column.index(curr)
        text += first_index_column[index][0]
        curr = first_index_column[index]

    return text

if __name__ == '__main__':
    # with open('test70.txt', 'r+') as f:
    # with open('extra70.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9j.txt', 'r+') as f:
        last_col = [s for s in f.readline().rstrip()]

    last_col = [s for s in 'BBDAD$A']

    str = invert_bwt(last_col)

    print(str)