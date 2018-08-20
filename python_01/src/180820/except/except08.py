# raise : 강제로 예외 발생

def some_function():
    num = int(input('1~10 사이의 정수를 입력하세요'))

    if num < 1 or num > 10:
        raise Exception('{} : 유효하지 않은 숫자입니다.'.format(num))

    else:
        print('입력한 숫자는 {}'.format(num))


try:
    some_function()
except Exception as e:
    print(e)
