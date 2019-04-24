# -*- coding: utf-8 -*-
import re
import codecs
import math
from summa import keywords
from summa.summarizer import summarize

file_num = 4


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


# Get Word List
def get_words(filename):
    file = codecs.open(filename + '.txt', 'r', 'utf-8')
    file_str = file.read()
    file_str = file_str.lower()
    file_str = re.sub('\\s{2,}|\t|\n', ' ', file_str)                              # delete \t \n
    file_str = re.sub('\\s+', ' ', file_str)                                       # delete spare spaces
    words = file_str.split(' ')
    words = [word for word in words if word.find("@") < 0 and word.find("/") < 0]  # delete links and mail box addresses
    file_str = ' '.join(words)
    file_str = re.sub('[^a-z\']', ' ', file_str)                                   # delete special characters
    file_str = re.sub('\\s+', ' ', file_str)                                       # delete spare spaces
    word_list = delete_stopwords(file_str)                                         # delete stop words
    word_list = [word for word in word_list if '\'' not in word]
    file.close()
    return word_list


def get_word_count(words):
    word_dict = {}
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict


def get_tf_idf(words, word_cnt, word_appear):
    tf_idf = {}
    total_word_count = len(words)
    for key, value in word_cnt.items():
        tf = 1.0 * value / total_word_count
        idf = math.log(1.0 * file_num / word_appear[key])
        tf_idf[key] = tf * idf
    return tf_idf


def get_text_rank(filename):
    file = codecs.open(filename + '.txt', 'r', 'utf-8')
    summary = summarize(file.read(), ratio=0.1)
    result = keywords.keywords(summary, scores=True)
    file.close()
    return result


filename1 = 'txt/Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services'
filename2 = 'txt/WEF_A_Blueprint_for_Digital_Identity'
filename3 = 'txt/WEF_The_future__of_financial_services'
filename4 = 'txt/WEF_The_future_of_financial_infrastructure'
words1 = get_words(filename1)
words2 = get_words(filename2)
words3 = get_words(filename3)
words4 = get_words(filename4)
word_list = words1 + words2 + words3 + words4
word_appear_count = {}
for word in word_list:
    word_appear_count[word] = 0
    if word in words1:
        word_appear_count[word] += 1
    if word in words2:
        word_appear_count[word] += 1
    if word in words3:
        word_appear_count[word] += 1
    if word in words4:
        word_appear_count[word] += 1
word_count = get_word_count(word_list)
word_tf_idf = get_tf_idf(word_list, word_count, word_appear_count)
word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
word_tf_idf = sorted(word_tf_idf.items(), key=lambda item: item[1], reverse=True)
# text rank
# text_rank1 = get_text_rank(filename1)
# text_rank2 = get_text_rank(filename2)
# text_rank3 = get_text_rank(filename3)
# text_rank4 = get_text_rank(filename4)
# word_text_rank = {}
# for word in word_count:
#     word_text_rank[word] = 0
# for score in text_rank1:
#     word_text_rank[score[0]] += score[1]
# for score in text_rank2:
#     word_text_rank[score[0]] += score[1]
# for score in text_rank3:
#     word_text_rank[score[0]] += score[1]
# for score in text_rank4:
#     word_text_rank[score[0]] += score[1]
# for key in word_text_rank:
#     word_text_rank[key] /= 1.0 * word_appear_count[key]
# word_text_rank = sorted(word_text_rank.items(), key=lambda item: item[1], reverse=True)
'''
for key, value in word_count:
    print(key + ": " + str(value))
'''
csvfile = codecs.open('csv/word_count.csv', 'w', 'utf-8')
csvfile.write("Word,Count\n")
for key, value in word_count:
    csvfile.write(key + "," + str(value) + "\n")
csvfile.close()

csvfile = codecs.open('csv/word_tf_idf.csv', 'w', 'utf-8')
csvfile.write("Word,TF-IDF\n")
for key, value in word_tf_idf:
    csvfile.write(key + "," + str(value) + "\n")
csvfile.close()

# csvfile = codecs.open('csv/word_text_rank.csv', 'w', 'utf-8')
# csvfile.write("Word,Text Rank Score\n")
# for key, value in word_text_rank:
#     csvfile.write(key + "," + str(value) + "\n")
# csvfile.close()


