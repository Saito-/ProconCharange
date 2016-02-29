# coding: utf-8

MAX_D = 10000

N = 4
T = 2
m = [3, 2]
d = [
	[1, 2, 4],
	[1, 3],
]

E = [[0 for j in xrange(MAX_D + 1)] for i in xrange(T)]

def gcd(a, b):
	if b == 0: return a
	return gcd(b, a%b)

if __name__ == '__main__':
	for i in xrange(T):
		for j in xrange(m[i]):
			E[i][d[i][j]] += 1
		for a in xrange(1, MAX_D+1):
			E[i][a] += E[i][a-1]
	
	K = 0
	A = 0
	B = N * N
	a = 1
	while a <= N and a <= MAX_D:
		s = 0
		s2 = 0
		for i in xrange(T):
			s += E[i][a]
			s2 += E[i][a] * E[i][a]
		if a < MAX_D:
			A += s*s - s2 + s*N
			K += A / B
			A %= B
		else:
			n = n - MAX_D + 1
			K += s*n / N
			A += (s * s - s2)*n + s*n % N*N
			K += A / B
			A %= B
			if A < 0:
				A += B
				K -= 1
		a += 1
	d = gcd(A, B)
	print K, '+', A/d, '/', B/d
