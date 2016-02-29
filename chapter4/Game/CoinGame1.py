# coding: utf-8

X = 10
K = 2
A = [1, 4]

win = [True] * (X+1)

if __name__ == '__main__':
	win[0] = False

	for j in xrange(1, X + 1):
		win[j] = False
		for i in xrange(K):
			win[j] |= A[i] <= j and not win[j-A[i]]

	if win[X]: print 'Alice'
	else: print 'Bob'

