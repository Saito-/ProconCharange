# coding: utf-8

'''
A = [1, 1]
    [1, 0]

としたとき, A^n を求めると

Fn+1 = A^nF1
Fn   = A^nF0

として Fn が求められる
(Fn = A[1][0])
'''

M = 10000

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
	A = [
	[1, 1],
	[1, 0],
	]
	n = 10

	A = pow_mat(A, n)
	print A[1][0]
