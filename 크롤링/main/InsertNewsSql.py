# InsertNewsSql.py

from SqlCon import SqlCon

class InsertNewsSql:

    # 언론사 넣기
    def insertPress(news):
        cursor = SqlCon.Cursor()
        query = str.format("insert into Press (p_name) values('{0}')", news.press)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False
        else:
            True

    # 뉴스 핵심 내용 넣기
    def insertMainNews(news):
        cursor = SqlCon.Cursor()
        # 언론사 번호를 어떻게 넣냐
        query = str.format("insert into news (p_id, cd_id, n_title, n_input) values({0}, {1}, '{2}', '{3}')", news.cd_id, news.p_id, news.title, news.time)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False
        else:
            True

    # 뉴스 내용 넣기
    def insertDescNews(news):
        cursor = SqlCon.Cursor()
        query = str.format("insert into news_detail (nd_description, nd_img) values('{0}', '{1}')", news.content, news.pic_link)

        try:    # 같은 url을 수집할 경우 예외가 발생할 수 있다.
            cursor.execute(query)
            SqlCon.Commit()
        except:
            False
        else:
            True

