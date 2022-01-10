# NewsCatSql.py

from SqlCon import SqlCon

class NewsCatSql():
    # 언론사 전체 가져오기
    @staticmethod
    def findnidNumber():
        cursor = SqlCon.Cursor()
        query = str.format("select cd_id, c_id, cd_name from N_category_detail")
        try: 
            cursor.execute(query)
            row = cursor.fetchall()     # 검색 결과 중에 하나의 Row를 fetch하시오.
            SqlCon.Commit()
        except:
            return None
        else:
            return row
