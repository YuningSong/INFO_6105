import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split

data_array = pd.read_csv('featured_data.csv')

x = data_array.iloc[:, 2:].values
y = data_array.iloc[:, 1:2].values
y = y + 1
x2, x3, y2, y3 = train_test_split(x, y, random_state=1)

scaler = StandardScaler()  # standard scaler
scaler.fit(x2)             # training data
x2 = scaler.transform(x2)  # transform dataset

clf = MLPRegressor()
clf.fit(x2, y2.ravel())

y31 = clf.predict(x3)
mape_test = sum(np.abs((y31 - y3) / y3)) / len(y3) * 100
print('The network test mape is:\n', mape_test)

y21 = clf.predict(x2)
mape_train = sum(np.abs((y21 - y2) / y2)) / len(y2) * 100
print('The network training mape is:\n', mape_train)

y0 = cross_val_predict(clf, x3, y3, cv=5)
mape_cross = sum(np.abs((y0 - y3) / y3)) / len(y3) * 100
print('The forest mape (cross validation) is:\n', mape_cross)

# optimization
clf = MLPRegressor(learning_rate='constant', learning_rate_init=0.001, solver='lbfgs', alpha=1e-5,
                   hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(x2, y2.ravel())

y31 = clf.predict(x3)
mape_test = sum(np.abs((y31 - y3) / y3)) / len(y3) * 100
print('The network test mape is:\n', mape_test)

y21 = clf.predict(x2)
mape_train = sum(np.abs((y21 - y2) / y2)) / len(y2) * 100
print('The network training mape is:\n', mape_train)

y0 = cross_val_predict(clf, x3, y3, cv=5)
mape_cross = sum(np.abs((y0 - y3) / y3)) / len(y3) * 100
print('The forest mape (cross validation) is:\n', mape_cross)
