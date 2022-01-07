# https://dsc-sookmyung.tistory.com/85

# 아이디가 없는 경우 스크래핑
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")

#tags = soup.select("table tbody tr td em")    # soup.select("#_per")
#tags = soup.select(".lwidth tbody .strong td em")    # soup.select("table tbody tr td em")
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")    # nth-of-type을 사용하라는 에러 메시지가 출력되는 경우 nth-child()대신, nth-of-type()을 사용

for tag in tags:
    print(tag.text)

"""
# _per id를 가진 css 코드 가져오기
import requests
from bs4 import BeautifulSoup

def get_per(code):
    url = f"https://finance.naver.com/item/main.nhn?code={code}"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

print(get_per("000660")) # SK 하이닉스 PER 값
print(get_per("005930")) # 삼성전자 PER 값

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
"""