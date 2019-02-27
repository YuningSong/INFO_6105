# -*- coding:utf-8 -*-
from __future__ import division
import pandas
from sklearn.linear_model import LogisticRegressionCV as LRCV

data = pandas.read_csv('csv/learning_data.csv')

x = data.iloc[:, 3:].values
training_index = [i for i in range(len(x)) if i % 20 != 0]   # training set index
testing_index = [i for i in range(len(x)) if i % 20 == 0]    # testing set index
x1 = x[training_index, :]                                   # training X
x2 = x[testing_index, :]                                    # testing X

y = data.iloc[:, 2:3].values
y1 = y[training_index, :]                                   # training Y
y2 = y[testing_index, :]                                    # testing Y

lr = LRCV()                                                 # create logistic regression CV object
lr.fit(x1, y1)                                              # training model

# judging accuracy
print('The average accuracy of training set is：%s' % lr.score(x1, y1))
print('The average accuracy of testing set is：%s' % lr.score(x2, y2))

print('Coefficients:\n ', lr.coef_)         # coefficient
print('Constant value:\n ', lr.intercept_)  # constant

with open('result.txt', 'w') as file:
    file.write('The average accuracy of training set is：%s\n' % lr.score(x1, y1))
    file.write('The average accuracy of testing set is：%s\n' % lr.score(x2, y2))
    file.write('Coefficients:\n ' + str(lr.coef_) + '\n')
    file.write('Constant value:\n ' + str(lr.intercept_) + '\n')

y11 = lr.predict(x)     # re-judge all the jobs

# output
top100_words = []
with open('../Part1/top_100_key_words.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n')
        tmp = line.split(',')
        top100_words.append(tmp[1])
data_frame = pandas.read_csv('../Part1/top_100_key_words_with_jobs.csv', encoding='ISO-8859-1')
for i in range(100):
    data_frame.rename(columns={data_frame.columns[i+4]: top100_words[i]}, inplace=True)
data_frame = pandas.concat([data_frame, pandas.DataFrame({"Is Fintech Job": y11.tolist()})], axis=1)
data_frame.to_csv('csv/jobs_judge_result.csv', sep=',', header=True, index=False)