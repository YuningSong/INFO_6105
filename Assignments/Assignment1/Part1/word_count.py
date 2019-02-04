# -*- coding: utf-8 -*-
import re
import codecs
from collections import Counter


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
    file = codecs.open(filename + '.txt', 'r', 'utf-8')
    file_str = file.read()
    file_str = file_str.lower()
    file_str = re.sub('[^a-z ]', ' ', file_str)    # delete special characters
    file_str = re.sub('\\s+', ' ', file_str)        # delete spare spaces
    word_list = delete_stopwords(file_str)          # delete stop words

    count = {}
    for word in word_list:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    return count


filename1 = 'Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services'
filename2 = 'WEF_A_Blueprint_for_Digital_Identity'
filename3 = 'WEF_The_future__of_financial_services'
filename4 = 'WEF_The_future_of_financial_infrastructure'
word_count1 = operate_file(filename1)
word_count2 = operate_file(filename2)
word_count3 = operate_file(filename3)
word_count4 = operate_file(filename4)
word_count1 = Counter(word_count1)
word_count2 = Counter(word_count2)
word_count3 = Counter(word_count3)
word_count4 = Counter(word_count4)
word_count = dict(word_count1 + word_count2 + word_count3 + word_count4)
'''
for key, value in word_count:
    print(key + ": " + str(value))
'''
csvfile = codecs.open('word_count.csv', 'w', 'utf-8')
csvfile.write("Word,Count\n")
for key, value in word_count:
    csvfile.write(key + "," + str(value) + "\n")
csvfile.close()



