def findLongestGridPathLength(down_matrix, right_matrix):
    dp_mat = [[0]*(len(right_matrix[0]) + 1) for _ in range(len(down_matrix) + 1)]
    for i in range(len(right_matrix[0])):
        dp_mat[0][i+1] = right_matrix[0][i] + dp_mat[0][i]
    for i in range(len(down_matrix)):
        dp_mat[i+1][0] = down_matrix[i][0] + dp_mat[i][0]

    for i in range(1, len(dp_mat)):
        for j in range(1, len(dp_mat[0])):
            downVal = down_matrix[i-1][j]
            rightVal = right_matrix[i][j-1]

            dp_mat[i][j] = max(dp_mat[i-1][j] + downVal, dp_mat[i][j-1] + rightVal)


    return dp_mat[-1][-1]

with open('rosalind_ba5b.txt', 'r+') as f:
    values = f.readline().split()
    n, m = int(values[0]), int(values[1])
    down_matrix = []
    for i in range(n):
        line = f.readline()
        down_matrix.append([int(x) for x in line.split()])
    f.readline()
    right_matrix = []
    for i in range(n + 1):
        line = f.readline()
        right_matrix.append([int(x) for x in line.split()])

    num = findLongestGridPathLength(down_matrix, right_matrix)
    print(num)
