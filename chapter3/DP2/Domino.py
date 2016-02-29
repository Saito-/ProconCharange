# coding: utf-8

from copy import deepcopy

MAX_M = 15
n = 3
m = 3
color = [
[False, False, False],
[False,  True, False],
[False, False, False]
]

dp = [[0] * (1 << m) for i in xrange(2)]
dp[0][0] = 1

if __name__ == '__main__':
	crt = dp[0]
	nxt = dp[1]
	for i in xrange(n-1, 0-1, -1):
		for j in xrange(m-1, 0-1, -1):
			for used in xrange(1 << m):
				if (used >> j & 1) or color[i][j]:
					nxt[used]  = crt[used & ~(1 << j)]
				else:
					res = 0
					if j+1 < m and not (used >> (j+1) & 1) and not color[i][j+1]:
						res += crt[used | 1 << (j + 1)]
					if i+1 < n and not color[i+1][j]:
						res += crt[used | 1 << j]
					nxt[used] = res
			tmp = crt
			crt = nxt
			nxt = tmp
	print crt[0]
