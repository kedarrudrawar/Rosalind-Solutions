def negateStr(num):
    if num[0] == '+':
        return '-' + num[1:]
    else:
        return '+' + num[1:]


def reverse(start, end, P):
    beg = P[:start]
    mid = P[start:end + 1]
    for i in range(len(mid)):
        mid[i] = negateStr(mid[i])
    last = P[end + 1:]

    return beg + mid[::-1] + last


def printPerm(P):
    print('(' + ' '.join(P) + ')')


def greedySorting(P):
    dist = 0
    for i in range(len(P)):
        if int(P[i]) == i + 1:
            continue
        end = i
        for j in range(i, len(P)):
            if abs(int(P[j])) == i + 1:
                end = j
                break

        P = reverse(i,end,P)
        dist += 1

        printPerm(P)
        if int(P[i]) < 0:
            P[i] = negateStr(P[i])
            dist += 1
            printPerm(P)

    return P, dist


with open('rosalind_ba6a.txt', 'r+') as file:
    permline = file.readline().rstrip()[1:-1]
    perm = permline.split()
    greedySorting(perm)
