# -*- coding: utf-8 -*-
import re
import codecs

word_count = {}


def get_stop_words():
    stopwords = []
    file = open('stopwords.txt', 'r')
    file_str = file.read()
    file_str = re.sub('[^a-z\']', ' ', file_str)
    words = file_str.split(' ')
    file.close()
    return words


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
    file_str = re.sub('[^a-z\']', ' ', file_str)     # delete special characters
    file_str = re.sub('\\s+', ' ', file_str)        # delete spare spaces
    word_list = delete_stopwords(file_str)          # delete stop words
    word_list = [word for word in word_list if '\'' not in word]

    global word_count
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    file.close()


filename1 = 'Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services'
filename2 = 'WEF_A_Blueprint_for_Digital_Identity'
filename3 = 'WEF_The_future__of_financial_services'
filename4 = 'WEF_The_future_of_financial_infrastructure'
operate_file(filename1)
operate_file(filename2)
operate_file(filename3)
operate_file(filename4)
word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
'''
for key, value in word_count:
    print(key + ": " + str(value))
'''
csvfile = codecs.open('word_count.csv', 'w', 'utf-8')
csvfile.write("Word,Count\n")
for key, value in word_count:
    csvfile.write(key + "," + str(value) + "\n")
csvfile.close()



