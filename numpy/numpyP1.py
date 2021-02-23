# 导入包
import numpy as np
import time

# 打印版本
print(np.__version__)

# numpy与原生Python的性能对比--------------------------------------------------

# 需求：实现两个数组额加法

# 1.原生python
def sum_python(n):
    a = [i ** 2 for i in range(n)]  # 平方
    b = [i ** 3 for i in range(n)]  # 立方
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
        pass
    return c


print(sum_python(10))


# 2.numpy实现
def sum_numpy(n):
    '''
    numpy实现两个数组的加法（对应位上元素相加）
    （python原生语法中两个list相加是把两个list合并成一个大list而不是对应位置元素相加）
    :param n: 数组的长度
    :return: 和
    '''
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b  # 对应位上元素相加


r = sum_numpy(10)
print(r)
print(type(r))


# 运行时间的比较--------------------

# 1.原生python
tps = time.time()
for i in range(10000):
    sum_python(100)
    i += 1
tpe = time.time()
print('python time cost', tpe - tps, 's')

# 2.numpy实现
tns = time.time()
for i in range(10000):
    sum_numpy(100)
    i += 1
tne = time.time()
print('numpy time cost', tne - tns, 's')
