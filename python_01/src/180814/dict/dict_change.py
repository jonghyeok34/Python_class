# in 연산자를 이용해 딕셔너리에
# 프로그램 작성

# dic ={'이름' : 출생아수}
names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

k = input('이름을 입력하세요')

if(names[k]):
    names[k] =10

print(names)
