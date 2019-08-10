from HW.Week7.SuffixArray import suffixArray
from HW.Week7.BWT import bwt
from HW.Week1.HammingDistance import hammingDistance


def getLetterIndex(symbol):
    if symbol == '$':
        return 0
    return ord(symbol) - 64


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

            f_o = first_occurrence[getLetterIndex(symbol)]

            top = count(checkpoint_dict, top, symbol, last_column)
            bottom = count(checkpoint_dict, bottom + 1, symbol, last_column) - 1

            if f_o:
                top += f_o
                bottom += f_o


            # first_o = first_occurrence[getLetterIndex(symbol)]
            # top = first_o + count(checkpoint_dict, top, symbol, last_column)
            # bottom = first_o + count(checkpoint_dict, bottom + 1, symbol, last_column) - 1

        else:
            return top, bottom

    return top, bottom


def extend_seed(index, top, bottom, suffix_arr):
    return [int(suffix_arr[i]) - index for i in range(top, bottom + 1)]


def multiple_approximate_pattern_matching(text, patterns, d):
    last_column = [c for c in bwt(text)]
    suffix_arr = suffixArray(text)
    C = 5
    checkpoint_dict = generate_checkpoint_counts(last_column, C)

    ret_indices = []

    for pattern in patterns:

        # use set to prevent copies of same index from multiple seeds (for one pattern)
        pattern_match_indices = set()

        kmer_size = len(pattern)//(d + 1)
        pattern_seeds = [(pattern[i*kmer_size: i*kmer_size + kmer_size], i*kmer_size) for i in range(0, d)] +\
                        [(pattern[kmer_size * d:], kmer_size*d)]
        for seed_pair in pattern_seeds:
            top, bottom = better_bw_matching(last_column, seed_pair[0], checkpoint_dict)

            # iterate through all possible suffixes given from suffix array
            if top <= bottom:
                indices = extend_seed(seed_pair[1], top, bottom, suffix_arr)

                # check hamming dist
                for idx in indices:
                    hamm_dist = hammingDistance(pattern, text[idx: idx + len(pattern)])
                    if hamm_dist <= d:
                        pattern_match_indices.add(idx)

        ret_indices += list(pattern_match_indices)

    return ret_indices


if __name__ == '__main__':
    with open('Datasets/rosalind_ba9o.txt', 'r+') as f:
        text = f.readline().rstrip() + '$'
        patterns = [line.rstrip() for line in f.readline().split()]

        d = int(f.readline())

    C = 5

    indices = sorted(multiple_approximate_pattern_matching(text, patterns, d))
    print(' '.join([str(i) for i in indices]))

