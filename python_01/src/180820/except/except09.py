# 사용자 정의 예외 클래스

class InvalidIntException(Exception):
    def __init__(self, arg):
        super().__init__('정수가 아닙니다.{}'.format(arg))


# 정수로 변환해주는 함수
def convert_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalidIntException(text)


if __name__ == '__main__':
    try:
        text = input('숫자를 입력하세요')
        number = convert_to_integer(text)
    except Exception as e:
        print("예외가 발생했습니다: {}".format(e))
    else:
        print('type of number: {}'.format(type(number)))
        print('정수형식으로 변환되었습니다 {}'.format(number))
