from HW.Week7.BWT import bwt
from HW.Week7.SuffixArray import suffixArray


def getLetterIndex(symbol):
    if symbol == '$':
        return 0
    return ord(symbol) - 64


# Find first occurences of all symbols in the FIRST column
def find_first_occurences(last_column):
    first_occurence = [None]*27
    first_column = sorted(last_column)

    # set for $
    first_occurence[0] = 0

    for i in range(26):
        sym = chr(i + 64)
        for i, elem in enumerate(first_column):
            if elem == sym:
                first_occurence[getLetterIndex(sym)] = i
                break

    return first_occurence


def count(checkpoint_dict, index, symbol, last_column):
    C_index = index - (index % C)
    counter = checkpoint_dict[C_index][getLetterIndex(symbol)]
    for i in range(C_index, index):
        if last_column[i] == symbol:
            counter += 1

    return counter


def better_bw_matching(last_column, pattern, checkpoint_dict):
    first_occurrence = find_first_occurences(last_column)

    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            first_o = first_occurrence[getLetterIndex(symbol)]
            top = first_o + count(checkpoint_dict, top, symbol, last_column)
            bottom = first_o + count(checkpoint_dict, bottom + 1, symbol, last_column) - 1

        else:
            return top, bottom

    return top, bottom


def generate_checkpoint_counts(last_column, C):
    checkpoint_dict = {}
    count_arr = [0] * 27
    for i, elem in enumerate(last_column):
        if i % C == 0:
            checkpoint_dict[i] = list(count_arr)
        count_arr[getLetterIndex(elem)] += 1

    if (i + 1) % C == 0:
        checkpoint_dict[i + 1] = list(count_arr)

    return checkpoint_dict


def multiple_pattern_matching(text, patterns, suffix_arr, C):
    idx_list = []
    text = bwt(text)
    last_column = list(text)

    checkpoint_dict = generate_checkpoint_counts(last_column, C)

    for pattern in patterns:
        top, bottom = better_bw_matching(last_column, pattern, checkpoint_dict)
        for i in range(top, bottom + 1):
            idx_list.append(suffix_arr[i])

    return idx_list


if __name__ == '__main__':
    # with open('test/test74.txt', 'r+') as f:
    # with open('extra/extra74.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9n.txt', 'r+') as f:
        text = f.readline().rstrip() + '$'
        patterns = [pat.rstrip() for pat in f.readlines()]

    suffix_arr = suffixArray(text)

    C = 100

    indices = multiple_pattern_matching(text, patterns, suffix_arr, C)
    print(' '.join(indices))



