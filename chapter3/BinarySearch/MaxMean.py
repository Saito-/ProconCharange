# coding: utf-8

import math

n = 3
k = 2
w = [2, 5, 2]
v = [2, 3, 1]

y = [0] * n

tmp = [0] * n
for i in xrange(n):
	tmp[i] = w[i] / v[i]

inf = float(max(tmp))

def C(x):
	for i in xrange(n):
		y[i] = v[i] - x*w[i]
	y.sort()
	s = 0
	for i in xrange(k):
		s += y[n - i - 1]
	return s >= 0

def solve():
	lb = 0
	ub = inf

	for i in xrange(100):
		mid = (lb + ub)/2
		if C(mid):
			lb = mid
		else:
			ub = mid
	
	print '%.2f' % ub

if __name__ == '__main__':
	solve()
