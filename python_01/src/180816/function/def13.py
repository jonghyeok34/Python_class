# 중첩함수(nested function)
# 함수 안에 정의된 함수

import math


def stddev(*n):  # 표준편차
    def mean():  # 중첩함수(평균)
        return sum(n) / len(n)

    def variance(m):  # 중첩함수(분산)
        total = 0
        for i in n:
            total += (i - m) ** 2

        return total / (len(n) - 1)

    v = variance(mean())
    return math.sqrt(v)


print(stddev(1, 2, 3))
