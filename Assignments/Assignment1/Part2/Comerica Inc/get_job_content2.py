
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os
import time
chrome_driver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chrome_driver
driver = webdriver.Chrome(chrome_driver)

url = 'https://recruiting.adp.com/srccar/public/RTI.home?d=comerica-jobs&c=1057141#/'
driver.get(url)
content = driver.find_elements_by_xpath("//div[@class='col-sm-9 nopadding']")

file_cnt = 0
for i in range(27):
    cnt = 10
    if i == 26:
        cnt = 1
    for j in range(cnt):
        time.sleep(10)
        job_details = driver.find_elements_by_xpath("//a[@class='jobtitle']")
        job_details[j].click()
        time.sleep(10)

        source = driver.page_source
        html = bs(source, 'lxml')
        string = ""
        for content in html.contents:
            string += str(content) + "\n"
        file = open("Comerica/" + str(file_cnt) + ".html", 'w', encoding='utf-8')
        file.write(string)
        file.close()
        file_cnt += 1

        back = driver.find_elements_by_xpath("//*[@id=\"srccar\"]/div[2]/div[2]/div/div/div/div/div[1]/button")
        back[0].click()
    time.sleep(10)
    next_page = driver.find_elements_by_xpath("//*[@id=\"searchForm\"]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/button[2]")
    next_page[0].click()
