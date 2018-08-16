# sorted() : key 값을 이용해 오름차순으로 정렬

# dic ={'이름' : 출생아수}
names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

print(names)
ret1 = sorted(names)
print(ret1)


# 딕셔너리의 key를 return 하는 함수
def f1(x):
    return x[0]


# 딕셔너리의 value를 return 하는 함수
def f2(x):
    return x[1]


# 딕셔너리 key를 기준으로 오름차순(사전 순) 정렬
ret2 = sorted(names.items(), key=f1)

print("ret2=", ret2)

# 딕셔너리 value를 기준으로 오름차순 정렬: e.g) 1,2,3..
ret3 = sorted(names.items(), key=f2)
print("ret3=", ret3)

# 딕셔너리 key를 기준으로 내림차순(사전 순) 정렬
ret4 = sorted(names.items(), key=f1, reverse=True)
print("ret4=", ret4)

# 딕셔너리 value를 기준으로 내림차순 정렬: e.g) 3,2,1..
ret5 = sorted(names.items(), key=f2, reverse=True)
print("ret5=", ret5)
