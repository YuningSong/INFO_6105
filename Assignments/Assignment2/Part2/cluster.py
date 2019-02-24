import pandas

word_list = []
with open('../Part1/top_100_key_words_all_teams.csv', 'r', encoding='utf-8') as file:
    for line in file:
        tmp = line.split(',')
        word_list.append(tmp[1])

data_frame = pandas.read_csv('../Part1/TeamAll.csv')
columns = data_frame.columns.tolist()
rows = len(data_frame)
job_title = data_frame[columns[1]].tolist()
institution = data_frame[columns[2]].tolist()

data = []
for i in range(rows):
    dict = {}
    dict['job_title'] = job_title[i]
    dict['institution'] = institution[i]
    for j in range(100):
        dict[word_list[j]] = data_frame[columns[j+3].tolist()[i]]
    data.append(dict)

