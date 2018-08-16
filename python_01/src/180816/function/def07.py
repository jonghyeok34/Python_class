# 가변 매개변수가 있는 함수 정의 : *

# 가변 매개 변수는 여러 개의 값을 입력 받을 수 있다.
# *를 이용해 정의된 가변 매개 변수는 입력 받은 값을 튜플로 처리한다.


def merge_string(*text):
    result = ''
    for s in text:
        result += s

    return result


# 함수 호출
print(merge_string('안녕하세요. ', '반갑습니다.'))
print(merge_string("아버지가 ", '방에 ', "들어가십니다."))
