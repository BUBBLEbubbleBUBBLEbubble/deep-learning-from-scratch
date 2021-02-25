"""
Numpy常用random随机函数汇总
"""

'''
--官方文档地址：https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html

--Simple random data
rand(d0, d1, ..., dn)	Random values in a given shape.
randn(d0, d1, ..., dn)	Return a sample (or samples) from the “standard normal” distribution.
randint(low[, high, size, dtype])	Return random integers from low (inclusive) to high (exclusive).
random_integers(low[, high, size])	Random integers of type np.int between low and high, inclusive.
random_sample([size])	Return random floats in the half-open interval [0.0, 1.0).
random([size])	Return random floats in the half-open interval [0.0, 1.0).
ranf([size])	Return random floats in the half-open interval [0.0, 1.0).
sample([size])	Return random floats in the half-open interval [0.0, 1.0).
choice(a[, size, replace, p])	Generates a random sample from a given 1-D array
bytes(length)	Return random bytes.

--Permutations
shuffle(x)	Modify a sequence in-place by shuffling its contents.
permutation(x)	Randomly permute a sequence, or return a permuted range.
Distributions
beta(a, b[, size])	Draw samples from a Beta distribution.
binomial(n, p[, size])	Draw samples from a binomial distribution.
chisquare(df[, size])	Draw samples from a chi-square distribution.
dirichlet(alpha[, size])	Draw samples from the Dirichlet distribution.
exponential([scale, size])	Draw samples from an exponential distribution.
f(dfnum, dfden[, size])	Draw samples from an F distribution.
gamma(shape[, scale, size])	Draw samples from a Gamma distribution.
geometric(p[, size])	Draw samples from the geometric distribution.
gumbel([loc, scale, size])	Draw samples from a Gumbel distribution.
hypergeometric(ngood, nbad, nsample[, size])	Draw samples from a Hypergeometric distribution.
laplace([loc, scale, size])	Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay).
logistic([loc, scale, size])	Draw samples from a logistic distribution.
lognormal([mean, sigma, size])	Draw samples from a log-normal distribution.
logseries(p[, size])	Draw samples from a logarithmic series distribution.
multinomial(n, pvals[, size])	Draw samples from a multinomial distribution.
multivariate_normal(mean, cov[, size, ...)	Draw random samples from a multivariate normal distribution.
negative_binomial(n, p[, size])	Draw samples from a negative binomial distribution.
noncentral_chisquare(df, nonc[, size])	Draw samples from a noncentral chi-square distribution.
noncentral_f(dfnum, dfden, nonc[, size])	Draw samples from the noncentral F distribution.
normal([loc, scale, size])	Draw random samples from a normal (Gaussian) distribution.
pareto(a[, size])	Draw samples from a Pareto II or Lomax distribution with specified shape.
poisson([lam, size])	Draw samples from a Poisson distribution.
power(a[, size])	Draws samples in [0, 1] from a power distribution with positive exponent a - 1.
rayleigh([scale, size])	Draw samples from a Rayleigh distribution.
standard_cauchy([size])	Draw samples from a standard Cauchy distribution with mode = 0.
standard_exponential([size])	Draw samples from the standard exponential distribution.
standard_gamma(shape[, size])	Draw samples from a standard Gamma distribution.
standard_normal([size])	Draw samples from a standard Normal distribution (mean=0, stdev=1).
standard_t(df[, size])	Draw samples from a standard Student’s t distribution with df degrees of freedom.
triangular(left, mode, right[, size])	Draw samples from the triangular distribution over the interval [left, right].
uniform([low, high, size])	Draw samples from a uniform distribution.
vonmises(mu, kappa[, size])	Draw samples from a von Mises distribution.
wald(mean, scale[, size])	Draw samples from a Wald, or inverse Gaussian, distribution.
weibull(a[, size])	Draw samples from a Weibull distribution.
zipf(a[, size])	Draw samples from a Zipf distribution.

--Random generator
RandomState	Container for the Mersenne Twister pseudo-random number generator.
seed([seed])	Seed the generator.
get_state()	Return a tuple representing the internal state of the generator.
set_state(state)	Set the internal state of the generator from a tuple.
'''

# --------------------------------------------------
import numpy as np

np.random.seed(666)  # seed: 设定随机种子，这样每次生成的随机数会相同

# --------------------------------------------------
# 1. rand(d0, d1, ..., dn)
# 返回数据在[0, 1)之间，具有均匀分布

