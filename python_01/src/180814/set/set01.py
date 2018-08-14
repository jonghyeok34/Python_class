# 집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만들어진 자료형

# 집합(set) 자료형의 특징
# 1 중복 데이터 저장 불가
# 2 순서 없는 입출력

s1 = set((1, 2, 3, 3))
print('s1:', s1)

s2 = set('Hello')  # H,l,e,o
print('s2:', s2)

# set 자료형 인덱스로 접근 하려면?
# 리스트나 튜플로 변환한 후에 접근 가능

s3 = set([1, 2, 3])
# s3[2]  오류 발생

# set -> 리스트 :list()
list3 = list(s3)
print(list3[2])

# set -> 튜플 : tuple()
t3 = tuple(s3)
print(t3[2])

# 교집합(&), 합집합(|), 차집합(-)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 : &, intersection()
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 : |, union()
print(s1 | s2)
print(s1.union(s2))

# 차집합 : -, difference()
print(s1-s2)
print(s1.difference(s2))

print(s2-s1)
print(s2.difference(s1))

