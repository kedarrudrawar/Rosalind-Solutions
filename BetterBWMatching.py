from HW.Week7.BWT import bwt

def getLetterIndex(symbol):
    if symbol == '$':
        return 0
    return ord(symbol) - 64


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


def count(symbol, index, last_column):
    counter = 0
    for i in range(index):
        if last_column[i] == symbol:
            counter += 1
    return counter


def better_bw_matching(last_column, patterns):
    occurence_list = [0]*len(patterns)
    first_occurrence = find_first_occurences(last_column)

    for i, pattern in enumerate(patterns):
        top = 0
        bottom = len(last_column) - 1
        while top <= bottom:

            # print(pattern, top,bottom)

            if pattern:
                symbol = pattern[-1]
                pattern = pattern[:-1]

                f_o = first_occurrence[getLetterIndex(symbol)]

                print(top, bottom)
                top = count(symbol, top, last_column)
                bottom = count(symbol, bottom + 1, last_column) - 1


                if f_o:
                    top += f_o
                    bottom += f_o

            else:
                occurence_list[i] = bottom - top + 1
                break

    return occurence_list

if __name__ == '__main__':
    with open('Datasets/rosalind_ba9m.txt', 'r+') as f:
        last_column = [c for c in f.readline().rstrip()]
        patterns = f.readline().rstrip().split()

    last_column = [c for c in bwt('DADBAB$')]
    patterns = ['DBA']

    occurence_list = better_bw_matching(last_column, patterns)

    print(' '.join([str(i) for i in occurence_list]))

