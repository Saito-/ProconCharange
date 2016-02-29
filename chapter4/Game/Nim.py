# coding: utf-8

N = 3
A = [1, 2, 4]

if __name__ == '__main__':
	x = 0
	for i in xrange(N):
		x ^= A[i]
	if x != 0: print 'Alice'
	else: print 'Bob'
