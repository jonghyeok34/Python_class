# 예외처리 : try ~ except Exception  ~ except
# Exception 클래스로 예외를 받으면 다른 except 무시

my_list = [1, 2, 3]

try:
    index = int(input('인덱스 번호를 입력하세요'))
    print('{0}:{1}'.format(index, my_list[index]))
except IndexError as e:
    print('잘못 입력한 인덱스 번호 {}'.format(e))

except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다{}'.format(e))
else:
    print('리스트의 요소 출력에 성공했습니다.')
finally:
    print('항상 실행')
