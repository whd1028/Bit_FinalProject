import urllib.request as ureq
from bs4 import BeautifulSoup
from WebPage import WebPage
from CandidateSql import CandidateSql
from WebRobot import WebRobot
from EHHelper import EHHelper

try:
    # 언론사 추출
    tags_press_name = res.select(f'#groupOfficeList > table > tbody > tr:nth-child({i}) > td > ul > li:nth-child({j}) > a')
    tags_press_num = res.select(f'#groupOfficeList > table > tbody > tr:nth-child({i}) > td > ul > li:nth-child({j}) > a')[0]['href'] 

    # 제목 추출
    for tag_press_name in tags_press_name:
        press_name.append(tag_press_name.text.strip())

    # 언론사 번호만 따오기
    press_num.append(int(tags_press_num[39:42]))
except:
    i += 1          # tr 번호 증가
    j = 0           # li 번호 초기화
    if i > 10:      # 네이버에서 제공하는 언론사 카테고리는 총 10개
        False
    else:
        True