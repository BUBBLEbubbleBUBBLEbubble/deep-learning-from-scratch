"""
Numpy非常重要有用的数组合并操作
"""
'''
--背景：在给机器学习准备数据的过程中，经常需要进行不同来源的数据合并的操作。

--两类场景：
1.给已有的数据添加多行，比如增添一些样本数据进去；(一般对于机器学习，行就是样本)
2.给已有的数据添加多列，比如增添一些特征进去； (列代表特征)

--以下操作均可以实现数组合并：
  np.concatenate(array_list, axis=0/1）：  沿着指定axis进行数组的合并
  np.vstack或者np.row_stack(array_list)：  垂直vertically、按行row wise进行数据合并
  np.hstack或者np.column_stack(array_list)：  水平horizontally、按列column wise进行数据合并
'''

import numpy as np

# 1. 怎样给数据添加新的多行 (列数相同) -------------------------------------------------
a = np.arange(6).reshape(2, 3)  # 2行3列
b = np.random.randint(10, 20, size=(4, 3))  # 4行3列
print('a={}'.format(a))
print('b={}'.format(b))

# 方法1：
ab1 = np.concatenate([a, b])  # 默认axis=0是按行合并
print(ab1)

# 方法2
ab2 = np.vstack([a, b])
print(ab2)

# 方法3
ab3 = np.row_stack([a, b])
print(ab3)

# 2. 怎样给数据添加新的多列 (行数相同) ---------------------------------------
a = np.arange(12).reshape(3, 4)
b = np.random.randint(10, 20, size=(3, 2))
print('a={}'.format(a))
print('b={}'.format(b))

# 方法1
ab1 = np.concatenate([a, b], axis=1)  # axis=1指按列合并
print(ab1)

# 方法2
ab2 = np.hstack([a, b])
print(ab2)

# 方法3
ab3 = np.column_stack([a, b])
print(ab3)

