# FindNewsCat.py
# 카테고리 별 번호
# 경제 sid1=101
# 금융 sid2=259
# 증권 sid2=258
# 산업/재계 sid2=261
# 중기/벤처 sid2=771
# 부동산 sid2=260
# 글로벌 경제 sid2=262
# 생활경제 sid2=310
# 경제 일반 sid2=263

# input url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=' 

from CategorySql import CategorySql
from WebRobot import WebRobot

class FindNewsCat:
    def findNewsCat():
        # cat_name = []

        for i in range(6):
            url = f'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{i}'
            res = WebRobot.CollectHtml(url)
            # 대분류 추출
            tags_cat = res.select('#lnb > ul > li.on > a > span.tx')
            cat_num = 100+i
            # 대분류명 추출
            for tag_cat in tags_cat:
                cat_name = (tag_cat.text.strip())

            CategorySql.insertCat(cat_num, cat_name)     # 쿼리 넣기

            j = 1
            #cat_d_name = []

            # 소분류 추출
            while(True):
                try:
                    tags_cat_d = res.select(f'#snb > ul > li:nth-child({j}) > a')
                    tags_cat_d_id = res.select(f'#snb > ul > li:nth-child({j}) > a')[0]['href']

                    tag_cat_d_id = int(tags_cat_d_id[49:53])
                    
                    if not tags_cat_d:
                        break

                    j += 1

                    # 소분류명 추출
                    for tag_cat_d in tags_cat_d:
                        cat_d_name = (tag_cat_d.text.strip())

                        CategorySql.insertCatDet(tag_cat_d_id ,cat_num, cat_d_name)
                except:
                    break


    def catInsert(url):
        # 경제 카테고리
        eco_sids = ['sid2=259&sid1=101', 'sid2=258&sid1=101', 'sid2=261&sid1=101', 'sid2=771&sid1=101', 'sid2=260&sid1=101', 'sid2=262&sid1=101', 'sid2=310&sid1=101', 'sid2=263&sid1=101']
        sidurls = []
        for n in range(len(eco_sids)):
            sidurls.append(url+eco_sids[n]+'&mid=shm&date=')
        return sidurls, eco_sids    # 카테고리 주소와 카테고리 번호 리턴
