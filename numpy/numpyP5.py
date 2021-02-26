"""
Numpy常用的数学统计函数
"""

'''
1、Numpy有哪些数学统计函数：
函数名	说明
np.sum	所有元素的和
np.prod  所有元素的乘积
np.cumsum	元素的累积加和
np.cumprod	元素的累积乘积
np.min	最小值
np.max	最大值
np.percentile	0-100百分位数
np.quantile	  0-1分位数
np.median	中位数
np.average	 加权平均，参数可以指定weights
np.mean	 平均值
np.std	标准差
np.var	方差

2、怎样实现按不同的axis计算
以上函数，都有一个参数叫做axis用于指定计算轴为行还是列，如果不指定，那么会计算所有元素的结果

3、实例：机器学习将数据进行标准化
A = (A - mean(A, axis=0)) / std(A, axis=0)
'''


import numpy as np


# 1、Numpy的数学统计函数
# -------------------------------------------------------------------------
a = np.arange(1,13).reshape(3,4)
print(a)

# 若不指定axis，则Numpy的数学统计函数运算时默认将多维数组转为一维来进行计算

asum = np.sum(a)  # 和
print(asum)

aprod = np.prod(a)  # 乘积
print(aprod)

acumsum = np.cumsum(a)  # 从第一个元素到最后一个元素的分别的累计求和，即（1/1+2/1+2+3/1+2+3+4/1+2+3+4+5/...）
print(acumsum)

acumprod = np.cumprod(a)  # 从第一个元素开始累计相乘
print(acumprod)

amax = np.max(a)
print(amax)

# percentile 将元素先从小到大排列，指定在什么位置取数据。范围【0-100】。
apercentile = np.percentile(a, [25, 50, 75])  # 在排序后的1/4、1/2、3/4的位置处分别取数据
print(apercentile)
# ps: 若正好是偶数个元素，则50%会取中间两个数的平均值

# quantile 将元素先从小到大排列，指定在什么位置取数据。范围【0-1】
aquantile = np.quantile(a, [0.25, 0.5, 0.75])
print(aquantile)
# ps: 若正好是偶数个元素，则0.5会取中间两个数的平均值

amedian = np.median(a)  # 中位数
print(amedian)

amean = np.mean(a)  # 平均值
print(amean)

astd = np.std(a)  # 标准值
print(astd)

avar = np.var(a)  # 方差
print(avar)

# 加权平均  # weights的shape需要和arr一样
weights = np.random.rand(*a.shape)
aaverage = np.average(a, weights=weights)
print(aaverage)
a = np.arange(1,13).reshape(3,4)
print(a)

# 若不指定axis，则Numpy的数学统计函数运算时默认将多维数组转为一维来进行计算

asum = np.sum(a)  # 和
print(asum)

aprod = np.prod(a)  # 乘积
print(aprod)

acumsum = np.cumsum(a)  # 从第一个元素到最后一个元素的分别的累计求和，即（1/1+2/1+2+3/1+2+3+4/1+2+3+4+5/...）
print(acumsum)

acumprod = np.cumprod(a)  # 从第一个元素开始累计相乘
print(acumprod)

amax = np.max(a)
print(amax)

# percentile 将元素先从小到大排列，指定在什么位置取数据。范围【0-100】。
apercentile = np.percentile(a, [25, 50, 75])  # 在排序后的1/4、1/2、3/4的位置处分别取数据
print(apercentile)
# ps: 若正好是偶数个元素，则50%会取中间两个数的平均值

# quantile 将元素先从小到大排列，指定在什么位置取数据。范围【0-1】
aquantile = np.quantile(a, [0.25, 0.5, 0.75])
print(aquantile)
# ps: 若正好是偶数个元素，则0.5会取中间两个数的平均值

amedian = np.median(a)  # 中位数
print(amedian)

amean = np.mean(a)  # 平均值
print(amean)

astd = np.std(a)  # 标准值
print(astd)

avar = np.var(a)  # 方差
print(avar)

# 加权平均  # weights的shape需要和arr一样
weights = np.random.rand(*a.shape)
aaverage = np.average(a, weights=weights)
print(aaverage)



# 2、Numpy的axis参数的用途
# -------------------------------------------------------------------------
# 上面所有的函数其实都有axis这个参数，当没有设定这个参数时，默认将各种形状的数组转化为一维数组来对待，再进行各种函数操作

# axis=0代表行、axis=1代表列

# 对于sum/mean/media等聚合函数：
# 理解1：axis=0代表把行消解掉，axis=1代表把列消解掉
# 理解2：axis=0代表跨行计算，axis=1代表跨列计算

a = np.arange(1,13).reshape(3,4)
print(a)

asum0 = a.sum(axis=0)  # 每列相加，最后生成一行四列的数组 / 跨行计算，将每行的同一列数据加起来
print(asum0)

asum1 = a.sum(axis=1)  # 每行相加，最后生成一行三列的数组 / 跨列计算，将每列的同一行数据加起来
print(asum1)

acumsum0 = a.cumsum(axis=0)  # 跨行累加 / 即列数不变，以每列为单位，跨行的元素累加
print(acumsum0)

acumsum1 = a.cumsum(axis=1)  # 跨列累加 / 即行数不变，以每行为单位，跨列的元素累加
print(acumsum1)



# 3、实例：机器学习将数据进行标准化
# -------------------------------------------------------------------------
arr = np.arange(12).reshape(3, 4)
print(arr)

'''
arr如果对应到现实世界的一种解释：
  行：每行对应一个样本数据
  列：每列代表样本的一个特征

数据标准化：
  对于机器学习、神经网络来说，不同列的量纲应该相同，训练收敛的更快；
  比如商品的价格是0到100元、销量是1万到10万个，这俩数字没有可比性，因此需要先都做标准化；
  不同列代表不同的特征，因此需要axis=0做计算
  标准化一般使用A = (A - mean(A, axis=0)) / std(A, axis=0)公式进行
'''

# 计算每列的均值
mean = np.mean(arr, axis=0)
print(mean)

# 计算每列的标准差
std = np.std(arr, axis=0)
print(std)

# 计算分子，注意每行都会分别减去[4., 5., 6., 7.]，这叫做numpy的广播
fenzi = arr - mean  # 3行4列 - 1行4列 =》 将1行4列复制转变为3行4列
print(fenzi)

result = fenzi / std
print(result)

# 用随机数再试一次 -----------
arr2 = np.random.randint(1, 100, size=(3, 4))
result = (arr2 - np.mean(arr2, axis=0)) / np.std(arr2, axis=0)
print(result)  # 结果的每列均值为0 方差为1



