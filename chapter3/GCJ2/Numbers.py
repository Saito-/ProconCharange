# coding: utf-8

M = 1000

def mul_mat(A, B):
	a = len(A)
	b = len(B[0])
	C = [[0] * b for i in xrange(a)]
	for i in xrange(a):
		for k in xrange(len(B)):
			for j in xrange(b):
				C[i][j] = C[i][j] + A[i][k] * B[k][j]

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
	A = [
	[3, 5],
	[1, 3],
	]
	n = 5

	A = pow_mat(A, n)
	print format((A[0][0]*2 + M - 1) % M, '03d')
