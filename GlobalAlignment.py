def initialize_global_mat(s1, s2, indelPen):
    dp_mat = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

    for i in range(len(dp_mat[0])):
        dp_mat[0][i] = -(i*indelPen)
    for i in range(len(dp_mat)):
        dp_mat[i][0] = -(i*indelPen)

    return dp_mat


def initialize_bt_mat(s1, s2):
    bt_mat = [[''] * (len(s1) + 1) for _ in range(len(s2) + 1)]
    for i in range(1, len(bt_mat)):
        bt_mat[i][0] = 'up'
    for i in range(1, len(bt_mat[0])):
        bt_mat[0][i] = 'left'

    return bt_mat


def getScoreValue(acid1, acid2):
    ind1 = acidIndexDict[acid1]
    ind2 = acidIndexDict[acid2]

    return scoring_matrix[ind1][ind2]


def findGlobalAlignment(s1, s2):
    bt_dict = {0:'diag', 1:'left', 2:'up'}
    indelPen = 5
    dp_mat = initialize_global_mat(s1, s2, indelPen)

    bt_mat = initialize_bt_mat(s1, s2)

    for i in range(1, len(dp_mat)):
        for j in range(1, len(dp_mat[0])):
            var = getScoreValue(s1[j-1], s2[i-1])
            values = [dp_mat[i-1][j-1] + var, dp_mat[i][j-1] - indelPen, dp_mat[i-1][j] - indelPen]
            dp_mat[i][j] = max(values)
            bt_mat[i][j] = bt_dict[values.index(dp_mat[i][j])]



    print(dp_mat[-1][-1])
    #
    # dp_mat = dp_mat#[::-1]
    #
    for i, line in enumerate(dp_mat):
        print(i, ':', line)
    # #
    for line in bt_mat:
        print(line)
    return backtrack_global(bt_mat, s1, s2)


def backtrack_global(bt_mat, s1, s2):
    s1align = ''
    s2align = ''

    i = len(bt_mat) - 1
    j = len(bt_mat[0]) - 1

    while i != -1 and j != -1:
        print(i, j, bt_mat[i][j])
        if bt_mat[i][j] == 'diag':
            s1align += s1[j-1]
            s2align += s2[i-1]

        elif bt_mat[i][j] == 'left':
            s2align += '-'
            s1align += s1[j-1]
            j -= 1
            continue

        elif bt_mat[i][j] == 'up':
            s2align += s2[i-1]
            s1align += '-'
            i -= 1
            continue

        i -= 1
        j -= 1

    return s1align[::-1], s2align[::-1]


with open('BLOSUM62.txt', 'r+') as f:
    acids = f.readline().split()
    acidIndexDict = {acid : i for i, acid in enumerate(acids)}
    scoring_matrix = []
    for i, line in enumerate(f):
        scoring_matrix.append([int(x) for x in line.split()[1:]])

with open('testNeha','r+') as file:
    s2 = file.readline().rstrip()

    s1 = file.readline().rstrip()


    alignment = findGlobalAlignment(s1, s2)
    print('\n'.join(alignment))
