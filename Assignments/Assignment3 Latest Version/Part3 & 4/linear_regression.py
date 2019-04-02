# -*- coding:utf-8 -*-
from __future__ import division
import pandas
import numpy
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import Normalizer

data = pandas.read_csv('featured_data.csv')
f = open('result_linear_regression.txt', 'w+')

x = data.iloc[:, 2:].values
y = data.iloc[:, 1:2].values
# Due to y can be 0, inorder to avoid the division zero exception, we need to add 1
y = y + 1

x1, x2, y1, y2 = train_test_split(x, y, random_state=1)
# print(x1.shape, x2.shape, y1.shape, y2.shape)

lr = LinearRegression()                                     # create linear regression object
lr.fit(x1, y1)                                              # training model

# Judging accuracy
print('The average accuracy of training set is: ', lr.score(x1, y1))
print('The average accuracy of testing set is: ', lr.score(x2, y2))
print('The average accuracy of training set is: ', lr.score(x1, y1), file=f)
print('The average accuracy of testing set is: ', lr.score(x2, y2), file=f)

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
print('Coefficients:\n ', lr.coef_, file=f)         # coefficient
print('Intercept:\n ', lr.intercept_, file=f)       # constant
print('MAPE Train(%):\n', mape_train*100, file=f)   # MAPE Train
print('MAPE Test(%):\n', mape_test*100, file=f)     # MAPE Test
print('MAPE Cross(%):\n', mape_cross*100, file=f)   # MAPE Cross


# L1 Normalize
norm1 = Normalizer(norm='l1')
data_array = norm1.fit_transform(data)
x = data.iloc[:, 2:].values
y = data.iloc[:, 1:2].values
y = y + 1
x1, x2, y1, y2 = train_test_split(x, y, random_state=1)
lr = LinearRegression()                                     # create linear regression object
lr.fit(x1, y1)                                              # training model
# Judging accuracy
print('\nL1 Normalize:')
print('\nL1 Normalize:', file=f)
print('The average accuracy of training set is: ', lr.score(x1, y1))
print('The average accuracy of testing set is: ', lr.score(x2, y2))
print('The average accuracy of training set is: ', lr.score(x1, y1), file=f)
print('The average accuracy of testing set is: ', lr.score(x2, y2), file=f)
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
print('Coefficients:\n ', lr.coef_, file=f)         # coefficient
print('Intercept:\n ', lr.intercept_, file=f)       # constant
print('MAPE Train(%):\n', mape_train*100, file=f)   # MAPE Train
print('MAPE Test(%):\n', mape_test*100, file=f)     # MAPE Test
print('MAPE Cross(%):\n', mape_cross*100, file=f)   # MAPE Cross

# L2 normalize
norm2 = Normalizer(norm='l2')
data_array = norm1.fit_transform(data)
x = data.iloc[:, 2:].values
y = data.iloc[:, 1:2].values
y = y + 1
x1, x2, y1, y2 = train_test_split(x, y, random_state=1)
lr = LinearRegression()                                     # create linear regression object
lr.fit(x1, y1)                                              # training model
# Judging accuracy
print('\nL2 Normalize:')
print('\nL2 Normalize:', file=f)
print('The average accuracy of training set is: ', lr.score(x1, y1))
print('The average accuracy of testing set is: ', lr.score(x2, y2))
print('The average accuracy of training set is: ', lr.score(x1, y1), file=f)
print('The average accuracy of testing set is: ', lr.score(x2, y2), file=f)
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
print('Coefficients:\n ', lr.coef_, file=f)         # coefficient
print('Intercept:\n ', lr.intercept_, file=f)       # constant
print('MAPE Train(%):\n', mape_train*100, file=f)   # MAPE Train
print('MAPE Test(%):\n', mape_test*100, file=f)     # MAPE Test
print('MAPE Cross(%):\n', mape_cross*100, file=f)   # MAPE Cross
