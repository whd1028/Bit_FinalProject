# 3. 웹 로봇을 사용하여 수집 테스트
# 다른 방향 찾기
import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from WebPageSql import WebPageSql
from CandidateSql import CandidateSql
from WebRobot import WebRobot


cnt = 0
def CollectedWebPageEventHandler(url,depth,wp):
    global cnt                  # 전역변수 cnt를 사용할 것입니다.
    print("===", cnt)
    print("수집완료 : ", url)
    print("\t", depth)
    cnt+=1

# seed site가 등록된 이후에는 생략할 수 있다
#seed_url = input("Seed Site : ")        # 시드 사이트 등록 시 생략
seed_url = "https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=20220105&page=1"
CandidateSql.AddCandidate(seed_url,0)   # 시드 사이트 등록 시 생략
WebRobot.CollectTM(5,CollectedWebPageEventHandler)


