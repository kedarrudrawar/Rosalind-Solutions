with open('rosalind_ba1a.txt', 'r+') as f:
    text = f.readline().rstrip()
    pattern = f.readline().rstrip()

    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if text[i:i+k] == pattern:
            count += 1

print(count)
