"""
Numpy计算数组中满足条件元素个数
"""
'''
总结：numpy的布尔索引用法。 arr[arr本身与数字进行比较的表达式]
'''
'''
需求：有一个非常大的数组比如1亿个数字，求出里面数字小于5000的数字数目
'''

import time
import numpy as np

# 1. 使用numpy的random模块生成1亿个数字------------------
arr = np.random.randint(1, 10000, size=int(1e8))  # 10的8次方=一亿
print(arr[:10])  # 查看前十个数字
print(arr.size)  # 查看数组大小

# 2. 使用Python原生语法实现------------------------------
pyarr = list(arr)  # 转换成python中的list类型
# 计算下结果，用于对比是否准确
time_start1 = time.time()
l = len([x for x in pyarr if x > 5000])  # 应该大约是一半
time_end1 = time.time()
print(l)
print('python''s time cost', time_end1 - time_start1, 's')

# 3. 使用numpy的向量化操作实现-----------------------------
# 计算下结果，用于对比是否准确
time_start2 = time.time()
s = arr[arr > 5000].size  # arr>5000返回的是布尔值，这样arr[true].size就指的是元素大于5000的总个数
time_end2 = time.time()
print(s)
print('(arr>5000)[:10]:{}'.format((arr > 5000)[:10]))  # (arr>5000)输出的是true/false, 查看前十个
print('arr[arr>5000][:10]:{}'.format(arr[arr > 5000][:10]))  # 这里注意只会输出上一行为true的元素，即输出元素>5000的前十个数字。arr[true]
print('python''s time cost', time_end2 - time_start2, 's')

# 4. 对比下时间 -------------------------------------------
# 16.8*1000 / 590 = 28.47457627118644
# 所以用numpy比原生语法快了很多很多
