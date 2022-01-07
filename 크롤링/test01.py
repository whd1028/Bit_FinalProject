import requests
from bs4 import BeautifulSoup
import urllib.request
 
url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=448&aid=0000348147"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
if response.getcode() != 200:
            print("err!!")
            exit(0)

html = BeautifulSoup(response,'html.parser')


"""
html = requests.get(url).text
response = requests.get(url)

soup = BeautifulSoup(html, "html5lib")

tags = soup.select("#article_content")

for tag in tags:
    print(tag.text)

"""
"""
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

else : 
    print(response.status_code)
"""

