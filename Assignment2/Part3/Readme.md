## Part 3: Feature Engineering
### Author: Jixiao Yang
### 1. [get_learning_data.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/get_learning_data.py)
* Get the related learning data from the job data list
* Input: 
  * [fintech_related_keywords.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/fintech_related_keywords.csv)
  * [top_100_key_words_with_jobs.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part1/top_100_key_words_with_jobs.csv)
* Output: 
  * [learning_data.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/csv/learning_data.csv)
### 2. [logistic_regression.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/logistic_regression.py)
* Use [`Logistic Regression CV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html) 
model to build a model to determine if the job is related to fintech or not
* Input: [learning_data.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/csv/learning_data.csv)
* Output: 
  * [result.txt](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/result.txt)
  * [jobs_judge_result.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/csv/jobs_judge_result.csv)
