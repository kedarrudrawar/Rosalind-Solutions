def bwt(text):
    return ''.join([line[-1] for line in sorted([text[-i:] + text[:-i] for i in range(len(text))])])

if __name__ == '__main__':
    # with open('test69.txt', 'r+') as f:
    # with open('Datasets/rosalind_ba9i.txt', 'r+') as f:
    #     text = f.readline().rstrip()

    text = 'GCGTGCCTGGTCA$'
    text = 'AABC$'
    arr = sorted([text[-i:] + text[:-i] for i in range(len(text))])
    for line in arr:
        print(line)

    # print(text[-0:] + text[:-0])

    # transform = bwt(text)
    # print(transform)