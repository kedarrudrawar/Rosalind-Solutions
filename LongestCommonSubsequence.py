def initialize_mat(s1, s2):
    dp_mat = [[0] * len(s1) for _ in range(len(s2))]

    currCount = 0
    for i in range(len(dp_mat)):
        if s1[0] == s2[i]:
            if currCount == 0:
                currCount = 1
        dp_mat[i][0] = currCount

    currCount = 0
    for i in range(len(dp_mat[0])):
        if s1[i] == s2[0]:
            if currCount == 0:
                currCount = 1
        dp_mat[0][i] = currCount

    return dp_mat

def findLongestCommonSubseq(s1, s2):
    dp_mat = initialize_mat(s1, s2)

    for i in range(1, len(dp_mat)):
        for j in range(1, len(dp_mat[0])):
            var = 1 if s2[i] == s1[j] else 0
            dp_mat[i][j] = max(max(dp_mat[i-1][j-1] + var, dp_mat[i][j-1]), dp_mat[i-1][j])

    i = len(dp_mat) - 1
    j = len(dp_mat[0]) - 1
    lcs = ''
    while i != -1 and j != -1:
        if i == 0 or j == 0:
            if i == 0 and j == 0:
                return s1[j] + lcs
            if i == 0:
                if dp_mat[i][j] == dp_mat[i][j-1]:
                    j -= 1
                    continue
                return s1[j] + lcs
            if j == 0:
                if dp_mat[i][j] == dp_mat[i-1][j]:
                    i -= 1
                    continue
                return s1[j] + lcs

        if dp_mat[i][j] == dp_mat[i-1][j]:
            i -= 1
            continue
        elif dp_mat[i][j] == dp_mat[i][j-1]:
            j -= 1
            continue
        elif dp_mat[i][j] == dp_mat[i-1][j-1]:
            i -= 1
            j -= 1
            continue

        lcs = s1[j] + lcs
        i -= 1
        j -= 1

    return lcs


with open('test.txt', 'r+') as f:
    str1 = f.readline().rstrip()
    str2 = f.readline().rstrip()
    lcs = findLongestCommonSubseq(str1, str2)
    print(lcs)
