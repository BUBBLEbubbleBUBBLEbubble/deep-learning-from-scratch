"""
Numpy求解线性方程组
对于Ax=b，已知A和b，怎么算出x ?
"""

'''
1. 引入包---------------------
'''
import numpy as np

'''
2. 求解--------------------------
'''
A = np.array(
    [
        [1, -2, 1],
        [0, 2, -8],
        [-4, 5, 9]
    ]
)
b = np.array([0, 8, -9])
print(A)
print(b)

'''
3. 调用solve方法直接求解--------------------
'''
x = np.linalg.solve(A,b)
print(x)

'''
4. 验证--------------------
'''
# 验证单个方程
print(A[1].dot(x))
# 验证整个矩阵计算
print(A.dot(x) == b)