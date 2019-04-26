from math import ceil
import csv
import os


def dataset_path():
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), '../dataset/yelp_feature.csv')


def cal_dataset_pages(filepath, limits):
    with open(filepath, 'r+', encoding='utf-8') as f:
        row_length = len(f.readlines())
        pages = int(ceil(row_length / limits))
    return pages


def show_csv(filepath, page, limit):
    with open(filepath, 'r+', encoding='utf-8') as f:
        reader = csv.reader(f)
        data_frame = []
        for row in reader:
            if reader.line_num == 1:
                data_frame.append(row)
            if (page - 1) * limit + 1 < reader.line_num <= page * limit + 1:
                row[0] = float(row[0])
                row[1] = int(row[0])
                row[2] = int(row[0])
                row[3] = int(row[0])
                row[4] = float(row[0])
                row[5] = float(row[0])
                data_frame.append(row)
    return data_frame
