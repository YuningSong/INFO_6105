from bs4 import BeautifulSoup as bs
import pandas as pd

job_title = []
job_num = []
job_functional_group = []
job_full_time = []
job_description = []
for i in range(261):
    with open('Comerica/' + str(i) + '.html', 'r', encoding='utf-8') as file:
        soup = bs(file.read(), 'lxml')

        title = soup.find("span", class_="jobTitle").text
        job_title.append(title)

        num = soup.find("span", class_="jobnum").text
        job_num.append(num)

        tmp = soup.find_all("div", class_="col-sm-4 col-resize3")
        if len(tmp) == 3:
            functional_group = tmp[1].find("div", class_="resultfootervalue").text
            full_time = tmp[2].find("div", class_="resultfootervalue").text
            job_functional_group.append(functional_group)
            job_full_time.append(full_time)
        elif len(tmp) == 2:
            functional_group = tmp[0].find("div", class_="resultfootervalue").text
            full_time = tmp[1].find("div", class_="resultfootervalue").text
            job_functional_group.append(functional_group)
            job_full_time.append(full_time)

        tmp = soup.find("div", class_="container-fluid")
        tmp1 = tmp.find_all("div", class_="col-sm-6")
        description = tmp1[0].find("div", class_="contentHead").text + '\n'
        description += tmp1[0].find("div", class_="content").text + '\n'
        content_head = tmp1[1].find_all("div", class_="contentHead")
        content = tmp1[1].find_all("div", class_="content")
        for j in range(len(content_head)):
            description += content_head[j].text + '\n'  # Qualifications, Work Schedule, Work Location(s), About Comerica
            description += content[j].text + '\n'
        job_description.append(description)

test_df = pd.DataFrame({
    "Job Title": job_title,
    "Job No": job_num,
    "Functional Group": job_functional_group,
    "Full Time": job_full_time,
    "Job Description": job_description
})
test_df.to_csv('result2.csv', sep=',', header=True, index=True)

