import sys

openGapPen = 11
gapExtPen = 1

with open('BLOSUM62.txt', 'r+') as f:
    acids = f.readline().split()
    acidIndexDict = {acid : i for i, acid in enumerate(acids)}
    scoring_matrix = []
    for i, line in enumerate(f):
        scoring_matrix.append([int(x) for x in line.split()[1:]])


def getScoreValue(acid1, acid2):
    ind1 = acidIndexDict[acid1]
    ind2 = acidIndexDict[acid2]

    return scoring_matrix[ind1][ind2]


def initialize_affine_matrices(s1, s2):
    upper_mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    middle_mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    lower_mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    upper_mat[0][0] = -sys.maxsize
    lower_mat[0][0] = -sys.maxsize

    for i in range(1, len(lower_mat)):
        lower_mat[i][0] = gapExtPen * -i
    for i in range(1, len(upper_mat[0])):
        upper_mat[0][i] = gapExtPen * -i

    return upper_mat, middle_mat, lower_mat

def initialize_affine_backtracks(s1, s2):
    upper_bt = [[''] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    middle_bt = [[''] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    lower_bt = [[''] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(lower_bt)):
        lower_bt[i][0] = 'up'
    for i in range(1, len(upper_bt[0])):
        upper_bt[0][i] = 'left'

    return upper_bt, middle_bt, lower_bt

def affineGapPenaltyAlignment(s1, s2):
    lower_bt_dict = {0 : 'up', 1 : 'middle'}
    upper_bt_dict = {0 : 'left', 1 : 'middle'}
    middle_bt_dict = {0 : 'lower', 1 : 'diag', 2 : 'upper'}

    upper_mat, middle_mat, lower_mat = initialize_affine_matrices(s1, s2)
    upper_bt, middle_bt, lower_bt = initialize_affine_backtracks(s1, s2)

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            lower_possibities = [lower_mat[i-1][j] - gapExtPen, middle_mat[i-1][j] - openGapPen]
            lower_mat[i][j] = max(lower_possibities)
            lower_bt[i][j] = lower_bt_dict[lower_possibities.index(lower_mat[i][j])]

            upper_possibilities = [upper_mat[i][j-1] - gapExtPen, middle_mat[i][j-1] - openGapPen]
            upper_mat[i][j] = max(upper_possibilities)
            upper_bt[i][j] = upper_bt_dict[upper_possibilities.index(upper_mat[i][j])]

            middle_possibilities = [lower_mat[i][j], middle_mat[i-1][j-1] + getScoreValue(s1[i-1], s2[j-1]), upper_mat[i][j]]
            middle_mat[i][j] = max(middle_possibilities)
            middle_bt[i][j] = middle_bt_dict[middle_possibilities.index(middle_mat[i][j])]

    print(middle_mat[-1][-1])

    s1Align = ''
    s2Align = ''

    i = len(middle_bt) - 1
    j = len(middle_bt[0]) - 1

    currMat = middle_bt

    while i != 0 and j != 0:
        currDir = currMat[i][j]
        if currMat == middle_bt:
            if currDir == 'diag':
                i -= 1
                j -= 1
                s1Align += s1[i]
                s2Align += s2[j]
            elif currDir == 'lower':
                currMat = lower_bt
            elif currDir == 'upper':
                currMat = upper_bt

        elif currMat == lower_bt:
            if currDir == 'middle':
                currMat = middle_bt
            i -= 1
            s1Align += s1[i]
            s2Align += '-'

        elif currMat == upper_bt:
            if currDir == 'middle':
                currMat = middle_bt
            j -= 1
            s1Align += '-'
            s2Align += s2[j]

    return s1Align[::-1], s2Align[::-1]


with open('rosalind_ba5j.txt', 'r+') as f:
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()
    alignment = affineGapPenaltyAlignment(s1, s2)
    print('\n'.join(alignment))