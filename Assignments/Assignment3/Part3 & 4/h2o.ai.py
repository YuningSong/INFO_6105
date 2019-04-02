import h2o
import numpy as np
from h2o.estimators.xgboost import H2OXGBoostEstimator
from h2o.estimators.gbm import H2OGradientBoostingEstimator
h2o.init()
train = h2o.import_file("loan_tmp1.csv")

x = train.columns
y = "grade"
x.remove(y)

# try using the `keep_cross_validation_predictions` (boolean parameter):
# first initialize your estimator, set nfolds parameter
xgb = H2OXGBoostEstimator(keep_cross_validation_predictions = True)

gbm_model = H2OGradientBoostingEstimator()
gbm_model.train(x=["annual_inc", "dti", "pub_rec", "int_rate", "loan_amnt", "total_rec_int", "inq_last_6mths",
                   "installment", "open_acc", "collection_recovery_fee", "collections_12_mths_ex_med", "delinq_2yrs",
                   "recoveries", "revol_bal", "revol_util", "total_acc", "total_rec_late_fee", "emp_length", "home_ownership",
                   "term"], y="grade", training_frame=train)

print(gbm_model)
print(y)

gbm_model.predict(train)


#Mean Absolute Percentage Error for Linear Regression Model
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
