# items() :딕셔너리의 key, value 모두 추출

# dic = {'이름': 출생아수}

names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

items = names.items()
print(items)

for item in names.items():
    print(item)

for k, v in names.items():
    print(k, ':', v)
