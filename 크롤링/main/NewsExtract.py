# NewsExtract.py

from WebRobot import WebRobot

class NewsExtract():
    def __init__(self, title, content, time, link, pic_link, press, cd_id, c_id):
        self.title = title[0]
        self.content = content[0]
        self.time = time
        self.link = link[0]
        self.pic_link = pic_link[0]
        self.press = press[0]
        self.cd_id = cd_id
        self.c_id = c_id

    # 원하는 항목 다 가져오기
    # 완성된 기사 url을 input 사용
    @staticmethod
    def Extract(url, cd_id, c_id):
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
                # 언론사 추출
                tags_media = res.select('#main_content > div.article_header > div.press_logo > a > img')[0]['alt']


                # 빈 리스트 생성
                title =[]
                content = []
                time_temp = []
                link = []
                pic_link = []
                press = []

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
                    time_temp.append(tag_time.text.strip())

                # 날짜 오전 오후 처리
                if time_temp[0][12:14] == "오후":
                    # 1시부터 9시
                    if len(time_temp[0]) == 19:
                        time = time_temp[0][:12] + str(int(time_temp[0][15:16])+12) + time_temp[0][16:]
                    # 10시부터 12시
                    elif len(time_temp[0]) == 20:
                        time = time_temp[0][:12] + str(int(time_temp[0][15:17])+12) + time_temp[0][17:]
                elif time_temp[0][12:14] == "오전":
                    # 1시부터 9시
                    if len(time_temp[0]) == 19:
                        time = time_temp[0][:12] + time_temp[0][15:]
                    # 10시부터 12시
                    elif len(time_temp[0]) == 20:
                        time = time_temp[0][:12] + time_temp[0][15:]


                # 원문 링크 추출
                link.append(tags_link.strip())

                # 사진 추출
                pic_link.append(tags_pic_link.strip())

                # 언론사 추출
                press.append(tags_media.strip())


                return NewsExtract(title, content, time, link, pic_link, press, cd_id, c_id)

        except:
            return False


# a1 = NewsExtract.Extract("https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=277&aid=0005027945", 100,100)
# a2 = NewsExtract.Extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=018&aid=0005123091", 100,100)
# a3 = NewsExtract.Extract("https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=025&aid=0003165201", 100,100)
# a4 = NewsExtract.Extract("https://news.naver.com/main/read.naver?mode=LS2D&mid=shm&sid1=101&sid2=259&oid=277&aid=0005027916", 100,100)
# print("오전1자리",a1.time)
# print("오전2자리",a2.time)
# print("오후1자리",a3.time)
# print("오후2자리",a4.time)