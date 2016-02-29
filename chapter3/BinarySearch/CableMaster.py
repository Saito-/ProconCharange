# coding: utf-8

import math

N = 4
K = 11
L = [8.02, 7.43, 4.57, 5.39]

inf = max(L) + 1

def C(x):
	n = 0
	for i in xrange(N):
		n += (int)(L[i]/x)
	return n >= K

def solve():
	lb = 0
	ub = inf

	for i in xrange(100):
		mid = (lb + ub)/2
		if C(mid):
			lb = mid
		else:
			ub = mid
	print '%.2f' % (math.floor(ub*100)/100)

if __name__ == '__main__':
	solve()
