"""
Numpy实现SVD矩阵分解
"""
'''
--奇异值分解（Singular Value Decomposition，SVD）是一种矩阵分解（Matrix Decomposition）的方法。

--任意一个矩阵可以奇异值分解成三个矩阵：
  A (m*n) = U (m*m) * S (m*n) * V' (n*n)
  PS: S是个对角矩阵，即除了对角线其余元素都是0.
      V'指转置

'''


# 1. 引入包 ------------------------------------------
import numpy as np

# 2. 实现矩阵分解 ------------------------------------------
A = np.random.randint(1,10,(8,4))
print(A)

# 实现矩阵分解 --------------------------------
U, S, V = np.linalg.svd(A, full_matrices=False)
print('U.shape: {}, S.shape: {}, V.shape: {} ' .format(U.shape, S.shape, V.shape))
print('U={}'.format(U))
print('S={}'.format(S))  # 因为是对角矩阵，这里进行了简写
print('diag.S={}'.format(np.diag(S)))
print('V={}'.format(V))


# 3. 从分量还原矩阵 ------------------------------------------
a = U @ np.diag(S) @ V
print(a)




