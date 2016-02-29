# coding: utf-8:

inf = float('inf')
MAX_N = 8

n = 2
m = 4
a = 2
b = 1
t = [3, 1]

d = [
[  0, -1,  3,  4],
[ -1,  0,  3,  5],
[  3,  3,  0, -1],
[  2,  5, -1,  0]
]

dp = [[inf]*MAX_N for i in xrange(1 << MAX_N)]
dp[(1 << n) - 1][a - 1] = 0

if __name__ == '__main__':
	res = inf
	for S in xrange((1 << n) - 1, 0-1, -1):
		res = min(res, dp[S][b-1])
		for v in xrange(m):
			for i in xrange(n):
				if S >> i & 1:
					for u in xrange(m):
						if d[v][u] >= 0:
							dp[S & ~(1 << i)][u] = min(
								dp[S & ~(1 << i)][u],
								dp[S][v] + float(d[v][u])/t[i]
							)
	if res == inf:
		print 'Impossible'
	else:
		print res

