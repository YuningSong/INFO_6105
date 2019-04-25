# Part 1: Extract keywords from documents to build a dictionary of top keywords
### Author: Jixiao Yang
### 1. File functions: 
* [extract_text.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/extract_text.py)   
  * Transform pdf to txt  
  * Input: 4 pdf files at [/pdf](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part1/pdf)
  * Output: 4 txt files at [/txt](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part1/txt)
* [count & tf-idf.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/count%20%26%20tf-idf.py)   
  * Get word count and tf-idf from txt folder
  * Input: 4 txt files at [/txt](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part1/txt)
  * Output:
    * [word_count.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/csv/word_count.csv)
    * [word_tf_idf.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/csv/word_tf_idf.csv)
* [text_rank.py](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/text_rank.py)   
  * Get text rank from pdf
  * Input: 4 pdf files at [/pdf](https://github.com/kinyang007/INFO_6105/tree/master/Assignment1/Part1/pdf)
  * Output: [word_text_rank.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/csv/word_text_rank.csv)
  * Due to the space complexity of TextRank Algorithm implemented in [summa](https://github.com/summanlp/textrank) is
   <a href="https://www.codecogs.com/eqnedit.php?latex=O(n^{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(n^{2})" title="O(n^{2})" /></a>
   and the total words of the 4 pdf documents is too large for the space requirements, we can get the TextRank score list using [summa](https://github.com/summanlp/textrank) 
   in each pages of every pdf documents. Then merge the lists of TextRank score getting from each pages and divided the score value by the total page number.
   The formula is as shown below:<br/>
   <div align="center">
   <a href="https://www.codecogs.com/eqnedit.php?latex=S&space;=&space;\frac{\sum_{i=1}^{P}S_{i}}{P}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S&space;=&space;\frac{\sum_{i=1}^{P}S_{i}}{P}" title="S = \frac{\sum_{i=1}^{P}S_{i}}{P}"/></a>
   </div>
   <div style="text-indent:10em;">
   <a href="https://www.codecogs.com/eqnedit.php?latex=S" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S" title="S" /></a>
   is the final TextRank score of a word, 
   <a href="https://www.codecogs.com/eqnedit.php?latex=S_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S_{i}" title="S_{i}" /></a>
   is the score of the word in page i and 
   <a href="https://www.codecogs.com/eqnedit.php?latex=P" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P" title="P" /></a>
   is the total page number.
   If the word does not appear in page i then <a href="https://www.codecogs.com/eqnedit.php?latex=S_{i}=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S_{i}=0" title="S_{i}=0" /></a>.
   </div>
 ### 2. Final Results
 * (1) Word Count: [word_count_top100.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/csv/word_count_top100.csv)
 * (2) TF-IDF:     [word_tf_idf_top100.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/csv/word_tf_idf_top100.csv)
 * (3) Text Rank:  [word_text_rank_top100.csv](https://github.com/kinyang007/INFO_6105/blob/master/Assignment1/Part1/csv/word_text_rank_top100.csv)
