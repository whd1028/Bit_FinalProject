#SqlCon.py
import mysql.connector
class SqlCon:
    hostlink = 'finalproject-1.c4jotwudvoiz.ap-northeast-2.rds.amazonaws.com'
    #conn = mysql.connector.connect(host = '127.0.0.1', port = '3306', user='root', password='1234', database='news_summary')  # 해당 인자도 다 변수로 사용할 수 있으면 좋다
    conn = mysql.connector.connect(host = hostlink, port = '3306', user='admin', password='12341234', database='News_Summary')  # 해당 인자도 다 변수로 사용할 수 있으면 좋다

    @staticmethod
    def Cursor():
        return SqlCon.conn.cursor()

    @staticmethod
    def Close():
        SqlCon.conn.close()

    @staticmethod
    def Commit():
        SqlCon.conn.commit()


SqlCon.Cursor()