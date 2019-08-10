import math
import sys

def center_of_gravity(cluster):
    cog = [0]*len(cluster[0])
    for point in cluster:
        for i in range(len(point)):
            cog[i] += point[i]

    cog = [cog[i]/len(cluster) for i in range(len(cog))]
    return cog


def euclidean_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i])**2
    return math.sqrt(sum)


def centers_to_clusters(centers, points):
    clusters = [[] for _ in range(len(centers))]

    for p in points:
        min_dist = sys.maxsize
        clust = 0
        for i, c in enumerate(centers):
            if min_dist > euclidean_distance(p, c):
                min_dist = euclidean_distance(p, c)
                clust = i

        clusters[clust].append(p)

    return centers, clusters


def clusters_to_centers(clusters, centers):
    for i, cluster in enumerate(clusters):
        centers[i] = center_of_gravity(cluster)

    return centers


def lloyd_clustering(points, k):
    centers = [points[i] for i in range(k)]
    clusters = [0]

    prev_centers, prev_clusters = None, None

    while prev_centers != centers and prev_clusters != clusters:
        prev_clusters = list(clusters)
        prev_centers = list(centers)

        centers, clusters = centers_to_clusters(centers, points)
        centers = clusters_to_centers(clusters, centers)

    for c in centers:
        for i in range(len(c)):
            c[i] = format(round(c[i], 3), '.3f')

    return centers


if __name__ == '__main__':
    # with open('test/test81.txt', 'r+') as file:
    # with open('Datasets/rosalind_ba8c.txt', 'r+') as file:
    with open('/Users/KedarRudrawar/Downloads/rosalind_ba8c-4.txt', 'r+') as file:
        split = file.readline().split()
        k, m = int(split[0]), int(split[1])
        points = []
        for line in file:
            points.append([float(i) for i in line.split()])

    centers = lloyd_clustering(points, k)
    for c in centers:
        mapped = map(str, c)
        print(' '.join(mapped))




