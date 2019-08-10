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

    vertEnd = vertStart
    if bt_right[vertStart] == 'diag':
        vertEnd += 1
        horizontalEnd += 1
    elif bt_right[vertStart] == 'down':
        vertEnd += 1
    elif bt_right[vertStart] == 'right':
        horizontalEnd += 1

    # return [(vertStart, horizontalStart), (vertEnd, horizontalEnd)]  # for problem 46 - Rosalind
    return [(vertStart,horizontalStart), bt_right[vertStart]]


def linearSpaceAlignment(top, bottom, left, right, s1, s2):
    indelPen = 5
    alignment = ['','']
    if left == right:
        for i in range(top, bottom):
            alignment[0] += s1[i]
            alignment[1] += '-'
        return alignment
    if top == bottom:
        for i in range(left, right):
            alignment[1] += s2[i]
            alignment[0] += '-'
        return alignment

    (midVert, midHoriz), midEdge = findMiddleEdge(s1[top:bottom], s2[left:right], indelPen)
    midVert += top
    midHoriz += left

    alignment = linearSpaceAlignment(top, midVert, left, midHoriz, s1, s2)

    if midEdge == 'diag':
        alignment[0] += s1[midVert]
        alignment[1] += s2[midHoriz]
        midVert += 1
        midHoriz += 1
    elif midEdge == 'right':
        alignment[0] += '-'
        alignment[1] += s2[midHoriz]
        midHoriz += 1
    elif midEdge == 'down':
        alignment[0] += s1[midVert]
        alignment[1] += '-'
        midVert += 1

    newAlig = linearSpaceAlignment(midVert, bottom, midHoriz, right, s1, s2)
    alignment[0] += newAlig[0]
    alignment[1] += newAlig[1]

    return alignment

def calcScore(alignment, indelPen):
    s1 = alignment[0]
    s2 = alignment[1]
    score = 0
    for i in range(len(s1)):
        if s1[i] == '-' or s2[i] == '-':
            score -= indelPen
        else:
            score += getScoreValue(s1[i], s2[i])

    return score

with open('test.txt', 'r+') as f:
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()


    indelPen = 5
    alignment = linearSpaceAlignment(0, len(s1), 0, len(s2), s1, s2)
    score = calcScore(alignment, indelPen)
    print(score)

    print('\n'.join(alignment))
