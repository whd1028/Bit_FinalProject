# main.py

from Function import Function

def main():
    print("==================메뉴==================")
    print("1. 언론사 업데이트")
    print("2. 과거 뉴스 넣기")
    print("3. 최신 뉴스 넣기")
    select = input("숫자를 입력해주세요 : ")
    if int(select) == 1:
        print("언론사 업데이트 중")
        Function.press()
        print("언론사 업데이트가 끝났습니다.")
    elif int(select) == 2:
        print("과거 뉴스 정보를 DB에 넣습니다.")
        Function.pastNews()
    elif int(select) == 3:
        print("최신 뉴스 정보를 DB에 넣습니다.")
        Function.presentNews()

if __name__ == "__main__":
    main()
