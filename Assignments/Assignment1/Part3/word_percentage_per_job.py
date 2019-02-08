import csv
import pandas as pd
import math

data_frame = pd.read_csv('../Part2/result_final.csv')
rows = len(data_frame)

result1 = pd.read_csv('../Part2/Huntington Bancshares/result1.csv')
job_title1 = result1['Job Title'].tolist()
result2 = pd.read_csv('../Part2/Comerica Inc/result2.csv')
job_title2 = result2['Job Title'].tolist()
job_title = job_title1 + job_title2

data = []
i = 0
for index, row in data_frame.iterrows():
    dict = {}
    dict['Job No'] = row['Job No']
    dict['Institution'] = row['Institution']
    dict['Job Title'] = job_title[math.floor(i/3)]
    i += 1
    dict['List ID'] = row['List ID']
    for j in range(100):
        dict[str(j+1)] = row[str(j+1)]
    data.append(dict)

top_keywords1 = []
with open('../Part1/csv/word_count_top100.csv', 'r', encoding='utf-8') as file:
    for line in file:
        str_list = line.split(',')
        top_keywords1.append(str_list[0])
top_keywords2 = []
with open('../Part1/csv/word_tf_idf_top100.csv', 'r', encoding='utf-8') as file:
    for line in file:
        str_list = line.split(',')
        top_keywords2.append(str_list[0])
top_keywords3 = []
with open('../Part1/csv/word_text_rank_top100.csv', 'r', encoding='utf-8') as file:
    for line in file:
        str_list = line.split(',')
        top_keywords3.append(str_list[0])

# word_total1 = {}
# word_total2 = {}
# word_total3 = {}
# for i in range(100):
#     word_total1[str(i+1)] = 0
#     word_total2[str(i+1)] = 0
#     word_total3[str(i+1)] = 0
# for dict in data:
#     if dict['List ID'] == 1:
#         for i in range(100):
#             word_total1[str(i+1)] += dict[str(i+1)]
#     elif dict['List ID'] == 2:
#         for i in range(100):
#             word_total2[str(i+1)] += dict[str(i+1)]
#     elif dict['List ID'] == 3:
#         for i in range(100):
#             word_total3[str(i+1)] += dict[str(i+1)]
# for dict in data:
#     if dict['List ID'] == 1:
#         for i in range(100):
#             dict[str(i + 1)] /= 1.0 * word_total1[str(i+1)]
#     elif dict['List ID'] == 2:
#         for i in range(100):
#             dict[str(i + 1)] /= 1.0 * word_total1[str(i+1)]
#     elif dict['List ID'] == 3:
#         for i in range(100):
#             dict[str(i + 1)] /= 1.0 * word_total1[str(i+1)]

title = ['Job No', 'Institution', 'Job Title', 'List ID']
file1 = open('list1.csv', 'w', encoding='utf-8', newline='')
file2 = open('list2.csv', 'w', encoding='utf-8', newline='')
file3 = open('list3.csv', 'w', encoding='utf-8', newline='')
writer1 = csv.writer(file1)
writer2 = csv.writer(file2)
writer3 = csv.writer(file3)
writer1.writerow(title + top_keywords1)
writer2.writerow(title + top_keywords2)
writer3.writerow(title + top_keywords3)
for dict in data:
    tmp = [dict['Job No'], dict['Institution'], dict['Job Title'], dict['List ID']]
    for i in range(100):
        tmp.append(dict[str(i+1)])
    if dict['List ID'] == 1:
        writer1.writerow(tmp)
    elif dict['List ID'] == 2:
        writer2.writerow(tmp)
    elif dict['List ID'] == 3:
        writer3.writerow(tmp)
file1.close()
file2.close()
file3.close()
