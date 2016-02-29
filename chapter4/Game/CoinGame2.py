# coding: utf-8

N = 3
K = 3
A = [1, 3, 4]
X = [5, 6, 8]

max_x = max(X)

grundy = [0] * (max_x + 1)

if __name__ == '__main__':
	for j in xrange(1, max_x+1):
		s = set()
		for i in xrange(K):
			if A[i] <= j: s.add(grundy[j - A[i]])
		g = 0
		while g in s: 
			g += 1
		grundy[j] = g
	x = 0
	for i in xrange(N):
		x ^= grundy[X[i]]

	if x != 0: print 'Alice'
	else: print 'Bob'
