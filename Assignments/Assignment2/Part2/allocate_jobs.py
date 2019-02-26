import numpy
import pandas
import csv


def load_data(filepath):
    """
    :param filepath:
    :return: A numpy matrix of words appear numbers which jobs contain 'fintech' keyword
    """
    data_frame = pandas.read_csv(filepath)
    rows = len(data_frame)

    vector_set = []
    job_info = []
    for i in range(rows):
        info = data_frame.iloc[i]
        job_info.append(info)
        vector = []
        for j in range(100):
            vector.append(data_frame.loc[i][j+4])
        vector_set.append(vector)
    print(len(vector_set))
    return job_info, numpy.mat(vector_set)


def calculate_euclidean_distance(vector1, vector2):
    """
    Calculate euclidean distance between two vectors

    :param vector1:
    :param vector2:
    :return: The euclidean distance between vector1 and vector2
    """
    return numpy.sqrt(numpy.sum(numpy.power(vector1 - vector2, 2)))


job_info, word_vector_set = load_data('../Part1/top_100_key_words_with_jobs.csv')
centroids = numpy.loadtxt(open('csv/cluster_center.csv', 'r'), delimiter=',', skiprows=0)
row, col = word_vector_set.shape
print('read finished')

cluster_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
for i in range(row):
    min_dist = numpy.inf
    min_id = -1
    for j in range(8):
        dist = calculate_euclidean_distance(centroids[j, :], word_vector_set[i, :])
        if dist < min_dist:
            min_dist = dist
            min_id = j
    cluster_dict[min_id+1].append(job_info[i])
print('calculate finished')

top100_words = []
with open('../Part1/top_100_key_words.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        tmp = line.split(',')
        top100_words.append(tmp[1])

header = ['Job Number', 'Job Title', 'Institution', 'URL'] + top100_words
for key, value in cluster_dict.items():
    with open('csv/clusters/cluster' + str(key) + '.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for tmp in value:
            writer.writerow(tmp)
