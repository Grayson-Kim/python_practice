import requests, csv
from bs4 import BeautifulSoup

url = 'https://www.byui.edu/admissions/apply/international-students/application-process'

filename = 'byu_deadline.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
deadlines = csv.writer(f)

title = 'Semester	Final Application Deadline'.split('\t')
deadlines.writerow(title)

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
byu_rows = soup.find('table', attrs={'class':'table'}).find('tbody').find_all('tr')

for idx in byu_rows:
    columns = idx.find_all('td')
    if len(columns) <= 1: # 이걸 안하면 title 과 data 사이에 공백 라인이 생기더라
        continue
    data = [column.get_text() for column in columns]
    deadlines.writerow(data)