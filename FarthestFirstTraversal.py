import math
import sys

def euclidean_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])**2
    return math.sqrt(sum)


def max_distance_centers(points, centers):
    max_dist = 0
    furthest_point = points[0]
    for point in points:
        distance = sys.maxsize
        for center in centers:
            if point in centers:
                continue
            distance = min(distance, euclidean_distance(point, center))
        if distance > max_dist and distance != sys.maxsize:
            max_dist = distance
            furthest_point = point

    return furthest_point


def farthest_first_traversal(points, k):
    centers = [points[0]]

    while len(centers) < k:
        data_point = max_distance_centers(points, centers)
        centers.append(data_point)

    return centers



if __name__ == '__main__':
    with open('Datasets/rosalind_ba8a.txt', 'r+') as f:
    # with open('extra/extra79.txt', 'r+') as f:
    # with open('test/test79.txt', 'r+') as f:
        split = f.readline().split()
        k, m = int(split[0]), int(split[1])
        points = []
        for line in f.readlines():
            point = [float(i) for i in line.split()]
            points.append(point)


    centers = farthest_first_traversal(points, k)
    for line in centers:
        list_str = map(str, line)
        print(' '.join(list_str))


