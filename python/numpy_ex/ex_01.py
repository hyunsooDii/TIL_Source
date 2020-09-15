# 배열 - 동일 data type

import numpy as np

data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
print(a1)

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print(a2)

print(a1.dtype)
print(a2.dtype)

data3 = np.array([0.5, 2, 0.01, 8])
print(data3)

data4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data4)