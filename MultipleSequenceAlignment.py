def initialize_multiple_mat(s1, s2, s3):
    return [[[0]*(len(s3) + 1) for _ in range(len(s2) +1)] for i in range(len(s1) + 1)]


def initialize_multiple_bt_mat(s1, s2, s3):
    bt_mat = [[['']*(len(s3) + 1) for _ in range(len(s2) +1)] for i in range(len(s1) + 1)]

    for i in range(1, len(bt_mat)):
        bt_mat[i][0][0] = 'i-1,j,k'
    for j in range(1, len(bt_mat[0])):
        bt_mat[0][j][0] = 'i,j-1,k'
    for k in range(1, len(bt_mat[0][0])):
        bt_mat[0][0][k] = 'i,j,k-1'

    for i in range(1, len(bt_mat)):
        for k in range(1, len(bt_mat[0][0])):
            bt_mat[i][0][k] = 'i-1,j,k-1'

    for j in range(1, len(bt_mat[0])):
        for k in range(1, len(bt_mat[0][0])):
            bt_mat[0][j][k] = 'i,j-1,k-1'

    for i in range(1, len(bt_mat)):
        for j in range(1, len((bt_mat[0]))):
            bt_mat[i][j][0] = 'i-1,j-1,k'

    return bt_mat


def backtrack_3d(bt_mat):
    s1Align = ''
    s2Align = ''
    s3Align = ''

    i = len(bt_mat) - 1
    j = len(bt_mat[0]) - 1
    k = len(bt_mat[0][0]) - 1

    while i != 0 or j != 0 or k != 0:
        if bt_mat[i][j][k] == 'i-1,j,k':
            i -= 1
            s1Align += s1[i]
            s2Align += '-'
            s3Align += '-'

        elif bt_mat[i][j][k] == 'i,j-1,k':
            j -= 1
            s2Align += s2[j]
            s1Align += '-'
            s3Align += '-'

        elif bt_mat[i][j][k] == 'i,j,k-1':
            k -= 1
            s3Align += s3[k]
            s2Align += '-'
            s1Align += '-'

        elif bt_mat[i][j][k] == 'i-1,j-1,k':
            i -= 1
            j -= 1
            s1Align += s1[i]
            s2Align += s2[j]
            s3Align += '-'
        elif bt_mat[i][j][k] == 'i-1,j,k-1':
            i -= 1
            k -= 1
            s1Align += s1[i]
            s3Align += s3[k]
            s2Align += '-'

        elif bt_mat[i][j][k] == 'i,j-1,k-1':
            j -= 1
            k -= 1
            s3Align += s3[k]
            s2Align += s2[j]
            s1Align += '-'

        elif bt_mat[i][j][k] == 'i-1,j-1,k-1':
            i -= 1
            j -= 1
            k -= 1
            s1Align += s1[i]
            s2Align += s2[j]
            s3Align += s3[k]

    return s1Align[::-1], s2Align[::-1], s3Align[::-1]


def multipleSequenceAlignment(s1, s2, s3):
    bt_dict = {0:'i-1,j,k', 1:'i,j-1,k', 2:'i,j,k-1', 3:'i-1,j-1,k', 4:'i-1,j,k-1', 5:'i,j-1,k-1', 6:'i-1,j-1,k-1'}

    dp_mat = initialize_multiple_mat(s1, s2, s3)
    bt_mat = initialize_multiple_bt_mat(s1, s2, s3)

    for i in range(1, len(dp_mat)):
        for j in range(1, len(dp_mat[0])):
            for k in range(1, len(dp_mat[0][0])):
                var = 1 if s1[i-1] == s2[j-1] == s3[k-1] else 0
                values = [dp_mat[i-1][j][k], dp_mat[i][j-1][k], dp_mat[i][j][k-1], dp_mat[i-1][j-1][k],
                          dp_mat[i-1][j][k-1], dp_mat[i][j-1][k-1], dp_mat[i-1][j-1][k-1] + var]
                dp_mat[i][j][k] = max(values)
                bt_mat[i][j][k] = bt_dict[values.index(dp_mat[i][j][k])]

    print(dp_mat[-1][-1][-1])
    return backtrack_3d(bt_mat)


with open('rosalind_ba5m.txt', 'r+') as f:
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()
    s3 = f.readline().rstrip()
    alignment = multipleSequenceAlignment(s1, s2, s3)
    print('\n'.join(alignment))

