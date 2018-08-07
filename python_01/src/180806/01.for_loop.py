# 1부터 10까지 합
sum = 0

for i in range(1, 11):
    sum += i
print("sum is", sum, ", 인정?")


for i in range(1, 10):
    print()
    print('[', i, '단', ']')

    for j in range(1, 10):
        print('{0}*{1} = {2}'.format(i, j, i * j))