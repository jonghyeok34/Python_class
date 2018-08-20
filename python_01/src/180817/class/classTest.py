# if __name__ = '__main__':
# __name__은 현재 모듈의 이름을 가지는 내장 변수
# 구현한 코드가 다른 파이썬 파일에 의해 import해서 사용할 수 없다.

class Test:
    a = 30
    b = 'python'


if __name__ == '__main__':
    t = Test()  # 인스턴스화
    print(t.a)
    print(t.b)
