# lambda

# 1. 이름이 없는 한 줄 짜리 함수
# 2. 일반적인 함수를 사용하기 힘든 경우 사용

# 형식 : lambda 인자1, 인자2..: 실행 코드

# lambda 정의
add = lambda x, y: x + y


def add1(x, y): return x + y


ret1 = add(1, 3)
print('ret1', ret1)

func = [lambda x: x + '.ppt', lambda x: x + '.docx']
ret2 = func[0]('Intro')
ret3 = func[1]('REPORT')
print('ret2', ret2)
print('ret3', ret3)

# dic ={'이름' : 출생아수}
names = {'Mary': 10999, 'Sams': 2111, 'Amy': 9778, 'Tom': 20245,
         'Micheal': 27115, 'Bob': 5887, 'Kelly': 7855}

# 이름 기준으로 정렬 key (x[0])
s_names1 = sorted(names.items(), key=lambda x: x[0])
print(s_names1)

# 출생아 수 기준으로 정렬 value (x[1])
s_names2 = sorted(names.items(), key=lambda x: x[1])
print(s_names2)

