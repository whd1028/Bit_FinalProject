#SqlCon.py
import pymssql
class SqlCon:
    conn = pymssql.connect('127.0.0.1:1433','sa','1234','WSE')  # 해당 인자도 다 변수로 사용할 수 있으면 좋다

    @staticmethod
    def Cursor():
        return SqlCon.conn.cursor()

    @staticmethod
    def Close():
        SqlCon.conn.close()

    @staticmethod
    def Commit():
        SqlCon.conn.commit()

