# values()

names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

vals = names.values()
print(vals)

# 리스트 생성
vals_list = list(vals)
ret = sum(vals_list)  # 리스트의 합
print('출생아 수 총계', ret)
