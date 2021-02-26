"""
Numpy怎样给数组增加一个维度
"""

'''
-背景：
很多数据计算都是二维或三维的，对于一维的数据输入为了形状匹配，经常需升维变成二维

-需要：
在不改变数据的情况下，添加数组维度；（注意观察这个例子，维度变了，但数据不变）
原始数组：一维数组arr=[1,2,3,4]，其shape是(4, )，取值索引分别为arr[0],arr[1],arr[2],arr[3]
变形数组：二维数组arr[[1,2,3,4]]，其shape实(1,4),【即一行四列，数据的本身没有变，只是维度增加了】 取值索引分别为a[0,0],a[0,1],a[0,2],a[0,3]

-实操：
经常需要在纸上手绘数组的形状，来查看不同数组是否形状匹配，是否需要升维降维来对齐

-3种方法：
np.newaxis：关键字，使用索引的语法给数组添加维度
np.expand_dims(arr, axis)：方法，和np.newaxis实现一样的功能，给arr在axis位置添加维度
np.reshape(a, newshape)：方法，给一个维度设置为1完成升维。 newshape可以是数字（一维）可以是元组（多维）
'''

import numpy as np

arr = np.arange(5)
print(arr)
print('arr shape:{}'.format(arr.shape))  # 注意，当前是一维向量

# 方法1：np.newaxis关键字 --------------------------------------------------------

# 注意：np.newaxis其实就是None的别名
print(np.newaxis is None)
print(np.newaxis == None)
# 即以下所有的np.newaxis的位置，都可以用None替代

# 给一维向量添加一个行维度---------------------
a = arr[np.newaxis, :]
print(a)
print(a.shape)
# 数据现在是(一行*五列)，数据本身没有增减，只是多了一级括号

a = arr[None, :]
print(a)
print(a.shape)

# 给一维向量添加一个列维度-------------------
b = arr[:, np.newaxis]
print(b)
print(b.shape)
# 数据现在是(五行*一列)，数据本身没有增减，只是多了一级括号

b = arr[:, None]
print(b)
print(b.shape)

# 方法2：np.expand_dims方法 -----------------------------------------------------------
# np.expand_dims方法实现的效果，和np.newaxis关键字是一模一样的
print(arr)
print('arr shape:{}'.format(arr.shape))  # 注意，当前是一维向量

# 给一维数组添加一个行维度 ----------------
a = np.expand_dims(arr, axis=0)  # 相当于arr[np.newaxis, :]
print(a)
print(a.shape)

# 给一维数组添加一个列维度 ----------------
b = np.expand_dims(arr, axis=1)  # 相当于arr[:, np.newaxis]
print(b)
print(b.shape)

# 方法3：np.reshape方法 -----------------------------------------------------------------
print(arr)
print('arr shape:{}'.format(arr.shape))  # 注意，当前是一维向量

# 给一维数组添加一个行维度/列维度---------------------
a = np.reshape(arr, (1, 5))  # 一行五列
print(a)
print(a.shape)
b = np.reshape(arr, (5, 1))  # 五行一列
print(b)
print(b.shape)


# 有个问题这个5，可能再现实案例中不不好得到这个数据,索引这是用-1来代替，它会自动算出这个数字
aa = np.reshape(arr, (1, -1))  # 一行n列  # numpy见到这个-1会用（元素个数/给的行数）算出这里应该的列数，即5/1=1
print(aa)
print(aa.shape)
bb = np.reshape(arr, (-1, 1))  # n行一列
print(bb)
print(bb.shape)
