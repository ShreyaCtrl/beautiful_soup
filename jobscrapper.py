from bs4 import BeautifulSoup
import requests

job_field = input('enter a field for job : ')
job_location = input('enter a field for job : ')
html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_field}&txtLocation={job_location}').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs_desc = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs_desc:
    recency = job.find('span', class_='sim-posted').span.text
    if 'few' or '1' or '2' in recency:
        company_name = soup.find('h3', class_='joblist-comp-name')
        period = job.find('ul', class_='top-jd-dtl clearfix')
        skills = job.find('span', class_='srp-skills')
        apply_link = job.find('a', class_='waves-effect waves-light btn')
        # desc = job.find('li', class_=None)
        print(company_name.text.strip())
        print(period.text.strip().replace('card_travel',''))
        print(skills.text.strip())
        # print(desc.text.strip())
        print(recency)
        print(apply_link['href'])
        print('----------------------')
# companies = soup.find_all('h3', class_='joblist-comp-name')
# for company in companies:
#     print(company.text.strip())
#
# period = soup.find_all('ul', class_='top-jd-dtl clearfix')
# for per in period:
#     print(per.text.strip())