# Function.py

from FindMainNews import FindMainNews
from FindNewsCat import FindNewsCat
from FindPress import FindPress
from PressSql import PressSql
from NewsSql import NewsSql

class Function():

    @staticmethod
    def Press():
        # 언론사 테이블 넣기
        press = FindPress.findPress()
        PressSql.insertPress(press)

    @staticmethod
    def News():
        print("1. 2010년 1월 1일부터 넣기")
        print("2. 오늘 날짜부터 넣기")
        select = input("번호를 입력해주세요 : ")
        if int(select) == 1:
            countdays = 0
        elif int(select) == 2:
            countdays = int(input("며칠 전까지 가져올까요? "))
        else:
            print("잘 못 입력했습니다.")

        # 뉴스 테이블 넣기
        url = 'https://news.naver.com/main/list.naver?mode=LS2D&' 

        # url에 카테고리 포함시키기
        cat_urls, cat_no = FindNewsCat.catInsert(url)

        for cu in range(len(cat_urls)):
            sid1 = cat_no[cu][14:17]
            sid2 = cat_no[cu][5:8]

            # 완성된 뉴스 url로 만들기
            newsurls = FindMainNews.NewsInsert(cat_urls[cu], int(select), countdays, sid1)   # 인자는 url과 오늘로부터 며칠 전꺼까지 가져올 것인지 설정

            for newsurl in newsurls:
                try:
                    news = FindMainNews.Extract(newsurl, sid2, sid1)    # url과 sid2 sid1를 인자로 넣음

                    # 뉴스 세부 내용 저장
                    NewsSql.insertNews(news)
                    # 뉴스 본문 저장
                    NewsSql.insertDescNews(news)

                    
                    print("제목 :", news.title)
                    """
                    print("내용 :", news.content)
                    print("날짜 :", news.time)
                    print("원문 링크 :", news.link)
                    print("사진 링크 :", news.pic_link)
                    print("언론사 :", news.press)
                    print("해당 카테고리 : ", cat_no[14:17])
                    print("해당 세부 카테고리 : ", cat_no[5:8])
                    """
                except:
                    continue