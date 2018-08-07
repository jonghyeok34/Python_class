# 조건문 : if ~else문
# 키보드로 입력한 값이 홀수인지 짝수인지 판별하는 프로그램

num = int(input('정수를 입력해주세요: '))

if num % 2 == 0:
    print('{}은 짝수입니다.'.format(num))
else:
    print('{}은 홀수입니다.'.format(num))

for i in range(0, 2):
    print(i)