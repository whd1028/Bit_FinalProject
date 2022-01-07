# 언론사만 따오기

import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from WebPageSql import WebPageSql
from CandidateSql import CandidateSql
from WebRobot import WebRobot
from EHHelper import EHHelper


# 기사 가져오기
res = WebRobot.CollectHtml("https://news.naver.com/main/officeList.naver")
i = 0   # tr tag 돌리기
j = 0   # li tag 돌리기

# 빈 리스트 생성
press_name = []
press_num = []

while(True):
    try:
        j += 1
        # 언론사 추출
        tags_press_name = res.select(f'#groupOfficeList > table > tbody > tr:nth-child({i}) > td > ul > li:nth-child({j}) > a')
        tags_press_num = res.select(f'#groupOfficeList > table > tbody > tr:nth-child({i}) > td > ul > li:nth-child({j}) > a')[0]['href'] 

        # 제목 추출
        for tag_press_name in tags_press_name:
            press_name.append(tag_press_name.text.strip())

        # 언론사 번호만 따오기
        press_num.append(tags_press_num[39:42])
    except:
        i += 1
        j = 0
        if i > 10:
            break
        else:
            continue


# 테스트
print("언론사 :", len(press_name), type(press_name))
print("언론사 번호 :", len(press_num), type(press_num))
