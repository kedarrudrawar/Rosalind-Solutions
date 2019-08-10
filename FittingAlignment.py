def initialize_fitting_mat(s1, s2, indelPen):
    dp_mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(dp_mat[0])):
        dp_mat[0][i] = -(i*indelPen)
    for i in range(len(dp_mat)):
        dp_mat[i][0] = 0

    return dp_mat


def initialize_bt_mat(s1, s2):
    bt_mat = [[''] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(bt_mat)):
        bt_mat[i][0] = 'source'
    for i in range(1, len(bt_mat[0])):
        bt_mat[0][i] = 'left'

    return bt_mat




def findFittingAlignment(s1, s2):
    bt_dict = {0:'diag', 1:'left', 2:'up'}
    indelPen = 1
    dp_mat = initialize_fitting_mat(s1, s2, indelPen)

    bt_mat = initialize_bt_mat(s1, s2)

    maxVal = 0
    startPoint = []

    for i in range(1, len(dp_mat)):
        for j in range(1, len(dp_mat[0])):
            var = 1 if s1[i-1] == s2[j-1] else -1
            values = [dp_mat[i-1][j-1] + var, dp_mat[i][j-1] - indelPen, dp_mat[i-1][j] - indelPen]
            dp_mat[i][j] = max(values)
            bt_mat[i][j] = bt_dict[values.index(dp_mat[i][j])]
            if j == len(dp_mat[0]) - 1:
                if dp_mat[i][j] > maxVal:
                    maxVal = dp_mat[i][j]
                    startPoint = [i,j]

    print(dp_mat[startPoint[0]][startPoint[1]])

    return backtrack_local(startPoint, bt_mat, s1, s2)


def backtrack_local(startPoint, bt_mat, s1, s2):
    s1align = ''
    s2align = ''

    i = startPoint[0]
    j = startPoint[1]

    while bt_mat[i][j] != 'source':
        if bt_mat[i][j] == 'diag':
            s1align += s1[i-1]
            s2align += s2[j-1]

        elif bt_mat[i][j] == 'left':
            s2align += s2[j-1]
            s1align += '-'
            j -= 1
            continue

        elif bt_mat[i][j] == 'up':
            s2align += '-'
            s1align += s1[i-1]
            i -= 1
            continue

        i -= 1
        j -= 1

    return s1align[::-1], s2align[::-1]



with open('rosalind_ba5h.txt','r+') as file:
    s1 = file.readline().rstrip()
    s2 = file.readline().rstrip()


    alignment = findFittingAlignment(s1, s2)
    print('\n'.join(alignment))
