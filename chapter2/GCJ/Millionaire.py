# coding: utf-8

M = 3
P = 0.75
X = 600000

dp = [[0 for i in range(1 << M + 1)] for j in range(2)]

def solve():
	n = 1 << M
	prv = dp[0]
	nxt = dp[1]
	prv[n] = 1.0

	for r in xrange(M):
		for i in xrange(n+1):
			jub = min(i, n-i)
			t = 0.0
			for j in xrange(jub+1):
				t = max(t, P * prv[i+j] + (1-P)*prv[i-j])
			nxt[i] = t
		tmp = prv
		prv = nxt
		nxt = tmp
	
	i = X*n / 1000000
	print '%.6f' % prv[i]
	
if __name__ == '__main__':
	solve()
