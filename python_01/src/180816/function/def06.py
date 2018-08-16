# 기본값이 있는 함수 정의

def str(text, cnt=1):
    for i in range(cnt):
        print(i + 1, text)
    print()

str('출력합니다')

str('출력합니다', 4)
