# coding: utf-8

MAX_N = 15
inf = float('inf')

n = 5
d = [
[   0,   3, inf,   4, inf ],
[ inf,   0,   5, inf, inf ],
[   4, inf,   0,   5, inf ],
[ inf, inf, inf,   0,   3 ],
[   7,   6, inf, inf,   0 ],
]

dp = [[-1]*n for j in xrange(1 << MAX_N)]

def rec(S, v):
	if dp[S][v] >= 0: return dp[S][v]
	if S == (1 << n) - 1 and v == 0: 
		dp[S][v] = 0
		return dp[S][v]
	
	res = inf
	for u in xrange(n):
		if not (S >> u & 1):
			res = min(res, rec(S | 1 << u, u) + d[v][u])
	dp[S][v] = res
	return res

if __name__ == '__main__':
	print rec(0, 0)
