def create_index_column(column):
    col_dict = {}
    for i, elem in enumerate(column):
        if elem in col_dict:
            col_dict[elem] += 1
        else:
            col_dict[elem] = 1
        column[i] = (elem, col_dict[elem])

    return column

def last_to_first(last_col, index):

    last_index_column = create_index_column(list(last_col))
    first_index_column = create_index_column(sorted(last_col))

    return first_index_column.index(last_index_column[index])



if __name__ == '__main__':
    # with open('test71.txt') as f:
    with open('Datasets/rosalind_ba9k.txt', 'r+') as f:
        last_col = [s for s in f.readline().rstrip()]
        index = int(f.readline())

    index = last_to_first(last_col, index)
    print(index)