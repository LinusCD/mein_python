import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


r = requests.get('http://www.qiushibaike.com', headers = headers)
content = r.text
soup = BeautifulSoup(content, 'lxml')


page_numbers = {'0','1','2'}


for  page_number in page_numbers:
    r = requests.get('https://www.qiushibaike.com/8hr/page/'+ page_number + '/', headers=headers)
    content = r.text
    soup = BeautifulSoup(content, 'lxml')


    divs = soup.find_all(class_= re.compile('article block untagged mb15 typs_(long|hot|recent|old)'))

    for div in divs:
        if div.find_all(class_='thumb'):
            continue
        joke = div.span.get_text()
        print(joke)
        print('-------')