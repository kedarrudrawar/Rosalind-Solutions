import math
import sys


def euclidean_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])**2
    return math.sqrt(sum)


def min_distance(point, centers):
    min_dist = euclidean_distance(point, centers[0])
    for i in range(1, len(centers)):
        min_dist = min(min_dist, euclidean_distance(point, centers[i]))

    return min_dist


def squared_error_distortion(points, centers):
    sum = 0
    for point in points:
        sum += min_distance(point, centers)**2

    return round(sum / len(points), 3)


if __name__ == '__main__':
    # with open('test/test80.txt', 'r+') as f:
    with open('Datasets/rosalind_ba8b.txt', 'r+') as f:
        line = f.readline().split()
        k, m = int(line[0]), int(line[1])

        centers = []
        points = []

        curr = centers
        for line in f:
            if line[0] == '-':
                curr = points
                continue
            line = line.split()
            curr.append([float(line[i]) for i in range(len(line))])

    distortion = squared_error_distortion(points, centers)
    print(distortion)


