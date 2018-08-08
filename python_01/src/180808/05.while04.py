
# 구구단 2~9단 출력


dan = 2
while dan <= 9:
    print("[{}단]".format(dan))
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(dan, i, dan*i))
        i += 1
    dan += 1


coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee -= 1
    print("남은 커피의 양은 {}개 입니다.".format(coffee))
    if not coffee:
        print("커피가 다 떨어져 판매를 중지합니다")
        break;