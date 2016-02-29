# coding: utf-8

'''
Gauss-Jordan の消去法 (計算量 O(n^3))
'''

EPS = 1e-8

'''
Ax = b を解く
'''
def gauss_jordan(A, b):
	n = len(A)
	B = [[0 for j in xrange(n+1)] for i in xrange(n)] 
	
	for i in xrange(n):
		for j in xrange(n):
			B[i][j] = A[i][j]
	for i in xrange(n):
		B[i][n] = b[i]
	
	for i in xrange(n):
		pivot = i
		for j in xrange(i, n):
			if abs(B[j][i]) > abs(B[pivot][i]): pivot = j
		tmp = B[i]
		B[i] = B[pivot]
		B[pivot] = tmp

		if abs(B[i][i]) < EPS: return []

		div = B[i][i]
		for j in xrange(i, n+1): 
			B[i][j] /= div
		for j in xrange(n):
			if i != j:
				mul = B[j][i]
				for k in xrange(i, n+1):
					B[j][k] -= mul * B[i][k]	

	x = [0] * n
	for i in xrange(n): x[i] = B[i][n]
	return x

if __name__ == '__main__':
	A =[
	[1., -2., 3.],
	[4., -5., 6.],
	[7., -8., 10.],
	]
	b = [6., 12., 21.]

	x = gauss_jordan(A, b)
	print x
