import h2o
from h2o.estimators.xgboost import H2OXGBoostEstimator
import numpy as np
h2o.init()


# Import a sample binary outcome training set into H2O
train = h2o.import_file("/Users/fengcu/Desktop/6105/assignment3/featured_data.csv")

# Identify predictors and response
x = train.columns
# This argument is the name (or index) of the response column.
y = "int_rate"
x.remove(y)

# try using the `keep_cross_validation_predictions` (boolean parameter):
# first initialize your estimator, set n folds parameter
xgb = H2OXGBoostEstimator(keep_cross_validation_predictions = True)
# keep_cross_validation_predictions: Specify whether to keep the predictions
# of the cross-validation predictions. This needs to be set to TRUE if running
# the same AutoML object for repeated runs because CV predictions are required
# to build additional Stacked Ensemble models in AutoML. This option defaults to FALSE.

from h2o.estimators.gbm import H2OGradientBoostingEstimator
#Builds gradient boosted trees on a parsed data set, for regression or classification.
gbm_model = H2OGradientBoostingEstimator()
# training_frame: Specifies the training set.
gbm_model.train(x = ["loan_amnt", "annual_inc", "dti", "delinq_2yrs", "inq_last_6mths", "total_acc"], y = "int_rate", training_frame=train)

print(gbm_model)
print(y)

gbm_model.predict(train)

#Mean Absolute Percentage Error for Linear Regression Model
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100