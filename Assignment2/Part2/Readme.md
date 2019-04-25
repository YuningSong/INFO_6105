## Part 2: Forming clusters(categories) for different areas in fintech
### Author: Jixiao Yang
### 1. [get_cluster_data.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/get_cluster_data.py)
* Get job words as cluster data from the job list
* Input:  [top_100_key_words_with_jobs.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part1/top_100_key_words_with_jobs.csv)
* Output: [job_words.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/job_words.csv)
### 2. [cluster.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/cluster.py)
* Build clusters with fintech jobs, using [`K-Means Clustering Algorithm`](https://en.wikipedia.org/wiki/K-means_clustering)
* Output the cluster centers we calculate
* Input:  [job_words.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/job_words.csv)
* Output: [cluster_center.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/cluster_center.csv)
### 3. [allocate_jobs.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/allocate_jobs.py)
* Divide jobs into different clusters according to the cluster centers and analyse clusters' data
* Input: 
  * [top_100_key_words_with_jobs.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part1/top_100_key_words_with_jobs.csv)
  * [top_100_key_words.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part1/top_100_key_words.csv)
  * [cluster_center.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/cluster_center.csv)
* Output:
  * [cluster_statistic_data.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/cluster_statistic_data.csv)
  * Different cluster csvs under [/csv](https://github.com/kinyang007/INFO_6105/tree/master/Assignment2/Part2/csv)
### 4. [fintech_related_words.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/fintech_related_words.py)
* Get fintech related words using the cluster centers
* Input:
  * [top_100_key_words.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part1/top_100_key_words.csv)
  * [cluster_center.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/cluster_center.csv)
* Output: 
  * [fintech_related_keywords.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/fintech_related_keywords.csv)
  * [fintech_related_keywords_divided_into_clusters.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment2/Part2/csv/fintech_related_keywords_divided_into_clusters.csv)
