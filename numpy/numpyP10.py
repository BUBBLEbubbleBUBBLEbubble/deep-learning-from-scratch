"""
Numpy怎样对数组排序
"""
'''
--Numpy给数组排序的三个方法：
  numpy.sort：返回排序后数组的拷贝  https://numpy.org/doc/stable/reference/generated/numpy.sort.html
  array.sort：原地排序数组而不是返回拷贝
  numpy.argsort：间接排序，返回的是排序后的数字索引

--3个方法都支持一个参数kind，可以是以下一个值：
  quicksort：快速排序，平均O(nlogn)，不稳定情况
  mergesort：归并排序，平均O(nlogn)，稳定排序
  heapsort：堆排序，平均O(nlogn)，不稳定排序
  stable：稳定排序

--kind默认值是quicksort，快速排序平均情况是最快，保持默认即可
'''


import numpy as np
import time

# 1. np.sort返回排序后的数组 ----------------------------------------------
arr = np.array([3, 2, 4, 5, 1, 9, 7, 8, 6])
print('原arr:{}'.format(arr))
arr1 = np.sort(arr)  # 返回拷贝后的数组
print('排序后：{}'.format(arr1))
print('原arr:{}'.format(arr))  # 原数组不变

# 2. array.sort进行原地排序-------------------------------------------------
arr = np.array([3, 2, 4, 5, 1, 9, 7, 8, 6])
print('原arr:{}'.format(arr))
# arr2 = arr.sort() 这样arr2会返回None。因为.sort()本身是对arr的一种函数操作，即相当于本身是个函数集合，在处理一个函数，而这个函数没有返回一个元素，而是只对arr进行了修改
arr.sort()
arr2 = arr
print('排序后：{}'.format(arr2))
print('原arr:{}'.format(arr))  # 原数组变了

# 3. np.argsort 返回的是有序数字的索引-----------------------------------------------------
arr = np.array([3, 2, 4, 5, 1, 9, 7, 8, 6])
print('原arr:{}'.format(arr))
# 获得排序元素对应的索引数字列表
indices = np.argsort(arr)
print('排序的索引：{}'.format(indices))
arr3 = arr[indices]  # 可以直接获取对应的数据列表
print('排序后：{}'.format(arr3))
print('原arr:{}'.format(arr))  # 原数组不变

# 4. Python原生sorted与np.sort的性能对比------------------------------------------------

arr_np = np.random.randint(0, 100, 100*10000)
time_start1 = time.time()
np.sort(arr_np) #
time_end1 = time.time()
print('numpy np.sort time cost', time_end1-time_start1,'s')

# 将numpy arr变成python list
arr_py = arr_np.tolist()
time_start2 = time.time()
sorted(arr_py)
time_end2 = time.time()
print('python sorted time cost', time_end2-time_start2,'s')

# 显然numpy np.sort的时间要少很多

