# coding: utf-8

M = 4

def mul_mat(A, B):
	a = len(A)
	b = len(B[0])
	C = [[0] * b for i in xrange(a)]
	for i in xrange(a):
		for k in xrange(len(B)):
			for j in xrange(b):
				C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % M

	return C

def pow_mat(A, n):
	a = len(A)
	B = [[0] * a for i in xrange(a)]

	for i in xrange(a):
		B[i][i] = 1

	while n > 0:
		if n & 1: B = mul_mat(B, A)
		A = mul_mat(A, A)
		n >>= 1
	return B

if __name__ == '__main__':
	n = 2
	k = 2
	B = [[0]*(n*2) for i in xrange(n*2)]
	A = [
	[0, 1],
	[1, 1],
	]

	for i in xrange(n):
		for j in xrange(n):
			B[i][j] = A[i][j]
		B[i + n][i] = 1
		B[i + n][i + n] = 1

	for i in xrange(n*2):
		print B[i]

	B = pow_mat(B, k+1)

	for i in xrange(n):
		for j in xrange(n):
			a = B[i+n][j] % M
			if i == j: a = (a + M - 1) % M
			print a,
		print
