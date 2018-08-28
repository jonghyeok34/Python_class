import numpy as np

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)  # 배열생성
print(arr1)
print(type(arr1))

print(arr1.ndim)  # 1
print(arr1.dtype)  # float64
print(arr1.shape)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)

print("dimension:", arr2.ndim)
print("data type:", arr2.dtype)
print("x행 y열:", arr2.shape)
