## Part 5: Pipline and Dockerize
### Author: Yuning Song
### 1. [pipline.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part5/pipeline.py)
* Make the output of the get_learning_data.py as the input of the logistic_regression.py automaticly using luigi
* Input: 
  * [fintech_related_keywords.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/fintech_related_keywords.csv)
  * [top_100_key_words_with_jobs.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part1/top_100_key_words_with_jobs.csv)
* Output: 
  * [result.txt](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part3/result.txt)   
  *This part of code should run under the luigi environment and the connection with localhost:8082
### 2. Dockerize the pipline and push it to the docker hub.
* Download and install docker environment. Create a container to run both the localhost and the pipline application.
* [My Docker Hub](https://cloud.docker.com/repository/registry-1.docker.io/shadder2k/info6105)
