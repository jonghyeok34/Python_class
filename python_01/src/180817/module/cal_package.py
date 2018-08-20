# my_package 패키지 안에 있는 calculator.py 모듈 파일 불러오기

# 방법 1.
# from 패키지명 import 모듈명

from my_package import calculator

print(calculator.plus(10, 3))

# 방법 2
# import 패키지명.모듈명
import my_package.calculator

print(my_package.calculator.plus(10, 3))
# print(calculator.plus(10, 3))  # 방법 2로 할 시에는 패키지경로까지 모두 적어주어야 함.


# 방법 3
# import 패키지명.모듈명 as 별칭
import my_package.calculator as cal

print(cal.plus(10, 3))
print(cal.minus(10, 3))
print(cal.multiply(10, 3))
print(cal.divide(10, 3))


# 예제
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 5])
plt.ylabel('some numbers')
plt.show()
