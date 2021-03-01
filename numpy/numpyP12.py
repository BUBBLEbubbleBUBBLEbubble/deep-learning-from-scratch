"""
Numpy中重要的广播概念
"""
'''
--广播：
  简单理解为用于不同大小数组的二元通用函数（加、减、乘等）的一组规则

--广播的规则：
1.如果两个数组的维度数dim不相同，那么小维度数组的形状将会在左边补1
2.如果shape的维度不匹配，但是有维度是1，那么可以扩展维度是1的维度匹配另一个数组；
3.如果shape的维度不匹配，但是没有任何一个维度是1，则匹配失败引发错误；
'''

'''菜鸟教程总结
--广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。
  如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
  当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。

--广播的规则:
  让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
  输出数组的形状是输入数组形状的各个维度上的最大值。
  如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
  当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。

--简单理解：对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足：
  数组拥有相同形状。
  当前维度的值相等。
  当前维度的值有一个是 1。
  若条件不满足，抛出 "ValueError: frames are not aligned" 异常。
'''

import numpy as np


# 实例1：二维数组加一维数组 --------------------------------------------
a = np.ones((2,3))  # 2行3列
b = np.arange(3)  # 1行3列
print('a:{}'.format(a))
print('b:{}'.format(b))
print('a.shape {}'.format(a.shape))
print('b.shape {}'.format(b.shape))

# 形状不匹配但是可以相加
c = a + b  # a(2行3列) + b(1行3列) = a的两行分别加b
print(c)

'''
--分析：a.shape=(2, 3), b.shape=(3,)
  根据规则1，b.shape会变成(1, 3)
  根据规则2，b.shape再变成(2, 3)，相当于在行上复制
  完成匹配
'''


# 实例2：两个数组均需要广播 ------------------------------------
a = np.arange(3).reshape((3, 1))
b = np.arange(3)
print('a:{}'.format(a))
print('b:{}'.format(b))
print('a.shape {}'.format(a.shape))
print('b.shape {}'.format(b.shape))
c = a+b
print(c)

'''
--分析：a.shape为(3,1)，b.shape为(3,)：

  根据规则1，b.shape会变成(1, 3)
  根据规则2，b.shape再变成(3, 3)，相当于在行上复制
  根据规则2，a.shape再变成(3, 3)，相当于在列上复制
  完成匹配
'''


# 实例3：不匹配的例子 ------------------------------------
a = np.ones((3,2))
b = np.arange(3)
print('a:{}'.format(a))
print('b:{}'.format(b))
print('a.shape {}'.format(a.shape))
print('b.shape {}'.format(b.shape))
# c = a + b  # 会报错
# print(c)

'''
分析：a.shape为(3,2)，b.shape为(3,)：

根据规则1，b.shape会变成(1, 3)
根据规则2，b.shape再变成(3, 3)，相当于在行上复制
根据规则3，形状不匹配，但是没有维度是1，匹配失败报错
'''


# 实例4：numpy两个数组的相加、相减以及相乘都是对应元素之间的操作。---------------------
x = np.array([[2,2,3],[1,2,3]])
y = np.array([[1,1,3],[2,2,4]])
print('x:{}'.format(x))
print('y:{}'.format(y))
print('x.shape {}'.format(x.shape))
print('y.shape {}'.format(y.shape))
z = x * y  # numpy当中的数组相乘是对应元素的乘积，与线性代数当中的矩阵相乘不一样
print('z:{}'.format(z))
print('z.shape {}'.format(z.shape))


# 实例5：（乘法）当两个数组的形状并不相同的时候，我们可以通过扩展数组的方法来实现相加、相减、相乘等操作，。---------------------
x = np.array([[1,1,1],[2,2,2],[3,3,3]])  # 3行3列
y = np.array([[1,2,3]])  # 1行3列
print('x:{}'.format(x))
print('y:{}'.format(y))
print('x.shape {}'.format(x.shape))
print('y.shape {}'.format(y.shape))
z = x * y
print('z:{}'.format(z))
print('z.shape {}'.format(z.shape))
'''
首先将y复制三行形成3行3列，然后与x相乘
'''