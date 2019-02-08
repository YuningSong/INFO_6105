from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd

url_pd = pd.read_csv("position.csv")
url_df = pd.DataFrame(url_pd)
result = []
result = url_df['0'].tolist()

title = []
type_ = []
date = []
location = []
experience = []
job_description = []
for url in result:
    response = get(url)
    # print(response)
    soup = bs(response.content,'lxml')
    a = soup.find("span", class_="jdp-title-job-title").text
    b = soup.find("div", class_="job-date-posted").text[14:-1]
    c = soup.find("span", class_="jobLocation").text
    d = soup.find("div", class_="secondary-text-color").text
    e = soup.find("li", class_="job-experience")
    f = e.find("div", class_="secondary-text-color").text
    g = soup.find("div", class_="jdp-job-description-card content-card").text
    title.append(a)
    type_.append(d)
    date.append(b)
    location.append(c)
    experience.append(f)
    job_description.append(g)

test_df = pd.DataFrame({"Url":result,
                        "Job Title":title,
                        "Post Date":date,
                        "Job Type": type_,
                        "Location":location,
                        "Experience":experience,
                        "Job_Desciption":job_description})
test_df.to_csv('result1.csv', sep=',', header=True, index=True)
