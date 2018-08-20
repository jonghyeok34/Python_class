# 예외처리 : try ~ except ~except

# 코드에서 예외 발생 내용을 확인 할 떄 사용

my_list = [1, 2, 3]

try:
    index = int(input('인덱스 번호를 입력하세요'))
    print(my_list[index]/0)

except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다{}'.format(e))
except IndexError as e:
    print('잘못 입력한 인덱스 번호 {}'.format(e))
