# 마지막 페이지 찾기
from WebRobot import WebRobot



# 페이지 번호
pn = 1
# 마지막 페이지까지 반복문 돌리기
while(True):
    url = f"https://news.naver.com/main/list.naver?mode=LS2D&sid2=259&sid1=101&mid=shm&date=20220105&page={pn}"
    # 사이트
    res = WebRobot.CollectHtml(url)
    # 페이징 추출
    tags_page = res.select('#main_content > div.paging')

    # 페이징 담을 리스트
    p_num = []

    # 페이징 넘버 추출
    for tag_page in tags_page:
        temp = tag_page.text.strip()

    # 개행으로 구분된 페이징 스플릿하여 리스트 저장
    temp = temp.split("\n")

    # 만약 다음 페이지로 넘어갈 수 있으면 페이징 넘버 바꾸기
    if len(temp) == 11:         # 다음만 있는 페이지
        pn = int(temp[9])+1
        continue
    elif len(temp) == 12:       # 이전과 다음이 있는 페이지
        pn = int(temp[10])+1
        continue
    else :                      # 다음이 없는 페이지
        try:
            for i in range(len(temp)):
                if pn < int(temp[i+2]):     # 이전부터 시작하고, 현재 페이지가 1번과 같기 때문에 +2
                    pn = int(temp[i+2])
        except:
            print("끝 번호 : ", pn)
            break
            #return pn