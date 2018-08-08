# 1부터 100까지의 홀수 짝수끼리의 합을 각각 구하기

even = 0
odd = 0

for i in range(1, 101):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("1부터 100까지의 홀수의 합:", odd)
print("1부터 100까지의 짝수의 합:", even)
