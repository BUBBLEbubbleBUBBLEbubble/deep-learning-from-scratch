"""
Numpy的核心array对象以及创建array的方法
"""

'''
--array对象的背景：
# Numpy的核心数据结构，就叫做【array数组】，array对象可以是一维数组，也可以是多维数组；
# Python的List也可以实现相同的功能，但是array比List的优点在于【性能好、包含数组元数据信息、大量的便捷函数】；
# Numpy成为事实上的Scipy、Pandas、Scikit-Learn、Tensorflow、PaddlePaddle等【框架的“通用底层语言”】
# Numpy的array和Python的List的一个区别，是它【元素必须都是同一种数据类型】，比如都是数字int类型，这也是Numpy高性能的一个原因；

--array本身的属性：
# shape：返回一个【元组】，表示array的【维度】
# ndim：一个【数字】，表示array的【维度的数目】
# size：一个【数字】，表示array中【所有数据元素的数目】
# dtype：array中【元素的数据类型】

--创建array的方法：
# 从Python的列表List和嵌套列表创建array
# 使用预定函数arange、ones/ones_like、zeros/zeros_like、empty/empty_like、full/full_like、eye等函数创建
# 生成随机数的np.random模块构建

--array本身支持的大量操作和函数：
# 直接【逐元素】的【加减乘除】等算数操作
# 更好用的面向【多维】的【数组索引】
# 求sum/mean等聚合函数
# 线性代数函数，比如求解逆矩阵、求解方程组
'''

import numpy as np

# ---------------------------1. 使用Python的List和嵌套List创建一维的array和二维的array

# 创建一个一维数组，也就是Python的单元素List
x = np.array([1,2,3,4,5,6])
print(x)
# 创建一个二维数组，也就是Python的嵌套List
y = np.array([
    [1,2,3],
    [4,5,6]
])
print(y)


# ---------------------------2. 探索数组array的属性
print(x.shape)
print(y.shape)
print(x.ndim)
print(y.ndim)
print(x.size)
print(y.size)
print(x.dtype)
print(y.dtype)  # int代表数字


# ---------------------------3. 创建array的便捷函数


# 1.使用arange创建数字序列
# arange([start,] stop[, step,], dtype=None)
# 这个函数不管怎么传参，返回的都是一维向量
print(np.arange(10))
print(np.arange(2,10,2))  # 从2到9步长为2

# 2.使用ones创建全是1的数组
# np.ones(shape, dtype=None, order='C')
# shape : int or tuple of ints Shape of the new array, e.g., (2, 3) or 2.
print(np.ones(10))
print(np.ones((2,3)))

# 3.使用ones_like创建形状相同的数组
# ones_like(a, dtype=float, order='C')
# 传入一个现有的array，仿照这个形状创建全是1的数组
print(np.ones_like(x))
print(np.ones_like(y))

# 4.使用zeros创建全是0的数组
# np.zeros(shape, dtype=None, order='C')
print(np.zeros(10))
print(np.zeros((2,4)))

# 5.使用zeros_like创建形状相同的数组¶
# np.zeros_like(a, dtype=None)
print(np.zeros_like(x))
print(np.zeros_like(y))

# 6.使用empty创建全是0的数组
# empty(shape, dtype=float, order='C')
# 注意：数据是未初始化的，里面的值可能是随机值不要用。虽然都是0，但是又问题的不要用
print(np.empty(10))
print(np.empty((2,4)))

# 7.使用full创建指定值的数组
# np.full(shape, fill_value, dtype=None, order='C')
print(np.full(10,666))
print(np.full((2,4),666))

# 8.使用full_like创建形状相同的数组
# np.full_like(a, fill_value, dtype=None)
print(np.full_like(x,333))
print(np.full_like(y,555))

# 9.使用random模块生成随机数的数组
# randn(d0, d1, ..., dn)
print(np.random.randn())
print(np.random.randn(5))
print(np.random.randn(3,2))
print(np.random.randn(4,3,2))


# --------------------------- 4.array本身支持的大量操作和函数
# 这些操作如果用Python实现需要写很多for循环，用numpy数组很容易

A = np.arange(10).reshape(2,5)  # .reshape将一维数字整形成二维数字
print(A)
print(A.shape)

print(A+1)  # 给每个元素都+1. 【要是用基础python实现的话必须用for循环才行很麻烦

print(A*3)  # 每个元素*3

print(np.sin(A))  # 求每个元素的sin函数

print(np.exp(A))  # 每个元素e次方

A = np.arange(10).reshape(2,5)
B = np.random.randn(2,5)
print(B)

print(A+B)  # 对应元素的加法
print(A-B)  # 对应元素的减法
