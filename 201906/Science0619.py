import numpy as np

# 数组 np.array(list)
a = np.array([1.0, 2.0, 3.0])
print(a)
a[1] = 9.0
print(a)
# [1. 2. 3.]
# [1. 9. 3.]

# 矩阵 np.array([list,list...])
# 制定数据类型 dtype=np.float64
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
print(A)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 等差序列
start = 0.0
end = 1.0
number = 11
a = np.linspace(start,end,number)
print(a)
# [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]

A = np.random.random((3, 3))
B = np.random.random((3, 3))
print(A)
print(B)
print((A + B))

exit()
