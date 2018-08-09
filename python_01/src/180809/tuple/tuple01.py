# 튜플(tuple)

# 튜플 생성1

a = (1, 2, 3, 'a', 'b', 'c')
print(a)
print(type(a))

# 튜플 생성2

b = 1, 2, 3, 4
print(b)
print(type(b))


# 튜플(슬라이싱) : [start:end]

c = (1, 2, 3, 4, 5, 6)
print(c[0])
print(c[3])
print(c[1:3])   # 처음부터 3번째 앞까지
print(c[:3])    # 처음부터 3번째 앞까지
print(c[2:])    # 2번부터 끝까지


# 튜플 연산
d = (1, 2, 3)
e = (4, 5, 6)
f = d + e
print('f:', f)

# 튜플 원소 수정 : 튜플은 원소의 값을 수정할 수 없다.
g = (1, 2, 3)
# g[0] = 10     # 'tuple' object does not support item assignment
# print(g)

# 튜플 패킹(tuple packing) : 여러 데이터를 튜플로 묶는 것

j = 1, 2, 3
print(j)

# 튜플 언패킹(tuple unpacking)
# : 튜플의 각 요소를 여러 개의 변수에 할당하는 것

one, two, three = j
print('one=', one)
print('two=', two)
print('three=', three)

# 언패킹을 이용한 변수에 다중 할당
city, latitude, longtitude = 'Seoul', 37.541, 126.986
print('city =', city)
print('latitude =', latitude)
print('longtitude =', longtitude)


# index() : 튜플 요소의 index번호를 구해주는 함수

k = ('abc', 'def', 'ghi')
print('index번호:', k.index('def'))

# count() : 매개 변수로 전달된 값과 같은 요소의 개수를 구해주는 함수

m = (1, 100, 2, 100, 3, 100)
print(m.count(100))
