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


def initialize_linear_mat(s1, indelPen):
    dp_mat= [[0] * 2 for _ in range(len(s1) + 1)]
    for i in range(len(dp_mat)):
        dp_mat[i][1] = -(i*indelPen)

    return dp_mat


def LCSalignmentScore(s1, s2, indelPen):
    print(s1, s2)
    bt_dict = {0:'diag', 1:'right', 2:'down'}
    dp_mat = initialize_linear_mat(s1, indelPen)

    bt_mat = [''] * len(dp_mat)

    for j in range(len(s2)):
        for i, pair in enumerate(dp_mat):
            dp_mat[i][0] = pair[1]
        dp_mat[0][1] = dp_mat[0][0] - indelPen
        for i in range(1, len(dp_mat)):
            var = getScoreValue(s1[i-1], s2[j])
            values = [dp_mat[i-1][0] + var, dp_mat[i][0] - indelPen, dp_mat[i-1][1] - indelPen]
            dp_mat[i][1] = max(values)
            if j == len(s2) - 1:
                bt_mat[i] = bt_dict[values.index(dp_mat[i][1])]


    return dp_mat, bt_mat


def findMiddleEdge(s1, s2, indelPen):
    left = s2[:len(s2)//2]
    right = s2[len(s2)//2:]

    print(left, right)

    matFromLeft, _ = LCSalignmentScore(s1, left, indelPen)
    matFromRight, bt_right = LCSalignmentScore(s1[::-1], right[::-1], indelPen)

    matFromRight = matFromRight[::-1]
    bt_right = bt_right[::-1]


    vertStart = 0
    horizontalStart = len(left)
    horizontalEnd = len(left)
    midEdgeSum = matFromLeft[0][1] + matFromRight[0][1]

    for i in range(len(matFromLeft)):
        if matFromLeft[i][1] + matFromRight[i][1] > midEdgeSum:
            midEdgeSum = matFromLeft[i][1] + matFromRight[i][1]
            vertStart = i

    for line in matFromLeft:
        print(line)

    print('RIGHT')

    for line in matFromRight:
        print(line)



    vertEnd = vertStart
    if bt_right[vertStart] == 'diag':
        vertEnd += 1
        horizontalEnd += 1
    elif bt_right[vertStart] == 'down':
        vertEnd += 1
    elif bt_right[vertStart] == 'right':
        horizontalEnd += 1

    # return [(vertStart, horizontalStart), (vertEnd, horizontalEnd)]
    return [(vertStart,horizontalStart), bt_right[vertStart]]

with open('test.txt', 'r+') as f:
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()
    indelPen = 5
    edge = findMiddleEdge(s1, s2, indelPen)
    print(edge[0], edge[1])


