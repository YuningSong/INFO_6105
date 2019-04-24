import csv
import re           #provide regular expression 
import os           #use oeprating system dependent functionality
import codecs       #define base classes for standard python codecs

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):    #use os.walk to enumerate all files in the directory
        for file in files:
            yield file


def readFromCSV(csvFile):
    obj = []
    csv_reader = csv.reader(open(csvFile))         #return a reader object which will iterate over lines in the given csvfile
    for row in csv_reader:
        if(len(row)!=0):
            obj.append(row[1])
    return obj[0:100]

def countWordsFreq(content,csvFile):
    count = []
    keywords = readFromCSV(csvFile)
    for keyword in keywords:
        num = len(re.findall(keyword, content, re.IGNORECASE))   #return all non-overlapping matches of pattern in string, as a list of strings
        if(num==0):
            count.append(0)
        else:
            count.append(num)
    return count

if __name__ == '__main__':

    path = "/Users/fengcu/PycharmProjects/Job Description_All Teams/JobDescription_Team12.csv"
    writePath1 = "/Users/fengcu/PycharmProjects/Job Description_All Teams/JobDescription_Team12.csv"  #from team 1 to team 12
    out1 = open(writePath1, 'a', newline='')
    csv_write_1 = csv.writer(out1, dialect='excel')      #return a writer object responsible for converting the user's data into delimited strings on the given file-like object
    with codecs.open(path,'rb','utf8','ignore')as file:  #open an encoded file using the given mode and return a wrapped version providing transparent encoding/decoding
        reader = csv.reader(file)
        key = []
        key.append('job no')
        key.append('job title')
        key.append('institution')
        key.append('URL')
        for j in range(100):
            key.append(j + 1)
        csv_write_1.writerow(key)
        i = 0
        for row in reader:
            # if(len(row)!=4):
            #     continue
            # else:
                l = []
                l.append(i)
                l.append(row[0])
                l.append(row[1])
                l.append(row[3])
                count = countWordsFreq(row[2],"/Users/fengcu/Desktop/6105/assignment_2/part1_dataset/top_100_key_words_with_jobs.csv")
                for keywordId in range(100):
                    l.append(count[keywordId])
                csv_write_1.writerow(l)



