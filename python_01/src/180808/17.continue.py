

# 1부터 10 사이의 수 중에 홀수만 출력
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("홀수=", i)

# 1 ~100 중에서 5의 배수만 출력

for i in range(1, 101):
    if i % 5 != 0:
        continue
    print("5의 배수:", i)