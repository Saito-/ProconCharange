# coding: utf-8

MAX_N = 100
MAX_P = 100

'''
 ユークリッド互除法
'''
def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)


'''
 拡張ユークリッド互除法
'''
def extgcd(a, b, x, y):
	d = a
	if b != 0:
		d = extgcd(b, a % b, y, x)
		y -= (a / b) * x
	else:
		x = 1
		y = 0
	return d
'''
 逆元 (ay = 1(mod m) となる y を求める)
'''
def mod_inverse(a, m):
	x = 0
	y = 1
	extgcd(a, m, x, y)
	return (m + x % m) % m

'''
 オイラー関数
'''
def euler_phi(n):
	res = n
	i = 2
	while i * i <= n:
		if n % i == 0:
			res = res / i * (i - 1)
			while n % i == 0: n /= i
		i += 1
	if n != 1:
		res = res / n * (n - 1)
	return res


euler_table = [0] * MAX_N

def euler_phi2()
	for i in xrange(MAX_N): euler[i] = i
	for i in xrange(2, MAX_N):
		for j in xrange(i, MAX_N, j+=i):
			euler[j] = euler[j] / i * (i-1)

'''
 連立線形合同式の解法
'''
def linear_congruence(A, B, M):
	x = 0
	m = 1
	for i in xrange(len(A)):
		a = A[i] * m
		b = B[i] - A[i] * x
		d = gcd(M[i], a)
		t = b / d * mod_inverse(a/d, M[i]/d) % (M[i] / d)
		x = x + m * t
		m *= M[i] / d
	return (x % m, m)

fact_modp = [0] * MAX_P
'''

'''
