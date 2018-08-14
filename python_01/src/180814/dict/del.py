# del 명령 : 딕셔너리 요소 제거
# clear() : 딕셔너리에 있는 모든 요소 제거
# dic ={'이름' : 출생아수}
names = {'Mary': 10999, 'Sam': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

# 딕셔너리에서 key가 Sam인요소 제거
del names['Sam']
print(names)

# 딕셔너리의 모든 요소 제거
names.clear()
print(names)

