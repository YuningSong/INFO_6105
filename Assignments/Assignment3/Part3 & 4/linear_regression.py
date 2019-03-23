# -*- coding:utf-8 -*-
from __future__ import division
import pandas
import numpy
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import Normalizer

data = pandas.read_csv('featured_data.csv')

x = data.iloc[:, 2:].values
# print(x)

y = data.iloc[:, 1:2].values
# print(y)

x1, x2, y1, y2 = train_test_split(x, y, random_state=1)
# print(x1.shape, x2.shape, y1.shape, y2.shape)

lr = LinearRegression()                                     # create linear regression object
lr.fit(x1, y1)                                              # training model
# print(lr.predict(x2))

# judging accuracy
print('The average accuracy of training set is：%s' % lr.score(x1, y1))
print('The average accuracy of testing set is：%s' % lr.score(x2, y2))

y11 = lr.predict(x1)
y22 = lr.predict(x2)
y0_cross = cross_val_predict(lr, x, y, cv=5)
mape_train = numpy.sum(numpy.abs((y11 - y1) / y1)) / len(y)
mape_test = numpy.sum(numpy.abs((y22 - y2) / y2)) / len(y)
mape_cross = numpy.sum(numpy.abs((y0_cross - y) / y)) / len(y)

print('Coefficients:\n ', lr.coef_)         # coefficient
print('Intercept:\n ', lr.intercept_)       # constant
print('MAPE Train(%):\n', mape_train*100)   # MAPE Train
print('MAPE Test(%):\n', mape_test*100)     # MAPE Test
print('MAPE Cross(%):\n', mape_cross*100)   # MAPE Cross


# l1 normalize
norm1 = Normalizer(norm='l1')
data_array = norm1.fit_transform(data)
x = data.iloc[:, 2:].values
y = data.iloc[:, 1:2].values
x1, x2, y1, y2 = train_test_split(x, y, random_state=1)
lr = LinearRegression()                                     # create linear regression object
lr.fit(x1, y1)                                              # training model
# judging accuracy
print('L1 Normalize:')
print('The average accuracy of training set is：%s' % lr.score(x1, y1))
print('The average accuracy of testing set is：%s' % lr.score(x2, y2))
y11 = lr.predict(x1)
y22 = lr.predict(x2)
y0_cross = cross_val_predict(lr, x, y, cv=5)
mape_train = numpy.sum(numpy.abs((y11 - y1) / y1)) / len(y)
mape_test = numpy.sum(numpy.abs((y22 - y2) / y2)) / len(y)
mape_cross = numpy.sum(numpy.abs((y0_cross - y) / y)) / len(y)
print('Coefficients:\n ', lr.coef_)         # coefficient
print('Intercept:\n ', lr.intercept_)       # constant
print('MAPE Train(%):\n', mape_train*100)   # MAPE Train
print('MAPE Test(%):\n', mape_test*100)     # MAPE Test
print('MAPE Cross(%):\n', mape_cross*100)   # MAPE Cross

# l2 normalize
norm2 = Normalizer(norm='l2')
data_array = norm1.fit_transform(data)
x = data.iloc[:, 2:].values
y = data.iloc[:, 1:2].values
x1, x2, y1, y2 = train_test_split(x, y, random_state=1)
lr = LinearRegression()                                     # create linear regression object
lr.fit(x1, y1)                                              # training model
# judging accuracy
print('L2 Normalize:')
print('The average accuracy of training set is：%s' % lr.score(x1, y1))
print('The average accuracy of testing set is：%s' % lr.score(x2, y2))
y11 = lr.predict(x1)
y22 = lr.predict(x2)
y0_cross = cross_val_predict(lr, x, y, cv=5)
mape_train = numpy.sum(numpy.abs((y11 - y1) / y1)) / len(y)
mape_test = numpy.sum(numpy.abs((y22 - y2) / y2)) / len(y)
mape_cross = numpy.sum(numpy.abs((y0_cross - y) / y)) / len(y)
print('Coefficients:\n ', lr.coef_)         # coefficient
print('Intercept:\n ', lr.intercept_)       # constant
print('MAPE Train(%):\n', mape_train*100)   # MAPE Train
print('MAPE Test(%):\n', mape_test*100)     # MAPE Test
print('MAPE Cross(%):\n', mape_cross*100)   # MAPE Cross


'''
with open('result.txt', 'w') as file:
    file.write('The average accuracy of training set is：%s\n' % lr.score(x1, y1))
    file.write('The average accuracy of testing set is：%s\n' % lr.score(x2, y2))
    file.write('Coefficients:\n ' + str(lr.coef_) + '\n')
    file.write('Intercept:\n ' + str(lr.intercept_) + '\n')
    file.write('MAPE Train(%):\n' + str(mape_train*100) + '\n')
    file.write('MAPE Test(%):\n' + str(mape_test*100) + '\n')
    file.write('MAPE Cross(%):\n' + str(mape_cross*100) + '\n')
'''
