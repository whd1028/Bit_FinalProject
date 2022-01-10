# NewsExtract.py

from WebRobot import WebRobot
from Article import Article
from NewsSql import NewsSql
class NewsExtract():
    # 원하는 항목 다 가져오기
    # 완성된 기사 url을 input 사용
    @staticmethod
    def extract(url, cd_id, c_id):
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
                # 언론사 이름 추출
                tags_media = res.select('#main_content > div.article_header > div.press_logo > a > img')[0]['alt']

                # 제목 추출
                title = tags_title[0].text.strip()

                # 내용 추출
                #print(tags_content[0].text)
                temp_content = tags_content[0].text
                temp_content = temp_content.replace("\xa0", " ")
                temp_content = temp_content.replace("\n", "")
                temp_content = temp_content.replace("\t", " ")
                temp_content = temp_content.replace("\'", "\\\'")
                temp_content = temp_content.replace("\"", "\\\"")
                content = temp_content.strip()
                print(content)

                # 날짜 추출
                time_temp = tags_time[0].text.strip()

                # 날짜 오전 오후 처리
                if time_temp[12:14] == "오후":
                    # 1시부터 9시
                    if len(time_temp) == 19:
                        time = time_temp[:12] + str(int(time_temp[15:16])+12) + time_temp[16:]
                    # 10시부터 12시
                    elif len(time_temp) == 20:
                        time = time_temp[:12] + str(int(time_temp[15:17])+12) + time_temp[17:]
                elif time_temp[12:14] == "오전":
                    # 1시부터 9시
                    if len(time_temp) == 19:
                        time = time_temp[:12] + time_temp[15:]
                    # 10시부터 12시
                    elif len(time_temp) == 20:
                        time = time_temp[:12] + time_temp[15:]

                # 원문 링크 추출
                link = tags_link.strip()
                
                # 사진 추출
                pic_link = tags_pic_link.strip()

                # 언론사 이름 추출
                press_name = tags_media.strip()

                # 언론사 번호 추출
                if url[44:].startswith('LS2D'):             # LS2D인 경우
                    press_num = int(url[79:82])
                elif url[44:].startswith('LSD'):            # LSD인 경우
                    press_num = int(url[78:81])
                else:
                    press_num = 0

                return Article(title, content, time, link, pic_link, press_name, press_num, cd_id, c_id)

        except:
            return False


#a1 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LPOD&mid=sec&oid=009&aid=0004906767", 226,105)
#NewsSql.insertDescNews(a1)
# a3 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=025&aid=0003165201", 100,100)
# a2 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=018&aid=0005123091", 100,100)
# a4 = NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=277&aid=0005027916", 100,100)
# print("오전1자리",a1.time)
# print("오전2자리",a2.time)
# print("오후1자리",a3.time)
# print("오후2자리",a4.time)

#NewsExtract.extract("https://news.naver.com/main/read.naver?mode=LPOD&mid=sec&oid=009&aid=0004906767", 100,100)