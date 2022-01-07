# Function.py

from FindMainNews import FindMainNews
from FindNewsCat import FindNewsCat
from FindPress import FindPress
from InsertPress import InsertPress

class Function():

    def Press():
        # 언론사 테이블 넣기
        press = FindPress.findPress()
        InsertPress.insertPress(press)

    def News():
        # 뉴스 테이블 넣기
        url = 'https://news.naver.com/main/list.naver?mode=LS2D&' 

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsert(url)

        for cu in range(len(cat_urls)):
            # 완성된 뉴스 url로 만들기
            newsurls = FindMainNews.NewsInsert(cat_urls[cu], 1, cat_no[cu])   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

            # 마지막 페이지까지 추출하기
            for no in range(len(newsurls)):
                try:
                    news = FindMainNews.Extract(newsurls[no])

                    print(no,"번 째 넣는 중")

                except:
                    continue
