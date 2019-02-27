# -*- coding:utf-8 -*-
from __future__ import division
import csv
import luigi
import pandas as pd
from sklearn.linear_model import LogisticRegressionCV as LRCV

data_frame = pd.read_csv('../Part2/csv/fintech_related_keywords.csv')
related_words_rank = data_frame['Rank'].tolist()
related_words = data_frame['Word'].tolist()
learning_data = []
data_frame = pd.read_csv('../Part1/top_100_key_words_with_jobs.csv')
#data = pd.read_csv('../Part3/csv/learning_data.csv')
rows = len(data_frame)

class Get_Learning_Data(luigi.Task):

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("../Part3/csv/learning_data.csv")

    def run(self):
        with self.output().open('w') as f:
            for i in range(rows):
                tmp = {}
                tmp['Job Title'] = data_frame.loc[i][1]
                tmp['Institution'] = data_frame.loc[i][2]
                if data_frame.loc[i][35] != 0:
                    tmp['Is Fintech Job'] = 1
                else:
                    tmp['Is Fintech Job'] = 0
                for j in range(len(related_words)):
                    tmp[related_words[j]] = data_frame.loc[i][related_words_rank[j] + 3]
                learning_data.append(tmp)

            header = ['Job Title', 'Institution', 'Is Fintech Job'] + related_words
            writer = csv.writer(f)
            writer.writerow(header)
            for tmp in learning_data:
                writer.writerow(tmp.values())

class Regression(luigi.Task):

    def requires(self):
        return [Get_Learning_Data()]

    def output(self):
        return luigi.LocalTarget("../Part3/result.txt")

    def run(self):
        with  self.output().open('w') as fout:
            data = pd.read_csv('../Part3/csv/learning_data.csv')
            x = data.iloc[:, 3:].values
            training_index = [v for v in range(len(x)) if v % 5 == 0]  # training set index
            testing_index = [v for v in range(len(x)) if v % 5 != 0]  # testing set index
            x1 = x[training_index, :]  # training X
            x2 = x[testing_index, :]  # testing X

            y = data.iloc[:, 2:3].values
            y1 = y[training_index, :]  # training Y
            y2 = y[testing_index, :]  # testing Y

            lr = LRCV()  # create logistic regression CV object
            lr.fit(x1, y1)  # training model
            fout.write('The average accuracy of training set is：%s\n' % lr.score(x1, y1))
            fout.write('The average accuracy of testing set is：%s\n' % lr.score(x2, y2))
            fout.write(str(lr.coef_) + '\n')
            fout.write(str(lr.intercept_))

if __name__ == '__main__':
    luigi.run()
