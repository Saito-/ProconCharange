# coding: utf-8

n = 7
k = 3
a = [2, 2, 3, 4, 4, 5, 5]

dp = [0] * (n + 1)
S = [0] * (n + 1)
deq = [0] * n

def f(j, x):
	return -a[j] * x + dp[j] - S[j] + a[j] * j

def check(f1, f2, f3):
	a1 = -a[f1]
	b1 = dp[f1] - S[f1] + a[f1] * f1
	a2 = -a[f2]
	b2 = dp[f2] - S[f2] + a[f2] * f2
	a3 = -a[f3]
	b3 = dp[f3] - S[f3] + a[f3] * f3
	return (a2 - a1) * (b3 - b2) >= (b2 - b1) * (a3 - a2)

if __name__ == '__main__':
	for i in xrange(n):
		S[i+1] = S[i] + a[i]
	
	s = 0
	t = 1
	deq[0] = 0
	dp[0] = 0

	for i in xrange(k, n + 1):
		if i - k >= k:
			while s + 1 < t and check(deq[t-2], deq[t-1], i-k): t -= 1
			deq[t] = i - k
			t += 1
		while s + 1 < t and f(deq[s], i) >= f(deq[s+1], i): s += 1
		dp[i] = S[i] + f(deq[s], i)
	print dp[n]





