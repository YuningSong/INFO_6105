from sklearn.externals import joblib


def random_forest(average_star, elite_count, fans, friends_count, business_average_star):
    model = joblib.load("models/RD_model.joblib")
    x = [[average_star, elite_count, fans, friends_count, business_average_star]]
    y = model.predict(x)
    return y[0]


# def knn(average_star, elite_count, fans, friends_count, business_average_star):
#     model = joblib.load("models/knn_model_1.joblib")
#     x = [[average_star, elite_count, fans, friends_count, business_average_star]]
#     y = model.predict(x)
#     return y[0]
