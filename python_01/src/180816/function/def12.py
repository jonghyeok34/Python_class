# 함수를 변수에 담아서 사용하기

# 예1
def something(a):
    print(a)


# 함수 이름을 변수 p에 저장
p = something
p(123)
p('abc')


# 예2
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


first = [plus, minus]
print(first[0](1, 2))  # plus실행
print(first[1](1, 2))  # minus실행


# 예3: 함수를 매개 변수로 사용
def hello_korean():
    print('안녕하세요')


def hello_english():
    print('hello')


def greet(hello):  # 함수를 매개변수로 전달한 함수
    hello()

greet(hello_english)
greet(hello_korean)
