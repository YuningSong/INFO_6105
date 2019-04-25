# Part 2: Analyze data from 2 banks with the algorithm

## 1. Huntington Bancshares Part
### (1) [get_job_url.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/get_job_url.py)   
* Author: Yuning Song
* Scrap different urls of jobs from [Jobs At Huntington](https://careers.huntington.com/en-US/search)
* Output: [position.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/position.csv)
### (2) [get_job_content.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/get_job_content.py)  
* Author: Yuning Song
* Get and analyse html contents to get job informations from urls in [position.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/position.csv)
* Output: [result1.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/result1.csv)
### (3) [get_keywords.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/get_keywords.py)
* Author: Jixiao Yang
* Do keyword extraction for job informations and compare the keywords with top 100 keywords got in [Part1](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part1)
* Output: [result_Huntington Bancshares.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Huntington%20Bancshares/result_Huntington%20Bancshares.csv)

## 2. Comerica Inc Part
### (1) [get_job_content2.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Comerica%20Inc/get_job_content2.py)
* Author: Jixiao Yang 
* Scrap html contents from [Comerica Bank Jobs](https://recruiting.adp.com/srccar/public/RTI.home?d=comerica-jobs&c=1057141#/)
* Output: html files in [/Comerica](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part2/Comerica%20Inc/Comerica)
### (2) [get_job_content2_handle.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Comerica%20Inc/get_job_content2_handle.py)
* Author: Jixiao Yang 
* Analyse html contents to get job informations from html files in [/Comerica](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part2/Comerica%20Inc/Comerica)
* Output: [result2.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Comerica%20Inc/result2.csv)
### (3) [get_keywords2.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Comerica%20Inc/get_keywords2.py)
* Author: Jixiao Yang 
* Do keyword extraction for job informations and compare the keywords with top 100 keywords got in [Part1](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part1)
* Output: [result_Comerica Inc.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/Comerica%20Inc/result_Comerica%20Inc.csv)

## 3. Final Result:
* [result_final.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part2/result_final.csv)
