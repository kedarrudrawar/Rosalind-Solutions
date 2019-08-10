from HW.Week9.LloydClustering import *
import math


def weighted_cog(hidden_matrix_i, points):
    m = len(points[0])

    weighted_cog = [0]*m

    for i in range(m):
        numerator = sum([points[idx][i] *responsibility for idx, responsibility in enumerate(hidden_matrix_i)])
        denominator = sum([r for r in hidden_matrix_i])
        weighted_cog[i] = numerator/denominator

    return weighted_cog




def soft_clusters_to_centers(hidden_matrix, points):
    centers = [0]*len(hidden_matrix)
    for i in range(len(hidden_matrix)):
        centers[i] = weighted_cog(hidden_matrix[i], points)

    return centers


def generate_hidden_matrix(centers, points, beta):
    hidden_matrix = [[0]*len(points) for i in range(len(centers))]

    for j, p in enumerate(points):
        if p in centers:
            continue

        arr = [math.e**(-beta * euclidean_distance(p, c)) for c in centers]
        denominator = sum(arr)

        for i, c in enumerate(centers):
            numerator = math.e**(-beta * euclidean_distance(p, c))
            hidden_matrix[i][j] = numerator / denominator

    return hidden_matrix


def soft_k_means_clustering(k, beta, points):
    centers = [points[i] for i in range(k)]

    for i in range(100):
        hidden_matrix = generate_hidden_matrix(centers, points, beta)
        centers = soft_clusters_to_centers(hidden_matrix, points)

    for i in range(len(centers)):
        for j in range(len(centers[0])):
            centers[i][j] = format(centers[i][j], '.3f')

    return centers


if __name__ == '__main__':
    # with open('test/test82.txt','r+') as file:
    with open('Datasets/rosalind_ba8d.txt','r+') as file:
        split = file.readline().split()
        k, m = int(split[0]), int(split[1])
        beta = float(file.readline())

        points = []
        for line in file:
            points.append([float(i) for i in line.split()])

    centers = soft_k_means_clustering(k, beta, points)
    for c in centers:
        print(' '.join(c))