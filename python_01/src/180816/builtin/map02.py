# map()
# 인자를 바꾸어가며 함수를 반복호출해 결과를 리턴 받는 함수

li = [1, 2, 3, 4, 5]
ld = lambda x: x * x


def f(x): return x * x


print("반복문을 이용한 실행")
for imsi in li:
    print(f(imsi), end=' ')

print('\nmap함수를 이용한 실행')

result = list(map(ld, li))
print(result)

print('\nlambda & map함수를 이용한 실행')
result2 = list(map(lambda x: x * x, li))
print(result2)
