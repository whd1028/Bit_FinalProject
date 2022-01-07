# 날짜 처리하기
# 출처: https://24hours-beginner.tistory.com/116 [365일 24시간 초보]

import datetime 

def time(numdays) : # 나오게할 날짜 갯수
    baseDate = datetime.date.today() 
    d_list = [baseDate - datetime.timedelta(days=x) for x in range(numdays)]
    print("baseDate: ", baseDate) 
    date_list = []
    for date in d_list : 
        temp = date.strftime("%Y%m%d")
        date_list.append(temp)
    return date_list 

#print(type(time(15)[3]))
#print(time(15))
