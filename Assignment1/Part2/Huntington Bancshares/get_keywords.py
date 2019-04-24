import pandas as pd
import re
import csv


def get_stop_words():
    file = open('../../Part1/stopwords.txt', 'r')
    file_str = file.read()
    file_str = re.sub('[^a-z\']', ' ', file_str)
    words = file_str.split(' ')
    file.close()
    return words


def delete_stopwords(file_str):
    stopwords = get_stop_words()
    words_list = file_str.split(' ')
    words_list = [word for word in words_list if word not in stopwords]
    return words_list


def get_words(file_str):
    file_str = file_str.lower()
    file_str = re.sub('[^a-z\']', ' ', file_str)                                   # delete special characters
    file_str = re.sub('\\s+', ' ', file_str)                                       # delete spare spaces
    word_list = delete_stopwords(file_str)                                         # delete stop words
    word_list = [word for word in word_list if '\'' not in word or word is '']
    return word_list


def get_word_frequency(words):
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


data_frame = pd.read_csv('result1.csv')
columns = data_frame.columns.tolist()
rows = len(data_frame)

urls = data_frame[columns[1]].tolist()
job_title = data_frame[columns[2]].tolist()
location = data_frame[columns[5]].tolist()
job_description = data_frame[columns[7]].tolist()

data = []
for i in range(rows):
    dict = {}
    dict['url'] = urls[i]
    dict['job_title'] = job_title[i]
    dict['location'] = location[i]
    dict['description'] = job_description[i]
    dict['word_list'] = get_words(dict['description'])
    #print(dict['word_list'])
    dict['word_frequency'] = get_word_frequency(dict['word_list'])
    # print(dict['word_frequency'])
#    dict['word_frequency_ranked'] = sorted(dict['word_frequency'].items(), key=lambda item: item[1], reverse=True)
    data.append(dict)

top_keywords_csv = open('../../Part1/csv/word_count_top100.csv', 'r', encoding='utf-8')
top_keywords = []
for line in top_keywords_csv:
    str_list = line.split(',')
    top_keywords.append(str_list[0])
for dict in data:
    word_counter = {}
    for word in top_keywords:
        if word in dict['word_frequency']:
            word_counter[word] = dict['word_frequency'][word]
        else:
            word_counter[word] = 0
        # print(word_counter)
    dict['word_counter'] = word_counter

top_keywords_csv = open('../../Part1/csv/word_tf_idf_top100.csv', 'r', encoding='utf-8')
top_keywords = []
for line in top_keywords_csv:
    str_list = line.split(',')
    top_keywords.append(str_list[0])
for dict in data:
    word_counter = {}
    for word in top_keywords:
        if word in dict['word_frequency']:
            word_counter[word] = dict['word_frequency'][word]
        else:
            word_counter[word] = 0
        # print(word_counter)
    dict['word_tf_idf'] = word_counter

top_keywords_csv = open('../../Part1/csv/word_text_rank_top100.csv', 'r', encoding='utf-8')
top_keywords = []
for line in top_keywords_csv:
    str_list = line.split(',')
    top_keywords.append(str_list[0])
for dict in data:
    word_counter = {}
    for word in top_keywords:
        if word in dict['word_frequency']:
            word_counter[word] = dict['word_frequency'][word]
        else:
            word_counter[word] = 0
        # print(word_counter)
    dict['word_text_rank'] = word_counter


header = ["Job No", "Institution", "URL", "List ID"]
for i in range(100):
    header.append(str(i+1))
with open('result_Huntington Bancshares.csv', "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    i = 0
    for dict in data:
        i += 1
        csv_list = [i, 'Huntington Bancshares', dict['url'], 1]
        csv_list += dict['word_counter'].values()
        writer.writerow(csv_list)
        csv_list = [i, 'Huntington Bancshares', dict['url'], 2]
        csv_list += dict['word_tf_idf'].values()
        writer.writerow(csv_list)
        csv_list = [i, 'Huntington Bancshares', dict['url'], 3]
        csv_list += dict['word_text_rank'].values()
        writer.writerow(csv_list)
