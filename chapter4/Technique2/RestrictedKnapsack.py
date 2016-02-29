# coding: utf-8

n = 3
w = [3, 2, 4]
v = [2, 4, 3]
m = [5, 1, 3]
W = 12

dp = [0] * (W + 1)
deq = [0] * (W + 1)
deqv = [0] * (W + 1)

if __name__ == '__main__':
	for i in xrange(n):
		for a in xrange(w[i]):
			s = 0
			t = 0
			j = 0
			while j * w[i] + a <= W:
				val = dp[j * w[i] + a] - j * v[i]
				while s < t and deqv[t-1] <= val: t -= 1
				deq[t] = j
				deqv[t] = val
				t += 1
				dp[j * w[i] + a] = deqv[s] + j * v[i]
				if deq[s] == j - m[i]:
					s += 1
				j += 1
	print dp[W]
