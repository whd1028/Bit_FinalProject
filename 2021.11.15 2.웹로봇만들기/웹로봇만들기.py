#웹로봇만들기.py
import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from WebPageSql import WebPageSql
from CandidateSql import CandidateSql
from WebRobot import WebRobot

# 3. 수집 테스트
cnt = 0
def CollectedWebPageEventHandler(url,depth,wp):
    global cnt                  # 전역변수 cnt를 사용할 것입니다.
    print("===", cnt)
    print("수집완료 : ", url)
    print("\t", depth)
    cnt+=1

# seed site가 등록된 이후에는 생략할 수 있다
seed_url = input("Seed Site : ")        # 시드 사이트 등록 시 생략
CandidateSql.AddCandidate(seed_url,0)   # 시드 사이트 등록 시 생략
WebRobot.CollectTM(5,CollectedWebPageEventHandler)

"""
# 2. 파싱 단위테스트
# 네이버 페이지에서 소스 보기 한 것과 비슷한 것 출력
res = WebRobot.CollectHtml("http://naver.com")
print(res)
"""

"""
# 1. 웹페이지 수집 단위테스트
res = WebRobot.Collect("http://naver.com")
print(res)
"""