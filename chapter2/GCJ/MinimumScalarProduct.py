# coding:utf-8

import numpy as np

def solve(v1, v2):
	n = len(v1)
	ans = 0
	u1 = sorted(v1)
	u2 = sorted(v2, reverse=True)
	for i in xrange(n):
		ans += u1[i]*u2[i]
	return ans

if __name__ == '__main__':
	v1 = [1, 2, -5]
	v2 = [-2, 4, 1]
	print solve(v1, v2)
	v1 = [1, 2, 3, 4, 5]
	v2 = [1, 0, 1, 0, 1]
	print solve(v1, v2)
