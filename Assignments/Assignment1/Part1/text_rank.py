# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from summa import keywords
import re
import codecs

file_list = ['Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services',
             'WEF_A_Blueprint_for_Digital_Identity',
             'WEF_The_future__of_financial_services',
             'WEF_The_future_of_financial_infrastructure']


# read pdf file
def parse(file_name):
    file_string_list = []
    fp = open("pdf/" + file_name + ".pdf", 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    results = x.get_text()
                    file_string_list.append(results)
    return file_string_list


def get_list_text_rank_score(str_list):
    score_list = []
    for string in str_list:
        result = keywords.keywords(string, scores=True)
        score_list.append(result)
    return score_list


def get_stop_words():
    file = open('stopwords.txt', 'r')
    file_str = file.read()
    file_str = re.sub('[^a-z\']', ' ', file_str)
    words = file_str.split(' ')
    file.close()
    return words


def delete_stopwords(words_dict):
    stop_words = get_stop_words()
    words_dic = words_dict
    keys = words_dic.keys()
    for key in list(keys):
        if key in stop_words:
            del words_dic[key]
    return words_dic


def get_text_rank(file_name_list):
    file_str_list = []
    for file_name in file_name_list:
        file_str_list += parse(file_name)

    page_num = len(file_str_list)
    text_rank_lists = get_list_text_rank_score(file_str_list)
    text_rank = {}
    for page_text_rank_list in text_rank_lists:
        for word_tuple in page_text_rank_list:
            if word_tuple[0] not in text_rank:
                text_rank[word_tuple[0]] = word_tuple[1]
            else:
                text_rank[word_tuple[0]] += word_tuple[1]
    text_rank = delete_stopwords(text_rank)
    text_rank = sorted(text_rank.items(), key=lambda item: item[1], reverse=True)
    for key, value in text_rank:
        value /= 1.0 * page_num
    return text_rank


text_rank_score = get_text_rank(file_list)
csvfile = codecs.open('csv/word_text_rank.csv', 'w', 'utf-8')
csvfile.write("Word,Text Rank Score\n")
for key, value in text_rank_score:
    csvfile.write(key + "," + str(value) + "\n")
csvfile.close()