a = np.random.rand(5)  # 一位数组
print(a)

b = np.random.rand(3, 4)  # 二维数组
print(b)

c = np.random.rand(2, 3, 4)  # 三维数组
print(c)

# --------------------------------------------------
# 2. randn(d0, d1, ..., dn)
# 返回数据具有标准正态分布（均值0，方差1）

a = np.random.randn(5)  # 一位数组
print(a)

b = np.random.randn(3, 4)  # 二维数组
print(b)

c = np.random.randn(2, 3, 4)  # 三维数组
print(c)

# --------------------------------------------------
# 3. randint(low[, high, size, dtype])  []指可选参数
# 生成随机整数，包含low，不包含high
# 如果high不指定，则从[0, low)中生成数字

a = np.random.randint(3)  # randint(low) 生成0到3之间的不包含3的随机整数
print(a)

b = np.random.randint(1, 10)  # 生成1到9之间的随机整数
print(b)

c = np.random.randint(10, 30, size=(5))  # 生成5个10到29之间的随机整数
print(c)

d = np.random.randint(10, 30, size=(2, 3, 5))  # 生成2块3行5列的10到29之间的随机整数
print(d)

# --------------------------------------------------
# 4. random([size])
# 生成[0.0, 1.0)的随机数

a = np.random.random(5)
print(a)

b = np.random.random(size=(3, 4))
print(b)

c = np.random.random(size=(3, 4, 5))
print(c)

# --------------------------------------------------
# 5. choice(a[, size, replace, p])
# a是一维数组，从它里面生成随机结果

a = np.random.choice(5, 3)  # 这时候，a是数字，则从range(5)中生成，size为3
print(a)

b = np.random.choice(5, (2, 3))  # 这时候，a是数字，则从range(5)中生成2行3列的数组
print(b)

c = np.random.choice([2, 3, 6, 7, 9], 3)  # 这时候，a是数组，从里面随机取出数字
print(c)

d = np.random.choice([2, 3, 6, 7, 9], (2, 3))
print(d)

# --------------------------------------------------
# 6. shuffle(x)
# 把一个数组x进行随机排列

a = np.arange(10)
print(a)
np.random.shuffle(a)
print(a)

b = np.arange(20).reshape(4, 5)
print(b)
np.random.shuffle(b)  # 如果数组是多维的，则只会在第一维度打散数据；即整行整行打乱，每行本身的元素不会打乱
print(b)

# --------------------------------------------------
# 7. permutation(x)
# 把一个数组x进行随机排列，或者数字的全排列

a = np.random.permutation(10)  # 这时候，生成range(10)的随机排列
print(a)

b = np.arange(9).reshape((3, 3))  # 多维数组时，在第一维度进行打散，以行为单位进行重排
bb = np.random.permutation(b)  # !!注意，这里不会更改原来的arr，会返回一个新的copy
print('bb={}'.format(bb))  # 重排后被copy到新数组
print('b={}'.format(b))  # 原数组没变


# --------------------------------------------------
# 8. normal([loc, scale, size])
# 按照平均值loc和方差scale生成高斯分布的数字

a = np.random.normal(1,10,5)  # 生成平均值为1，方差为10的一维数组size=5
print(a)

b = np.random.normal(1,10,(3,4))
print(b)


# --------------------------------------------------
# 9. uniform([low, high, size])
# 在[low, high)之间生成均匀分布的数字

a = np.random.uniform(1,10,5)  # 产生从1到10的均匀分布的一维数组size=5
print(a)

b = np.random.uniform(1,10,(3,4))  # 产生从1到10的均匀分布数组（3行4列）
print(b)


# --------------------------------------------------
# 实例：对数组加入随机噪声
import matplotlib.pyplot as plt

# 绘制sin曲线
x = np.linspace(-10,10,100)  # 在-10到10之间戳100个点
y = np.sin(x)  # x和y一一对应，且每个x生成一个对应的y
plt.plot(x,y)
plt.show()
# 生成一个很完美的sin图像，但是一般机器学习这样完美的图是不存在的，
# 一般都有很多噪声，随机数可以用来加入这些噪声
x = np.linspace(-10,10,100)
y = np.sin(x) + np.random.rand(len(x))  # 这里len指维度，即加入的噪声与x和y的维度是相同
plt.plot(x,y)
plt.show()












# --------------------------------------------------