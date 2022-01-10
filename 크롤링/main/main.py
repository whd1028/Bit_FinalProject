# main.py

from Function import Function

def main():
    print("언론사 업데이트 중")
    #Function.press()
    print("언론사 업데이트가 끝났습니다.")
    print("==================================================================================================")
    print("뉴스 정보를 DB에 넣습니다.")
    Function.news()


if __name__ == "__main__":
    main()
