# 2단 ~ 9단까지 출력 작성 (for 문)

# ,를 이용해 출력
for dan in range(2, 10):
    print("[", dan, "단]")
    for i in range(1, 10):
        print(dan, "*", i, "=", dan*i)

# format()을 이용해 출력
for dan in range(2, 10):
    print("[{} 단]".format(dan))
    for i in range(1, 10):
        print("{}*{}={}".format(dan, i, dan*i))

