from sklearn.externals import joblib


def model_analysis(average_star, elite_count, review_count, business_average_star):
    model = joblib.load("models/knn1_model.joblib")
    x = [[average_star, elite_count, review_count, business_average_star]]
    y = model.predict(x)
    return y[0]
