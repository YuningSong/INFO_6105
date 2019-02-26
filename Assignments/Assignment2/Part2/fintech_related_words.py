import numpy
import pandas

centroids = numpy.loadtxt(open('csv/cluster_center.csv', 'r'), delimiter=',', skiprows=0)
row, col = centroids.shape

top100_words = []
with open('../Part1/top_100_key_words.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        tmp = line.split(',')
        top100_words.append(tmp[1])

cluster_related_words = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
related_words = {}
for i in range(row):
    for j in range(col):
        if centroids[i, j] >= 2:
            cluster_related_words[i+1].append(top100_words[j])
            if top100_words[j] not in related_words:
                related_words[j+1] = top100_words[j]

related_words = sorted(related_words.items(), key=lambda item: item[0])
print(len(related_words), related_words)
with open('csv/fintech_related_keywords.csv', 'w') as file:
    file.write('Rank,Word\n')
    for key, value in related_words:
        file.write(str(key) + ',' + value + '\n')

data_frame = pandas.DataFrame({
    "Cluster1": cluster_related_words[1],
    "Cluster2": cluster_related_words[2],
    "Cluster3": cluster_related_words[3],
    "Cluster4": cluster_related_words[4],
    "Cluster5": cluster_related_words[5],
    "Cluster6": cluster_related_words[6],
    "Cluster7": cluster_related_words[7],
    "Cluster8": cluster_related_words[8]
})
data_frame.to_csv('csv/fintech_related_keywords_divided_into_clusters.csv', sep=',', header=True, index=False)
