import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
import pandas as pd
data = pd.read_csv('/Users/yuningsong/Desktop/Info6105/featured_data.csv',sep=',')
data = data[0:4000]
X = data[data.columns[1:]]
y = data[data.columns[0]]
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=1)
automl = autosklearn.classification.AutoSklearnClassifier()
automl.fit(X_train, y_train)
y_hat = automl.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))