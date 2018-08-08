# 키보드로 입력한 점수가 어느 학점에 해당하는지 판별하는 프로그램 작성

s = int(input("0~100점 사이의 점수를 입력하세요: "))


if s >= 90:
    print('A학점')
elif s >= 80:
    print('B학점')
elif s >= 70:
    print('C학점')
elif s >= 60:
    print('D학점')
else:
    print('E학점')
