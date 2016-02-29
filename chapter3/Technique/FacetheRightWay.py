# coding: utf-8

N = 7
dirs = [1,1,0,1,0,1,1]

f = [0] * N

def calc(K):
	for i in xrange(len(f)): 
		f[i] = 0
	res = 0
	Sum = 0
	for i in xrange(N - K + 1):
		if (dirs[i] + Sum) % 2 != 0:
			res += 1
			f[i] = 1
		Sum += f[i]
		if i - K + 1 >= 0:
			Sum -= f[i - K + 1]
	for i in xrange(N-K+1, N):
		if (dirs[i] + Sum) % 2 != 0:
			return -1
		if i - K + 1 >= 0:
			Sum -= f[i - K + 1]
	return res

if __name__ == '__main__':
	K = 1
	M = N
	for k in xrange(1, N+1):
		m = calc(k)
		if m >= 0 and M > m:
			M = m
			K = k
	print K, M
