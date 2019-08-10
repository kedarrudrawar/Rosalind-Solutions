def initialize_global_mat(s1, s2, indelPen):
    dp_mat = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

    for i in range(len(dp_mat[0])):
        dp_mat[0][i] = -(i*indelPen)
    for i in range(len(dp_mat)):
        dp_mat[i][0] = -(i*indelPen)

    return dp_mat

def findMinEditDist(s1, s2):
    indelPen = -1
    dp_mat = initialize_global_mat(s1, s2, indelPen)

    for i in range(1, len(dp_mat)):
        for j in range(1, len(dp_mat[0])):
            var = 1 if s1[j-1] != s2[i-1] else 0
            values = [dp_mat[i-1][j-1] + var, dp_mat[i][j-1] - indelPen, dp_mat[i-1][j] - indelPen]
            dp_mat[i][j] = min(values)

    return dp_mat[-1][-1]



with open('rosalind_ba5g.txt','r+') as file:
    s1 = file.readline().rstrip()
    s2 = file.readline().rstrip()

    distance = findMinEditDist(s1, s2)
    print(distance)
