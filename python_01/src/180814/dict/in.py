# in 연산자를 이용해 딕셔너리에
# 프로그램 작성

# dic ={'이름' : 출생아수}
names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

k = input('이름을 입력하세요')

if k in names:
    print("이름이 %s인 출생아수는 %d명입니다." % (k, names[k]))

else:
    print('자료에 %s인 이름이 존재하지 않습니다.' %k)
