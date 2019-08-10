import sys
def minNumCoinsForChange(total, coins):
    dp_mat = [sys.maxsize]*(total + 1)
    dp_mat[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                if dp_mat[i - coin] + 1 < dp_mat[i]:
                    dp_mat[i] = dp_mat[i - coin] + 1
    return dp_mat[-1]




with open('rosalind_ba5a.txt', 'r+') as f:
    total = int(f.readline())
    coins = [int(x) for x in f.readline().split(',')]
    print(minNumCoinsForChange(total, coins))