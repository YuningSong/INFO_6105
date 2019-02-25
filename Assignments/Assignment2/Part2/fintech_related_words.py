import numpy

centroids = numpy.loadtxt(open('csv/cluster_center.csv', 'r'), delimiter=',', skiprows=0)
row, col = centroids.shape

top100_words = []
with open('../Part1/top_100_key_words.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        tmp = line.split(',')
        top100_words.append(tmp[1])

related_words = {}
for i in range(row):
    for j in range(col):
        if centroids[i, j] >= 2 and top100_words[j] not in related_words:
            related_words[j+1] = top100_words[j]
related_words = sorted(related_words.items(), key=lambda item: item[0])
print(len(related_words), related_words)
with open('csv/fintech_related_keywords.csv', 'w') as file:
    file.write('Rank,Word\n')
    for key, value in related_words:
        file.write(str(key) + ',' + value + '\n')
