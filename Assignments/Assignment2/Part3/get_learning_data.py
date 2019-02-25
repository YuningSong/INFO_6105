import pandas
import csv

data_frame = pandas.read_csv('../Part2/csv/fintech_related_keywords.csv')
related_words_rank = data_frame['Rank'].tolist()
related_words = data_frame['Word'].tolist()

learning_data = []
data_frame = pandas.read_csv('../Part1/top_100_key_words_with_jobs.csv')
rows = len(data_frame)
for i in range(rows):
    tmp = {}
    tmp['Job Title'] = data_frame.loc[i][1]
    tmp['Institution'] = data_frame.loc[i][2]
    if data_frame.loc[i][35] != 0:
        tmp['Is Fintech Job'] = 1
    else:
        tmp['Is Fintech Job'] = 0
    for j in range(len(related_words)):
        tmp[related_words[j]] = data_frame.loc[i][related_words_rank[j]+3]
    learning_data.append(tmp)

header = ['Job Title', 'Institution', 'Is Fintech Job'] + related_words
with open('csv/learning_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for tmp in learning_data:
        writer.writerow(tmp.values())

