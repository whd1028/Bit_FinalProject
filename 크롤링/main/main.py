# main.py

from Function import Function

def main():
    print("==================메뉴==================")
    print("1. bs4 선택")
    print("2. selenium 선택")
    select1 = input("숫자를 입력해주세요 : ")
    if int(select1) == 1:
        print("Beautifulsoup를 선택하였습니다.")
        print("1. 언론사 업데이트")
        print("2. 과거 뉴스 넣기")
        print("3. 최신 뉴스 넣기")
        select2 = input("숫자를 입력해주세요 : ")
        if int(select2) == 1:
            print("언론사 업데이트 중")
            Function.press()
            print("언론사 업데이트가 끝났습니다.")
        elif int(select2) == 2:
            print("과거 뉴스 정보를 DB에 넣습니다.")
            Function.pastNews()
        elif int(select2) == 3:
            print("최신 뉴스 정보를 DB에 넣습니다.")
            Function.presentNews()
    elif int(select1) == 2:
        print("Selenium을 선택하였습니다.")


if __name__ == "__main__":
    main()
