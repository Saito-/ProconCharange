# coding: utf-8

import math

N = 5
M = 3
x = [1, 2, 8, 4, 9]

inf = max(x) + 1

def C(d):
	last = 0
	for i in xrange(1, M):
		crt = last + 1
		while crt < N and x[crt] - x[last] < d:
			crt += 1
		if crt == N: return False
		last = crt
	return True

def solve():
	lb = 0
	ub = inf
	x.sort()

	while ub - lb > 1:
		mid = (lb + ub)/2
		if C(mid):
			lb = mid
		else:
			ub = mid
	
	print lb

if __name__ == '__main__':
	solve()
