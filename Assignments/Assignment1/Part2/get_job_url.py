import requests, re
import pandas as pd
import time


def getURL(pageNum):
    url = 'https://careers.huntington.com/en-US/search?pagenumber='
    urls = []
    for i in range(pageNum):
        urls.append(url + str(i + 1))
    return urls


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('404 error!')
        return ' '


def fillPositionList(html):
    time.sleep(2)
    pattern = re.compile('"url": "(.*?)"')
    p = re.findall(pattern, html)
    if p:
        p_de = sorted(set(p), key=p.index)
        return p
    return 'N'


def printCsv(sinfo):
    df = pd.DataFrame(sinfo)
    df.to_csv('position.csv', sep=',', header=True, index=True)  # set output path
    # print(df)


def main():
    sinfo = []
    urls = getURL(6)  # set the number of page you want
    i = 1
    for url in urls:
        html = getHTMLText(url)
        sinfo.extend(fillPositionList(html))
        if i % 5 == 0:
            print("%d / %d" % (i, len(urls)))
        i += 1
    printCsv(sinfo)


main()
