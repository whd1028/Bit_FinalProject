# FindMainNews.py
import datetime 
from datetime import date, timedelta
from WebRobot import WebRobot
from NewsSql import NewsSql

class FindMainNews:
    def __init__(self, title, content, time, link, pic_link, press, p_id, cd_id):
        self.title = title[0]
        self.content = content[0]
        self.time = time[0]
        self.link = link[0]
        self.pic_link = pic_link[0]
        self.press = press[0]
        self.p_id = p_id
        self.cd_id = cd_id


    # 시간 처리해서 가져오기
    def GetTime(numdays) : # 나오게할 날짜 갯수
        baseDate = datetime.date.today() 
        d_list = [baseDate - datetime.timedelta(days=x) for x in range(numdays)]
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 

    # 2010년부터 가져오기
    def GetTime_Since2010() : # 나오게할 날짜 갯수
        baseDate = datetime.date(2010, 1, 1)
        d_day = datetime.date.today() - baseDate
        d_day = int(str(d_day)[0:4])
        d_list = [baseDate + datetime.timedelta(days=x) for x in range(d_day)]
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 

    # 날짜가 포함된 url을 넣어 마지막 페이지 찾기
    # input url 형식
    # url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=20220105&page="
    def FindLastPage(url):
        # 페이지 번호
        pn = 1
        # 마지막 페이지까지 반복문 돌리기
        while(True):
            total_url = url+str(pn)
            # 사이트
            res = WebRobot.CollectHtml(total_url)
            # 페이징 추출
            tags_page = res.select('#main_content > div.paging')

            # 페이징 담을 리스트
            p_num = []

            # 페이징 넘버 추출
            for tag_page in tags_page:
                temp = tag_page.text.strip()

            # 개행으로 구분된 페이징 스플릿하여 리스트 저장
            temp = temp.split("\n")

            # 이전 버튼이 존재 여부 테스트
            try:
                int(temp[0])

            # 이전 버튼이 있는 경우
            except:
                if len(temp) == 12:       # 이전과 다음이 있는 페이지
                    pn = int(temp[10])+1
                    continue
                else:
                    # 이전과 다음이 없는 경우 멈춤
                    break

            # 이전 버튼이 없는 경우
            else:
                if len(temp) == 11:         # 다음만 있는 페이지
                    pn = int(temp[9])+1
                    continue
                else:
                    # 다음이 없는 경우 멈춤
                    break

        try:
            for i in range(len(temp)):
                if pn < int(temp[i+2]):     # 이전부터 시작하고, 현재 페이지가 1번과 같기 때문에 +2
                    pn = int(temp[i+2])
        except:
            print("끝 번호 : ", pn)
            return pn
                    

    # 링크 타고 들어가기
    # input url 형식
    # url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=' 
    def NewsInsert(url, select, countdays, cat_no):
        i = 0
        inputurl = url
        if select == 1:
            getTime = FindMainNews.GetTime_Since2010()  # 2010년부터 오늘까지 다가져오기
        elif select == 2:
            getTime = FindMainNews.GetTime(countdays)   # 오늘로부터 countdays일 가져오기
        links = []            # 반환할 리스트
        for gt in getTime:
            d_url = inputurl + gt + "&page="
            
            # 마지막 페이지 찾기
            lastUrl = FindMainNews.FindLastPage(d_url)

            # 마지막 페이지까지 추출하기
            for ex in range(lastUrl):
                ex = ex+1
                url = d_url + str(ex)
                # 웹페이지 수집하기
                res = WebRobot.CollectHtml(url)
                if res == None:                     # 웹 페이지 수집 실패했을 때 종료
                    break

                atags = res.find_all('a')
                for atag in atags:
                    # 다운로드 어트리뷰트가 있는지 확인 (파일을 다운로드 받는 태그가 아닐 때)
                    if atag.has_attr('download') == False:
                        try:
                            link = atag['href']     # href의 있는 경우 링크를 얻어오기               
                        except:
                            # continue 사용 이유 : href가 없어 예외가 발생된 경우에도 뒤에 있는 하이퍼링크들도 조사를 해야하기 때문에 continue를 사용한다.
                            continue        
                        else:
                            # 경제만 추출(sid1=101)
                            if link.startswith('https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101') or link.startswith('http://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101'):
                                links.append(link)
                                try:
                                    news = FindMainNews.Extract(link, cat_no[5:8], cat_no[14:17])

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
        return links


    # 원하는 항목 다 가져오기
    # 완성된 기사 url을 input 사용
    def Extract(url, p_id, cd_id):
        try :
            # 기사 가져오기
            res = WebRobot.CollectHtml(url)

            # 제목 추출
            tags_title = res.select('#articleTitle')
            # 내용 추출
            tags_content = res.select('#articleBodyContents')
            # 날짜 추출
            tags_time = res.select('#main_content > div.article_header > div.article_info > div > span:nth-child(1)')
            # 원문 링크 추출
            tags_link = res.select('#main_content > div.article_header > div.article_info > div > a:nth-of-type(1)')[0]['href'] 
            # 사진 링크 추출
            try:
                tags_pic_link = res.select("#articleBodyContents > .end_photo_org > img")[0]['src']
            except:
                tags_pic_link = 'None'
            finally:
                # 언론사 추출
                tags_media = res.select('#main_content > div.article_header > div.press_logo > a > img')[0]['alt']


                # 빈 리스트 생성
                title =[]
                content = []
                time = []
                link = []
                pic_link = []
                press = []

                # 제목 추출
                for tag_title in tags_title:
                    title.append(tag_title.text.strip())

                # 내용 추출
                for tag_content in tags_content:
                    temp_content = tag_content.text
                    temp_content = temp_content.replace("\xa0", " ")
                    temp_content = temp_content.replace("\n", "")
                    temp_content = temp_content.replace("\t", " ")
                    content.append(temp_content.strip())

                # 날짜 추출
                for tag_time in tags_time:
                    time.append(tag_time.text.strip())

                # 원문 링크 추출
                link.append(tags_link.strip())

                # 사진 추출
                pic_link.append(tags_pic_link.strip())

                # 언론사 추출
                press.append(tags_media.strip())


                return FindMainNews(title, content, time, link, pic_link, press, p_id, cd_id)

        except:
            return False
