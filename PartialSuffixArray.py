from HW.Week7.SuffixArray import suffixArray

def partial_suffix_array(text, K):
    suffix_array = suffixArray(text)

    for i, elem in enumerate(suffix_array):
        if int(suffix_array[i]) % K == 0:
            print(str(i) + ',' + suffix_array[i])

if __name__ == '__main__':
    # with open('test/test77.txt', 'r+') as f:
    with open('Datasets/rosalind_ba9q.txt', 'r+') as f:
        text = f.readline().rstrip()
        K = int(f.readline())

    partial_suffix_array(text, K)
