## Part 2: Forming clusters(categories) for different areas in fintech
### Author: Jixiao Yang
### 1. [get_data_with_fintech.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/get_data_with_fintech.py)
* Definition: If a job contains `fintech` keyword, this job is related to fintech.
* Get fintech jobs from the job list
* Input:  [top_100_key_words_with_jobs.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part1/top_100_key_words_with_jobs.csv)
* Output: [job_words_with_fintech.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/csv/job_words_with_fintech.csv)
### 2. [cluster.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/cluster.py)
* Build clusters with fintech jobs, using [`K-Means Clustering Algorithm`](https://en.wikipedia.org/wiki/K-means_clustering)
* Output the cluster centers we calculate
* Input:  [job_words_with_fintech.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/csv/job_words_with_fintech.csv)
* Output: [cluster_center.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/csv/cluster_center.csv)
### 3. [fintech_related_words.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/fintech_related_words.py)
* Get fintech related words using the cluster centers
* Input:
  * [top_100_key_words.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part1/top_100_key_words.csv)
  * [cluster_center.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/csv/cluster_center.csv)
* Output: 
  * [fintech_related_keywords.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignments/Assignment2/Part2/csv/fintech_related_keywords.csv)
