import h2o
from h2o.estimators.xgboost import H2OXGBoostEstimator
import numpy as np
h2o.init()


# Import a sample binary outcome training set into H2O
train = h2o.import_file("loan_top100.csv")

x = train.columns
y = "int_rate"
x.remove(y)

# try using the `keep_cross_validation_predictions` (boolean parameter):
# first initialize your estimator, set nfolds parameter
xgb = H2OXGBoostEstimator(keep_cross_validation_predictions = True)

from h2o.estimators.gbm import H2OGradientBoostingEstimator
gbm_model = H2OGradientBoostingEstimator()
gbm_model.train(x = ["loan_amnt", "annual_inc", "dti", "delinq_2yrs", "inq_last_6mths", "total_acc"], y = "int_rate", training_frame=train)

print(gbm_model)
print(y)

gbm_model.predict(train)

#Mean Absolute Percentage Error for Linear Regression Model
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100