# 키보드로 입력받은 구구단 1개단 출력

dan = int(input("원하는 단을 입력해주세요: "))

for i in range(1, 10):
    print("{} * {} = {}".format(dan, i, dan*i))
