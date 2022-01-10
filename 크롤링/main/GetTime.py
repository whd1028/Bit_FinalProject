# GetTime.py
import datetime 

class GetTime():
    # 시간 처리해서 가져오기
    @staticmethod
    def getTime(numdays) : # 나오게할 날짜 갯수
        baseDate = datetime.date.today() 
        d_list = [baseDate - datetime.timedelta(days=x) for x in range(numdays)]
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 

    # 2019년부터 가져오기
    @staticmethod
    def getTime_Past() : # 나오게할 날짜 갯수
        baseDate = datetime.date(2019, 1, 1)
        d_day = datetime.date.today() - baseDate
        d_day = int(str(d_day)[0:4])
        d_list = [baseDate + datetime.timedelta(days=x) for x in range(d_day)]
        print("baseDate: ", baseDate) 
        date_list = []
        for date in d_list : 
            temp = date.strftime("%Y%m%d")
            date_list.append(temp)
        return date_list 