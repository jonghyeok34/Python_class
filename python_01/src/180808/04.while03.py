# 키보드로 1개단 입력을 받아 구구단 출력


dan = int(input('원하는 단을 입력하세요: '))

i = 1
while i <= 9:
    print("{} * {} = {} ".format(dan, i, dan*i))
    i += 1
