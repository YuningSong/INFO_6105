# -*- coding:utf-8 -*-
from __future__ import division
import pandas as pd
from sklearn.linear_model import LogisticRegressionCV as LRCV

data = pd.read_csv('csv/learning_data.csv')

x = data.iloc[:, 3:].values
training_index = [v for v in range(len(x)) if v % 5 == 0]   # training set index
testing_index = [v for v in range(len(x)) if v % 5 != 0]    # testing set index
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

print('Coefficients:\n ', lr.coef_)       # coefficient
print('Constant value:\n ', lr.intercept_)  # constant

with open('result.txt', 'w') as file:
    file.write('The average accuracy of training set is：%s\n' % lr.score(x1, y1))
    file.write('The average accuracy of testing set is：%s\n' % lr.score(x2, y2))
    file.write(str(lr.coef_) + '\n')
    file.write(str(lr.intercept_))
