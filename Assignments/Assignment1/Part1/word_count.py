# -*- coding: utf-8 -*-
import re


def get_stop_words():
    stopwords = []
    file = open('stopwords.txt', 'r')
    for line in file:
        line = line.strip('\n')
        stopwords.append(line)
    file.close()
    return stopwords


def delete_stopwords(file_str):
    stopwords = get_stop_words()
    words_list = file_str.split(' ')
    words_list = [word for word in words_list if word not in stopwords]
    # print(len(words_list))
    return words_list


def operate_file(filename):
    file = open(filename + '.txt', 'r')
    file_str = file.read()
    file_str = file_str.lower()
    file_str = re.sub('[^a-z ]', ' ', file_str)     # delete special characters
    file_str = re.sub('\\s+', ' ', file_str)        # delete spare spaces
    word_list = delete_stopwords(file_str)          # delete stop words

    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    for key, value in word_count:
        print(key + ": " + str(value))
    return word_count


filename = 'Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services'
operate_file(filename)

