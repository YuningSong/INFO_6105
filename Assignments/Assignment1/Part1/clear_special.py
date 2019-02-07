# -*- coding: utf-8 -*-
import re
import codecs


def get_stop_words():
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
    return words_list


file = codecs.open('txt/Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services.txt', 'r', 'utf-8')
file_str = file.read()
file_str = file_str.lower()
file_str = re.sub('\\s{2,}|\t|\n', ' ', file_str)
file_str = re.sub('\\s+', ' ', file_str)
words = file_str.split(' ')
words = [word for word in words if word.find("@") < 0 and word.find("/") < 0]
file_str = ' '.join(words)
file_str = re.sub('[^a-z\']', ' ', file_str)
file_str = re.sub('\\s+', ' ', file_str)
words = delete_stopwords(file_str)
words = [word for word in words if len(word) > 3]
print(len(words))
'''
for word in words:
    print(word)
'''
# print(len(words))
