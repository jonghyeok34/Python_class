# 일반 매개변수와 가변 매개 변수 같이 사용되는 함수


# 반드시 일반 매개변수가 먼저와야 함.
def print_args(n, *args):
    for i in range(n):
        print(args[i])


# 함수 호출
print_args(3, '파이썬', '오라클', '자바')
