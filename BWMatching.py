from HW.Week7.BWT import bwt

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


def bw_matching(last_column, patterns):
    occurence_list = [0]*len(patterns)
    for i, pattern in enumerate(patterns):
        top = 0
        bottom = len(last_column) - 1
        while top <= bottom:
            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]
                if symbol in last_column[top:bottom + 1]:
                    top_ind = -1
                    bottom_ind = -1
                    for j in range(top, len(last_column)):
                        if symbol == last_column[j]:
                            top_ind = j
                            break
                    for j in range(bottom, top_ind - 1, -1):
                        if symbol == last_column[j]:
                            bottom_ind = j
                            break

                    top = last_to_first(last_column, top_ind)
                    bottom = last_to_first(last_column, bottom_ind)


                else:
                    top, bottom = 0, 0
                    break
            else:
                print(top,bottom)
                occurence_list[i] = bottom - top + 1
                break

    return occurence_list


if __name__ == '__main__':
    # with open('test72.txt', 'r+') as f:
    # with open('extra72.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9l.txt', 'r+') as f:
        last_column = [c for c in f.readline().rstrip()]
        patterns = f.readline().rstrip().split()

    last_column = [c for c in bwt('ACATGCTACTTT')]
    patterns = ['TA']

    occurrences = bw_matching(last_column, patterns)
    print(' '.join([str(i) for i in occurrences]))
