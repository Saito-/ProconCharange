# coding: utf-8

inf = float("inf")

P = 20
Q = 3
A = [0, 3, 6, 14, 21]

dp = [[0 for i in range(Q+2)] for j in range(Q+1)]

def solve():
	for w in range(2, Q+2):
		for i in range(Q-w+2):
			j = i + w
			t = inf
			for k in range(i+1, j):
				t = min(t, dp[i][k] + dp[k][j])
			dp[i][j] = t + A[j] - A[i] - 2
	
	print dp[0][Q+1]

if __name__ == '__main__':
	solve()
