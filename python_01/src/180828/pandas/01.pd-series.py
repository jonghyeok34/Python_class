import numpy as np
import pandas as pd

# 1차원 데이터는 Series() 사용
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)

# 1.스칼라(scalar) 데이터
s1 = pd.Series(7, index=['a', 'b', 'c'])
print(s1)

# 2.일차원 배열 데이터
s2 = pd.Series(np.random.randn(5))  # 난수 5개 발생
print(s2)

s3 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s3)

# 3.리스트 데이터
s4 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s4)

# 4. 딕셔너리 데이터

s5 = pd.Series({'a': 0, 'b': 1, 'c': 2})
print(s5)
