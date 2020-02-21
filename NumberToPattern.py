def numToSymbol(num):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'C'
    elif num == 2:
        return 'G'
    elif num == 3:
        return 'T'

def numToPattern(i, k):
    if k == 1:
        return numToSymbol(i)
    prefixInd = i // 4
    rem = i % 4
    sym = numToSymbol(rem)
    prefix = numToPattern(prefixInd, k - 1)

    return prefix + sym

if __name__ == '__main__':
    print(numToPattern(10, 3))
    # with open('rosalind_ba1m.txt', 'r+') as f:
      #  index = int(f.readline().rstrip())
      #  k = int(f.readline().rstrip())

    # print(numToPattern(index, k))
