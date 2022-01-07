# https://kejdev.tistory.com/67

import urllib.request 
from bs4 import BeautifulSoup # 웹 스크롤링을 위한 모듈 
def fetch_list_url(): 
    for i in range(100): 
        list_url = "http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&submedia=&sort=d&period=all&datefrom=2000.01.01&dateto=2020.03.22&pageseq="+str(i) 
        url = urllib.request.Request(list_url) 
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(res, "html.parser") 
        for link in soup.find_all('dt'): # dt 태그 밑에 있는 
            for i in link: # a 태그를 가져오기 
                print(i.get('href')) # 기사 URL 
                print(i.get_text('href')) # 기사 제목 fetch_list_url()


fetch_list_url()


