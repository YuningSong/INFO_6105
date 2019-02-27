import pandas
import csv

data_frame = pandas.read_csv('../Part2/csv/fintech_related_keywords.csv')
related_words_rank = data_frame['Rank'].tolist()
related_words = data_frame['Word'].tolist()

learning_data = []
for id in range(8):
    print('Cluster', id+1)
    data_frame = pandas.read_csv('../Part2/csv/clusters/cluster' + str(id+1) + '.csv')
    rows = len(data_frame)
    for i in range(rows):
        tmp = {}
        tmp['Job Title'] = data_frame.iloc[i][1]
        tmp['Institution'] = data_frame.iloc[i][2]
        tmp['Is Fintech Job'] = data_frame.iloc[i][-1]
        for j in range(len(related_words)):
            tmp[related_words[j]] = data_frame.iloc[i][related_words_rank[j]+3]
        learning_data.append(tmp)

header = ['Job Title', 'Institution', 'Is Fintech Job'] + related_words
with open('csv/learning_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for tmp in learning_data:
        writer.writerow(tmp.values())

