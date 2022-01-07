# 1. 웹페이지 수집 단위테스트 - 내용 가져오기
# 가져와야 할 정보
# 제목, 내용, 날짜, 원문링크, 사진, 언론사, 분류
import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from WebPageSql import WebPageSql
from CandidateSql import CandidateSql
from WebRobot import WebRobot
from EHHelper import EHHelper


# 기사 가져오기
res = WebRobot.CollectHtml("https://news.naver.com/main/ranking/read.naver?mode=LSD&mid=shm&sid1=001&oid=119&aid=0002564100&rankingType=RANKING")

# 제목 추출
tags_title = res.select('#articleTitle')
# 내용 추출
tags_content = res.select('#articleBodyContents')
# 날짜 추출
tags_time = res.select('#main_content > div.article_header > div.article_info > div > span:nth-child(1)')
# 원문 링크 추출
tags_link = res.select('#main_content > div.article_header > div.article_info > div > a:nth-of-type(1)')[0]['href'] 
# 사진 링크 추출
tags_pic_link = res.select("#articleBodyContents > .end_photo_org > img")[0]['src']
# 언론사 추출
tags_media = res.select('#main_content > div.article_header > div.press_logo > a > img')[0]['alt']
# 카테고리 추출
tags_cat = res.select('#articleBody > div.guide_categorization > a > em')

# 빈 리스트 생성
title =[]
content = []
time = []
link = []
pic_link = []
media = []
cat = []

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
media.append(tags_media.strip())

# 카테고리 추출
# 2개 이상 카테고리에 해당하는 경우가 있음
for tag_cat in tags_cat:
    cat.append(tag_cat.text.strip())

# 테스트
print("제목 :", title[0])
print("내용 :", content[0])
print("날짜 :", time[0])
print("원문 링크 :", link[0])
print("사진 링크 :", pic_link[0])
print("언론사 :", media[0])
print("카테고리 :", cat)