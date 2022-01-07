#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://www.alba.co.kr/job/Detail.asp?adid=110532587&listmenucd=BRAND"
html = requests.get(url).text
response = requests.get(url)

soup = BeautifulSoup(html, "html5lib")

tags = soup.select("#InfoApply > div.detail-content__recruit-list > dl:nth-child(3) > dd > p.detail-content__contact.detail-content__en > span:nth-child(1)")

for tag in tags:
    print(tag.text)

"""
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
"""

