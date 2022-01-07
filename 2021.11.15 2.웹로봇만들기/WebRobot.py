# WebRobot.py

import urllib.request as ureq
from bs4 import BeautifulSoup
from CandidateSql import CandidateSql
from WebPage import WebPage
from WebPageSql import WebPageSql
import threading

class WebRobot:
    # 웹 페이지를 수집만을 위한 메소드
    # url : 수집할 사이트 주소
    @staticmethod
    def Collect(url):
        try:
            # 웹 페이지 수집 객체 생성
            request = ureq.Request(url)
            # 웹 페이지 요청 (반환값은 요청 결과 웹 페이지)
            response = ureq.urlopen(request)
        except:                             # 요청 실패하였을 때
            return None 
        else : 
            if response.getcode() != 200:   # 요쳥 결과 값이 성공이 아닐 때
                return None
            return response                 # 요청 성고하였을 때

    # html 웹페이지 수집 메소드
    # url : 수집할 웹페이지 주소
    @staticmethod
    def CollectHtml(url):                   # HTML 파싱을 하기 위함
        # 웹 페이지 수집 요청
        response = WebRobot.Collect(url)
        if response == None:                # 결과가 없을 때
            return None
        try :
            # html로 파싱
            html = BeautifulSoup(response,'html.parser')
        except :                            # 파싱 예외 발생할 때
            return None
        else :                              # 파싱 성공했을 때
            return html


    # 주기적으로 수집하는 메소드
    # period : 수집주기
    # tm_callback : 수집하였을 때 이를 통보 받을 이벤트 핸들러
    @staticmethod
    def CollectTM(period, tm_callback):     # 주기적으로 수집이 되었는지 알고싶을 때 tm_callback을 돌려주면 된다
        # 수집후보 사이트 얻어오기
        url,depth = CandidateSql.GetCandidate()

        # 주기적인 타이머 객체 생성
        timer = threading.Timer(period, WebRobot.CollectTM, [period, tm_callback])
        # 타이머 가동 (수집하는 페이지에 에러가 뜬 경우에도 다른 페이지를 수집하기 위해 타이머 먼저 실행)
        timer.start()

        if url == "":                       # 수집 후보 사이트가 없을 때 종료
            return

        # 웹페이지 수집하기
        res = WebRobot.CollectHtml(url)
        if res == None:                     # 웹 페이지 수집 실패했을 때 종료
            return

        # 수집한 정보로 WebPage 객체를 생성
        wp = WebPage.MakeWebPage(url, res)
        if wp == None:                      # WebPage 객체 생성 실패했을 때 종료
            # 버그 상황을 로그 파일에 레포팅을 하고 싶을 때 여기에 작성 가능
            return

        # DB에 수집한 WebPage 정보를 기록
        WebPageSql.AddPage(wp)

        # 수집한 웹 페이지에 있는 링크 각각에 대하여
        for link in wp.links:
            # 수집 후보 사이트로 등록(depth는 현재 depth)
            CandidateSql.AddCandidate(link,depth+1)     # 시드 사이트보다 뎁스 1 증가시키며 저장하기 => 안으로 들어가며 처리


        if tm_callback != None:                     # 이벤트 핸들러가 있을 때
            tm_callback(url,depth,wp)               # 이벤트 통보(개시)
            # 위 조건으로 통보가 됬을 때 내가 하는게 아닌 사용하는 곳에서 한다
            # => 이벤트로 처리하기 위한 이벤트 핸들러는 사용하는 곳에서 정의하여 라이브러리로 전달
            # => 라이브러리에서 사건이 발생되었을 때 이벤트핸들러를 호출
            # 호출하는 방향이 응용->라이브러리가 정상이지만 반대로 수행되기 때문에 callback이다.
            # 콜백 중 지금 하고 있는 것들을 확인하면 이벤트 처리에 사용하고 있다.


        # 사건이 발생했을 때 처리해야하는 객체와 사건을 발생했다는 것을 인지하는 객체가 서로 다를 때
        # 사건(event)이 발생했다라는 것을 인지한 객채가 처리하는 객체에게 통보하는 것 = 개시하다(출판,publishing) 
        # => 처리하는 객체는 사건이 발생했는지 인지하는 핸들러에게 이벤트 핸들러 정의한 것을 전달한다 (구독)
        # 이 것을 옵저버 패턴이라고 한다.