# from 모듈명 import 변수명, 함수명
# 와일드 카드(*)를 사용하면 모듈 내 모든 변수와 모든 함수를 이용가능

# from calculator import plus
# from calculator import minus  # import
# from calculator import multiply  # import
# from calculator import divide  # import

# from calculator import plus, minus, multiply, divide  # 한줄에 임포트 가능
from calculator import *  # 한줄에 임포트 가능

print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
