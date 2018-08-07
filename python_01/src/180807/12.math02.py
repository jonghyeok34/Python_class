import math
from math import factorial

# math 모듈의 pi와 e
print(math.pi)
print(math.e)

# 제곱:pow() / 제곱근:sqrt()
print('2의 세제곱', math.pow(2, 3))
print('5의 제곱근', math.sqrt(5))

# factorial()
print('4! =', math.factorial(4))
print('5! =', math.factorial(5))
print('10! =', math.factorial(10))
print('100! =', math.factorial(100))
print('10000! =', math.factorial(10000))
print('4!=', factorial(4))  # factorial() 이라는 함수만으로도 사용 가능(함수 import 시)

