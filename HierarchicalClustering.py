def find_min_distance(distance_dict):
    return min(distance_dict, key=lambda k: distance_dict[k])


def find_distance(distance_dict, cluster1, cluster2):
    if (cluster1, cluster2) in distance_dict:
        return distance_dict[(cluster1, cluster2)]
    return distance_dict[(cluster2, cluster1)]


def find_length(cluster):
    return len(cluster.split('_'))


def set_avg_distance(distance_dict, cluster1, cluster2, cluster_array):
    cluster_array.remove(cluster1)
    cluster_array.remove(cluster2)
    copy = list(cluster_array)

    for c in copy:
        dist1 = find_distance(distance_dict, cluster1, c) * find_length(cluster1)
        dist2 = find_distance(distance_dict, cluster2, c) * find_length(cluster2)
        avg_dist = (dist1 + dist2) / (find_length(cluster1) + find_length(cluster2))

        # Remove from dictionary
        c1_tuple = (cluster1, c) if (cluster1, c) in distance_dict else (c, cluster1)
        c2_tuple = (cluster2, c) if (cluster2, c) in distance_dict else (c, cluster2)
        del distance_dict[c1_tuple]
        del distance_dict[c2_tuple]

        # Add new cluster to dictionary and array
        distance_dict[(cluster1 + '_' + cluster2, c)] = avg_dist

    cluster_array.append(cluster1 + '_' + cluster2)
    cluster_tuple = (cluster1, cluster2) if (cluster1, cluster2) in distance_dict else (cluster2, cluster1)
    del distance_dict[cluster_tuple]


def printClusters(cluster1, cluster2):
    merged = cluster1 + '_' + cluster2
    print(' '.join(merged.split("_")))


def print_dict(distance_dict):
    for elem in distance_dict:
        print(elem, ':', distance_dict[elem])


def hierarchical_clustering(distance_dict, cluster_array, n):
    while len(distance_dict) > 0:
        min_coord = find_min_distance(distance_dict)
        cluster1 = min_coord[0]
        cluster2 = min_coord[1]

        set_avg_distance(distance_dict, cluster1, cluster2, cluster_array)

        printClusters(cluster1, cluster2)









if __name__ == '__main__':
    # with open('test/test83.txt', 'r+') as file:
    with open('/Users/KedarRudrawar/Desktop/Winter Quarter 2019/BENG 181/HW/Week9/Datasets/rosalind_ba8e.txt', 'r+') as file:
        n = int(file.readline())
        distance_dict = {}
        for i, line in enumerate(file.readlines()):
            line = line.split()
            for j in range(i + 1, len(line)):
                distance_dict[(str(i + 1), str(j + 1))] = float(line[j])



    cluster_array = [str(i + 1) for i in range(n)]

    hierarchical_clustering(distance_dict, cluster_array, n)

