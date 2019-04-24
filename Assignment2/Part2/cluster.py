import numpy


def calculate_euclidean_distance(vector1, vector2):
    """
    Calculate euclidean distance between two vectors

    :param vector1:
    :param vector2:
    :return: The euclidean distance between vector1 and vector2
    """
    return numpy.sqrt(numpy.sum(numpy.power(vector1 - vector2, 2)))


def rand_centroids(vector_set, k):
    """
    Initialize centroids of k clusters
    Select k existing vectors in vector set as initial centroid vectors

    :param vector_set: The set of vectors (Type: Matrix)
    :param k:          Number of clusters
    :return:           k initial centroid vectors
    """
    rand_row = numpy.arange(vector_set.shape[0])
    numpy.random.shuffle(rand_row)
    return vector_set[rand_row[0: k]]


def k_means(vector_set, k, times=30):
    """
    K-Means Clustering Algorithm
    Create k initial centroid vectors at first
    In each iteration, assign each vector in vector set to the nearest centroid vector,
    then re-calculate the centroid vector of each cluster.

    :param vector_set: The set of vectors (Type: Matrix)
    :param k:          Number of clusters
    :param times:      Times to iterate
    :return:           centroids of k clusters, clusters list
    """
    row, col = numpy.shape(vector_set)
    cluster_assess = numpy.mat(numpy.zeros((row, 2)))
    centroids = rand_centroids(vector_set, k)
    # print(centroids)

    # cluster_changed = True
    # cnt = 0
    # while cluster_changed:
    #     cluster_changed = False
    #     cnt += 1
    for cnt in range(times):
        print('Loop', cnt)
        for i in range(row):
            min_dist = numpy.inf
            min_id = -1
            for j in range(k):
                dist = calculate_euclidean_distance(centroids[j, :], vector_set[i, :])
                if dist < min_dist:
                    min_dist = dist
                    min_id = j
            # if cluster_assess[i, 0] != min_id:
            #     cluster_changed = True
            cluster_assess[i, :] = min_id, min_dist
        for i in range(k):
            vectors_in_cluster = vector_set[numpy.nonzero(cluster_assess[:, 0] == i)[0]]
            centroids[i, :] = numpy.rint(numpy.mean(vectors_in_cluster, axis=0))
    return centroids, cluster_assess


word_vector_set = numpy.loadtxt(open('csv/job_words.csv', 'r'), delimiter=',', skiprows=0)
center, clusters = k_means(word_vector_set, 8, times=30)
print(center)
numpy.savetxt('csv/cluster_center.csv', center, delimiter=',')
