# coding: utf-8

import math
import bisect

MAX_N = 100000
MAX_M = 5000

N = 7
M = 3

B = 1000

A = [0, 1, 5, 2, 6, 3, 7, 4]
I = [2, 4, 1]
J = [5, 4, 7]
K = [3, 1, 3]

nums = sorted(A)
bucket = [[] for i in xrange(MAX_N/B)]

if __name__ == '__main__':
	for i in xrange(N):
		bucket[i/B].append(A[i])
	
	for i in xrange(MAX_N/B):
		if len(bucket[i]) == 0: break
		bucket[i] = sorted(bucket[i])
	
	for i in xrange(M):
		l = I[i]
		r = J[i] + 1
		k = K[i]

		lb = -1
		ub = N-1

		while ub - lb > 1:
			md = (lb + ub) / 2
			x = nums[md]
			tl = l
			tr = r
			c = 0
			while tl < tr and tl % B != 0:
				if A[tl] <= x:
					c += 1
				tl += 1
			while tl < tr and tr % B != 0:
				if A[tr-1] <= x:
					c += 1
				tr -= 1
			while tl < tr:
				b = tl / B
				c += bisect.bisect_right(bucket[b], x) - bucket[b][0]
				tl += B

			if c >= k: ub = md
			else: lb = md

		print nums[ub]
