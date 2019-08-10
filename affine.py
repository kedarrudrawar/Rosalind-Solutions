from collections import defaultdict

def rev(string):
    str_lst = list(string)
    str = ""
    while(len(str_lst) > 0):
        str += str_lst.pop()
    return str

def score_matrix(file):
    lines = []
    for line in file:
        lines.append(line[:-1])

    score_dict = defaultdict(int)
    letters = lines[0].split()
    for x in range(1, len(lines)):
        line = lines[x].split()
        for i in range(1, len(line)):
            let1 = line[0]
            let2 = letters[i]
            score_dict[(let1, let2)] = int(line[i])
    return score_dict

def affine_traverse(v, w, score_mat):
    inf = -float('inf')
    opening = 11
    extension = 1
    lower = [[0 for j in range(len(v) + 1)] for i in range(len(w) + 1)]
    middle = [[0 for j in range(len(v) + 1)] for i in range(len(w) + 1)]
    upper = [[0 for j in range(len(v) + 1)] for i in range(len(w) + 1)]
    backtrack = [['' for j in range(len(v)+1)] for i in range(len(w)+1)]

    #initializing tables accordingly:
    upper[0][0], lower[0][0], = inf, inf
    upper[0][1], lower[1][0] = -opening, -opening

    for i in range(2, len(middle)):
        lower[i][0] = lower[i-1][0] - extension
    for j in range(2, len(middle[0])):
        upper[0][j] = upper[0][j-1] - extension

    for i in range(1, len(w)+1):
        for j in range(1, len(v)+1):
            lower[i][j] = max(lower[i-1][j]-extension, middle[i-1][j] - opening)
            upper[i][j] = max(lower[i][j-1]-extension, middle[i][j-1] - opening)
            middle[i][j] = max(lower[i][j], upper[i][j], (middle[i-1][j-1]+score_mat[(v[j-1], w[i-1])]))

            if middle[i][j] == lower[i][j]:
                backtrack[i][j] = 'd'
            elif middle[i][j] == upper[i][j]:
                backtrack[i][j] = 'r'
            elif middle[i][j] == (middle[i-1][j-1]+score_mat[(v[j-1], w[i-1])]):
                backtrack[i][j] = 'm'

    print(middle[len(middle)-1][len(middle[0])-1])
    affine_align(backtrack, v, w, len(w), len(v), "", "")

def affine_align(backtrack, v, w, i, j, lcsv, lcsw):
    if i == 0 and j == 0:
        print(rev(lcsv))
        print(rev(lcsw))
        return
    if backtrack[i][j] == 'd':
        lcsv += "-"
        lcsw += w[i-1]
        affine_align(backtrack, v, w, i-1, j, lcsv, lcsw)
    elif backtrack[i][j] == 'r':
        lcsw += "-"
        lcsv += v[j-1]
        affine_align(backtrack, v, w, i, j-1, lcsv, lcsw)
    elif backtrack[i][j] == 'm':
        lcsw += w[i-1]
        lcsv += v[j-1]
        affine_align(backtrack, v, w, i-1, j-1, lcsv, lcsw)

file = open("rosalind_ba5j.txt")
seq1 = "YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE"
seq2 = "YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE"
seq2 = "PRTEINS"
seq1 = "PRTWPSEIN"
print(float('inf'))
affine_traverse(seq1, seq2, score_matrix(open("blosum.txt")))