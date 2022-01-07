# 경제 - 금융 뉴스 홈에서 뉴스 링크 따오기
from WebRobot import WebRobot
from WebPage import WebPage
i = 0
while(True):
    url = f'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=259&sid1=101&date=20220105&page={i}'
    i = i+1
    # 웹페이지 수집하기
    res = WebRobot.CollectHtml(url)
    if res == None:                     # 웹 페이지 수집 실패했을 때 종료
        break

    atags = res.find_all('a')
    links = []            # 반환할 리스트
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

    print("===================================================================================")
    print(i)
    for k in range(len(links)):
        print(links[k])