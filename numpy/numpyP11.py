"""
Numpy中数组的乘法
"""
'''
--按照两个相乘数组A和B的维度不同，分为以下乘法：
  1.数字与一维/二维数组相乘；
  2.一维数组与一维数组相乘；
  3.二维数组与一维数组相乘；
  4.二维数组与二维数组相乘；

--numpy有以下乘法函数：
  1.*符号或者np.multiply：  逐元素乘法，对应位置的元素相乘，要求shape相同
  2.@符号或者np.matmul：  矩阵乘法，形状要求满足(n,k),(k,m)->(n,m)
  3.np.dot：  点积乘法

--解释：点积，也叫内积，也叫数量积
  两个向量a = [a1, a2,…, an]和b = [b1, b2,…, bn]的点积定义为：
  a·b = a1b1 + a2b2 + …… + anbn
'''

import numpy as np

# 1. 数字与一维数组/二维数组相乘---------------------------------------

# 一维数组
A = np.arange(10)
print(A)
a = A * 0.5  # *意思是逐元素乘法
print(a)

# 二维数组
B = np.arange(12).reshape(3, 4)
print(B)
b = B * 0.5  # *意思是逐元素乘法
print(b)


# 2. 一维数组与一维数组相乘--------------------------------------------
A = np.arange(1, 11)
B = np.arange(1, 11) * 0.1
print('A:{}'.format(A))
print('B:{}'.format(B))

# 1.逐元素乘法
ab1 = np.multiply(A,B)
print(ab1)

ab2 = A * B
print(ab2)

# 2.点积/内积/数量积
ab1 = A@B
print(ab1)

ab2 = np.matmul(A,B)
print(ab2)

ab3 = np.dot(A,B)
print(ab3)

# 以上三个，相当于
ab4 = np.sum(A*B)
print(ab4)


# 3. 二维数组和一维数组相乘---------------------------------------------
A = np.arange(1, 21).reshape(5, 4)  # 5行4列
B = np.arange(1, 5) * 0.1  # 1行5列
print('A:{}'.format(A))
print('B:{}'.format(B))

# 逐元素乘法 [A的每行的每个元素与B的每个元素相乘]
ab1 = A * B
print(ab1)

ab2 = np.multiply(A,B)
print(ab2)

# 矩阵乘法 [A的每行的每个元素与B的每个元素相乘的结果相加成为一个元素的值，即A的每行与B内积的结果作为一个元素]
ab1 = A @ B
print(ab1)

ab2 = np.matmul(A,B)
print(ab2)

ab3 = np.dot(A,B)
print(ab3)


# 4. A和B都是二维数组，实现矩阵乘法---------------------------------------
A = np.arange(12).reshape(3, 4)
B = np.arange(20).reshape(4, 5)
print('A:{}'.format(A))
print('B:{}'.format(B))
# 两个二维数组相乘，第一个数组的列数要和第二个数组的行数相等。【 a行b列 * b行c列 = a行c列 】

ab1 = A@B
print(ab1)

ab2 = np.matmul(A,B)
print(ab2)

ab3 = np.dot(A,B)
print(ab3)






