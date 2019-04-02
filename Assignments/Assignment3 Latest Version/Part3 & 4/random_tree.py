from __future__ import division
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict

data_array = pd.read_csv('featured_data.csv')

x = data_array.iloc[:, 2:].values
y = data_array.iloc[:, 1:2].values
# Due to y can be 0, inorder to avoid the division zero exception, we need to add 1
y = y + 1

x2, x3, y2, y3 = train_test_split(x, y, random_state=1)

dtr = GradientBoostingRegressor()
dtr.fit(x2, y2)

y31 = dtr.predict(x3)
mape_test = sum(np.abs((y31 - y3) / y3)) / len(y3) * 100
print('The forest test mape is:\n', mape_test)

y21 = dtr.predict(x2)
mape_train = sum(np.abs((y21 - y2) / y2)) / len(y2) * 100
print('The forest training mape is:\n', mape_train)

y0 = cross_val_predict(dtr, x, y, cv=5)
mape_cross = sum(np.abs((y0 - y) / y)) / len(y) * 100
print('The forest mape (cross validation) is:\n', mape_cross)


# optimization
x = data_array.iloc[:, 2:].values
y = data_array.iloc[:, 1:2].values
y = y + 1
x2, x3, y2, y3 = train_test_split(x, y, random_state=1)

dtr = GradientBoostingRegressor(n_estimators=200, max_depth=15)
dtr.fit(x2, y2)

y31 = dtr.predict(x3)
mape_train = sum(np.abs((y31 - y3) / y3)) / len(y3) * 100
print('The forest test mape is:\n', mape_train)

y21 = dtr.predict(x2)
mape_test = sum(np.abs((y21 - y2) / y2)) / len(y2) * 100
print('The forest training mape is:\n', mape_test)

y0 = cross_val_predict(dtr, x, y, cv=5)
mape_cross = sum(np.abs((y0 - y) / y)) / len(y) * 100
print('The forest mape (cross validation) is:\n', mape_cross)
