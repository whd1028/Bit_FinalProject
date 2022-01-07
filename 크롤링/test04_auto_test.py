# 시드 사이트로부터 기존 모델사용해 파싱 후 DB에 넣어보기
import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from WebRobot import WebRobot
from WebPageSql import WebPageSql
import pymssql

url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259"

#웹 요청 개체 생성
request = ureq.Request(url)

#웹 요청 수행 - 결과 반환
response = ureq.urlopen(request)

if response.getcode()!=200:         #요청 결과가 실패일 때
    print("요청 실패")
    exit(0)                         #프로그램 종료
#BeautifulSoup으로 html 파싱
html = WebRobot.CollectHtml(url)
#WebPage 개체 생성
wp = WebPage.MakeWebPage(url,html)  #웹 페이지 개체 생성
if wp == None:                      #개체 생성 실패했을 때
    print("WebPage 개체 생성 실패")
    exit(0)                         #프로그램 종료
WebPageSql.AddPage(wp)              #수집한 웹 페이지 정보를 DB에 반영



