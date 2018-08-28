import numpy as np

# 배열의 자료형을 변경하기 위해서는 astype()함수로 변경 할 수 있다.
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.float32)
print(arr1.dtype)
print(arr2.dtype)

arr3 = np.array([1, 2, 3, 4, 5])
print(arr3.dtype)
float_arr3 = arr3.astype(np.float64)
print(float_arr3)
print(float_arr3.dtype)

arr4 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr4.dtype)
int_arr4 = arr4.astype(np.int32)
print(int_arr4)
print(int_arr4.dtype)
